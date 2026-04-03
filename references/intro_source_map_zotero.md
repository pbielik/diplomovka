# Source map pre úvod a Zotero citekeys

Tento súbor prepája citekeys použité v `manuscript/20_introduction.md` s konkrétnymi zdrojmi, ktoré majú byť vložené do Zotera.
Je to iba intro-výrez zo širšieho literature bundle so vstupným rozcestníkom v `docs/literature/literature_map_diplomovka.md`.
Ak pridávaš nový zdroj, najprv ho zaraď do tematického klastru v `docs/literature/source_clusters.md` a až potom ho doplň sem, ak naozaj vstupuje do úvodu.

Odporúčanie:
- importuj zdroj do Zotera cez DOI / PMID / URL,
- nastav citekey podľa návrhu nižšie,
- po synchronizácii Better BibTeX skontroluj, že citekey v `.bib` sedí s markdown draftom.

## 1. AI v psychológii, psychiatrii a medicíne

### `obradovich2024llmpsychiatry`
- **Title:** Opportunities and risks of large language models in psychiatry
- **Use in text:** všeobecný vstup do témy LLM v psychiatrii a mental health research
- **Suggested section:** 1.1 všeobecný úvod
- **Identifier:** PMC11566298

### `meng2024llmmedicine`
- **Title:** The application of large language models in medicine: A scoping review
- **Use in text:** širší rámec využitia LLM v medicíne, vrátane tvorby dokumentov, edukácie a tréningových simulácií
- **Suggested section:** 1.1 a 1.2.3
- **Identifier:** PMC11091685

## 2. AI simulácie a simulovaní pacienti vo vzdelávaní

### `ajluni2025psychiatriceducation`
- **Title:** Artificial intelligence in psychiatric education: Enhancing clinical competence through simulation
- **Use in text:** AI simulácie v psychiatrickom vzdelávaní, bezpečné a škálovateľné klinické skúsenosti
- **Suggested section:** 1.1 a 1.2.2
- **Identifier:** PMC12077637

### `yu2025simulatedpatientsystems`
- **Title:** Simulated patient systems powered by large language model-based AI agents offer potential for transforming medical education
- **Use in text:** LLM-based simulated patients, medicínske a tréningové využitie, realistické a čitateľné encountery
- **Suggested section:** 1.1 a 1.2.3
- **Identifier:** PMC12808140

### `brugge2024patientsimulation`
- **Title:** Large language models improve clinical decision making of medical students through patient simulation and structured feedback: a randomized controlled trial
- **Use in text:** simulácia rozhovorov a štruktúrovaná spätná väzba v tréningu
- **Suggested section:** 1.1 a 1.2.3
- **Identifier:** PMC11605890

## 3. Vinety, štandardizované prípady a simulácia v edukácii

### `evans2015vignettes`
- **Title:** Vignette methodologies for studying clinicians’ decision-making: Validity, utility, and application in ICD-11 field studies
- **Use in text:** vinetové metodológie, klinické rozhodovanie, validita a použiteľnosť viniet
- **Suggested section:** 1.2.2
- **Identifier:** PMC6224682

### `baguley2022vignettedata`
- **Title:** Statistical modelling of vignette data in psychology
- **Use in text:** vinety ako multidimenzionálne scenáre v psychológii a dôsledky pre modelovanie dát
- **Suggested section:** 1.2.2
- **Identifier:** PMC9796090

### `williams2017simulationmentalhealth`
- **Title:** Simulation and mental health outcomes: a scoping review
- **Use in text:** simulácie a štandardizovaní pacienti v mental health education
- **Suggested section:** 1.1, 1.2.2
- **Identifier:** PMC5806484

### `dawood2024standardizedpatient`
- **Title:** Evaluation of the Effectiveness of Standardized Patient Simulation as a Teaching Method in Psychiatric and Mental Health Nursing
- **Use in text:** štandardizovaní pacienti ako tréningový nástroj v psychiatric/mental health education
- **Suggested section:** 1.2.2
- **Identifier:** PMC11206419

## 4. Depresívna symptomatika a klinický rámec

### `kennedy2008coresymptoms`
- **Title:** Core symptoms of major depressive disorder: relevance to diagnosis and treatment
- **Use in text:** jadrové symptómy depresie, depresívna nálada a anhedónia ako kľúčové črty
- **Suggested section:** 1.2.1
- **Identifier:** PMC3181882

### `maj2020depressioncharacterization`
- **Title:** The clinical characterization of the adult patient with depression aimed at personalization of management
- **Use in text:** širší klinický obraz depresie, mierna/stredná/ťažká depresia a funkčný dopad
- **Suggested section:** 1.2.1
- **Identifier:** PMC7491646

### `kroenke2001phq9`
- **Title:** The PHQ-9: validity of a brief depression severity measure
- **Use in text:** PHQ-9 ako stručný a validný nástroj na zachytenie depresívnej symptomatiky a závažnosti
- **Suggested section:** 1.2.1
- **Identifier:** PMID 11556941

### `guidi2011clinicalinterviewdepression`
- **Title:** The Clinical Interview for Depression: a comprehensive review of studies and clinimetric properties
- **Use in text:** význam klinického interview pri komplexnom zachytení depresívnej symptomatiky
- **Suggested section:** 1.2.1
- **Identifier:** PMID 20975323

## 5. Limity LLM a klinická bezpečnosť

### `roustan2025cliniciansguide`
- **Title:** The Clinicians’ Guide to Large Language Models: A General Perspective With a Focus on Hallucinations
- **Use in text:** hallucinations, limity LLM, potreba kritickej integrácie v klinickom kontexte
- **Suggested section:** 1.1 a 1.2.3
- **Identifier:** PMC11815294

### `asgari2025hallucinationframework`
- **Title:** A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation
- **Use in text:** potreba fidelity medzi výstupom modelu a ground truth; bezpečnostný rámec
- **Suggested section:** 1.2.3
- **Identifier:** PMC12075489

## 6. Mapping placeholderov na citekeys

- `placeholder_ai_psychology` → `[@obradovich2024llmpsychiatry; @meng2024llmmedicine]`
- `placeholder_ai_simulation` → `[@ajluni2025psychiatriceducation; @yu2025simulatedpatientsystems; @brugge2024patientsimulation]`
- `placeholder_vignettes_training` → `[@evans2015vignettes; @williams2017simulationmentalhealth]`
- `placeholder_llm_limitations` → `[@roustan2025cliniciansguide; @asgari2025hallucinationframework]`
- `placeholder_depression_review` → `[@kennedy2008coresymptoms; @maj2020depressioncharacterization]`
- `placeholder_phq_or_dsm` → `[@kroenke2001phq9; @kennedy2008coresymptoms]`
- `placeholder_clinical_interview` → `[@guidi2011clinicalinterviewdepression; @maj2020depressioncharacterization]`
- `placeholder_vignette_methods` → `[@evans2015vignettes; @baguley2022vignettedata]`
- `placeholder_education_cases` → `[@williams2017simulationmentalhealth; @dawood2024standardizedpatient]`
- `placeholder_llm_general` → `[@meng2024llmmedicine; @yu2025simulatedpatientsystems]`
- `placeholder_hallucination_or_clinical_llm` → `[@roustan2025cliniciansguide; @asgari2025hallucinationframework]`

## 7. Minimum jadro do Zotera

Ak chceš ísť rýchlo a bez nafukovania knižnice, minimum pre úvod je týchto 10 zdrojov:
- obradovich2024llmpsychiatry
- ajluni2025psychiatriceducation
- evans2015vignettes
- williams2017simulationmentalhealth
- kennedy2008coresymptoms
- maj2020depressioncharacterization
- kroenke2001phq9
- guidi2011clinicalinterviewdepression
- roustan2025cliniciansguide
- asgari2025hallucinationframework
