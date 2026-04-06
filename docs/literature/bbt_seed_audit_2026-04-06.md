# Audit Better BibTeX seed vs literature workflow

> Dátum auditu: 2026-04-06
> Scope: `references/zotero-thesis-seed.bib`, `references/bibliography-notes.md`, `references/intro_source_map_zotero.md`, `manuscript/20_introduction.md`, `docs/literature/`

## Verdikt

Aktuálny `references/zotero-thesis-seed.bib` sa nedá považovať za spoľahlivý seed pre markdown drafty. Repo už má jasne pomenované citekeys a priority v source mapách a literature bundle, ale seed s nimi momentálne nie je zosúladený.

## Addendum po hromadnom importe `bibliography-notes`

> Stav po importe: 2026-04-06 večer

- Do repa pribudol importér `references/scripts/import_bibliography_notes_to_zotero.py`, ktorý ťahá metadata z PubMed, PMC, DOI a WHO URL a ukladá ich cez lokálny Zotero connector.
- Do repa pribudli aj `references/scripts/cleanup_zotero_duplicates_and_enable_export.py` a `references/scripts/export_cleaned_collection_to_bib.py` pre Zotero duplicate cleanup a deterministický BBT export.
- `references/zotero-thesis-seed.bib` aj `references/zotero-thesis.bib` už obsahujú cleaned export pre current thesis collection.
- Post-cleanup kontrola cez import script dáva stav `36 exact + 0 ambiguous` proti `references/bibliography-notes.md`.
- `yu2025SimulatedPatientSystems` case-conflict bol odstránený; canonical citekey v exporte je už len `yu2025simulatedpatientsystems`.
- Legacy duplicity `omar2024ApplicationsLargeLanguageb`, `2025ApplicationsLargeLanguage`, `li2026LargeLanguageModelc` a `beck2010DifferentialdiagnostikDepression` už v cleaned exporte nie sú.

Nižšie uvedené tabuľky zachytávajú pre-import audit snapshot a stále sú užitočné pre cleanup legacy duplicít a noise položiek.

## Rýchle zhrnutie

| Kontrola | Výsledok |
| --- | --- |
| Počet záznamov v `references/zotero-thesis-seed.bib` | `77` |
| Počet citekeys použitých v `manuscript/20_introduction.md` | `15` |
| Exact-key zhoda intro citekeys vs seed | `0 / 15` |
| Počet citekeys evidovaných v `references/bibliography-notes.md` | `36` |
| Exact-key zhoda bibliography-notes citekeys vs seed | `0 / 36` |
| Finálny auto-export `references/zotero-thesis.bib` | `chýba` |

## 1. Blocking gap: citekeys už použité v rukopise, ale chýbajúce v seede

Tieto citekeys sú už priamo použité v `manuscript/20_introduction.md`, takže ich absencia blokuje čistý Zotero/BBT workflow.

| Citekey | Funkcia v rukopise | Stav v seede |
| --- | --- | --- |
| `obradovich2024llmpsychiatry` | všeobecný vstup do LLM v psychiatrii | `missing exact key` |
| `meng2024llmmedicine` | širší medicínsky rámec LLM | `missing exact key` |
| `ajluni2025psychiatriceducation` | AI simulácie v psychiatrickom vzdelávaní | `missing exact key` |
| `yu2025simulatedpatientsystems` | simulated patients / training artifact | `missing exact key`; obsahovo zrejme prítomné len ako `yu2025SimulatedPatientSystems` |
| `brugge2024patientsimulation` | patient simulation a feedback | `missing exact key` |
| `evans2015vignettes` | vignette methodology | `missing exact key` |
| `baguley2022vignettedata` | modelovanie vignette dát | `missing exact key` |
| `williams2017simulationmentalhealth` | simulation v mental health education | `missing exact key` |
| `dawood2024standardizedpatient` | standardized patient v psychiatric education | `missing exact key` |
| `kennedy2008coresymptoms` | jadrové symptómy MDD | `missing exact key` |
| `maj2020depressioncharacterization` | klinický obraz depresie | `missing exact key` |
| `kroenke2001phq9` | PHQ-9 anchor | `missing exact key` |
| `guidi2011clinicalinterviewdepression` | klinické interview pri depresii | `missing exact key` |
| `roustan2025cliniciansguide` | hallucinations a klinické limity LLM | `missing exact key` |
| `asgari2025hallucinationframework` | clinical safety / hallucination framing | `missing exact key` |

## 2. P1 a bundle zdroje, ktoré seed stále nekryje

Toto je prvý batch zdrojov, ktoré literature bundle explicitne odporúča doplniť ako najvyššiu prioritu.

| Citekey | Prečo je dôležitý | Stav v seede |
| --- | --- | --- |
| `mcintyre2019mddvsbipolar` | diferenciálna diagnostika MDD vs bipolarita | `missing` |
| `dubovsky2021psychoticdepression` | psychotické črty a red flags | `missing` |
| `polit2007cvi` | CVI framing pre content validity | `missing` |
| `boateng2018scaledevelopment` | pilotný vývoj a validácia scale | `missing` |
| `rutherfordhemming2015simulationcvi` | CVI priamo pre simulation scenarios | `missing` |
| `kononowicz2019virtualpatients` | virtual patients systematický prehľad | `missing` |
| `who2021ethicsaiforhealth` | autoritatívny ethics/governance rámec | `missing` |
| `who2024lmmguidance` | guidance k large multimodal models v health | `missing` |
| `goddard2012automationbias` | automation bias a mitigácie | `missing` |
| `jakobsson2005ordinalagreement` | agreement pri ordinálnych ratingoch | `missing` |
| `nelson2015manyratersordinal` | many-rater ordinal agreement | `missing` |

## 3. Relevantné zdroje prítomné len pod nestabilným alebo netarget citekey

Tieto položky sú v seed súbore obsahovo prítomné, ale pod citekeyom, ktorý nezodpovedá workflow dokumentom alebo je zbytočne dlhý.

| Workflow cieľ | Aktuálny citekey v seede | Potrebná akcia |
| --- | --- | --- |
| `yu2025simulatedpatientsystems` | `yu2025SimulatedPatientSystems` | zjednotiť na lowercase target key |
| `guo2024llmmentalhealth` | `guo2024LargeLanguageModels` | uzamknúť kratší citekey zodpovedajúci bundle |
| `omar2024llmpsychiatry` | `omar2024ApplicationsLargeLanguage` a `omar2024ApplicationsLargeLanguageb` | zlúčiť duplicitu a nechať 1 canonical key |
| `terwee` content-validity paper | `terwee2018COSMINMethodologyEvaluating` | skrátiť na stabilný citekey pred prvým použitím v texte |

## 4. Seed noise a duplicity

Aktuálny seed mieša jadro diplomovky so všeobecnými alebo slabými webovými položkami, ktoré by nemali ísť do hlavného thesis exportu.

### Zjavne slabé alebo pomocné položky

- `2023ContentValidity` (`Wikipedia`)
- `2023ValidityPsychologyResearch`
- `2023ValidityPsychologyResearcha`
- `2024FaceValiditya`
- `2026DelphiMethod` (`Wikipedia`)
- `GuidePsychometricValidity`
- `GuidePsychometricValiditya`
- `PsychometricValidityGuide`
- `TheoryFacetsFacets`
- `ManyFacetRaschMeasurement` (`Scribd` landing page)

### Duplicity podľa DOI

| DOI | Duplicita |
| --- | --- |
| `10.1024/0040-5930/a000094` | `beck2010DifferentialDiagnosisMajor`, `beck2010DifferentialdiagnostikDepression` |
| `10.2196/69284` | `2025ApplicationsLargeLanguage`, `jin2025ApplicationsLargeLanguage` |
| `10.2196/79039` | `li2026LargeLanguageModel`, `li2026LargeLanguageModelc` |
| `10.3389/fpsyt.2024.1422807` | `omar2024ApplicationsLargeLanguage`, `omar2024ApplicationsLargeLanguageb` |

## 5. Chýbajúce bundle-level must-read opory mimo aktuálneho seed workflow

Nie všetky kritické položky ešte majú citekey-ready most v seede alebo notes workflowe.

| Zdroj / oblasť | Poznámka |
| --- | --- |
| `kroenke2009phq8` | source clusters ho označujú ako veľmi dôležitý pre populačné anchorovanie seedov |
| `koo2016icc` | bundle a preset ho používajú ako metodický anchor, ale seed ho neobsahuje |
| COSMIN User Manual | source clusters ho výslovne odporúčajú pre content validity workflow |
| WHO / safety framing jadro | v P1 je už pomenované, ale seed ho ešte nekryje |

## 6. Odporúčaný cleanup poriadok

1. Neprepisuj manuscript citekeys na aktuálne seed citekeys. Seed je momentálne slabší než source mapy a literature bundle.
2. Použi `references/bibliography-notes.md` a `references/intro_source_map_zotero.md` ako importný most pre intro core a P1 batch.
3. V Zotere uzamkni exact citekeys podľa workflow dokumentov, nie podľa aktuálneho seed dumpu.
4. Pred exportom odstráň z thesis kolekcie duplicity a odsuň pomocné webové/glossary položky mimo core export.
5. Zapni alebo obnov auto-export do `references/zotero-thesis.bib`.
6. Až z čistého exportu odvodzuj nový seed alebo canonical citekey list pre markdown drafty.
7. Po každej väčšej zmene citekeys re-run audit proti `manuscript/20_introduction.md`, `manuscript/30_method.md`, `manuscript/50_discussion.md` a `references/bibliography-notes.md`.

## Definition of done pre seed cleanup

- `references/zotero-thesis.bib` reálne existuje v repo
- intro citekeys majú exact-key pokrytie `15 / 15`
- odporúčaný P1 batch má exact-key pokrytie `11 / 11`
- každý paper má jeden canonical citekey
- thesis export neobsahuje Wikipedia, generic blog posts ani duplicity toho istého DOI
- markdown drafty, bibliography notes a finálny export používajú tie isté citekeys
