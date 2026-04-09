# 40 Results / Výsledky

> Táto kapitola je pripravená ako placeholder kostra zosynchronizovaná s Úvodom (`H1`–`H9`, `VO1`–`VO8`) a s analytickým plánom v Metóde (časť 2.8). Finálne hodnoty, tabuľky a grafy sa doplnia po vyčistení dát v `analysis/data_clean/`, behu pipeline `analysis/scripts/thesis_rating_pipeline.R` a vygenerovaní výstupov do `analysis/outputs/`, `tables/` a `figures/`.

## 3 Výsledky

### 3.1 Logika prezentácie výsledkov

Výsledky sú prezentované po blokoch outcome-ov a v poradí, ktoré zodpovedá Úvodu aj Metóde: najprv deskriptívny blok globálnej kvality interview a symptom fidelity (`VO1`, `VO2`), potom blok kvality merania a zhody (`VO6`), následne konfirmačný blok efektu `guardrail` (`H1`–`H5`, priamy príspevok k `VO1` a `VO2`), rozšírený blok efektu `profile` a interakcie `guardrail × profile` (`VO3`–`VO5`, `H6`–`H9`) a napokon doplnkový exploračný blok (`VO7`, `VO8`). Takéto radenie sleduje logiku skúmaných premenných, nie technickú náročnosť štatistických postupov.

Explicitné mapovanie výskumných otázok na výsledkové bloky je v tejto placeholder verzii nasledovné:

- `VO1`: sekcie 3.2, 3.3, 3.5.1, 3.5.2 a 3.5.5.
- `VO2`: sekcie 3.2, 3.3 a 3.5.4.
- `VO3`: sekcie 3.6.1 a 3.6.2.
- `VO4`: sekcia 3.6.3 vrátane `profile` kontrastov pre `symptom_error_mean`, `severity_error`, `impact_error` a `defect_index`.
- `VO5`: sekcia 3.6.4.
- `VO6`: sekcia 3.4.
- `VO7`: sekcia 3.7.1.
- `VO8`: sekcia 3.7.2.

V texte reportujeme len číselné údaje, ktoré sú nevyhnutné pre interpretáciu hypotéz a výskumných otázok. Rozsiahlejšie výstupy sú umiestnené do tabuliek a grafov, aby sa údaje zbytočne neopakovali. Pri každom inferenčnom výsledku uvádzame popri `p`-hodnote aj odhad efektu, jeho 95 % interval spoľahlivosti a vecnú interpretáciu smeru a veľkosti rozdielu.

### 3.2 Charakteristika datasetu a základné deskriptíva (`VO1`, deskriptívna časť `VO2`)

Do finálnej analýzy bolo zaradených **[doplniť počet hodnotiteľov]** hodnotiteľov, ktorí spolu vytvorili **[doplniť počet ratingov]** platných ratingov. Hodnotených bolo 72 transkriptov vygenerovaných z 12 seed scenárov a 6 experimentálnych variantov (2 úrovne `guardrail` × 3 úrovne `profile`). Priemerný počet hodnotení na jeden transkript bol **[doplniť priemer]** (`SD` = **[doplniť]**, rozsah **[doplniť]**–**[doplniť]**). Základné charakteristiky datasetu sú uvedené v Tabuľke 1.

Deskriptívne ukazovatele primárnych a sekundárnych premenných sumarizuje Tabuľka 2. Pre ordinálne položky sú uvedené mediány a interkvartilové rozpätia, pre kompozity `plausibility_index`, `defect_index`, `symptom_error_mean`, `severity_error` a `impact_error` aj priemery a smerodajné odchýlky.

> Doplniť:
> - **Tabuľka 1** — počet hodnotiteľov, počet ratingov, počet transkriptov, rozdelenie ratingov podľa `guardrail` a `profile`, priemerný počet ratingov na transkript a na hodnotiteľa.
> - **Tabuľka 2** — deskriptívne ukazovatele pre `G1`–`G5`, `A1`–`A9`, `S1`, `S2`, `R1`–`R5`, `plausibility_index`, `defect_index`, `symptom_error_mean`, `severity_error`, `impact_error` (medián, IQR, prípadne priemer a SD podľa typu premennej).
> - **Obrázok 1** — histogramy alebo boxploty `plausibility_index` a `defect_index` podľa kombinácií `guardrail × profile`.

### 3.3 Frekvenčné rozdelenie a vnútorná konzistencia ratingového nástroja (`VO1`, meracia opora pre `VO2`)

Ako prvý analytický krok bolo zostavené frekvenčné rozdelenie odpovedí na položky `G1`–`G5`, `A1`–`A9`, `S1`, `S2` a `R1`–`R5`. Cieľom tohto kroku bolo posúdiť, či hodnotitelia využívali celé spektrum odpoveďových kategórií a či niektoré položky nevykazovali systematicky jednostranné rozdelenie. Frekvenčné analýzy ukázali, že **[doplniť stručné zhrnutie využitia škál: napr. položky `G1`–`G5` pokrývali celé spektrum / niektoré položky `R` boli koncentrované v dolných kategóriách / vybrané `A` domény vykazovali zreteľný strop alebo dno]**.

Vnútorná konzistencia bola vyhodnocovaná pre tri obsahovo definované bloky položiek v súlade s Metódou (2.8.3) [@terwee2018COSMINMethodologyEvaluating; @marko2016VyuzitieZneuzitieCronbachovej]:

- blok `G1`–`G5`: Cronbachovo α = **[doplniť]**, McDonaldovo ω = **[doplniť]**;
- plausibility blok `G1`, `G3`, `G4`: α = **[doplniť]**, ω = **[doplniť]**;
- blok `R1`–`R5`: α = **[doplniť]**, ω = **[doplniť]**.

Tieto výsledky naznačujú, že kompozity `plausibility_index` a `defect_index` boli **[doplniť: dostatočne / iba čiastočne / nedostatočne]** vnútorne konzistentné pre ďalšie použitie v inferenčnej analýze.

> Doplniť:
> - **Tabuľka 3** — frekvenčné rozdelenia kľúčových položiek (najmä `G1`–`G5` a `R1`–`R5`).
> - **Tabuľka 4** — vnútorná konzistencia (α a ω) pre tri bloky a stručné item-total korelácie len pre tie položky, ktorých vyradenie by α/ω významne zmenilo.

### 3.4 Interrater reliabilita (`VO6`)

Interrater reliabilita bola vyhodnotená pre hlavné kompozitné ukazovatele `plausibility_index`, `defect_index` a `symptom_error_mean` prostredníctvom intraclass correlation coefficient (ICC) v súlade s analytickým plánom v časti 2.8.4 Metódy [@mchugh2012InterraterReliabilityKappa; @nelson2015manyratersordinal]. V reporte uvádzame zvolený typ ICC (model **[doplniť: 2,k / 3,k / iný]**, **[doplniť: konzistencia / absolútna zhoda]**, **[doplniť: single / average measures]**) a interpretačnú kategóriu zhody.

Hodnoty ICC dosiahli **[doplniť hodnotu]** pri `plausibility_index` (95 % CI **[doplniť]**), **[doplniť]** pri `defect_index` (95 % CI **[doplniť]**) a **[doplniť]** pri `symptom_error_mean` (95 % CI **[doplniť]**). Tieto hodnoty zodpovedajú interpretačnej kategórii **[doplniť: nízka / stredná / dobrá / výborná]** zhody pri prvom kompozite, **[doplniť]** zhody pri druhom a **[doplniť]** zhody pri treťom. Výsledky podporujú záver, že **[doplniť stručnú interpretáciu: aspoň časť kompozitov bola dostatočne stabilná pre inferenčnú analýzu / zhoda bola limitovaná a inferenčné výsledky treba interpretovať opatrne]**.

> Doplniť:
> - **Tabuľka 5** — hodnoty ICC, 95 % CI a interpretačné kategórie pre `plausibility_index`, `defect_index` a `symptom_error_mean`.

### 3.5 Jadrové výsledky: efekt štruktúrujúceho klinického usmernenia (`H1`–`H5`, priamy príspevok k `VO1` a `VO2`)

Jadrové hypotézy boli overované pomocou lineárnych zmiešaných modelov (pre kompozity a error-based ukazovatele) a ordinal cumulative link mixed modelov (pre jednotlivé ordinálne položky), ktorých všeobecná špecifikácia je uvedená v časti 2.8.5 Metódy [@hedeker2016MixedeffectsLocationScaleModel; @christensenCumulativeLinkModels]:

```
outcome ~ guardrail * profile + (1 | seed_id) + (1 | rater_id)
```

#### 3.5.1 `H1` — Klinická plausibilita (`plausibility_index`)

`H1` predpokladala, že interview vytvorené s aktívnym `guardrail = on` budú odbornými hodnotiteľmi posudzované ako klinicky vierohodnejšie než interview s `guardrail = off`, a to na úrovni `plausibility_index` aj jednotlivých položiek `G1`, `G3` a `G4`.

Model pre `plausibility_index` ukázal, že hlavný efekt `guardrail` bol **[doplniť: štatisticky významný / nevýznamný]** (`b` = **[doplniť]**, 95 % CI **[doplniť]**, `p` = **[doplniť]**). Odhadované marginálne priemery dosiahli **[doplniť hodnotu]** pre `guardrail = on` a **[doplniť hodnotu]** pre `guardrail = off`. Hypotéza `H1` bola na úrovni kompozitu **[podporená / nepodporená / podporená čiastočne]**.

Doplnkové ordinálne modely pre jednotlivé položky `G1`, `G3` a `G4` ukázali, že efekt `guardrail` bol **[doplniť stručné zistenie pre jednotlivé položky]**, čo umožňuje lokalizovať, či sa prípadný hlavný efekt prejavil najmä vo vierohodnosti, vnútornej konzistencii alebo symptomatickom súlade.

> Doplniť:
> - Tabuľku odhadov pre `plausibility_index` (hlavné efekty `guardrail`, `profile`, interakcia, varianty náhodných efektov).
> - Stĺpcový alebo bodový graf odhadovaných marginálnych priemerov `plausibility_index` podľa `guardrail × profile`.

#### 3.5.2 `H2` — Prirodzenosť a vnútorná konzistencia (`G2`)

`H2` predpokladala, že interview s aktívnym `guardrail` budú prirodzenejšie a vnútorne konzistentnejšie, najmä na položke `G2`. Cumulative link mixed model pre `G2` ukázal, že efekt `guardrail` bol **[doplniť: významný / nevýznamný]** (odhad **[doplniť]**, 95 % CI **[doplniť]**, `p` = **[doplniť]**) v smere **[vyššej / porovnateľnej / nižšej]** prirodzenosti pri `guardrail = on`. Hypotéza `H2` bola **[podporená / nepodporená / podporená čiastočne]**.

> Doplniť:
> - Tabuľku odhadov ordinálneho modelu pre `G2`.
> - Krátky graf alebo mosaic plot rozdelenia kategórií `G2` podľa `guardrail`.

#### 3.5.3 `H3` — Defect index (`defect_index`, `R1`–`R5`)

`H3` predpokladala, že interview s aktívnym `guardrail` budú obsahovať menej red flags a iných problematických prvkov, a to na úrovni `defect_index` aj jednotlivých položiek `R1`–`R5`.

Lineárny zmiešaný model pre `defect_index` ukázal hlavný efekt `guardrail` **[doplniť: významný / nevýznamný]** (`b` = **[doplniť]**, 95 % CI **[doplniť]**, `p` = **[doplniť]**). Interview s `guardrail = on` vykazovali **[nižšiu / porovnateľnú / vyššiu]** mieru defektov než interview s `guardrail = off`. Hypotéza `H3` bola na úrovni kompozitu **[podporená / nepodporená / podporená čiastočne]**.

Na úrovni jednotlivých položiek sa najvýraznejší rozdiel objavil pri **[doplniť konkrétne `R` položky]**, zatiaľ čo pri položkách **[doplniť]** sa efekt nepreukázal. Tieto položkové výsledky uvádzame ako spresnenie hlavného kompozitového výsledku.

> Doplniť:
> - Tabuľku odhadov pre `defect_index`.
> - Položkové porovnanie len pre tie `R` položky, kde efekt zmysluplne dopĺňa interpretáciu kompozitu.

#### 3.5.4 `H4` — Symptom fidelity voči seed anchorom (`symptom_error_mean`, `severity_error`, `impact_error`)

`H4` predpokladala, že interview s aktívnym `guardrail` budú symptomaticky primeranejšie vzhľadom na cieľový seed scenár než interview bez tohto usmernenia, a to na úrovni `symptom_error_mean`, `severity_error` a `impact_error`.

Lineárne zmiešané modely ukázali, že hlavný efekt `guardrail` bol **[doplniť]** pri `symptom_error_mean` (`b` = **[doplniť]**, 95 % CI **[doplniť]**, `p` = **[doplniť]**), **[doplniť]** pri `severity_error` (`b` = **[doplniť]**, 95 % CI **[doplniť]**, `p` = **[doplniť]**) a **[doplniť]** pri `impact_error` (`b` = **[doplniť]**, 95 % CI **[doplniť]**, `p` = **[doplniť]**). Interview s `guardrail = on` vykazovali **[nižšiu / porovnateľnú / vyššiu]** priemernú absolútnu chybu voči seed anchorom. Hypotéza `H4` bola **[podporená / nepodporená / podporená čiastočne]**.

Doplnkovo, na úrovni jednotlivých symptomatických domén `A1`–`A9`, najvyššia zhoda so seed anchorami bola pri oblastiach **[doplniť]**, zatiaľ čo najproblematickejšie boli oblasti **[doplniť]**. Tieto doménové výsledky interpretujeme ako spresnenie hlavného error-based výsledku, nie ako samostatnú hypotetickú vetvu.

> Doplniť:
> - Tabuľku odhadov pre `symptom_error_mean`, `severity_error` a `impact_error`.
> - Doménový prehľad priemerných absolútnych chýb pre `A1`–`A9`.

#### 3.5.5 `H5` — Tréningová použiteľnosť (`G5`)

`H5` predpokladala, že interview s aktívnym `guardrail` budú odbornými hodnotiteľmi posudzované ako použiteľnejšie na tréningové alebo výučbové účely, a to na úrovni položky `G5`. Cumulative link mixed model pre `G5` ukázal, že efekt `guardrail` bol **[doplniť: významný / nevýznamný]** (odhad **[doplniť]**, 95 % CI **[doplniť]**, `p` = **[doplniť]**), pričom interview s `guardrail = on` boli posudzované ako **[použiteľnejšie / porovnateľne použiteľné / menej použiteľné]** než interview s `guardrail = off`. Hypotéza `H5` bola **[podporená / nepodporená / podporená čiastočne]**.

> Doplniť:
> - Tabuľku odhadov ordinálneho modelu pre `G5`.

### 3.6 Rozšírené výsledky: efekt štýlu odpovedania a interakcia (`Blok B` a `Blok C`; `VO3`–`VO5`, `H6`–`H9`)

Rozšírené hypotézy `H6`–`H9` sa týkajú efektu premennej `profile` (štýl odpovedania simulovaného pacienta na úrovniach `R1`, `R2`, `R3`) a interakcie `guardrail × profile`. V logike Úvodu a Metódy ide o pokračovanie **Bloku B** (`VO3`, `VO4`, `H6`–`H8`) a **Bloku C** (`VO5`, `H9`), pričom `VO6`–`VO8` ostávajú mimo tejto hypotetickej vetvy.

#### 3.6.1 `H6` — Profile a klinická plausibilita (`VO3`)

`H6` predpokladala, že interview s vyváženým alebo rozvinutým štýlom odpovedania (`profile = R2` alebo `R3`) budú klinicky vierohodnejšie než interview so zdržanlivým štýlom (`profile = R1`), a to na úrovni `plausibility_index`.

Hlavný efekt `profile` v modeli pre `plausibility_index` bol **[doplniť: významný / nevýznamný]** (`F` = **[doplniť]** alebo `LR` = **[doplniť]**, `p` = **[doplniť]**). Kontrasty `R2` vs. `R1` a `R3` vs. `R1` ukázali odhady **[doplniť]** a **[doplniť]** (95 % CI **[doplniť]** a **[doplniť]**). Hypotéza `H6` bola **[podporená / nepodporená / podporená čiastočne]**.

#### 3.6.2 `H7` — Profile a prirodzenosť/použiteľnosť (`G2`, `G5`, `VO3`)

`H7` predpokladala, že interview s rozvinutejším štýlom odpovedania (`profile = R3`) budú prirodzenejšie a tréningovo použiteľnejšie než interview so zdržanlivejším štýlom (`profile = R1`, `R2`), najmä na položkách `G2` a `G5`. Ordinal mixed modely ukázali, že efekt `profile` bol **[doplniť]** pre `G2` a **[doplniť]** pre `G5`. Kontrast `R3` vs. `R1`/`R2` bol **[doplniť]** pre `G2` a **[doplniť]** pre `G5`. Hypotéza `H7` bola **[podporená / nepodporená / podporená čiastočne]**.

#### 3.6.3 `H8` — Profile, symptomatická presnosť a red flags (`VO4`)

`H8` predpokladala, že interview s rozvinutejším štýlom odpovedania (`profile = R3`) budú poskytovať symptomaticky bohatší a presnejší obraz prípadu než interview so zdržanlivejším štýlom (`profile = R1`), teda budú mať nižší `symptom_error_mean`. Primárne testovaným outcome tejto hypotézy bol preto `symptom_error_mean`. Keďže `VO4` je formulovaná širšie, v tejto podsekcii budú v skrátenej podobe reportované aj hlavné efekty `profile` pre `severity_error`, `impact_error` a `defect_index`, aj keď pre tieto výstupy nebola formulovaná samostatná smerová hypotéza.

Lineárny zmiešaný model ukázal, že efekt `profile` na `symptom_error_mean` bol **[doplniť]** (`F` = **[doplniť]**, `p` = **[doplniť]**). Kontrast `R3` vs. `R1` bol **[doplniť]** (95 % CI **[doplniť]**). Hypotéza `H8` bola **[podporená / nepodporená / podporená čiastočne]**. Na úrovni širšie formulovanej `VO4` bol hlavný efekt `profile` **[doplniť]** aj pri `severity_error`, **[doplniť]** pri `impact_error` a **[doplniť]** pri `defect_index`, čo ukáže, či sa efekt štýlu odpovedania prejavuje iba v symptom fidelity, alebo aj v kvalite problematických prvkov rozhovoru.

#### 3.6.4 `H9` — Interakcia `guardrail × profile` (`VO5`)

`H9` predpokladala, že pozitívny účinok štruktúrujúceho klinického usmernenia bude výraznejší pri rozvinutejšom štýle odpovedania (`profile = R3`), najmä pri `plausibility_index` a `defect_index`.

Interakčný člen `guardrail × profile` bol pri `plausibility_index` **[doplniť: významný / nevýznamný]** (`p` = **[doplniť]**) a pri `defect_index` **[doplniť]** (`p` = **[doplniť]**). Aby bola explicitne uzavretá aj `VO5`, v tejto podsekcii sa doplnkovo uvedie, či sa analogický vzor interakcie objavil aj pri `symptom_error_mean`, `severity_error` a `impact_error`. Ak interakcia bola prítomná, jej smer naznačoval, že **[doplniť stručnú interpretáciu vzoru: napr. najvyššia plausibilita pri kombinácii `guardrail = on` a `profile = R3` / efekt `guardrail` je viditeľný len pri `R3`]**. Hypotéza `H9` bola **[podporená / nepodporená / podporená čiastočne]**.

> Doplniť:
> - **Tabuľka 6** — súhrn odhadov mixed modelov pre `plausibility_index`, `defect_index`, `symptom_error_mean`, `severity_error` a `impact_error` (hlavné efekty + interakcia).
> - **Obrázok 2** — odhadované marginálne priemery `plausibility_index` a `defect_index` podľa kombinácií `guardrail × profile` s 95 % CI.

### 3.7 Doplnkové a exploratórne analýzy (`VO7`, `VO8`)

#### 3.7.1 Vnímaný pôvod rozhovoru (`guessed_origin`, `guess_confidence`) — `VO7`

Položka `guessed_origin` zachytávala odhad hodnotiteľa, či ide o rozhovor AI-generovaný, ľudsky simulovaný, reálny alebo nejednoznačný. Frekvenčné rozdelenie odpovedí ukázalo, že hodnotitelia označili rozhovory ako `ai_generated` v **[doplniť %]** prípadov, ako `human_simulated` v **[doplniť %]**, ako `real` v **[doplniť %]** a ako `ambiguous` v **[doplniť %]** prípadov.

V exploratórnom logistickom modeli nad binarizovanou premennou „vnímané ako AI vs. nie AI" boli ako prediktory zaradené `plausibility_index` a `defect_index`. Vyššia hodnota `plausibility_index` bola spojená s **[doplniť: nižšou / porovnateľnou / vyššou]** pravdepodobnosťou označenia rozhovoru ako `ai_generated` (`OR` = **[doplniť]**, 95 % CI **[doplniť]**), zatiaľ čo vyššia hodnota `defect_index` bola spojená s **[doplniť: vyššou / porovnateľnou / nižšou]** pravdepodobnosťou tohto označenia (`OR` = **[doplniť]**, 95 % CI **[doplniť]**).

Položka `guess_confidence` zachytávala istotu odhadu pôvodu. Cumulative link mixed model ukázal, že istota odhadu bola **[doplniť: vyššia / porovnateľná / nižšia]** pri rozhovoroch s vyšším `plausibility_index` a **[doplniť]** pri rozhovoroch s vyšším `defect_index`.

> Doplniť:
> - Frekvenčný prehľad kategórií `guessed_origin` celkovo aj podľa kombinácií `guardrail × profile`.
> - Stručnú tabuľku logistického modelu pre binarizovanú `guessed_origin`.

#### 3.7.2 Otvorené komentáre (`comment`) — `VO8`

Otvorené komentáre v premennej `comment` boli analyzované stručným tematickým kódovaním v súlade s časťou 2.8.6 Metódy. Cieľom nebolo vytvoriť samostatnú kvalitatívnu líniu, ale pomenovať opakujúce sa dôvody pozitívneho a negatívneho hodnotenia, ktoré dopĺňajú kvantitatívne výsledky.

Najčastejšie pozitívne témy boli:

1. **[doplniť tému, napr. primeraná klinická logika a tematická pokrytosť]** — výskyt v **[doplniť počet]** komentároch;
2. **[doplniť tému, napr. zrozumiteľný a empatický jazyk klinika]** — výskyt v **[doplniť počet]** komentároch;
3. **[doplniť tému]** — výskyt v **[doplniť počet]** komentároch.

Najčastejšie negatívne témy boli:

1. **[doplniť tému, napr. šablónovitosť alebo priveľmi učebnicové formulácie]** — výskyt v **[doplniť počet]** komentároch;
2. **[doplniť tému, napr. slabší súlad medzi symptomatikou a osobným kontextom]** — výskyt v **[doplniť počet]** komentároch;
3. **[doplniť tému]** — výskyt v **[doplniť počet]** komentároch.

> Doplniť:
> - Stručnú tabuľku tém a frekvencií, ideálne s 1–2 ilustračnými citátmi pre každú tému (anonymizovane).

### 3.8 Stručné zhrnutie výsledkov

Výsledky na úrovni jadrových hypotéz naznačili, že efekt `guardrail` bol **[doplniť: prítomný / čiastočne prítomný / neprítomný]** pri `plausibility_index` (`H1`), **[doplniť]** pri `G2` (`H2`), **[doplniť]** pri `defect_index` (`H3`), **[doplniť]** pri error-based ukazovateľoch `symptom_error_mean`, `severity_error` a `impact_error` (`H4`) a **[doplniť]** pri `G5` (`H5`). Na úrovni rozšírených hypotéz boli efekty `profile` (`H6`–`H8`) **[doplniť: konzistentné / zmiešané / nepodporené]** a interakcia `guardrail × profile` (`H9`) bola **[doplniť: prítomná / čiastočne prítomná / nepodporená]**. Interrater reliabilita pre hlavné kompozity bola **[doplniť stručne]**, čo **[podporuje / čiastočne podporuje / oslabuje]** dôveru v inferenčné výsledky.

Záverečné zhrnutie tu zostáva vecné a sumarizačné: odpovedá na hypotézy `H1`–`H9` a výskumné otázky `VO1`–`VO8`, no neprináša novú interpretáciu — tá patrí až do kapitoly Diskusia.
