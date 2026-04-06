# Príručka: diplomovka s AI, agentmi, Zoterom a Wordom

Táto príručka je pracovný manuál pre tvoju diplomovku. Nie je to kópia fakultného sprievodcu. Je to praktický systém, ktorý je s ním zosúladený.

## 1. Základná filozofia
Tvoja práca má byť:
- písaná podľa IMRaD,
- priebežne citovaná,
- metodicky obhájiteľná,
- pripravená tak, aby si vedel rýchlo doplniť reálne dáta a finálne výsledky.

## 2. Čo je IMRaD v tvojom prípade
- `Introduction` = teoretické, empirické a metodologické východiská + cieľ + hypotézy
- `Method` = replikovateľný opis dizajnu, súboru, materiálu, nástroja, procedúry a analýz
- `Results` = dáta, reliabilita, deskriptíva, hypotézy, doplnkové analýzy
- `Discussion` = interpretácia, limity, implikácie, budúci výskum

Nepíš prácu ako „teoretická časť“ a „praktická časť“. Sekcie majú byť previazané.

## 3. Tvoj odporúčaný workflow
### 3.1 Literatúra
- všetko ide najprv do Zotera,
- citekeys držíš stabilné cez Better BibTeX,
- vo Worde používaš Zotero plugin,
- v markdown draftoch používaš `[@citekey]`.

### 3.2 Písanie
- drafty píšeš v repozitári,
- finálnu formálnu verziu skladáš vo Worde,
- `.docx` necommituješ pri každej malej zmene.

### 3.3 Agenti / AI
Agentom dávaj:
- `AGENTS.md`,
- lokálny sprievodca alebo jeho zhrnutie,
- konkrétny draft súbor,
- jasné obmedzenia: nič mimo IMRaD, nič bez citekeys, nič bez väzby na cieľ práce.

## 4. Repo logika
### 4.1 `manuscript/`
Tu vzniká obsah práce.

### 4.2 `references/`
Tu sú citekeys, import checklisty, source mapy a `.bib` most.

### 4.3 `notes/`
Tu sú výpisky a konzultačné poznámky.

### 4.4 `analysis/`
Tu sú šablóny dát, codebook a R pipeline.

## 5. Zotero + Better BibTeX + Word
### 5.1 Zotero
Používaj kolekcie:
- 00 Core
- 01 Teória
- 02 Metóda
- 03 Štatistika
- 04 Diskusia
- 05 AI a simulácia
- 06 Depresia a interview

### 5.2 Better BibTeX
Drž citekeys stabilné a auto-exportuj `.bib` súbor.

### 5.3 Word
Finálne citácie a bibliografiu rob vo Worde cez Zotero plugin.

## 6. Písanie s citekeys
V draftoch používaj:
- `[@obradovich2024llmpsychiatry]`
- `[@kroenke2001phq9]`
- `[@evans2015vignettes; @maj2020depressioncharacterization]`

Nepíš ručne finálne APA citácie, ak sa text ešte mení.

## 7. Čo máš už pripravené v tomto balíku
- outline
- názov a abstrakt
- reálny draft úvodu
- reálny draft metódy
- šablónu výsledkov
- šablónu diskusie
- hypotézy H1–H6
- codebook
- R pipeline
- Zotero source map
- import checklist
- AGENTS pravidlá

## 8. Minimálny denný rytmus
1. prečítaj 1–3 zdroje,
2. sprav 1–3 krátke výpisky,
3. uprav 1 konkrétny odsek v úvode alebo metóde,
4. nič nové nepridávaj bez väzby na cieľ práce.

## 9. Keď sa stratíš
Vráť sa k tejto postupnosti:
1. `00_START_HERE.md`
2. `README.md`
3. `AGENTS.md`
4. `manuscript/00_outline.md`
5. `manuscript/20_introduction.md`
6. `manuscript/30_method.md`

## 10. Čo dopĺňať až neskôr
- finálne čísla do výsledkov,
- finálne interpretácie do diskusie,
- finálny abstrakt,
- finálny názov, ak sa ešte zmení dôraz práce.

## 11. Čomu sa vyhnúť
- novým analýzam len kvôli rozsahu,
- ručnému miešaniu citácií a citekeys,
- prepisovaniu bibliografie mimo Zotera,
- rozbitiu IMRaD štruktúry,
- rozsiahlym teoretickým odbočkám bez väzby na výskumný problém.
