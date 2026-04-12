# 40 Results / Výsledky

> Táto kapitola je pripravená ako placeholder kostra zosynchronizovaná s Úvodom (H1 až H9, VO1 až VO8) a s analytickým plánom v Metóde (časť 2.8). Finálne hodnoty, tabuľky a grafy sa doplnia po vyčistení dát v priečinku analysis/data_clean, po behu pipeline analysis/scripts/thesis_rating_pipeline.R a po vygenerovaní výstupov do priečinkov analysis/outputs, tables a figures.

## 3 Výsledky

### 3.1 Logika prezentácie výsledkov

Výsledky sú prezentované po blokoch skúmaných premenných a v poradí, ktoré zodpovedá Úvodu aj Metóde. Najprv nasleduje deskriptívny blok globálnej kvality rozhovorov a symptomatickej primeranosti (VO1, VO2), potom blok kvality merania a zhody medzi hodnotiteľmi (VO6), následne konfirmačný blok efektu prítomnosti štruktúrujúceho klinického usmernenia (H1 až H5, priamy príspevok k VO1 a VO2), rozšírený blok efektu štýlu odpovedania simulovaného pacienta a interakcie oboch faktorov (VO3 až VO5, H6 až H9) a napokon doplnkový exploračný blok (VO7, VO8). Takéto radenie sleduje logiku skúmaných premenných, nie technickú náročnosť štatistických postupov.

Explicitné mapovanie výskumných otázok na výsledkové bloky je v tejto placeholder verzii nasledovné:

- VO1: sekcie 3.2, 3.3, 3.5.1, 3.5.2 a 3.5.5.
- VO2: sekcie 3.2, 3.3 a 3.5.4.
- VO3: sekcie 3.6.1 a 3.6.2.
- VO4: sekcia 3.6.3 vrátane kontrastov štýlu odpovedania simulovaného pacienta pre priemernú absolútnu chybu v symptomatických doménach, chybu odhadu závažnosti, chybu odhadu funkčného dopadu a index defektov.
- VO5: sekcia 3.6.4.
- VO6: sekcia 3.4.
- VO7: sekcia 3.7.1.
- VO8: sekcia 3.7.2.

V texte reportujeme len číselné údaje, ktoré sú nevyhnutné pre interpretáciu hypotéz a výskumných otázok. Rozsiahlejšie výstupy sú umiestnené do tabuliek a grafov, aby sa údaje zbytočne neopakovali. Pri každom inferenčnom výsledku uvádzame popri p-hodnote aj odhad efektu, jeho 95 % interval spoľahlivosti a vecnú interpretáciu smeru a veľkosti rozdielu.

### 3.2 Charakteristika datasetu a základné deskriptíva (VO1, deskriptívna časť VO2)

Do finálnej analýzy bolo zaradených **[doplniť počet hodnotiteľov]** hodnotiteľov, ktorí spolu vytvorili **[doplniť počet ratingov]** platných hodnotení. Hodnotených bolo 72 transkriptov vygenerovaných z 12 seed scenárov a 6 experimentálnych variantov, ktoré vznikli kombináciou dvoch úrovní prítomnosti štruktúrujúceho klinického usmernenia a troch úrovní štýlu odpovedania simulovaného pacienta. Priemerný počet hodnotení na jeden transkript bol **[doplniť priemer]** (SD = **[doplniť]**, rozsah **[doplniť]** až **[doplniť]**). Základné charakteristiky datasetu sú uvedené v Tabuľke 1.

Deskriptívne ukazovatele primárnych a sekundárnych premenných sumarizuje Tabuľka 2. Pre ľudsky hodnotené ordinálne položky sú uvedené mediány a interkvartilové rozpätia, pre kompozity indexu klinickej vierohodnosti, indexu defektov a pre transcript-level alebo priame error ukazovatele aj priemery a smerodajné odchýlky. Transcript-level PHQ-9 symptom metadata A1 až A9 budú v tejto tabuľke reportované oddelene od rater odpovedí, aby bolo zrejmé, že nejde o psychometrickú súčasť expertného dotazníka.

> Doplniť:
> - **Tabuľka 1** — počet hodnotiteľov, počet hodnotení, počet transkriptov, rozdelenie hodnotení podľa prítomnosti štruktúrujúceho klinického usmernenia a podľa štýlu odpovedania simulovaného pacienta, priemerný počet hodnotení na transkript a na hodnotiteľa.
> - **Tabuľka 2** — deskriptívne ukazovatele pre ľudské ratingy G1 až G5, S1, S2, R1 až R5, pre transcript-level A1 až A9 a pre hlavné kompozity (medián, IQR, prípadne priemer a SD podľa typu premennej).
> - **Obrázok 1** — histogramy alebo boxploty indexu klinickej vierohodnosti a indexu defektov podľa kombinácií oboch experimentálnych faktorov.

### 3.3 Predbežný expert review položiek a seed scenárov, frekvenčné rozdelenie a vnútorná konzistencia ratingového nástroja (VO1, meracia opora pre VO2)

Pred samotnou frekvenčnou a reliabilitnou analýzou hlavného ratingového datasetu bude stručne zhrnutý aj **pilotný expert review pass** zameraný na obsahovú primeranosť položiek autorského rater dotazníka a na klinickú ukotvenosť seed scenárov. V aktuálnom stave ide o malý expertný panel (`n = 4`), preto bude táto vrstva reportovaná opatrne ako **predbežná expertná obsahová kontrola**, nie ako plnohodnotná validácia nástroja. V texte bude uvedený počet expertov, počet posúdených položiek a seedov, počet odporúčaných úprav a stručné zhrnutie najčastejších pripomienok [@polit2007cvi; @terwee2018COSMINMethodologyEvaluating].

Ako prvý analytický krok bolo zostavené frekvenčné rozdelenie odpovedí na ľudsky hodnotené položky G1 až G5, S1, S2 a R1 až R5. Cieľom tohto kroku bolo posúdiť, či hodnotitelia využívali celé spektrum odpoveďových kategórií a či niektoré položky nevykazovali systematicky jednostranné rozdelenie. Transcript-level PHQ-9 symptom metadata A1 až A9 boli zhrnuté oddelene ako vlastnosť samotných transkriptov a ako podklad pre ich porovnanie so seed anchor profilmi. Frekvenčné analýzy ukázali, že **[doplniť stručné zhrnutie využitia škál: napr. položky G1 až G5 pokrývali celé spektrum / niektoré položky R boli koncentrované v dolných kategóriách / transcript-level PHQ-9 domény vykazovali zreteľný strop alebo dno]**.

Vnútorná konzistencia bola vyhodnocovaná pre tri obsahovo definované bloky položiek v súlade s Metódou (2.8.3) [@terwee2018COSMINMethodologyEvaluating; @marko2016VyuzitieZneuzitieCronbachovej]:

- blok G1 až G5: Cronbachovo α = **[doplniť]**, McDonaldovo ω = **[doplniť]**;
- blok indexu klinickej vierohodnosti, tvorený položkami G1, G3 a G4: α = **[doplniť]**, ω = **[doplniť]**;
- blok R1 až R5: α = **[doplniť]**, ω = **[doplniť]**.

Tieto výsledky naznačujú, že kompozity indexu klinickej vierohodnosti a indexu defektov boli **[doplniť: dostatočne / iba čiastočne / nedostatočne]** vnútorne konzistentné pre ďalšie použitie v inferenčnej analýze.

> Doplniť:
> - stručný prehľad pilotného expert review passu: počet expertov, počet posúdených položiek, počet posúdených seedov, počet revízií a 2 až 4 najčastejšie typy pripomienok.
> - **Tabuľka 3** — frekvenčné rozdelenia kľúčových položiek, najmä G1 až G5 a R1 až R5.
> - **Tabuľka 4** — vnútorná konzistencia (α a ω) pre tri bloky a stručné item-total korelácie len pre tie položky, ktorých vyradenie by α alebo ω významne zmenilo.

### 3.4 Interrater reliabilita (VO6)

Interrater reliabilita bola vyhodnotená pre hlavné kompozitné ukazovatele indexu klinickej vierohodnosti, indexu defektov a pre expertne hodnotené položky závažnosti a funkčného dopadu prostredníctvom intraclass correlation coefficient (ICC) v súlade s analytickým plánom v časti 2.8.4 Metódy [@mchugh2012InterraterReliabilityKappa; @nelson2015manyratersordinal]. Transcript-level PHQ-9 symptom metadata A1 až A9 do tohto bloku nevstupujú, keďže nejde o opakované ľudské hodnotenie. V reporte uvádzame zvolený typ ICC (model **[doplniť: 2,k / 3,k / iný]**, **[doplniť: konzistencia / absolútna zhoda]**, **[doplniť: single / average measures]**) a interpretačnú kategóriu zhody.

Hodnoty ICC dosiahli **[doplniť hodnotu]** pri indexe klinickej vierohodnosti (95 % CI **[doplniť]**), **[doplniť]** pri indexe defektov (95 % CI **[doplniť]**), **[doplniť]** pri expertne hodnotenej závažnosti a **[doplniť]** pri expertne hodnotenom funkčnom dopade. Tieto hodnoty zodpovedajú interpretačnej kategórii **[doplniť: nízka / stredná / dobrá / výborná]** zhody pri jednotlivých ukazovateľoch. Výsledky podporujú záver, že **[doplniť stručnú interpretáciu: aspoň časť kompozitov bola dostatočne stabilná pre inferenčnú analýzu / zhoda bola limitovaná a inferenčné výsledky treba interpretovať opatrne]**.

> Doplniť:
> - **Tabuľka 5** — hodnoty ICC, 95 % intervaly spoľahlivosti a interpretačné kategórie pre index klinickej vierohodnosti, index defektov, expertne hodnotenú závažnosť a expertne hodnotený funkčný dopad.

### 3.5 Jadrové výsledky: efekt prítomnosti štruktúrujúceho klinického usmernenia (H1 až H5, priamy príspevok k VO1 a VO2)

Jadrové hypotézy boli overované pomocou lineárnych zmiešaných modelov pre kompozitné a chybové ukazovatele a pomocou ordinálnych zmiešaných modelov pre jednotlivé ordinálne položky. Vo všeobecnej špecifikácii modelov bol ako fixný efekt zaradený hlavný účinok prítomnosti štruktúrujúceho klinického usmernenia, hlavný účinok štýlu odpovedania simulovaného pacienta a ich interakcia; ako náhodné efekty sa zohľadňovali seed scenár a identita hodnotiteľa [@hedeker2016MixedeffectsLocationScaleModel; @christensenCumulativeLinkModels].

#### 3.5.1 H1 — Klinická vierohodnosť (index klinickej vierohodnosti)

H1 predpokladala, že interview vytvorené so štruktúrujúcim klinickým usmernením budú odbornými hodnotiteľmi posudzované ako klinicky vierohodnejšie než interview vytvorené bez štruktúrujúceho klinického usmernenia, a to na úrovni indexu klinickej vierohodnosti aj jednotlivých položiek G1, G3 a G4.

Model pre index klinickej vierohodnosti ukázal, že hlavný efekt prítomnosti štruktúrujúceho klinického usmernenia bol **[doplniť: štatisticky významný / nevýznamný]** (b = **[doplniť]**, 95 % CI **[doplniť]**, p = **[doplniť]**). Odhadované marginálne priemery dosiahli **[doplniť hodnotu]** pri interview so štruktúrujúcim klinickým usmernením a **[doplniť hodnotu]** pri interview bez neho. Hypotéza H1 bola na úrovni kompozitu **[podporená / nepodporená / podporená čiastočne]**.

Doplnkové ordinálne modely pre jednotlivé položky G1, G3 a G4 ukázali, že efekt prítomnosti štruktúrujúceho klinického usmernenia bol **[doplniť stručné zistenie pre jednotlivé položky]**, čo umožňuje lokalizovať, či sa prípadný hlavný efekt prejavil najmä vo vierohodnosti, vnútornej konzistencii alebo symptomatickom súlade.

> Doplniť:
> - Tabuľku odhadov pre index klinickej vierohodnosti (hlavné efekty oboch faktorov, interakcia, varianty náhodných efektov).
> - Stĺpcový alebo bodový graf odhadovaných marginálnych priemerov indexu klinickej vierohodnosti podľa kombinácií oboch faktorov.

#### 3.5.2 H2 — Prirodzenosť a vnútorná konzistencia (G2)

H2 predpokladala, že interview vytvorené so štruktúrujúcim klinickým usmernením budú prirodzenejšie a vnútorne konzistentnejšie, najmä na položke G2. Ordinálny zmiešaný model pre G2 ukázal, že efekt prítomnosti štruktúrujúceho klinického usmernenia bol **[doplniť: významný / nevýznamný]** (odhad **[doplniť]**, 95 % CI **[doplniť]**, p = **[doplniť]**) v smere **[vyššej / porovnateľnej / nižšej]** prirodzenosti pri interview so štruktúrujúcim klinickým usmernením. Hypotéza H2 bola **[podporená / nepodporená / podporená čiastočne]**.

> Doplniť:
> - Tabuľku odhadov ordinálneho modelu pre G2.
> - Krátky graf alebo mozaikový prehľad rozdelenia kategórií G2 podľa prítomnosti štruktúrujúceho klinického usmernenia.

#### 3.5.3 H3 — Index defektov (index defektov, R1 až R5)

H3 predpokladala, že interview vytvorené so štruktúrujúcim klinickým usmernením budú obsahovať menej varovných signálov a iných problematických prvkov, a to na úrovni indexu defektov aj jednotlivých položiek R1 až R5.

Lineárny zmiešaný model pre index defektov ukázal hlavný efekt prítomnosti štruktúrujúceho klinického usmernenia **[doplniť: významný / nevýznamný]** (b = **[doplniť]**, 95 % CI **[doplniť]**, p = **[doplniť]**). Interview so štruktúrujúcim klinickým usmernením vykazovali **[nižšiu / porovnateľnú / vyššiu]** mieru defektov než interview bez neho. Hypotéza H3 bola na úrovni kompozitu **[podporená / nepodporená / podporená čiastočne]**.

Na úrovni jednotlivých položiek sa najvýraznejší rozdiel objavil pri **[doplniť konkrétne R položky]**, zatiaľ čo pri položkách **[doplniť]** sa efekt nepreukázal. Tieto položkové výsledky uvádzame ako spresnenie hlavného kompozitového výsledku.

> Doplniť:
> - Tabuľku odhadov pre index defektov.
> - Položkové porovnanie len pre tie položky R, pri ktorých efekt zmysluplne dopĺňa interpretáciu kompozitu.

#### 3.5.4 H4 — Symptomatická primeranosť voči seed kotvám (priemerná absolútna chyba v symptomatických doménach, chyba odhadu závažnosti, chyba odhadu funkčného dopadu)

H4 predpokladala, že interview vytvorené so štruktúrujúcim klinickým usmernením budú symptomaticky primeranejšie vzhľadom na cieľový seed scenár než interview bez tohto usmernenia. Primárnym indikátorom tejto vetvy bola priemerná absolútna odchýlka transcript-level PHQ-9 symptom profilov A1 až A9 od zodpovedajúcich seed anchorov; expertné odhady závažnosti a funkčného dopadu túto líniu dopĺňali ako samostatná ľudská vrstva.

Transcript-level porovnanie ukázalo, že priemerná absolútna chyba v symptomatických doménach A1 až A9 voči seed kotvám bola **[doplniť: nižšia / porovnateľná / vyššia]** pri interview so štruktúrujúcim klinickým usmernením než pri interview bez neho. Na úrovni expertne hodnotených položiek S1 a S2 budú reportované aj priame výsledky pre odhad závažnosti a odhad funkčného dopadu voči `1-5` seed anchorom. Hypotéza H4 bola **[podporená / nepodporená / podporená čiastočne]**, pričom jej jadro bolo ukotvené prednostne v transcript-level symptom fidelity.

Doplnkovo, na úrovni jednotlivých symptomatických domén A1 až A9, najvyššia zhoda so seed kotvami bola pri oblastiach **[doplniť]**, zatiaľ čo najproblematickejšie boli oblasti **[doplniť]**. Tieto doménové výsledky interpretujeme ako transcript-level spresnenie hlavného fidelity výsledku, nie ako samostatnú hypotetickú vetvu.

> Doplniť:
> - Tabuľku alebo kompaktný prehľad transcript-level priemernej absolútnej chyby v symptomatických doménach a aj expertne hodnotenej závažnosti a funkčného dopadu.
> - Doménový prehľad priemerných absolútnych chýb pre A1 až A9.

#### 3.5.5 H5 — Tréningová použiteľnosť (G5)

H5 predpokladala, že interview vytvorené so štruktúrujúcim klinickým usmernením budú odbornými hodnotiteľmi posudzované ako použiteľnejšie na tréningové alebo výučbové účely, a to na úrovni položky G5. Ordinálny zmiešaný model pre G5 ukázal, že efekt prítomnosti štruktúrujúceho klinického usmernenia bol **[doplniť: významný / nevýznamný]** (odhad **[doplniť]**, 95 % CI **[doplniť]**, p = **[doplniť]**), pričom interview so štruktúrujúcim klinickým usmernením boli posudzované ako **[použiteľnejšie / porovnateľne použiteľné / menej použiteľné]** než interview bez neho. Hypotéza H5 bola **[podporená / nepodporená / podporená čiastočne]**.

> Doplniť:
> - Tabuľku odhadov ordinálneho modelu pre G5.

### 3.6 Rozšírené výsledky: efekt štýlu odpovedania simulovaného pacienta a interakcia oboch faktorov (Blok B a Blok C; VO3 až VO5, H6 až H9)

Rozšírené hypotézy H6 až H9 sa týkajú efektu štýlu odpovedania simulovaného pacienta na úrovniach P1, P2 a P3 a interakcie medzi oboma experimentálnymi faktormi. V logike Úvodu a Metódy ide o pokračovanie Bloku B (VO3, VO4, H6 až H8) a Bloku C (VO5, H9), pričom VO6 až VO8 ostávajú mimo tejto hypotetickej vetvy.

#### 3.6.1 H6 — Štýl odpovedania a klinická vierohodnosť (VO3)

H6 predpokladala, že interview s vyváženým alebo rozvinutým štýlom odpovedania simulovaného pacienta (P2 alebo P3) budú klinicky vierohodnejšie než interview so zdržanlivým štýlom odpovedania (P1), a to na úrovni indexu klinickej vierohodnosti.

Hlavný efekt štýlu odpovedania simulovaného pacienta v modeli pre index klinickej vierohodnosti bol **[doplniť: významný / nevýznamný]** (F = **[doplniť]** alebo LR = **[doplniť]**, p = **[doplniť]**). Kontrasty P2 vs. P1 a P3 vs. P1 ukázali odhady **[doplniť]** a **[doplniť]** (95 % CI **[doplniť]** a **[doplniť]**). Hypotéza H6 bola **[podporená / nepodporená / podporená čiastočne]**.

#### 3.6.2 H7 — Štýl odpovedania, prirodzenosť a použiteľnosť (G2, G5, VO3)

H7 predpokladala, že interview s rozvinutejším štýlom odpovedania (P3) budú prirodzenejšie a tréningovo použiteľnejšie než interview so zdržanlivejším štýlom odpovedania (P1, P2), najmä na položkách G2 a G5. Ordinálne zmiešané modely ukázali, že efekt štýlu odpovedania simulovaného pacienta bol **[doplniť]** pre G2 a **[doplniť]** pre G5. Kontrast P3 vs. P1 alebo P2 bol **[doplniť]** pre G2 a **[doplniť]** pre G5. Hypotéza H7 bola **[podporená / nepodporená / podporená čiastočne]**.

#### 3.6.3 H8 — Štýl odpovedania, symptomatická presnosť a varovné signály (VO4)

H8 predpokladala, že interview s rozvinutejším štýlom odpovedania (P3) budú poskytovať symptomaticky bohatší a presnejší obraz prípadu než interview so zdržanlivejším štýlom odpovedania (P1), teda budú mať nižšiu priemernú absolútnu chybu transcript-level symptomatických domén A1 až A9 voči seed anchorom. Primárne testovaným výstupom tejto hypotézy bola preto priemerná absolútna chyba v symptomatických doménach. Keďže VO4 je formulovaná širšie, v tejto podsekcii budú v skrátenej podobe reportované aj hlavné efekty štýlu odpovedania simulovaného pacienta pre expertne hodnotenú závažnosť, expertne hodnotený funkčný dopad a index defektov, aj keď pre tieto výstupy nebola formulovaná samostatná smerová hypotéza.

Transcript-level porovnanie ukázalo, že efekt štýlu odpovedania simulovaného pacienta na priemernú absolútnu chybu v symptomatických doménach bol **[doplniť]**. Kontrast P3 vs. P1 bol **[doplniť]**. Hypotéza H8 bola **[podporená / nepodporená / podporená čiastočne]**. Na úrovni širšie formulovanej VO4 bude doplnkovo reportované aj to, či sa efekt štýlu odpovedania prejavil pri expertne hodnotenej závažnosti, expertne hodnotenom funkčnom dopade a indexe defektov, čo ukáže, či sa efekt štýlu odpovedania prejavuje iba v transcript-level symptomatickej primeranosti, alebo aj v kvalite problematických prvkov rozhovoru.

#### 3.6.4 H9 — Interakcia oboch faktorov (VO5)

H9 predpokladala, že pozitívny účinok štruktúrujúceho klinického usmernenia bude výraznejší pri rozvinutejšom štýle odpovedania (P3), najmä pri indexe klinickej vierohodnosti a indexe defektov.

Interakčný člen oboch faktorov bol pri indexe klinickej vierohodnosti **[doplniť: významný / nevýznamný]** (p = **[doplniť]**) a pri indexe defektov **[doplniť]** (p = **[doplniť]**). Aby bola explicitne uzavretá aj VO5, v tejto podsekcii sa doplnkovo uvedie, či sa analogický vzor interakcie objavil aj pri transcript-level symptom fidelity a pri expertne hodnotenej závažnosti a funkčnom dopade. Ak interakcia bola prítomná, jej smer naznačoval, že **[doplniť stručnú interpretáciu vzoru: napr. najvyššia klinická vierohodnosť pri kombinácii so štruktúrujúcim klinickým usmernením a s rozvinutým štýlom odpovedania / efekt štruktúrujúceho klinického usmernenia je viditeľný len pri P3]**. Hypotéza H9 bola **[podporená / nepodporená / podporená čiastočne]**.

> Doplniť:
> - **Tabuľka 6** — súhrn odhadov zmiešaných modelov pre index klinickej vierohodnosti, index defektov a expertne hodnotené severity/function outcome-y; transcript-level symptom fidelity A1 až A9 reportovať oddelene ako doplnkový komparačný prehľad.
> - **Obrázok 2** — odhadované marginálne priemery indexu klinickej vierohodnosti a indexu defektov podľa kombinácií oboch experimentálnych faktorov s 95 % intervalmi spoľahlivosti.

### 3.7 Doplnkové a exploratórne analýzy (VO7, VO8)

#### 3.7.1 Vnímaný pôvod rozhovoru a istota odhadu — VO7

Položka odhadovaného pôvodu rozhovoru zachytávala odhad hodnotiteľa, či ide o rozhovor AI-generovaný, ľudsky simulovaný, reálny alebo nejednoznačný. Frekvenčné rozdelenie odpovedí ukázalo, že hodnotitelia označili rozhovory ako AI-generované v **[doplniť %]** prípadov, ako ľudsky simulované v **[doplniť %]**, ako reálne v **[doplniť %]** a ako nejednoznačné v **[doplniť %]** prípadov.

V exploratórnom logistickom modeli nad binarizovanou premennou „vnímané ako AI vs. nie AI" boli ako prediktory zaradené index klinickej vierohodnosti a index defektov. Vyššia hodnota indexu klinickej vierohodnosti bola spojená s **[doplniť: nižšou / porovnateľnou / vyššou]** pravdepodobnosťou označenia rozhovoru ako AI-generovaného (OR = **[doplniť]**, 95 % CI **[doplniť]**), zatiaľ čo vyššia hodnota indexu defektov bola spojená s **[doplniť: vyššou / porovnateľnou / nižšou]** pravdepodobnosťou tohto označenia (OR = **[doplniť]**, 95 % CI **[doplniť]**).

Položka zachytávajúca istotu odhadu pôvodu ukázala, že istota odhadu bola **[doplniť: vyššia / porovnateľná / nižšia]** pri rozhovoroch s vyšším indexom klinickej vierohodnosti a **[doplniť]** pri rozhovoroch s vyšším indexom defektov.

> Doplniť:
> - Frekvenčný prehľad kategórií odhadovaného pôvodu rozhovoru celkovo aj podľa kombinácií oboch experimentálnych faktorov.
> - Stručnú tabuľku logistického modelu pre binarizovanú premennú vnímané ako AI vs. nie AI.

#### 3.7.2 Otvorené komentáre — VO8

Otvorené komentáre boli analyzované stručným tematickým kódovaním v súlade s časťou 2.8.6 Metódy. Cieľom nebolo vytvoriť samostatnú kvalitatívnu líniu, ale pomenovať opakujúce sa dôvody pozitívneho a negatívneho hodnotenia, ktoré dopĺňajú kvantitatívne výsledky.

Najčastejšie pozitívne témy boli:

1. **[doplniť tému, napr. primeraná klinická logika a tematická pokrytosť]** — výskyt v **[doplniť počet]** komentároch;
2. **[doplniť tému, napr. zrozumiteľný a empatický jazyk klinika]** — výskyt v **[doplniť počet]** komentároch;
3. **[doplniť tému]** — výskyt v **[doplniť počet]** komentároch.

Najčastejšie negatívne témy boli:

1. **[doplniť tému, napr. šablónovitosť alebo priveľmi učebnicové formulácie]** — výskyt v **[doplniť počet]** komentároch;
2. **[doplniť tému, napr. slabší súlad medzi symptomatikou a osobným kontextom]** — výskyt v **[doplniť počet]** komentároch;
3. **[doplniť tému]** — výskyt v **[doplniť počet]** komentároch.

> Doplniť:
> - Stručnú tabuľku tém a frekvencií, ideálne s jedným až dvoma ilustračnými citátmi pre každú tému v anonymizovanej podobe.

### 3.8 Stručné zhrnutie výsledkov

Výsledky na úrovni jadrových hypotéz naznačili, že efekt prítomnosti štruktúrujúceho klinického usmernenia bol **[doplniť: prítomný / čiastočne prítomný / neprítomný]** pri indexe klinickej vierohodnosti (H1), **[doplniť]** pri G2 (H2), **[doplniť]** pri indexe defektov (H3), **[doplniť]** pri chybových ukazovateľoch priemernej absolútnej chyby v symptomatických doménach, chyby odhadu závažnosti a chyby odhadu funkčného dopadu (H4) a **[doplniť]** pri G5 (H5). Na úrovni rozšírených hypotéz boli efekty štýlu odpovedania simulovaného pacienta (H6 až H8) **[doplniť: konzistentné / zmiešané / nepodporené]** a interakcia oboch faktorov (H9) bola **[doplniť: prítomná / čiastočne prítomná / nepodporená]**. Interrater reliabilita pre hlavné kompozity bola **[doplniť stručne]**, čo **[podporuje / čiastočne podporuje / oslabuje]** dôveru v inferenčné výsledky.

Záverečné zhrnutie tu zostáva vecné a sumarizačné: odpovedá na hypotézy H1 až H9 a výskumné otázky VO1 až VO8, no neprináša novú interpretáciu. Tá patrí až do kapitoly Diskusia.
