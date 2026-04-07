# Literárne medzery a coverage risks

Toto je pracovný gap memo. Drží to, čo ešte treba doplniť, aby bola metodická a argumentačná línia práce obhájiteľná.

## Prehľad medzier

| ID | Gap | Čo chýba | Prečo to potrebuješ | Priorita |
| --- | --- | --- | --- | --- |
| `A` | klinické jadro MDD | formálny klinický referenčný bod pre symptomatiku a diferenciálnu diagnostiku | seed konštrukcia, symptom domény, exclusion/safety | `P1` |
| `B` | expert validation rating nástroja | CVI, expert panel, Delphi-lite alebo podobný paper | obrana položiek G, A, R a pilotnej validity | `P1` |
| `C` | simulated patients framing | 1–2 zdroje priamo k simulated patients alebo virtual patients | framing práce ako simulation/training artifact | `P1` |
| `D` | safety a non-diagnostic framing | explicitné high-stakes a oversight zdroje | etika, limity, diskusia, obrana pri obhajobe | `P1` |
| `E` | agreement metrics pre ordinálne ratingy | weighted kappa alebo iný ordinal agreement zdroj | presnejšia metodická obrana | `P2` |
| `F` | epidemiologický úvodný zdroj pre depresiu | WHO fact sheet alebo ekvivalent s globálnymi odhadmi prevalencie, funkčného dopadu a suicidálneho rizika | otváracie paragrafy Úvodu, rámcovanie významu témy | `P1` |
| `G` | pred-LLM virtual patients v psychiatrickom tréningu | prehľadový zdroj o klasických virtual / simulated patients pre psychiatrické a komunikačné tréningy | ukotvenie posunu od klasických VP k LLM-based VP v Úvode | `P1` |
| `H` | LLM simulovaný pacient so štruktúrujúcim framework-om | CureFun, PATIENT-ψ alebo porovnateľná práca o klinicky ukotvenom LLM patient systéme | empirická opora pre H1-H5 a variable „štruktúrujúce klinické usmernenie" | `P1` |
| `I` | LLM klient s metakogníciou a kontrolou disclosure | MindVoyager alebo porovnateľná práca o realistickej klientskej simulácii s kontrolou openness | teoretická opora pre premennú „štýl odpovedania simulovaného pacienta" a H6-H9 | `P1` |

---

## Gap A: formálny klinický zdroj pre MDD

Momentálne máš symptom anchors, PHQ a Eurostat, ale chýba ti aspoň jeden klinický referenčný bod pre samotnú depresívnu symptomatiku.

**Doplniť:**
- DSM-5-TR alebo ekvivalentný kvalitný review k MDD symptomatike
- ideálne článok o diferenciácii MDD vs. grief / anxiety / bipolarity / psychosis features

**Načo to potrebuješ:**
- obhájenie seed konštrukcie
- obhájenie A1–A9 domén
- obhájenie exclusion/safety pravidiel

---

## Gap B: zdroj k tvorbe expertového rating instrumentu

COSMIN je silný základ, ale ešte chýba niečo bližšie k tomu, ako sa robí expert judgement scale alebo content validation panel pri novo vytvorenom nástroji.

**Doplniť:**
- CVI paper
- expert-panel validation paper
- prípadne Delphi alebo modified Delphi paper

**Načo to potrebuješ:**
- obhájiť, prečo sú položky G, A, R zostavené takto
- ukázať, ako prebiehal refine otázok
- vysvetliť, prečo je nástroj pilotne validovaný a nie plne validovaný

---

## Gap C: simulated patients / AI patients mimo všeobecného LLM health review

Máš blízky Nature/Communications Medicine smer, ale ešte by sa hodili 1–2 zdroje priamo na:
- simulated patients
- virtual standardized patients
- AI patient training
- medical alebo psychological education use-case

**Načo to potrebuješ:**
- ukotviť prácu nie ako „AI chatbota“, ale ako „simulation/training artifact“

---

## Gap D: high-stakes limitations / safety

Máš etiku všeobecne, ale potrebuješ aj explicitný argument, že:
- toto nie je diagnostický nástroj,
- ide o výskumno-tréningové použitie,
- human expert judgement ostáva rozhodujúci filter.

**Načo to potrebuješ:**
- etika
- limity
- diskusia
- obrana pred kritikou typu „AI nemôže robiť kliniku“

---

## Gap E: interrater agreement pri ordinálnych expert ratingoch

ICC je dobrý základ, ale ak budeš mať veľa ordinálnych položiek, môže sa zísť aj zdroj k:
- weighted kappa
- ordinal agreement metrics
- prípadne argument, prečo si zostal pri ICC alebo mixed models

**Načo to potrebuješ:**
- presnejšia metodická obrana
- posudok a obhajoba

---

## Gap F: epidemiologický a úvodný zdroj pre depresiu (citekey `who2025depression`)

V rozšírenom drafte Úvodu sa opierame o WHO 2025 fact sheet pre otváracie tvrdenia o prevalencii, funkčnom dopade a suicidálnom riziku, ale tento zdroj ešte nie je v Zotere.

**Doplniť:**
- World Health Organization. (2025). *Depressive disorder (depression)*. WHO fact sheet.
- URL: https://www.who.int/news-room/fact-sheets/detail/depression
- navrhovaný citekey: `who2025depression`
- klaster: `01 Depresia a MDD`
- priorita: `must-read`

**Načo to potrebuješ:**
- otváracie paragrafy kapitoly 1.1 Úvodu
- globálny rámec významu depresívnej symptomatiky

**Stav:**
- placeholder citekey `[@who2025depression]` je dočasne použitý v `manuscript/20_introduction.md`, kým zdroj nie je v Zotere

---

## Gap G: pred-LLM virtual patients v psychiatrickom tréningu (citekey `chaby2022embodiedvirtualpatients`)

Úvod argumentačne prechádza od klasických virtual / simulated patients k LLM-based systémom. Na ukotvenie pred-LLM stavu chýba prehľadový zdroj.

**Doplniť:**
- Chaby, L., Benamara, A., Pino, M., Prigent, E., Ravenet, B., Martin, J.-C., Vanderstichel, H., Becerril-Ortega, R., Rigaud, A.-S., & Chetouani, M. (2022). Embodied virtual patients as a simulation-based framework for training clinician-patient communication skills. *Frontiers in Virtual Reality, 3*, 827312.
- DOI: 10.3389/frvir.2022.827312
- navrhovaný citekey: `chaby2022embodiedvirtualpatients`
- klaster: `02 LLM, mental health a psychiatria` (subframe: klasické VP pred LLM)
- priorita: `should-read`

**Načo to potrebuješ:**
- kapitola 1.2 Úvodu
- obrana pri obhajobe, že simulated patients nevznikli s LLM

**Stav:**
- placeholder citekey `[@chaby2022embodiedvirtualpatients]` použitý v `manuscript/20_introduction.md`

---

## Gap H: LLM simulovaní pacienti so štruktúrujúcim framework-om (citekey-y `li2024curefun`, `wang2024patientpsi`, `lee2025adaptivevp`)

Jadrové hypotézy H1-H5 sa opierajú o tvrdenie, že klinicky ukotvené alebo štruktúrujúce usmernenie simulácie zvyšuje jej vierohodnosť. Tri kľúčové zdroje ešte nie sú v Zotere.

**Doplniť:**
- Li, Y., Zeng, C., Zhong, J., Zhang, R., Zhang, M., & Zou, L. (2024). *Leveraging large language model as simulated patients for clinical education*. arXiv. doi:10.48550/arXiv.2404.13066 — navrhovaný citekey: `li2024curefun`
- Wang, R., Milani, S., Chiu, J. C., Zhi, J., Eack, S. M., Labrum, T., Murphy, S. M., Jones, N., Hardy, K. V., Shen, H., Fang, F., & Chen, Z. (2024). PATIENT-ψ: Using large language models to simulate patients for training mental health professionals. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (pp. 12772–12797). doi:10.18653/v1/2024.emnlp-main.711 — navrhovaný citekey: `wang2024patientpsi`
- Lee, K., Lee, S., Kim, E. H., Ko, Y., Eun, J., Kim, D., Cho, H., Zhu, H., Kraut, R. E., Suh, E., Kim, E.-M., & Lim, H. (2025). Adaptive-VP: A framework for LLM-based virtual patients that adapts to trainees' dialogue to facilitate nurse communication training. In *Findings of the Association for Computational Linguistics: ACL 2025* (pp. 2319–2352). doi:10.18653/v1/2025.findings-acl.118 — navrhovaný citekey: `lee2025adaptivevp`
- klaster: `02 LLM, mental health a psychiatria`
- priorita: `must-read`

**Načo to potrebuješ:**
- kapitoly 1.3 a 1.6 Úvodu
- empirická opora pre H1-H5 a pre premennú „štruktúrujúce klinické usmernenie"

**Stav:**
- placeholder citekeys `[@li2024curefun]`, `[@wang2024patientpsi]`, `[@lee2025adaptivevp]` použité v `manuscript/20_introduction.md`
- pozor: existujúci `li2024ZeroshotExplainableMental` a `li2026LargeLanguageModel` v bibu NIE sú CureFun

---

## Gap I: LLM klient s metakogníciou a kontrolou disclosure (citekey `kim2025mindvoyager`)

Premenná „štýl odpovedania simulovaného pacienta" a rozšírené hypotézy H6-H9 sa opierajú o MindVoyager framework, ktorý chýba v Zotere.

**Doplniť:**
- Kim, M., Yoo, D., Hwang, Y., Kang, M., Kim, N., Gwak, M., Kwak, B.-W., Chae, H., Kim, H., Lee, Y., Kim, M. H., Jung, D., Chung, K.-M., & Yeo, J. (2025). Can you share your story? Modeling clients' metacognition and openness for LLM therapist evaluation. In *Findings of the Association for Computational Linguistics: ACL 2025* (pp. 25943–25962). doi:10.18653/v1/2025.findings-acl.1332
- navrhovaný citekey: `kim2025mindvoyager`
- klaster: `02 LLM, mental health a psychiatria`
- priorita: `should-read`

**Načo to potrebuješ:**
- kapitola 1.3 a 1.5 Úvodu
- teoretická opora pre premennú „štýl odpovedania" a rozšírené hypotézy H6-H9

**Stav:**
- placeholder citekey `[@kim2025mindvoyager]` použitý v `manuscript/20_introduction.md`
