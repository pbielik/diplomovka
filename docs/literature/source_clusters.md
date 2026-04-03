# Tematické klastre a jadro literatúry

Tento súbor drží pracovné klastre literatúry, odporúčané zdroje a ich prioritu. Je to detailná vrstva pod rozcestníkom v `literature_map_diplomovka.md`.
Ak potrebuješ okamžite konkrétny importný balík pre najkritickejšie medzery, otvor `p1_expansion_pass.md`.

## Kolekcie a tagy v Zotere

Odporúčané kolekcie:
- `Diplomovka/01 Depresia a MDD`
- `Diplomovka/02 LLM, mental health a psychiatria`
- `Diplomovka/03 Validácia rating nástroja`
- `Diplomovka/04 Metóda, štatistika a analytický dizajn`
- `Diplomovka/05 Všeobecná metodológia psychologického výskumu`
- `Diplomovka/06 Kvalitatívne metódy (optional)`
- `Diplomovka/07 Etika a AI governance`
- `Diplomovka/99 Tools a guides (not core)`

Odporúčané tagy:
- `must-read`
- `should-read`
- `optional`
- `methods`
- `validation`
- `ethics`
- `llm`
- `depression`
- `seeding`
- `analysis`

---

## 1. Jadro práce: depresívna symptomatika, anchorovanie seedov

### MUST-READ
1. **Kroenke, K., Spitzer, R. L., & Williams, J. B. W. (2001).**  
   *The PHQ-9: Validity of a brief depression severity measure.*  
   Journal of General Internal Medicine, 16(9), 606–613.  
   **Prečo:** základný zdroj pre PHQ-9, severity, symptom anchorovanie.

2. **Kroenke, K., Strine, T. W., Spitzer, R. L., et al. (2009).**  
   *The PHQ-8 as a measure of current depression in the general population.*  
   Journal of Affective Disorders, 114(1–3), 163–173.  
   **Prečo:** veľmi dôležité, ak seedovanie opieraš o populačné a survey dáta.

3. **Eurostat – EHIS depresívne symptómy**
   - `hlth_ehis_mh2e` – severity of current depressive symptoms by sex, age and educational attainment
   - `hlth_ehis_mh2i` – severity of current depressive symptoms by sex, age and income quintile
   **Prečo:** priama opora pre sociodemografické anchorovanie seedov.

### SHOULD-READ
4. **De la Torre, J. A., et al. (2022).**  
   *Prevalence of depression in Europe using two different PHQ-8 diagnostic algorithms.*  
   **Prečo:** vhodné na obhájenie toho, že PHQ-8/PHQ-9 a ich cut-offy nie sú úplne triviálne.

### Poznámka
Ak budeš písať kapitolu o symptomatike depresie, ešte sa hodí mať:
- buď **DSM-5-TR**,
- alebo aspoň kvalitný prehľadový klinický článok o MDD symptomatológii a diferenciálnej diagnostike.

---

## 2. LLM / AI v mental health a psychiatrii

### MUST-READ
1. **Guo, Z., et al. (2024).**  
   *Large Language Models for Mental Health Applications: Systematic Review.*  
   JMIR Mental Health.  
   **Prečo:** silný všeobecný prehľad, plus riziká, limity, etika.

2. **Omar, M., et al. (2024).**  
   *Applications of large language models in psychiatry: a systematic review.*  
   Frontiers in Psychiatry.  
   **Prečo:** užšie na psychiatriu; bližšie k tvojej práci než všeobecné AI-in-healthcare review.

3. **Yu, H., et al. (2025).**  
   *Simulated patient systems powered by large language model-based AI agents offer potential for transforming medical education.*  
   Communications Medicine / Nature portfolio.  
   **Prečo:** tematicky veľmi blízke k tvojej logike simulovaných pacientov a training use-case.

### SHOULD-READ
4. **Bucher, A., et al. (2025).**  
   *Systematic Review of Large Language Models in Mental Health Care.*  
   **Prečo:** novší systematický prehľad, vhodný ako mapovací sekundárny zdroj.

### OPTIONAL
5. Novšie reviews z rokov 2025–2026 o:
   - LLMs in psychotherapy
   - LLMs in psychiatric education
   - LLMs in simulated patients / standardized patients / OSCE training

---

## 3. Validácia ratingového nástroja

### MUST-READ
1. **Terwee, C. B., et al. (2018).**  
   *COSMIN methodology for evaluating the content validity of patient-reported outcome measures: a Delphi study.*  
   Quality of Life Research, 27(5), 1159–1170.  
   **Prečo:** najdôležitejší validačný rámec pre relevance / comprehensiveness / comprehensibility.

2. **COSMIN User Manual – Content Validity**  
   **Prečo:** praktický manuál k tomu, ako obsahovú validitu reálne robiť a reportovať.

### SHOULD-READ
3. Zdroj k **Content Validity Index (CVI)** – item-level a scale-level CVI  
   **Prečo:** ak budeš chcieť validačnú časť rating nástroja spraviť tradičnejšie a číselnejšie, nie len COSMIN opisom.

4. Zdroj k **expert panel methodology / Delphi-lite / face validity vs content validity**  
   **Prečo:** pomôže ti presne pomenovať, čo vlastne robíš a čo ešte nerobíš.

---

## 4. Štatistika a analytický dizajn

### MUST-READ
1. **Koo, T. K., & Li, M. Y. (2016).**  
   *A Guideline of Selecting and Reporting Intraclass Correlation Coefficients for Reliability Research.*  
   Journal of Chiropractic Medicine, 15(2), 155–163.  
   **Prečo:** interrater reliabilita, typ ICC, reporting.

2. **Sim, J. (2019).**  
   *Should treatment effects be estimated in pilot and feasibility studies?*  
   Pilot and Feasibility Studies.  
   **Prečo:** výborný zdroj na opatrnú interpretáciu pilotných odhadov.

3. **Muhammad, et al. (2023).**  
   *Guidelines for repeated measures statistical analysis...*  
   **Prečo:** opakované a zhlukované merania.

4. **Christensen, R. H. B.**  
   *Cumulative Link Models / ordinal package documentation.*  
   **Prečo:** pri ordinálnych ratingoch.

5. **Hedeker, D., et al. (2016).**  
   *A Mixed-effects Location-Scale Model for Ordinal Questionnaire Data.*  
   **Prečo:** hlbšie metodické krytie pre ordinálne mixed modely.

### SHOULD-READ
6. **Cohen, J. (1988).**  
   *Statistical Power Analysis for the Behavioral Sciences.*  
   **Prečo:** effect size, power, interpretácia.

7. **Krejcie, R. V., & Morgan, D. W. (1970).**  
   *Determining Sample Size for Research Activities.*  
   **Prečo:** klasika pre odhad vzorky; skôr ako doplnok.

8. **Marko, M. (2016).**  
   *Využitie a zneužitie Cronbachovej alfy...*  
   **Prečo:** ak budeš reportovať vnútornú konzistenciu kompozitov.

9. **Soukup, P. (2013).**  
   *Vecná významnosť výsledkov a jej možnosti merania.*  
   **Prečo:** užitočné k effect sizes a obhajobe nad rámec p-hodnôt.

### OPTIONAL
10. Zdroj k **generalizability theory** alebo **many-facet Rasch**  
   **Prečo:** len ak by si neskôr išiel do sofistikovanejšieho modelovania rater variability.

---

## 5. Všeobecná metodológia psychologického výskumu

### MUST-READ
1. **American Psychological Association. (2020).**  
   *Publication Manual of the American Psychological Association (7th ed.).*

2. **Boleková, V., Chlebcová, V., & Čerešník, M. (2022).**  
   *Sprievodca tvorbou záverečných prác.*

### SHOULD-READ
3. **Disman, M. (2011).**  
4. **Ferjenčík, J. (2000).**  
5. **Ritomský, A. (2016).**  
6. **Goodwin, C. J. (2011).**  
7. **Cozby, P. C. (2012).**

**Prečo:** terminológia, dizajn, hypotézy, výberový súbor, interpretácia, obhajoba.

---

## 6. Kvalitatívne metódy – iba ak použiješ komentáre alebo otvorené odpovede

### SHOULD-READ
1. **Braun, V., & Clarke, V. (2006).**  
   *Using thematic analysis in psychology.*

2. **Levitt, H. M. (2020).**  
   *Reporting Qualitative Research in Psychology.*

3. **Hendl, J. (2016).**  
4. **Miovský, M. (2006).**  
5. **Mayring, P. (2014).**

**Prečo:** ak budeš analyzovať otvorené komentáre raterov alebo robiť tematické kódovanie.

---

## 7. Etika a AI governance

### MUST-READ
1. **Haltaufderheide, J., et al. (2024).**  
   *The ethics of ChatGPT in medicine and healthcare: a systematic review.*

2. **Weiss, P. (2011).**  
   *Etické otázky v psychológii.*

### SHOULD-READ
3. Zdroj k:
   - privacy/confidentiality pri AI v healthcare
   - explainability / transparency
   - human oversight pri clinical AI
   - non-diagnostic educational simulation use-case

### OPTIONAL
4. Regulácia / guidance:
   - WHO guidance on AI for health
   - EU AI Act – iba ak budeš mať regulačné okienko, nie ako hlavné jadro diplomovky
