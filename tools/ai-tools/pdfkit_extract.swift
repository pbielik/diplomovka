import Foundation
import AppKit
import PDFKit
import Vision

let args = CommandLine.arguments

let useOCR = args.dropFirst().contains("--ocr")
let positionalArgs = args.dropFirst().filter { $0 != "--ocr" }

guard positionalArgs.count == 1 else {
    fputs("Usage: pdfkit_extract.swift [--ocr] <pdf-path>\n", stderr)
    exit(2)
}

let pdfPath = positionalArgs[0]
let url = URL(fileURLWithPath: pdfPath)

guard let document = PDFDocument(url: url) else {
    fputs("Unable to open PDF at \(pdfPath)\n", stderr)
    exit(1)
}

if document.isLocked && !document.unlock(withPassword: "") {
    fputs("Unable to unlock PDF with an empty password.\n", stderr)
    exit(1)
}

var pages: [String] = []
pages.reserveCapacity(document.pageCount)

for index in 0..<document.pageCount {
    guard let page = document.page(at: index) else {
        pages.append("")
        continue
    }
    let text: String
    if useOCR {
        text = autoreleasepool(invoking: {
            (try? ocrText(for: page)) ?? page.string ?? ""
        })
    } else {
        text = page.string ?? ""
    }
    pages.append(text)
}

do {
    let data = try JSONSerialization.data(withJSONObject: pages, options: [])
    FileHandle.standardOutput.write(data)
} catch {
    fputs("Failed to serialise extracted PDF text.\n", stderr)
    exit(1)
}

func ocrText(for page: PDFPage) throws -> String {
    guard let image = renderPage(page) else {
        return page.string ?? ""
    }

    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["sk-SK", "cs-CZ", "en-US"]

    let handler = VNImageRequestHandler(cgImage: image, options: [:])
    try handler.perform([request])

    let observations = request.results ?? []
    let sorted = observations.sorted { lhs, rhs in
        let yDelta = lhs.boundingBox.midY - rhs.boundingBox.midY
        if abs(yDelta) > 0.015 {
            return yDelta > 0
        }
        return lhs.boundingBox.minX < rhs.boundingBox.minX
    }

    let lines = sorted.compactMap { observation in
        observation.topCandidates(1).first?.string.trimmingCharacters(in: .whitespacesAndNewlines)
    }
    return lines.filter { !$0.isEmpty }.joined(separator: "\n")
}

func renderPage(_ page: PDFPage) -> CGImage? {
    let bounds = page.bounds(for: .mediaBox)
    let maxDimension = max(bounds.width, bounds.height)
    let scale = max(2.0, 1800.0 / maxDimension)
    let width = Int(bounds.width * scale)
    let height = Int(bounds.height * scale)

    guard let bitmap = NSBitmapImageRep(
        bitmapDataPlanes: nil,
        pixelsWide: width,
        pixelsHigh: height,
        bitsPerSample: 8,
        samplesPerPixel: 4,
        hasAlpha: false,
        isPlanar: false,
        colorSpaceName: .deviceRGB,
        bytesPerRow: 0,
        bitsPerPixel: 0
    ) else {
        return nil
    }

    guard let graphicsContext = NSGraphicsContext(bitmapImageRep: bitmap) else {
        return nil
    }

    NSGraphicsContext.saveGraphicsState()
    defer { NSGraphicsContext.restoreGraphicsState() }

    NSGraphicsContext.current = graphicsContext
    let context = graphicsContext.cgContext
    context.setFillColor(NSColor.white.cgColor)
    context.fill(CGRect(x: 0, y: 0, width: width, height: height))
    context.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: context)
    context.flush()

    return bitmap.cgImage
}
