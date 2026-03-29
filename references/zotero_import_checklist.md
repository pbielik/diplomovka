# Zotero import checklist pre diplomovku

Tento checklist je naviazaný na `intro_source_map_zotero.md` a je navrhnutý pre workflow:
- Zotero = master databáza zdrojov
- Better BibTeX = stabilné citekeys + auto-export `.bib`
- Word + Zotero plugin = finálne citácie a bibliografia
- repo = drafty, výpisky, R pipeline

## 0. Jednorazové nastavenie

### Zotero
- skontroluj, že beží desktop Zotero
- skontroluj, že máš prihlásené konto a sync
- v Zotere vytvor kolekciu `Diplomovka`
- pod ňou podkolekciu `01 Úvod`

### Word plugin
- otvor Zotero → Settings → Cite → Word Processors
- ak panel vo Worde nevidíš, daj `Reinstall Microsoft Word Add-in`

### Better BibTeX
- Tools → Plugins → nainštalovať Better BibTeX `.xpi`
- Zotero → Settings → Better BibTeX
- zapni stabilné citekeys
- nastav auto-export kolekcie `Diplomovka` do `references/zotero-thesis.bib`
- pri exporte zaškrtni `Keep updated`

## 1. Odporúčaný citekey formát

Používaj tvar:
- `autorRokKlucoveSlovo`

Konkrétne citekeys pre úvod:
- `obradovich2024llmpsychiatry`
- `meng2024llmmedicine`
- `ajluni2025psychiatriceducation`
- `yu2025simulatedpatientsystems`
- `brugge2024patientsimulation`
- `evans2015vignettes`
- `baguley2022vignettedata`
- `williams2017simulationmentalhealth`
- `dawood2024standardizedpatient`
- `kennedy2008coresymptoms`
- `maj2020depressioncharacterization`
- `kroenke2001phq9`
- `guidi2011clinicalinterviewdepression`
- `roustan2025cliniciansguide`
- `asgari2025hallucinationframework`

## 2. Najrýchlejší import: čo zadať do Add Item by Identifier

Tieto zdroje vieš pridať priamo cez magic wand v Zotere:

### Cez PMID
- `11556941` → `kroenke2001phq9`
- `20975323` → `guidi2011clinicalinterviewdepression`

## 3. Cez Zotero Connector z webstránky článku

Pre tieto zdroje je najpraktickejšie otvoriť stránku článku v prehliadači a uložiť ju cez Zotero Connector:
- `obradovich2024llmpsychiatry`
- `meng2024llmmedicine`
- `ajluni2025psychiatriceducation`
- `yu2025simulatedpatientsystems`
- `brugge2024patientsimulation`
- `evans2015vignettes`
- `baguley2022vignettedata`
- `williams2017simulationmentalhealth`
- `dawood2024standardizedpatient`
- `kennedy2008coresymptoms`
- `maj2020depressioncharacterization`
- `roustan2025cliniciansguide`
- `asgari2025hallucinationframework`

### Praktický postup
1. otvor článok v PMC / PubMed / na stránke vydavateľa
2. klikni na ikonu Zotero Connector
3. ulož do kolekcie `Diplomovka > 01 Úvod`
4. skontroluj typ záznamu (`Journal Article`)
5. skontroluj autorov, rok, názov časopisu, volume/issue/pages, DOI
6. ak sa pripojilo PDF, nechaj ho; ak nie, nevadí

## 4. Čo skontrolovať ručne po importe

Pri každom zdroji skontroluj:
- `Item Type` = `Journal Article`
- `Title`
- `Authors`
- `Publication`
- `Year`
- `Volume`
- `Issue`
- `Pages` alebo article number
- `DOI` (ak je dostupné)
- `Abstract` (voliteľné, ale užitočné)
- `Extra` pole nech je čisté, ak tam vedome nedávaš citekey override

## 5. Ako uzamknúť citekeys

Po importe každému záznamu nastav alebo skontroluj citekey podľa `intro_source_map_zotero.md`.

Ak Better BibTeX citekey negeneruje presne tak, ako chceš, uprav ho ručne v citekey poli BBT alebo cez BBT-managed citekey workflow.

Dôležité:
- po prvom použití citekey už názov nemeň bez dôvodu
- citekey musí sedieť s markdown draftom
- po zmene skontroluj, že sa prepísal aj `zotero-thesis.bib`

## 6. Minimum jadro pre úvod, ak sa ponáhľaš

Najprv importuj len týchto 10 zdrojov:
- `obradovich2024llmpsychiatry`
- `ajluni2025psychiatriceducation`
- `evans2015vignettes`
- `williams2017simulationmentalhealth`
- `kennedy2008coresymptoms`
- `maj2020depressioncharacterization`
- `kroenke2001phq9`
- `guidi2011clinicalinterviewdepression`
- `roustan2025cliniciansguide`
- `asgari2025hallucinationframework`

Až potom doplň zvyšok.

## 7. Rýchly kontrolný test po importe

Po importe urob tieto 4 kontroly:
1. V Zotere v kolekcii `01 Úvod` vidíš všetky zdroje.
2. `references/zotero-thesis.bib` obsahuje správne citekeys.
3. `manuscript/20_introduction.md` nemá citekeys, ktoré v `.bib` chýbajú.
4. Vo Worde vieš vložiť aspoň jednu testovaciu citáciu cez Zotero plugin.

## 8. Keď niečo zlyhá

### Identifier nič nenašiel
- skús PMID bez prefixu
- ak to stále nejde, otvor PubMed alebo PMC stránku a ulož cez Connector

### Connector uloží len web page
- otvor radšej abstrakt článku na PubMed alebo landing page článku u vydavateľa
- potom skontroluj, či sa typ preložil ako `Journal Article`

### Citekey v `.bib` nesedí s draftom
- oprav citekey v Zotere
- počkaj na auto-export alebo spusti export znova ručne

## 9. Po importe pokračuj takto

- doplň krátke poznámky do `notes/literature/`
- v `20_introduction.md` nechaj citekeys v tvare `[@citekey]`
- finálne citácie rieš až vo Worde cez Zotero plugin
