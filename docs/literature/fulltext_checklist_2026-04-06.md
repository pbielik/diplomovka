# Fulltext checklist pre Zotero attachments

> Snapshot dátum: 2026-04-06
> Zdroj stavu: Zotero DB backup `/tmp/codex-zotero-tagging/zotero.sqlite.20260406-231709`

Tento checklist slúži na praktické doťahanie full textov k citekey-ready jadru literatúry.
Je prioritizovaný podľa toho, čo reálne potrebuješ na výpisky a drafting.

## Rýchly súhrn

- core citekey-ready corpus: `39` zdrojov
- zdroje s aspoň jedným `PDF`: `21`
- zdroje bez attachmentu: `18`
- zdroje s `PDF` aj snapshot/web attachmentom: `1` (`omar2024llmpsychiatry`)

Pracovné pravidlo:
- `must-read` journal articles: ideálne mať `PDF`
- WHO/guidance/web zdroje: stačí `snapshot` alebo `PDF`
- `should-read` a `optional`: full text dopĺňať podľa toho, či na zdroj príde rad vo výpiskoch alebo texte

## 1. MUST-READ bez súboru

Toto je prvý batch, ktorý má zmysel dorobiť pred systematickými výpiskami.

| Stav | Citekey | Prečo priorita | Čo pridať |
| --- | --- | --- | --- |
| [ ] | `ajluni2025psychiatriceducation` | AI simulácie v psychiatrickom vzdelávaní; blízko k framingu práce | `PDF` |
| [ ] | `evans2015vignettes` | metodická opora pre vinety a klinické rozhodovanie | `PDF` |
| [ ] | `kroenke2001phq9` | kľúčový anchor paper pre PHQ-9 a symptom severity | `PDF` |
| [Payed] | `guidi2011clinicalinterviewdepression` | klinické interview pri depresii | `PDF` |
| [ ] | `polit2007cvi` | základný CVI paper pre content validity | `PDF` |
| [ ] | `nelson2015manyratersordinal` | metodická opora pre many-rater ordinal agreement | `PDF` |
| [ ] | `who2021ethicsaiforhealth` | autoritatívny ethics/governance rámec | `snapshot` alebo `PDF` |

## 2. SHOULD-READ bez súboru

Tieto zdroje už neblokujú prvé výpisky, ale oplatí sa ich postupne doplniť.

| Stav | Citekey | Funkcia | Čo pridať |
| --- | --- | --- | --- |
| [Payed] | `dubovsky2021psychoticdepression` | psychotická depresia a red flags | `PDF` |
| [ ] | `goddard2012automationbias` | automation bias v klinickom rozhodovaní | `PDF` |
| [Payed] | `hasson2000delphi` | Delphi metodológia | `PDF` |
| [Payed] | `khera2023automationbiasassistiveai` | assistive AI a automation bias | `PDF` |
| [ ] | `lynn1986contentvalidity` | klasický content validity paper | `PDF` |
| [ ] | `mchugh2012kappa` | interpretácia interrater reliability metrics | `PDF` |
| [ ] | `rutherfordhemming2015simulationcvi` | content validity v simulation-based education | `PDF` |
| [ ] | `who2024lmmguidance` | WHO guidance k large multimodal models | `snapshot` alebo `PDF` |

## 3. OPTIONAL bez súboru

Tieto položky sú už na druhý pass.

| Stav | Citekey | Funkcia | Čo pridať |
| --- | --- | --- | --- |
| [ ] | `hirschfeld2014bipolardifferential` | bipolar vs. unipolar differential | `PDF` |
| [ ] | `marasini2016weightedindexes` | weighted agreement indexes | `PDF` |
| [ ] | `mitani2017ordinalsummarymeasures` | ordinal summary measures | `PDF` |

## 4. Už pokryté PDF

Tieto položky už majú aspoň jeden `PDF` attachment v snapshot-e z 2026-04-06:

- `obradovich2024llmpsychiatry`
- `meng2024llmmedicine`
- `yu2025simulatedpatientsystems`
- `brugge2024patientsimulation`
- `baguley2022vignettedata`
- `williams2017simulationmentalhealth`
- `dawood2024standardizedpatient`
- `kennedy2008coresymptoms`
- `maj2020depressioncharacterization`
- `roustan2025cliniciansguide`
- `asgari2025hallucinationframework`
- `mcintyre2019mddvsbipolar`
- `boateng2018scaledevelopment`
- `cook2010computerizedvirtualpatients`
- `kononowicz2019virtualpatients`
- `howell2024genaipatientsafety`
- `jakobsson2005ordinalagreement`
- `terwee2018COSMINMethodologyEvaluating`
- `omar2024llmpsychiatry`
- `guo2024llmmentalhealth`
- `stein2021anxietycharacterization`

## 5. Praktický postup keď stránka má full access, ale Zotero nič nepripojí

1. Otvor existujúcu položku v Zotere, nie novú prázdnu kartu.
2. Na landing page článku klikni priamo na `PDF`, `Download PDF` alebo `Full text PDF`.
3. Stiahnutý súbor pretiahni myšou na existujúcu Zotero položku.
4. Alebo pravý klik na položku → `Add Attachment` → `Attach Stored Copy of File...`.
5. Pri WHO alebo HTML guidance použi `Add Attachment` → `Attach Link to URI` alebo ulož snapshot cez Connector.
6. Ak Connector vytvorí duplicitný parent item len kvôli attachmentu, nechaj lepší parent item, attachment presuň podň a duplicitu zmaž alebo merge-ni.

Preferované pravidlo:
- používaj `Attach Stored Copy of File...`, nie `Attach Link to File...`
- `stored copy` sa lepšie syncuje medzi zariadeniami

## 6. Najbližší odporúčaný sled

1. dorobiť `7` missing attachmentov z MUST-READ bloku,
2. potom spraviť výpisky pre `must-read`,
3. až následne dorábať SHOULD-READ metodické zdroje podľa toho, čo reálne vstupuje do textu.
