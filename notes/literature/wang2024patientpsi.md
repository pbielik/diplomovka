# wang2024patientpsi

## Plná citácia
Wang, R., Milani, S., Chiu, J. C., Zhi, J., Eack, S. M., Labrum, T., Murphy, S. M., Jones, N., Hardy, K. V., Shen, H., Fang, F., & Chen, Z. Z. (2024). *PATIENT-ψ: Using large language models to simulate patients for training mental health professionals*. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (pp. 12772–12797). Association for Computational Linguistics. https://doi.org/10.18653/v1/2024.emnlp-main.711

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.18653/v1/2024.emnlp-main.711`, URL `https://aclanthology.org/2024.emnlp-main.711/`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02.2 Simulated patients / virtual patients` + `02.5 Use of LLM`
- Overený attachment: open access na ACL Anthology, plné PDF (26 strán, EMNLP 2024 hlavná stopa, pp. 12772–12797) prečítané a evidence blocky doplnené nižšie

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- must-read

## Typ zdroja
- peer-reviewed konferenčný článok (EMNLP 2024)

## Hlavná myšlienka
- PATIENT-ψ je LLM-based simulačný framework, v ktorom sú simulovaní pacienti naprogramovaní na základe štruktúrovaných kognitívnych modelov pre CBT tréning; autori zdokumentovali, že psychoterapeutickí trénovaní aj experti hodnotia PATIENT-ψ ako bližší reálnym pacientom než samotné GPT-4.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md` (1.3 LLM simulovaní pacienti; 1.4 Potreba expertnej evaluácie); `manuscript/50_discussion.md` (porovnanie s existujúcimi expertnými evaluáciami)
- funkcia: teória / seeding / priamy precedens pre expert-based evaluáciu LLM simulovaného pacienta v duševnom zdraví

## Kľúčová definícia / výsledok / argument
- Kognitívne modely založené na CBT princípoch je možné použiť ako „programovanie" LLM, ktoré potom hrajú rolu simulovaného pacienta pre tréning formulácie CBT formulácie; expertná user study ukázala, že PATIENT-ψ je vnímaný ako bližší skutočným pacientom než GPT-4 bez takéhoto kognitívneho rámca.

## Evidenčné bloky

### Blok 1 — definícia frameworku PATIENT-ψ
- opiera sa o: Abstract
- locator: ACL Anthology 2024.emnlp-main.711, `Abstract`, URL ako vyššie
- kontrolný excerpt:
  > "we propose PATIENT-𝜓, a novel patient simulation framework for cognitive behavior therapy (CBT) training" ... "use large language models (LLMs) programmed with these cognitive models to act as a simulated therapy patient."
- parafráza: Autori predstavujú PATIENT-ψ ako simulačný framework špecificky pre CBT tréning, v ktorom sú veľké jazykové modely „naprogramované" kognitívnymi modelmi a následne hrajú rolu simulovaného terapeutického pacienta.
- use: priamy precedens pre framing „LLM so štruktúrujúcim klinickým usmernením" v našej 1.3; opora pre odlíšenie plain-LLM baseline vs. guardrailed LLM

### Blok 2 — kognitívne modely ako základ simulácie
- opiera sa o: Abstract
- locator: ACL Anthology 2024.emnlp-main.711, `Abstract`
- kontrolný excerpt:
  > "we construct diverse patient cognitive models based on CBT principles"
- parafráza: Simulovaní pacienti v PATIENT-ψ nie sú generickí — sú konštruovaní z diverzných kognitívnych modelov založených na princípoch CBT.
- use: podpora pre myšlienku, že konkrétne štruktúrujúce rámce (CBT kognitívne modely v ich prípade, guardrails v našom) reálne formujú výstup simulovaného pacienta; analógia pre operacionalizáciu `guardrail` vo variables codebook

### Blok 3 — expertná user study
- opiera sa o: Abstract
- locator: ACL Anthology 2024.emnlp-main.711, `Abstract`
- kontrolný excerpt:
  > "we conducted a comprehensive user study of 13 mental health trainees and 20 experts" ... "PATIENT-𝜓 is perceived to be closer to real patient interactions than GPT-4, and PATIENT-𝜓-TRAINER holds strong promise to improve trainee competencies."
- parafráza: Autori realizovali rozsiahlu user study s 13 psychoterapeutickými tréningovými účastníkmi a 20 expertmi, pričom PATIENT-ψ bol hodnotený ako bližší reálnym pacientom než GPT-4, a tréningová varianta PATIENT-ψ-TRAINER vykazovala potenciál zlepšiť kompetencie stážistov.
- use: hlavný empirický precedens pre kapitolu 1.4 (potreba expertnej evaluácie); kvantitatívne aj kvalitatívne podporuje logiku, že expertné ratingy LLM simulovaných pacientov sú zmysluplné a interpretovateľné

### Blok 4 — dva klinické problémy: fidelity a effectiveness
- opiera sa o: §1 Introduction
- locator: PATIENT-ψ EMNLP 2024 PDF, p. 12773, §1 Introduction
- kontrolný excerpt:
  > "two major challenges must be addressed to realize this idea: Fidelity. How can we build simulated patients that closely resemble the communicative behaviors of real patients with mental health disorders? Effectiveness. How can we design an effective training scheme that allows trainees to benefit from interacting with these simulated patients?"
- parafráza: Autori formálne rozdeľujú výskumný problém LLM simulovaného pacienta na dve nezávislé výzvy — fidelity (nakoľko verne LLM napodobňuje komunikačné správanie reálneho pacienta) a effectiveness (nakoľko sa stážista pri interakcii s ním reálne učí).
- use: priamy precedens pre štruktúru našich hypotéz — H1-H5 odpovedajú na fidelity, kým H6-H9 odpovedajú na to, ako profil odpovedania mení dojem zo simulovaného pacienta; v 1.6 môžeme rámec fidelity/effectiveness explicitne citovať ako konceptuálny základ, na ktorom staviame

### Blok 5 — kognitívne modely a konverzačné štýly ako dva zdroje personalizácie
- opiera sa o: §1 Introduction
- locator: PATIENT-ψ EMNLP 2024 PDF, p. 12773, §1 Introduction
- kontrolný excerpt:
  > "We collaborate with clinical psychologists to curate a dataset, PATIENT-Ψ-CM, which comprises 106 high-quality and diverse patient cognitive models." ... "we also integrate six conversational styles into PATIENT-Ψ. These conversational styles were identified from our formative study with mental health domain experts."
- parafráza: PATIENT-ψ kombinuje dva nezávislé zdroje variability: 106 expertami curatovaných CBT kognitívnych modelov a šesť konverzačných štýlov pacienta, ktoré boli identifikované vo formatívnej štúdii s psychoterapeutickými expertmi.
- use: silný precedens pre náš dvojrozmerný dizajn — `guardrail` (analógia ku klinicky ukotvenému kognitívnemu modelu) a `profile` (analógia ku konverzačnému štýlu); v 1.5 to môžeme použiť ako empirickú oporu, že odlíšenie obsahu a štýlu komunikácie je zmysluplné aj v zaužívanej praxi v komunite

### Blok 6 — RQ framework užitočný pre štruktúrovanie evaluácie
- opiera sa o: §3 Experiment Setup
- locator: PATIENT-ψ EMNLP 2024 PDF, p. 12775, §3 Experiment Setup
- kontrolný excerpt:
  > "RQ 1 Fidelity: Does PATIENT-Ψ improve the fidelity of patient simulations compared to baselines? RQ 2 Accuracy: How closely does PATIENT-Ψ imitate the underlying cognitive model? RQ 3 Effectiveness: Do experts and trainees perceive PATIENT-Ψ-TRAINER as an effective tool for CBT training? RQ 4 AutoEval: Can we leverage existing methods, such as LLMs, to automatically evaluate the patient simulations?"
- parafráza: Wang a kol. svoju expertnú evaluáciu organizujú okolo štyroch výskumných otázok: fidelity voči reálnemu pacientovi, accuracy voči konkrétnemu kognitívnemu modelu, effectiveness ako tréningový nástroj a možnosť nahradiť expertné ratingy automatickou LLM evaluáciou.
- use: priamy precedens pre štruktúru našich VO1-VO8; v 1.6 a v `30_method.md` môžeme túto schému pripomenúť ako známy spôsob, ako rozdeliť evaluačný problém LLM simulovaného pacienta na merateľné komponenty

### Blok 7 — meracie nastavenie: 5-bodová Likertová škála + ±2 párové porovnanie
- opiera sa o: §3 Experiment Setup, Evaluation Dimensions
- locator: PATIENT-ψ EMNLP 2024 PDF, p. 12775, §3 Experiment Setup
- kontrolný excerpt:
  > "For pairwise comparisons, the options are: 'A is much better than B,' 'A is somewhat better than B,' 'about the same,' 'B is somewhat better than A,' and 'B is much better than A.' We map the results to a scale from -2 to 2, where ±2 indicates a strong preference. Individual measures use a 5-point Likert scale from 1 to 5, where 5 means 'strongly agree' or 'extremely accurate,' and 1 means 'strongly disagree' or 'not accurate at all.'"
- parafráza: Autori používajú dvojitú metodiku — 5-bodovú Likertovu škálu pre individuálne dimenzie a -2 až +2 bodovú pairwise škálu pre porovnanie dvoch systémov, pričom okraje zodpovedajú silnej preferencii.
- use: priamy metodický precedens pre náš ratingový hárok — naša 5-bodová expertná škála pre A1-A9 a globálne dimenzie je v zhode so štandardom v komunite; v `30_method.md` to môžeme citovať ako oporu pre voľbu počtu bodov škály

### Blok 8 — užšia veľkosť vzorky a typ účastníkov v user study
- opiera sa o: §3 Experiment Setup, User Study Details
- locator: PATIENT-ψ EMNLP 2024 PDF, p. 12776, §3 User Study Details
- kontrolný excerpt:
  > "Assessing simulated therapeutic dialogue is a cognitively difficult process that requires professional training and experience, making typical crowdsourcing data collection approaches difficult. To ensure high-quality evaluations from those with significant real patient experience (experts) and from the population who would use PATIENT-Ψ-TRAINER in practice (trainees), we recruit 20 current mental health practitioners and 13 social work students, respectively."
- parafráza: Autori zdôvodňujú malú vzorku tým, že hodnotenie simulovaného terapeutického dialógu je kognitívne náročné a vyžaduje odbornú prípravu, čo robí klasický crowdsourcing nepoužiteľným; preto cielene rekrutujú 20 praktizujúcich profesionálov v duševnom zdraví a 13 študentov sociálnej práce.
- use: kľúčový obhajovací bod v `50_discussion.md` a v Limits — naša „malá" expertná vzorka je v súlade s tým, ako sa expert evaluation v tejto oblasti reálne robí; aj špičkový EMNLP paper má len 33 účastníkov spolu

### Blok 9 — RQ1 Fidelity: PATIENT-ψ vs. GPT-4 baseline, µ = 1.3 (p < 10⁻⁴)
- opiera sa o: §4.1 RQ 1: Fidelity to Real Patients
- locator: PATIENT-ψ EMNLP 2024 PDF, p. 12777, §4.1, Table 3
- kontrolný excerpt:
  > "Paired t-tests show that PATIENT-Ψ significantly outperforms the other methods (p < 10⁻⁴), indicating that PATIENT-Ψ provides the most realistic patients, addressing RQ 1 positively." ... „PATIENT-Ψ vs. GPT-4 1.3*** ... PATIENT-Ψ vs. Traditional 1.3*** ... GPT-4 vs. Traditional 0.7*"
- parafráza: V párovej expertnej evaluácii PATIENT-ψ signifikantne prevyšuje vanilla GPT-4 baseline aj klasické tréningové techniky (priemerný pairwise rating µ = 1.3 na škále -2 až +2, p < 10⁻⁴), pričom GPT-4 voči tradičným metódam je síce lepšie (µ = 0.7), ale len na p < 0.05.
- use: hlavná empirická opora pre H1/H2 — štruktúrujúce klinické usmernenie (CBT kognitívny model u Wanga, `guardrail` u nás) reálne posúva expertné hodnotenie plausibility ďaleko nad plain LLM baseline; v Discussion ako porovnávací bod a v Introduction ako empirický motivátor

### Blok 10 — kvalitatívny insight: GPT-4 baseline „too forthcoming"
- opiera sa o: §4.1 RQ 1
- locator: PATIENT-ψ EMNLP 2024 PDF, p. 12777, §4.1
- kontrolný excerpt:
  > "Experts expressed that PATIENT-Ψ offered a more realistic challenge of extracting information from patients, unlike the baseline which was too forthcoming with responses. One expert noted that sessions with the baseline felt 'almost like doing therapy with a therapist,' highlighting the challenge of simulating real patient behavior — even with advanced LLMs likely pretrained on an extensive corpus of therapy knowledge."
- parafráza: Experti opisovali plain GPT-4 baseline ako „príliš ochotne odpovedajúci" — v jednom citáte expert porovnáva sedenie s baseline-om k „terapii s terapeutom" — zatiaľ čo PATIENT-ψ stavia stážistu pred realistickejšiu výzvu vyťahovať informácie z pacienta.
- use: priama paralela k našej premennej `profile` (R1/R2/R3 = otvorenosť disclosure simulovaného pacienta) — Wang dokumentuje exact ten istý jav, ktorý my budeme experimentálne varírovať; toto je silný precedens pre H6/H7 a pre naratívny argument v 1.5

### Blok 11 — limit: vzorka 33, perceived improvements, neexistencia objektívneho skill outcome
- opiera sa o: Limitations
- locator: PATIENT-ψ EMNLP 2024 PDF, p. 12780, §Limitations
- kontrolný excerpt:
  > "our measures of the training effectiveness are all perceived improvements from the participants after they practice with PATIENT-Ψ-TRAINER for two sessions. Measuring objective skill improvements could take the form of longitudinal randomized controlled trials (RCTs). Conducting these RCTs would also help address another limitation of our study, the sample size. Due to how specialized the participants must be to properly evaluate the tools and the 1−2 hours required to conduct each user study, the sample size of our study is only 33 in total."
- parafráza: Autori sami priznávajú dva hlavné limity — ich efektivitné miery sú percepčné (nie objektívne behaviorálne) a ich celková vzorka je len 33 účastníkov, pretože každé sedenie trvá 1-2 hodiny a vyžaduje odborného účastníka.
- use: priamy precedens pre formulovanie našich Limits v `50_discussion.md` — môžeme citovať Wanga ako etablovaný štandard v komunite a vďaka tomu obhájiť, prečo náš design používa expertné ratingy a nie longitudinálne behaviorálne outcomes

## Limity alebo pozor
- zameranie je na CBT a formuláciu kognitívneho modelu, nie priamo na expertné hodnotenie symptom fidelity depresie — preto je to precedens pre metodiku, nie priamy predchodca pre našu špecifickú rating task
- evaluácia je primárne „close to real patient" posúdenie; pri preberaní do našej diskusie treba presne oddeliť to od vernosti symptómov, ktorú riešime cez `symptom_error_mean` / `defect_index`
- vlastná „accuracy-fidelity trade-off" pasáž (p. 12777-12778) hovorí, že explicitné emočné slová môžu zlepšiť accuracy, ale znížiť realizmus pri určitých subpopuláciách — pri porovnaní s našimi A1-A9 doménami to treba držať v hlave

## Kľúčové citovateľné miesto
- PATIENT-ψ EMNLP 2024 PDF, p. 12773, §1 Introduction — fidelity vs. effectiveness ako dva problémy
- PATIENT-ψ EMNLP 2024 PDF, p. 12775-12776, §3 Experiment Setup — RQ framework, 5-bodová Likertova škála, ±2 pairwise, 33 odborných účastníkov
- PATIENT-ψ EMNLP 2024 PDF, p. 12777, §4.1 — RQ1 fidelity, µ = 1.3, p < 10⁻⁴
- PATIENT-ψ EMNLP 2024 PDF, p. 12780, Limitations — sample size 33 a perceived improvements

## Tagy
- llm / methods / seeding

## Status použitia
- must-cite / checked
