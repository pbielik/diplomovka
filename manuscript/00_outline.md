# 00 Outline diplomovej práce

> Táto osnova je uzamknutá podľa IMRaD a podľa sprievodcu fakulty. Každá hlavná sekcia má byť logicky previazaná s ostatnými: úvod vedie k cieľom a hypotézam, metóda ukazuje, ako boli operacionalizované, výsledky riešia iba to, čo bolo vopred definované, a diskusia interpretuje len tie zistenia, ktoré boli skutočne získané.

## Preferovaný názov
**Kvalita simulovaných klinických interview s depresívnou symptomatikou generovaných veľkým jazykovým modelom**

Alternatívny kratší názov:
**Odborné hodnotenie simulovaných klinických interview s depresívnou symptomatikou generovaných veľkým jazykovým modelom**

---

## Predné časti
- titulná strana
- zadanie práce
- čestné vyhlásenie / poďakovanie [ak relevantné]
- abstrakt v slovenskom jazyku
- kľúčové slová
- abstract v anglickom jazyku
- key words
- obsah
- zoznam tabuliek / obrázkov [ak relevantné]
- zoznam skratiek [ak relevantné]

---

## 1 Introduction / Úvod

### 1.1 Všeobecný úvod do problému
- digitalizácia psychologickej praxe a rastúca prítomnosť generatívnej AI
- potreba realistických, štandardizovaných a metodologicky kontrolovaných tréningových materiálov
- význam simulovaných rozhovorov pre výučbu, tréning a pilotné testovanie nástrojov
- citlivosť oblasti depresívnej symptomatiky a potreba klinickej vierohodnosti

### 1.2 Prehľad literatúry
- depresívna symptomatika a jej klinický obraz
- diagnostické a symptomatické domény relevantné pre rozhovor (A1–A9)
- simulované prípady, vinety a ich využitie v psychologickom výskume a vzdelávaní
- generatívna AI v psychológii a v oblasti simulácie dialógu
- riziká AI generovaných rozhovorov: klišé, nekonzistentnosť, nesúlad symptomatiky, neprirodzenosť jazyka

### 1.3 Pojmový rámec výskumného problému
- klinická vierohodnosť
- prirodzenosť jazyka a štýlu odpovedí
- vnútorná konzistentnosť rozhovoru
- symptom fidelity voči seed anchorom
- defect / red-flag dimenzia
- tréningová a výučbová použiteľnosť

### 1.4 Cieľ práce
**Hlavný cieľ:**
Overiť, do akej miery sú AI-generované simulované interview s depresívnou symptomatikou odbornými hodnotiteľmi vnímané ako klinicky vierohodné, prirodzené, konzistentné a zodpovedajúce cieľovému symptomatickému profilu, a zároveň preskúmať, či sa tieto hodnotenia menia v závislosti od experimentálne manipulovaných vlastností generovania rozhovoru.

**Sekundárne ciele:**
- preskúmať mieru zhody rozhovorov so seed anchorami v symptomatických doménach A1–A9
- preskúmať odhad závažnosti a funkčného dopadu vo vzťahu k cieľovým seed profilom
- zachytiť červené vlajky a nedostatky rozhovorov
- zistiť, do akej miery sú rozhovory považované za použiteľné na tréningové a výučbové účely

### 1.5 Výskumné otázky a hypotézy
- H1–H6 podľa finálneho analytického plánu
- teoretické formulácie v texte, empirické formulácie a modely v metóde / prílohe

---

## 2 Method / Metóda

### 2.1 Charakter výskumu a výskumný dizajn
- pilotná kvantitatívna metodologická štúdia
- faktorový experiment v rámci human-rated hodnotenia transkriptov
- faktory: `guardrail` (off/on), `profile` (P1/P2/P3)
- 12 seedov × 6 variantov = 72 transkriptov

### 2.2 Výskumný súbor
- odborní hodnotitelia z oblasti psychológie, psychoterapie a psychiatrie
- účelový výber
- skúsenosť s depresívnou symptomatikou alebo MDD
- jednotka analýzy: 1 hodnotenie 1 transkriptu 1 raterom

### 2.3 Výskumný materiál
- 72 textových transkriptov
- 12 seed scenárov S01–S12
- klinicky ukotvené anchor profily A1–A9, S1, S2
- finálny preset G0/G1 × P1/P2/P3

### 2.4 Hodnotiaci nástroj
- G1–G5: primárne outcome-y
- A1–A9, S1, S2: symptom fidelity a závažnosť
- R1–R5: defect / QC outcome-y
- guessed_origin, guess_confidence, comment: doplnkové premenné

### 2.5 Premenné a operacionalizácia
- nezávislé premenné: guardrail, profile
- random faktory: seed_id, rater_id
- kompozity: plausibility_index, defect_index, symptom_error_mean, severity_error, impact_error

### 2.6 Procedúra
- príprava seedov
- generovanie transkriptov
- technická kontrola
- hodnotenie v survey engine
- export do tabulkového formátu

### 2.7 Spracovanie dát a štatistická analýza
- recode a čistenie dát
- deskriptívna štatistika
- reliabilita a ICC
- LMM a ordinal mixed models
- doplnkové logistické / frekvenčné / kvalitatívne analýzy

### 2.8 Etické aspekty
- simulované transkripty
- dobrovoľná účasť hodnotiteľov
- nízke riziko
- anonymizované spracovanie odpovedí

---

## 3 Results / Výsledky

### 3.1 Úvod k výsledkom
- logika prezentácie podľa hypotéz a blokov outcome-ov

### 3.2 Deskriptívna charakteristika súboru a dát
- počet raterov
- počet ratingov
- rozdelenie ratingov podľa variantov
- dĺžka hodnotenia a prípadne počet turnov

### 3.3 Základné charakteristiky ratingového nástroja
- frekvencie odpovedí na položky
- vnútorná konzistencia blokov
- ICC pre hlavné kompozity

### 3.4 Primárne outcome-y
- H1: guardrail a klinická plausibilita
- H2: guardrail a defect index
- H3: profile a prirodzenosť
- H4: interakcia guardrail × profile

### 3.5 Sekundárne outcome-y
- H5: symptom_error_mean
- severity_error
- impact_error
- položky A1–A9 po doménach [ak relevantné]

### 3.6 Explorácie
- H6: perceived AI / guessed_origin
- comment: tematické zhrnutie
- sensitivity analyses

---

## 4 Discussion / Diskusia

### 4.1 Stručné zhrnutie hlavných zistení
- čo bolo podporené
- čo nebolo podporené

### 4.2 Interpretácia primárnych výsledkov
- guardrail ako mechanizmus stabilizácie rozhovoru
- profil ako mechanizmus rozvinutosti a prirodzenosti
- trade-off medzi naturalness a defect risk

### 4.3 Interpretácia fidelity výsledkov
- zhoda so seed profilom
- význam anchorovaného hodnotenia
- klinická a metodologická využiteľnosť seedov

### 4.4 Porovnanie s literatúrou
- AI simulácie
- vinety a štandardizované prípady
- psychologický tréning a rating realistickosti

### 4.5 Limity
- počet raterov
- pilotný charakter
- účelový výber expertov
- simulované textové interview bez neverbálnych signálov
- možná závislosť výsledkov od konkrétneho modelu a promptingu

### 4.6 Praktické dôsledky
- využitie vo výučbe a tréningu
- využitie pri pilotovaní interview protokolov
- metodologický prínos pre ďalší výskum

### 4.7 Budúce smerovanie
- viac raterov
- rozšírenie seed space
- porovnanie s ľudsky simulovanými alebo reálnymi rozhovormi
- longitudinálne alebo replikačné štúdie

---

## 5 Záver
- stručné zhrnutie prínosu práce
- metodologická hodnota
- odporúčania pre ďalší výskum

## Literatúra
- spravovaná v Zotere, finalizovaná vo Worde cez Zotero plugin

## Prílohy
- finálny ratingový nástroj
- seed anchor tabuľka
- doplnkové tabuľky a grafy
- etické dokumenty [ak relevantné]
- codebook a analytický plán [ak relevantné]
