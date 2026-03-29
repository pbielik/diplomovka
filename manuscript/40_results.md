# 40 Results / Výsledky

> Táto kapitola je pripravená ako reálna kostra výsledkov s thesis-ready formuláciami. Finálna verzia sa doplní po importe dát, behu R pipeline a vložení tabuliek a grafov.

## 3 Výsledky

### 3.1 Logika prezentácie výsledkov

Výsledky sú prezentované v logike, ktorá zodpovedá analytickému plánu výskumu. Najprv uvádzam základné charakteristiky datasetu a ratingového nástroja, následne prezentujem výsledky reliabilitných a deskriptívnych analýz a potom výsledky inferenčných modelov viazaných na jednotlivé hypotézy. V závere kapitoly uvádzam exploratórne výsledky súvisiace s odhadovaným pôvodom rozhovorov a otvorenými komentármi hodnotiteľov.

### 3.2 Charakteristika datasetu a základné deskriptíva

Do finálnej analýzy bolo zaradených **[doplniť počet]** hodnotiteľov, ktorí spolu vytvorili **[doplniť počet]** platných ratingov. Hodnotených bolo 72 transkriptov generovaných z 12 seed scenárov a 6 experimentálnych variantov. Priemerný počet hodnotení na jeden transkript bol **[doplniť]**. Základné charakteristiky datasetu uvádza Tabuľka 1.

**Sem vlož:**
- tabuľku s počtom raterov, počtom ratingov, počtom transcriptov
- rozdelenie podľa guardrail a profile
- prípadne priemernú dĺžku hodnotenia a počet turnov

### 3.3 Frekvenčné rozdelenie odpovedí a vnútorná konzistencia

Najprv boli analyzované frekvenčné rozdelenia odpovedí na hlavné položky ratingového nástroja. Tento krok umožnil získať prehľad o tom, ako boli využívané jednotlivé odpoveďové kategórie a či niektoré položky nevykazovali príliš jednostranné rozdelenie odpovedí. Frekvenčné analýzy preukázali, že **[doplniť stručné zhrnutie, napr. položky G1–G5 využívali celé spektrum odpovedí / defect položky boli skôr nízke / niektoré A domény boli systematicky vyššie]**.

V ďalšom kroku bola analyzovaná vnútorná konzistencia vybraných blokov položiek. Blok `G1–G5` dosiahol **[doplniť α / ω]**, plausibility blok `G1`, `G3`, `G4` dosiahol **[doplniť α / ω]** a blok `R1–R5` dosiahol **[doplniť α / ω]**. Tieto výsledky naznačujú, že **[doplniť interpretáciu: kompozity boli / neboli dostatočne konzistentné pre ďalšie použitie]**.

**Sem vlož:**
- tabuľku reliabilít
- prípadne tabuľku item-total korelácií

### 3.4 Interrater reliabilita

Interrater reliabilita bola vyhodnotená pre hlavné kompozitné ukazovatele, najmä `plausibility_index`, `defect_index` a `symptom_error_mean`. Hodnoty ICC naznačili, že zhoda medzi hodnotiteľmi bola **[doplniť: nízka / stredná / dobrá]** pri `plausibility_index`, **[doplniť]** pri `defect_index` a **[doplniť]** pri `symptom_error_mean`. Výsledky podporujú záver, že **[doplniť stručnú interpretáciu: aspoň časť kompozitov bola dostatočne stabilná pre inferenčnú analýzu / zhoda bola limitovaná a preto treba interpretovať opatrne]**.

### 3.5 Primárne outcome-y

#### 3.5.1 H1: Vplyv guardrailu na klinickú plausibilitu

Na overenie hypotézy H1 bol použitý lineárny zmiešaný model s `plausibility_index` ako závislou premennou, fixnými efektmi `guardrail`, `profile` a ich interakcie a náhodnými interceptmi pre `seed_id` a `rater_id`. Výsledky ukázali, že efekt guardrailu bol **[doplniť: štatisticky významný / nevýznamný]**, pričom rozhovory generované s aktívnym guardrailom dosahovali **[vyššie / porovnateľné / nižšie]** hodnoty klinickej plausibility než rozhovory bez guardrailu. Hypotéza H1 bola preto **[podporená / nepodporená / podporená čiastočne]**.

Okrem kompozitu boli analyzované aj jednotlivé položky `G1`, `G3` a `G4`. Na úrovni položiek sa ukázalo, že **[doplniť stručné zistenie]**.

#### 3.5.2 H2: Vplyv guardrailu na defect index

Na overenie hypotézy H2 bol použitý zmiešaný model s `defect_index` ako závislou premennou. Výsledky ukázali, že rozhovory generované s aktívnym guardrailom vykazovali **[nižšiu / porovnateľnú / vyššiu]** mieru defektov než rozhovory bez guardrailu. Efekt guardrailu bol **[doplniť]**. Hypotéza H2 bola **[podporená / nepodporená / podporená čiastočne]**.

Na úrovni jednotlivých položiek sa najvýraznejší rozdiel objavil pri **[doplniť R položky]**, zatiaľ čo pri položkách **[doplniť]** sa efekt nepreukázal.

#### 3.5.3 H3: Vplyv realizačného profilu na prirodzenosť jazyka

Hypotéza H3 predpokladala, že rozvinutejší realizačný profil `R3` bude spojený s vyššou prirodzenosťou jazyka než profily `R1` a `R2`. Analýza položky `G2` ukázala, že profil mal **[doplniť: významný / nevýznamný]** efekt. Rozhovory v profile `R3` boli hodnotené ako **[prirodzenejšie / rovnako prirodzené / menej prirodzené]** než rozhovory v profiloch `R1` a `R2`. Hypotéza H3 bola **[podporená / nepodporená / podporená čiastočne]**.

#### 3.5.4 H4: Interakcia guardrail × profile

Hypotéza H4 predpokladala interakčný efekt medzi guardrailom a realizačným profilom, pričom priaznivý efekt guardrailu sa mal prejaviť výraznejšie pri profile `R3`. Výsledky ukázali, že interakcia bola **[doplniť]** pri `plausibility_index` a **[doplniť]** pri `defect_index`. Ak bola interakcia prítomná, naznačovala, že **[doplniť stručnú interpretáciu]**.

**Sem vlož:**
- tabuľku hlavných mixed modelov
- graf odhadovaných marginálnych priemerov pre plausibility_index
- graf pre defect_index a/alebo G2

### 3.6 Sekundárne outcome-y

#### 3.6.1 H5: Symptom fidelity voči seed anchorom

Hypotéza H5 predpokladala, že rozhovory generované s aktívnym guardrailom budú presnejšie zodpovedať seed anchorom. Na jej overenie boli použité error-based premenné `symptom_error_mean`, `severity_error` a `impact_error`.

Výsledky ukázali, že guardrail mal **[doplniť]** efekt na `symptom_error_mean`, pričom rozhovory s aktívnym guardrailom vykazovali **[nižšiu / porovnateľnú / vyššiu]** priemernú absolútnu chybu voči seed anchorom. Podobne bol efekt guardrailu **[doplniť]** aj pri `severity_error` a `impact_error`. Hypotéza H5 bola preto **[podporená / nepodporená / podporená čiastočne]**.

Na úrovni jednotlivých symptomatických domén sa ukázalo, že najvyššia zhoda bola pri oblastiach **[doplniť]**, zatiaľ čo najproblematickejšie boli oblasti **[doplniť]**.

### 3.7 Explorácie

#### 3.7.1 H6: Súvislosť plausibility, defectov a vnímaného pôvodu rozhovoru

Hypotéza H6 predpokladala, že vyššia klinická plausibilita a nižšia miera defektov budú spojené s vyššou tréningovou použiteľnosťou rozhovoru a s nižšou pravdepodobnosťou, že bude rozhovor označený ako `ai_generated`. Výsledky ukázali, že `plausibility_index` bol **[doplniť: pozitívne / nevýznamne]** asociovaný s `G5`, zatiaľ čo `defect_index` bol s `G5` asociovaný **[negatívne / nevýznamne]**.

Pri položke `guessed_origin` sa ukázalo, že rozhovory s vyššou plausibilitou a nižším defect indexom boli **[menej / rovnako / viac]** často označované ako `ai_generated`. Tieto výsledky naznačujú, že **[doplniť stručnú interpretáciu]**.

#### 3.7.2 Otvorené komentáre hodnotiteľov

Otvorené komentáre boli analyzované stručným tematickým kódovaním. Najčastejšie sa objavovali tri typy postrehov:
1. **[doplniť tému, napr. primeraná klinická logika]**
2. **[doplniť tému, napr. šablónovitosť alebo priveľmi učebnicové formulácie]**
3. **[doplniť tému, napr. slabší súlad medzi symptomatikou a osobným kontextom]**

Tieto komentáre dopĺňajú kvantitatívne výsledky tým, že ukazujú, v čom hodnotitelia spontánne videli silné a slabé stránky rozhovorov.

### 3.8 Stručné zhrnutie výsledkov

Výsledky naznačili, že **[doplniť: guardrail bol / nebol prínosný pre klinickú plausibilitu]**, že realizačný profil ovplyvňoval najmä **[prirodzenosť / defecty / oboje]** a že zhoda so seed anchorami bola **[doplniť]**. Pilotný charakter štúdie zároveň ukázal, že ratingový rámec je použiteľný aj na systematické porovnávanie variantov generovania a že jeho ďalšie rozšírenie by mohlo podporiť budúci výskum v tejto oblasti.
