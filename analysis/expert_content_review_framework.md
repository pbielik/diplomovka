# Predbežný Expert Review Položiek A Seed Scenárov

Tento súbor slúži ako pracovný rámec pre **pilotný expert review pass** zameraný na:

- položky autorského rater dotazníka,
- jednotlivé seed scenáre,
- stručný záznam odporúčaných úprav pred hlavným hodnotením transkriptov.

## Prečo to v práci mať

Ratingový nástroj aj seed scenáre sú autorské. Popri neskoršej analýze vnútornej konzistencie a zhody medzi hodnotiteľmi preto dáva zmysel zaradiť aj **predbežnú obsahovú kontrolu** ešte pred alebo paralelne s hlavným ratingom. Pri aktuálnom stave nejde o plnohodnotnú psychometrickú validáciu ani o formálny Delphi proces. Ide o **malý pilotný expert review pass** s aktuálne dostupným panelom `n = 6`, ktorého cieľom je:

- zachytiť nejasné alebo redundantné položky,
- overiť, či položky zodpovedajú zamýšľaným konštruktom,
- skontrolovať klinickú plausibilitu a odlíšiteľnosť seedov,
- zdokumentovať, ktoré úpravy vznikli na základe expertnej spätnej väzby.

Tento framing je v súlade s opatrným používaním content validity pri nových nástrojoch a s tým, že pri malom počte expertov treba číselné ukazovatele vždy čítať spolu s komentármi [@polit2007cvi; @terwee2018COSMINMethodologyEvaluating; @boateng2018scaledevelopment].

## Čo majú experti posudzovať

### 1. Položky rater dotazníka

Pri položkách sleduj najmä:

- relevanciu položky pre zamýšľaný konštrukt,
- zrozumiteľnosť formulácie,
- obsahovú primeranosť k bloku, do ktorého položka patrí,
- vhodnosť odpoveďovej škály,
- potrebu preformulovania, zlúčenia alebo vyradenia položky.

Odporúčaný rozsah škálovania:

- `1 = nevhodné / nejasné / slabý fit`,
- `2 = skôr slabé`,
- `3 = primerané`,
- `4 = veľmi vhodné / jasné / silný fit`.

### 2. Seed scenáre

Pri seedoch sleduj najmä:

- klinickú plausibilitu prípadu,
- primeranosť symptomatických anchorov,
- odlíšiteľnosť seedu od ostatných prípadov,
- použiteľnosť pre tréning alebo výučbu,
- prítomnosť nejasností, rizikových miest alebo nelogických kombinácií.

## Minimálny report do diplomovky

Do rukopisu netreba tlačiť rozsiahlu validačnú prílohu. Stačí stručný, overiteľný blok:

1. počet expertov a ich základné profesijné zázemie,
2. počet posúdených položiek a počet posúdených seedov,
3. koľko položiek a seedov bolo po review upravených,
4. najčastejšie typy pripomienok,
5. pri položkách prípadne jednoduché pomocné ukazovatele item-level content validity.

Pri malom expertnom paneli (aktuálne `n = 6`) je rozumné držať sa tohto pravidla:

- číselné ukazovatele používaj len ako pomocnú oporu,
- hlavný dôraz daj na to, **čo bolo na základe review upravené**,
- neformuluj z toho silný claim typu „dotazník je validovaný“.

## Odporúčaná dátová štruktúra

Šablóny sú v:

- `analysis/templates/validation_experts_template.csv`
- `analysis/templates/rater_items_expert_review_template.csv`
- `analysis/templates/seeds_expert_review_template.csv`

Odporúčaný clean export po prepise reálnych formulárov:

- `analysis/data_clean/validation_experts_clean.csv`
- `analysis/data_clean/rater_items_expert_review_clean.csv`
- `analysis/data_clean/seeds_expert_review_clean.csv`

## Ako to reportovať opatrne

Bezpečný wording do rukopisu:

- `predbežná expertná obsahová kontrola`,
- `pilotný expert review pass`,
- `malý expertný panel`,
- `podklad pre revíziu položiek a seed scenárov`.

Vyhni sa wordingom:

- `kompletná validácia nástroja`,
- `definitívne potvrdená validita`,
- `Delphi štúdia`, ak neprebehli viaceré kolá a formálny Delphi proces.
