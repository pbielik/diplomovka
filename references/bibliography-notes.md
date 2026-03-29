# Bibliography notes — citekeys ↔ identifiers

Tento súbor slúži ako pracovný most medzi Zotero/Better BibTeX citekeys a identifikátormi zdrojov.
Použitie:
- importuj zdroj do Zotera cez PMID / PMCID alebo URL,
- nastav alebo skontroluj citekey,
- po auto-exporte Better BibTeX over, že citekey v `.bib` sedí s markdown draftmi.

---

## Copy-paste blok: citekey → PMID / PMCID / URL

```text
obradovich2024llmpsychiatry | PMCID: PMC11566298 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11566298/
meng2024llmmedicine | PMCID: PMC11091685 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11091685/
ajluni2025psychiatriceducation | PMCID: PMC12077637 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12077637/
yu2025simulatedpatientsystems | PMCID: PMC12808140 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12808140/
brugge2024patientsimulation | PMCID: PMC11605890 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11605890/
evans2015vignettes | PMCID: PMC6224682 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC6224682/
baguley2022vignettedata | PMCID: PMC9796090 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9796090/
williams2017simulationmentalhealth | PMCID: PMC5806484 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5806484/
dawood2024standardizedpatient | PMCID: PMC11206419 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11206419/
kennedy2008coresymptoms | PMCID: PMC3181882 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3181882/
maj2020depressioncharacterization | PMCID: PMC7491646 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7491646/
kroenke2001phq9 | PMID: 11556941 | URL: https://pubmed.ncbi.nlm.nih.gov/11556941/
guidi2011clinicalinterviewdepression | PMID: 20975323 | URL: https://pubmed.ncbi.nlm.nih.gov/20975323/
roustan2025cliniciansguide | PMCID: PMC11815294 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11815294/
asgari2025hallucinationframework | PMCID: PMC12075489 | URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12075489/
```

---

## Import blok pre Zotero — Add Item by Identifier

Skopíruj a vkladaj po riadkoch alebo naraz:

```text
PMC11566298
PMC11091685
PMC12077637
PMC12808140
PMC11605890
PMC6224682
PMC9796090
PMC5806484
PMC11206419
PMC3181882
PMC7491646
11556941
20975323
PMC11815294
PMC12075489
```

---

## Minimum jadro pre úvod

Ak chceš najprv importnúť iba minimum, začni týmito citekeys:

```text
obradovich2024llmpsychiatry
ajluni2025psychiatriceducation
evans2015vignettes
williams2017simulationmentalhealth
kennedy2008coresymptoms
maj2020depressioncharacterization
kroenke2001phq9
guidi2011clinicalinterviewdepression
roustan2025cliniciansguide
asgari2025hallucinationframework
```

---

## Kontrola po importe

Pri každom zdroji over:
- typ záznamu je správny (`journal article`),
- názov, autori, rok, journal, DOI/PMID/PMCID sú vyplnené,
- citekey presne sedí s markdown draftom,
- ak je dostupné PDF, ulož ho len ak ho naozaj potrebuješ.

---

## Poznámka k draftom

V markdown textoch používaj citekeys presne v tomto tvare:

```text
[@obradovich2024llmpsychiatry]
[@kroenke2001phq9]
[@evans2015vignettes]
```

Vo Worde ich potom nahraď živou Zotero citáciou.
