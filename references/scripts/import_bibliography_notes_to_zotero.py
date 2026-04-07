#!/usr/bin/env python3

import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_NOTES = REPO_ROOT / "references" / "bibliography-notes.md"
DEFAULT_BATCH = REPO_ROOT / "references" / "zotero-saveitems-batch-2026-04-06.json"
BBT_RPC_URL = "http://127.0.0.1:23119/better-bibtex/json-rpc"
ZOTERO_SAVEITEMS_URL = "http://127.0.0.1:23119/connector/saveItems"
RPC_ID = "codex"


WHO_MANUAL_ITEMS = {
    "who2021ethicsaiforhealth": {
        "itemType": "report",
        "title": "Ethics and governance of artificial intelligence for health",
        "creators": [{"name": "World Health Organization", "creatorType": "author"}],
        "date": "2021",
        "publisher": "World Health Organization",
        "place": "Geneva",
        "url": "https://www.who.int/publications/i/item/9789240029200",
    },
    "who2024lmmguidance": {
        "itemType": "report",
        "title": "Ethics and governance of artificial intelligence for health: guidance on large multi-modal models",
        "creators": [{"name": "World Health Organization", "creatorType": "author"}],
        "date": "2024",
        "publisher": "World Health Organization",
        "place": "Geneva",
        "url": "https://iris.who.int/handle/10665/375579",
    },
    "who2025depression": {
        "itemType": "webpage",
        "title": "Depressive disorder (depression)",
        "creators": [{"name": "World Health Organization", "creatorType": "author"}],
        "date": "2025",
        "websiteTitle": "WHO fact sheets",
        "publisher": "World Health Organization",
        "place": "Geneva",
        "url": "https://www.who.int/news-room/fact-sheets/detail/depression",
    },
}


DOI_CSL_ACCEPT = "application/vnd.citationstyles.csl+json"
META_RE = re.compile(
    r"<meta\s+[^>]*?(?:name|property)=[\"']([^\"']+)[\"'][^>]*?content=[\"']([^\"']*)[\"'][^>]*?>",
    re.IGNORECASE,
)


class ImportError(RuntimeError):
    pass


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


def http_request(url: str, *, method: str = "GET", headers=None, data: bytes | None = None) -> tuple[int, str]:
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "User-Agent": "Codex Zotero Importer/1.0",
            **(headers or {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return exc.code, body


def http_get(url: str, *, headers=None) -> str:
    status, body = http_request(url, headers=headers)
    if status < 200 or status >= 300:
        raise ImportError(f"GET {url} failed with HTTP {status}")
    return body


def post_json(url: str, payload: dict) -> tuple[int, str]:
    return http_request(
        url,
        method="POST",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload).encode("utf-8"),
    )


def bbt_rpc(method: str, params: list):
    status, body = post_json(
        BBT_RPC_URL,
        {"jsonrpc": "2.0", "method": method, "params": params, "id": RPC_ID},
    )
    if status != 200:
        raise ImportError(f"BBT RPC {method} failed with HTTP {status}")
    payload = json.loads(body)
    if "error" in payload:
        raise ImportError(payload["error"]["message"])
    return payload["result"]


def exact_citekey_exists(citekey: str) -> bool:
    return exact_citekey_state(citekey) == "exact"


def exact_citekey_state(citekey: str) -> str:
    try:
        bbt_rpc("item.export", [[citekey], "BetterBibTeX JSON"])
        return "exact"
    except ImportError as exc:
        message = str(exc)
        if "not found" in message:
            return "missing"
        if "duplicates found" in message:
            return "ambiguous"
        raise


def wait_for_exact_citekey(citekey: str, *, attempts: int = 15, sleep_seconds: float = 1.0) -> bool:
    for _ in range(attempts):
        if exact_citekey_exists(citekey):
            return True
        time.sleep(sleep_seconds)
    return False


def search_identifier(field: str, value: str) -> list[dict]:
    return bbt_rpc("item.search", [[[field, "is", value]]])


def parse_notes(notes_path: Path) -> list[dict]:
    entries = []
    for raw_line in notes_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or " | " not in line or line.startswith(("#", "`", "-", "|")):
            continue
        parts = [part.strip() for part in line.split("|")]
        citekey = parts[0]
        if not re.fullmatch(r"[a-z0-9]+", citekey):
            continue
        entry = {"citekey": citekey}
        for part in parts[1:]:
            if ":" not in part:
                continue
            name, value = part.split(":", 1)
            entry[name.strip().upper()] = value.strip()
        entries.append(entry)
    return entries


def first(values: list[str] | None) -> str | None:
    if not values:
        return None
    return values[0]


def normalize_space(value: str | None) -> str | None:
    if value is None:
        return None
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def strip_html(value: str | None) -> str | None:
    if not value:
        return None
    return normalize_space(re.sub(r"<[^>]+>", " ", value))


def extract_meta_tags(document: str) -> dict[str, list[str]]:
    meta: dict[str, list[str]] = {}
    for key, value in META_RE.findall(document):
        meta.setdefault(key.lower(), []).append(normalize_space(value))
    return meta


def fetch_page_meta(url: str) -> dict[str, list[str]]:
    return extract_meta_tags(http_get(url))


def fetch_doi_csl(doi: str) -> dict:
    body = http_get(
        f"https://doi.org/{urllib.parse.quote(doi)}",
        headers={"Accept": DOI_CSL_ACCEPT},
    )
    return json.loads(body)


def parse_meta_authors(meta: dict[str, list[str]]) -> list[dict]:
    authors: list[dict] = []
    raw_names = list(meta.get("citation_author", []))
    if not raw_names and meta.get("citation_authors"):
        raw_names = [name for name in meta["citation_authors"][0].split(";") if name.strip()]
    for raw_name in raw_names:
        name = normalize_space(raw_name)
        if not name:
            continue
        if "," in name:
            last, first_name = [part.strip() for part in name.split(",", 1)]
            authors.append({"firstName": first_name, "lastName": last, "creatorType": "author"})
            continue
        parts = name.split()
        if len(parts) == 1:
            authors.append({"name": name, "creatorType": "author"})
            continue
        if len(parts) == 2 and re.fullmatch(r"[A-Z][A-Z.-]*", parts[1]):
            authors.append({"firstName": parts[1], "lastName": parts[0], "creatorType": "author"})
            continue
        authors.append({"firstName": " ".join(parts[:-1]), "lastName": parts[-1], "creatorType": "author"})
    return authors


def creators_from_csl(authors: list[dict] | None) -> list[dict]:
    creators = []
    for author in authors or []:
        if author.get("literal"):
            creators.append({"name": normalize_space(author["literal"]), "creatorType": "author"})
        else:
            creators.append(
                {
                    "firstName": normalize_space(author.get("given", "")) or "",
                    "lastName": normalize_space(author.get("family", "")) or "",
                    "creatorType": "author",
                }
            )
    return creators


def format_csl_date(date_obj: dict | None) -> str | None:
    if not date_obj:
        return None
    parts = (date_obj.get("date-parts") or [[]])[0]
    if not parts:
        return None
    if len(parts) == 1:
        return str(parts[0])
    if len(parts) == 2:
        return f"{parts[0]}-{int(parts[1]):02d}"
    return f"{parts[0]}-{int(parts[1]):02d}-{int(parts[2]):02d}"


def csl_value(value):
    if isinstance(value, list):
        return normalize_space(value[0]) if value else None
    if isinstance(value, str):
        return normalize_space(value)
    return None


def add_if(item: dict, field: str, value):
    if value not in (None, "", []):
        item[field] = value


def map_csl_type(csl_type: str | None) -> str:
    return {
        "journal-article": "journalArticle",
        "article-journal": "journalArticle",
        "report": "report",
        "webpage": "webpage",
        "paper-conference": "conferencePaper",
        "proceedings-article": "conferencePaper",
    }.get(csl_type or "", "journalArticle")


def is_arxiv_doi(doi: str | None) -> bool:
    return bool(doi) and doi.lower().startswith("10.48550/arxiv.")


def enrich_with_entry_ids(item: dict, entry: dict, meta: dict[str, list[str]] | None):
    add_if(item, "DOI", normalize_space(item.get("DOI")) or entry.get("DOI") or first((meta or {}).get("citation_doi")))
    add_if(item, "PMID", entry.get("PMID") or first((meta or {}).get("citation_pmid")))
    pmcid = entry.get("PMCID") or first((meta or {}).get("citation_pmcid"))
    add_if(item, "PMCID", pmcid)


def item_from_csl(entry: dict, csl: dict, meta: dict[str, list[str]] | None) -> dict:
    doi_value = entry.get("DOI") or csl_value(csl.get("DOI"))
    if is_arxiv_doi(doi_value):
        item_type = "preprint"
    else:
        item_type = map_csl_type(csl.get("type"))
    item = {
        "id": entry["citekey"],
        "itemType": item_type,
        "title": csl_value(csl.get("title")),
        "creators": creators_from_csl(csl.get("author")),
        "citationKey": entry["citekey"],
        "extra": f"Citation Key: {entry['citekey']}",
        "attachments": [],
        "tags": [],
    }
    add_if(item, "abstractNote", strip_html(csl.get("abstract")))
    add_if(item, "date", format_csl_date(csl.get("issued")) or format_csl_date(csl.get("published-online")) or format_csl_date(csl.get("published")))
    add_if(item, "publicationTitle", csl_value(csl.get("container-title")))
    add_if(item, "journalAbbreviation", csl_value(csl.get("container-title-short")))
    add_if(item, "volume", csl_value(csl.get("volume")))
    add_if(item, "issue", csl_value(csl.get("issue")))
    add_if(item, "pages", csl_value(csl.get("page")))
    add_if(item, "ISSN", csl_value(csl.get("ISSN")))
    add_if(item, "publisher", csl_value(csl.get("publisher")))
    add_if(item, "language", csl_value(csl.get("language")))
    add_if(item, "url", entry.get("URL") or csl_value((csl.get("resource") or {}).get("primary", {}).get("URL")) or csl_value(csl.get("URL")))
    enrich_with_entry_ids(item, entry, meta)
    return item


def item_from_meta(entry: dict, meta: dict[str, list[str]]) -> dict:
    item = {
        "id": entry["citekey"],
        "itemType": "journalArticle",
        "title": first(meta.get("citation_title")),
        "creators": parse_meta_authors(meta),
        "citationKey": entry["citekey"],
        "extra": f"Citation Key: {entry['citekey']}",
        "attachments": [],
        "tags": [],
    }
    add_if(item, "date", first(meta.get("citation_publication_date")) or first(meta.get("citation_date")))
    add_if(item, "publicationTitle", first(meta.get("citation_journal_title")) or first(meta.get("citation_publisher")))
    add_if(item, "volume", first(meta.get("citation_volume")))
    add_if(item, "issue", first(meta.get("citation_issue")))
    first_page = first(meta.get("citation_firstpage"))
    last_page = first(meta.get("citation_lastpage"))
    if first_page and last_page:
        item["pages"] = f"{first_page}-{last_page}"
    else:
        add_if(item, "pages", first_page)
    add_if(item, "ISSN", first(meta.get("citation_issn")))
    add_if(item, "url", entry.get("URL") or first(meta.get("citation_abstract_html_url")) or first(meta.get("citation_full_html_url")))
    enrich_with_entry_ids(item, entry, meta)
    return item


def item_from_who(entry: dict) -> dict:
    base = WHO_MANUAL_ITEMS[entry["citekey"]].copy()
    item = {
        "id": entry["citekey"],
        **base,
        "citationKey": entry["citekey"],
        "extra": f"Citation Key: {entry['citekey']}",
        "attachments": [],
        "tags": [],
    }
    return item


def resolve_item(entry: dict) -> dict:
    if entry["citekey"] in WHO_MANUAL_ITEMS:
        return item_from_who(entry)

    meta = {}
    url = entry.get("URL")
    if url and any(host in url for host in ("pubmed.ncbi.nlm.nih.gov", "pmc.ncbi.nlm.nih.gov")):
        meta = fetch_page_meta(url)

    doi = entry.get("DOI") or first(meta.get("citation_doi"))
    if doi:
        return item_from_csl(entry, fetch_doi_csl(doi), meta)
    if meta:
        return item_from_meta(entry, meta)
    raise ImportError(f"No resolver available for {entry['citekey']}")


def find_existing_identifier_hits(item: dict) -> list[dict]:
    for field in ("DOI", "PMID", "PMCID"):
        value = item.get(field)
        if value:
            return search_identifier(field, value)
    return []


def build_import_plan(entries: list[dict]) -> tuple[list[dict], list[str], list[str]]:
    plan = []
    exact_existing = []
    ambiguous_existing = []
    for entry in entries:
        citekey = entry["citekey"]
        state = exact_citekey_state(citekey)
        if state == "exact":
            exact_existing.append(citekey)
            continue
        if state == "ambiguous":
            ambiguous_existing.append(citekey)
            continue
        item = resolve_item(entry)
        identifier_hits = find_existing_identifier_hits(item)
        plan.append(
            {
                "citekey": citekey,
                "item": item,
                "identifierHits": identifier_hits,
            }
        )
    return plan, exact_existing, ambiguous_existing


def import_item(item: dict) -> None:
    session_id = f"codex-{item['id']}"
    status, body = post_json(
        ZOTERO_SAVEITEMS_URL,
        {"sessionID": session_id, "items": [item]},
    )
    if status != 201:
        raise ImportError(f"saveItems failed for {item['id']} with HTTP {status}: {body}")
    if not wait_for_exact_citekey(item["citationKey"]):
        raise ImportError(f"{item['citationKey']} was not visible in Better BibTeX after import")


def write_batch(batch_path: Path, plan: list[dict]) -> None:
    batch = {
        "sessionID": "codex-bibliography-notes-batch-2026-04-06",
        "items": [row["item"] for row in plan],
    }
    batch_path.write_text(json.dumps(batch, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_only_arg(values: list[str] | None) -> set[str]:
    selected: set[str] = set()
    for value in values or []:
        for citekey in value.split(","):
            citekey = citekey.strip()
            if citekey:
                selected.add(citekey)
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description="Import bibliography-notes citekeys into Zotero via local connector.")
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--batch-output", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--import", dest="do_import", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--only", action="append", help="Comma-separated citekeys to process")
    args = parser.parse_args()

    entries = parse_notes(args.notes)
    only = parse_only_arg(args.only)
    if only:
        entries = [entry for entry in entries if entry["citekey"] in only]
    if args.limit:
        entries = entries[: args.limit]
    if not entries:
        raise ImportError("No entries selected for import")

    log(f"Parsed {len(entries)} entries from {args.notes}")
    plan, exact_existing, ambiguous_existing = build_import_plan(entries)
    write_batch(args.batch_output, plan)
    log(f"Exact citekeys already present: {len(exact_existing)}")
    log(f"Case-conflict citekeys requiring manual cleanup: {len(ambiguous_existing)}")
    log(f"Prepared import plan for: {len(plan)}")
    if exact_existing:
        log("Skipped exact citekeys: " + ", ".join(exact_existing))
    if ambiguous_existing:
        log("Skipped ambiguous citekeys: " + ", ".join(ambiguous_existing))
    for row in plan:
        hits = [hit.get("citekey") for hit in row["identifierHits"] if hit.get("citekey") != row["citekey"]]
        if hits:
            log(f"Identifier already present under other keys for {row['citekey']}: {', '.join(hits)}")

    if args.do_import:
        imported = []
        failures = []
        for row in plan:
            try:
                import_item(row["item"])
                imported.append(row["citekey"])
                log(f"Imported {row['citekey']}")
                time.sleep(0.2)
            except ImportError as exc:
                failures.append((row["citekey"], str(exc)))
                log(f"FAILED {row['citekey']}: {exc}")
        log(f"Imported total: {len(imported)}")
        if failures:
            log(f"Failed total: {len(failures)}")
            for citekey, reason in failures:
                log(f"Failure detail {citekey}: {reason}")
            raise ImportError("Some items failed to import")
    else:
        log("Dry run only; no items were imported")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ImportError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
