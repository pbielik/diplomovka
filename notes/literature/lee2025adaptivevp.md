# lee2025adaptivevp

## Plná citácia
Lee, K., Lee, S., Kim, E. H., Ko, Y., Eun, J., Kim, D., Cho, H., Zhu, H., Kraut, R. E., Suh, E. E., Kim, E.-m., & Lim, H. (2025). *Adaptive-VP: A framework for LLM-based virtual patients that adapts to trainees' dialogue to facilitate nurse communication training*. In *Findings of the Association for Computational Linguistics: ACL 2025*. Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.findings-acl.118

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.18653/v1/2025.findings-acl.118`, URL `https://aclanthology.org/2025.findings-acl.118/`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02.2 Simulated patients / virtual patients` + `02.5 Use of LLM`
- Overený attachment: open access na ACL Anthology, plné PDF (34 strán, Findings of ACL 2025, pp. 2319–2352) prečítané a evidence blocky doplnené nižšie

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- must-read

## Typ zdroja
- peer-reviewed konferenčný článok (Findings of ACL 2025)

## Hlavná myšlienka
- Adaptive-VP je LLM-based framework virtual patients pre tréning ošetrovateľskej komunikácie, ktorý dynamicky mení správanie simulovaného pacienta podľa kvality študentovho vstupu (napríklad eskaluje hostilitu, keď je komunikácia neefektívna), pričom zachováva bezpečnosť učiaceho sa.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md` (1.3 LLM simulovaní pacienti; 1.5 Pojmový rámec — adaptívne správanie vs. štýl odpovedania); `manuscript/50_discussion.md` (limity nášho statického dizajnu vs. ich adaptívny dizajn)
- funkcia: teória / seeding / metodický precedens pre operacionalizáciu „štýl odpovedania" (`profile` v našom experimente)

## Kľúčová definícia / výsledok / argument
- Adaptive-VP ukazuje, že LLM-based virtual patients môžu mať okrem statického profilu aj modul adaptívneho správania, ktorý v reálnom čase prepína medzi viac vs. menej kooperatívnymi reakciami — čo legitimizuje náš dizajn s viacerými profilmi odpovedania (R1/R2/R3) ako zjednodušenú, statickú verziu rovnakej základnej myšlienky.

## Evidenčné bloky

### Blok 1 — definícia frameworku Adaptive-VP
- opiera sa o: Abstract
- locator: ACL Anthology 2025.findings-acl.118, `Abstract`, URL ako vyššie
- kontrolný excerpt:
  > "We introduce Adaptive-VP, a VP dialogue generation framework that leverages large language models (LLMs) to dynamically adapt VP behavior based on trainee input."
- parafráza: Autori predstavujú Adaptive-VP ako framework na generovanie dialógu s virtual patient, ktorý využíva veľké jazykové modely a dynamicky prispôsobuje správanie simulovaného pacienta podľa toho, čo a ako trénovaný človek povie.
- use: priamy precedens pre používanie LLM ako moderovaného virtual patient s explicitným mechanizmom reakcie; opora pre odlíšenie plain-LLM baseline vs. štruktúrovaný dizajn v 1.3

### Blok 2 — pipeline + modulárny assessment
- opiera sa o: Abstract
- locator: ACL Anthology 2025.findings-acl.118, `Abstract`
- kontrolný excerpt:
  > "The framework features a pipeline for constructing clinically grounded yet flexible VP scenarios and a modular system for assessing trainee communication and adjusting VP responses in real time."
- parafráza: Adaptive-VP kombinuje pipeline na tvorbu klinicky ukotvených, no stále flexibilných VP scenárov s modulárnym systémom, ktorý hodnotí komunikáciu trénovaného človeka a v reálnom čase upravuje odpovede virtuálneho pacienta.
- use: podpora pre metodické odlíšenie štruktúrujúceho klinického usmernenia (`guardrail`) od štýlu odpovedania (`profile`) — ich „adjust VP responses in real time" je bohatšia verzia nášho statického, ale kontrolovaného nastavenia profilov

### Blok 3 — eskalácia hostility ako špecifické adaptívne správanie
- opiera sa o: Abstract
- locator: ACL Anthology 2025.findings-acl.118, `Abstract`
- kontrolný excerpt:
  > "When trainees respond ineffectively, VPs should escalate in hostility or become uncooperative—yet this level of adaptive interaction remains largely unsupported."
- parafráza: Autori argumentujú, že keď stážista reaguje neefektívne, virtuálny pacient by mal eskalovať hostilitu alebo sa stať menej kooperatívnym, no tento typ adaptívnej interakcie zatiaľ nie je vo väčšine systémov podporovaný.
- use: seminárny bod pre diskusiu — náš statický dizajn profilov (R1/R2/R3) je zámerné zjednodušenie tohto problému; v limits sekcii môžeme priamo citovať, že ďalší krok by bola dynamická adaptácia ako u Adaptive-VP

### Blok 4 — evaluácia s expertnými sestrami
- opiera sa o: Abstract
- locator: ACL Anthology 2025.findings-acl.118, `Abstract`
- kontrolný excerpt:
  > "Automated evaluation using a corpus from practicing nurses showed that our communication skill evaluation mechanism reflected real-world proficiency levels." ... "Expert nurses further confirmed that Adaptive-VP produced more natural and realistic interactions than existing approaches."
- parafráza: Automatizovaná evaluácia postavená na korpuse od reálnych sestier ukázala, že metrika komunikačných zručností odráža reálne úrovne proficiencie, a expertné sestry následne potvrdili, že Adaptive-VP generuje prirodzenejšie a realistickejšie interakcie než existujúce prístupy.
- use: priamy precedens pre expertný audit LLM simulovaných pacientov v 1.4; podpora pre náš argument, že expertné ratingy sú potrebné okrem automatických metrík

### Blok 5 — štyri moduly Adaptive-VP architektúry
- opiera sa o: §3 Overview of Adaptive-VP Framework
- locator: Adaptive-VP Findings of ACL 2025 PDF, p. 2321-2322, §3.1-3.4
- kontrolný excerpt:
  > "First, the Evaluation Module assesses trainee utterances using a multi-agent evaluation process based on criteria informed by best practices and literature in nursing communication. Based on this assessment, the Dynamic Adaptation Module then determines the direction of the VP's next response and passes this to the Dialogue Generation Module, which generates a contextually appropriate VP dialogue. Finally, the Safety Monitoring Module reviews the generated VP dialogue before presenting it to trainees, ensuring learner safety by filtering harmful content (e.g., extreme toxicity), while preserving the realism of interaction."
- parafráza: Adaptive-VP rozkladá adaptáciu virtuálneho pacienta na štyri samostatné moduly: evaluáciu trainee výroku (multi-agent assessment), dynamické určenie smerovania ďalšej odpovede pacienta, samotnú generáciu dialógu a bezpečnostný filter, ktorý zabezpečuje, že realistický pacient nikdy neprekročí ochrannú hranicu pre učiaceho sa.
- use: precedens pre štruktúrovanie diskusie o tom, prečo náš statický `guardrail` × `profile` dizajn zámerne zjednodušuje túto architektúru — môžeme citovať Lee a kol. v Limits ako bohatšie pokračovanie a v 1.5 ako oporu pre to, že clinically grounded usmernenie a bezpečnostný layer sú samostatné koncepty, ktoré sa oplatí oddeliť

### Blok 6 — pipeline tvorby VP scenárov so step-by-step expert validáciou
- opiera sa o: §3.1 Challenge 1 + §4 Developing VP Cases
- locator: Adaptive-VP Findings of ACL 2025 PDF, p. 2321-2323, §3.1 a §4
- kontrolný excerpt:
  > "Our pipeline consists of five stages. First, it is necessary to 1) clarify the training goal ... Second, we 2) incorporate relevant literature ... Third, we 3) specify the training context ... 4) generates draft VP cases ... Finally, 5) expert validation involves clinical educators and experienced practitioners reviewing the generated profiles and scenarios."
- parafráza: Lee a kol. opisujú päťkrokový pipeline tvorby VP scenárov: vyjasnenie tréningového cieľa, integrácia relevantnej literatúry, špecifikácia tréningového kontextu, draft VP scenárov a finálna expertná validácia klinickými edukátormi a praktikami.
- use: priamy metodický precedens pre náš seed workflow (klinické jadro MDD → A1-A9 domény → expert review) — v `30_method.md` môžeme tento päťkrokový pipeline citovať ako oporu pre to, že seed konštrukcia s expertnou validáciou je v komunite štandard

### Blok 7 — between-subjects štúdia s 28 sestrami a EFA s α = 0.96 / 0.97
- opiera sa o: §8 Human Evaluation
- locator: Adaptive-VP Findings of ACL 2025 PDF, p. 2326, §8 Evaluation Procedure
- kontrolný excerpt:
  > "We recruited 28 experienced nurses (≥3 years of clinical experience) and randomly assigned them to one of two conditions: Static (n = 14) or Dynamic VP (n = 14). Each participant interacted with eight VP agents and then rated their perceived realism using a six-item questionnaire adapted from prior work (Wind et al., 2004), scored on a five-point Likert scale (1 = Not realistic at all, 5 = Highly realistic). An exploratory factor analysis (EFA) revealed that these six items grouped into two distinct factors: Role Fidelity (Cronbach's α = 0.96) and Conversational Realism (Cronbach's α = 0.97)."
- parafráza: V hlavnej user study Lee a kol. zaradili 28 skúsených sestier (≥3 roky praxe) do dvoch podmienok (Static n=14 / Dynamic n=14), pričom každý účastník interagoval s ôsmimi VP agentmi a hodnotil ich na šesťpoložkovom dotazníku adaptovanom z Wind a kol. 2004; EFA odhalila dva faktory — Role Fidelity (α = 0.96) a Conversational Realism (α = 0.97).
- use: metodický precedens pre náš ratingový hárok — môžeme citovať, že 5-bodová expertná škála aplikovaná na viacero VP agentov per účastník je realistický a publikovateľný design; α nad 0.95 je plus pre obhájenie nášho cieľa konzistentného expert ratingu

### Blok 8 — LMM s Condition × Patient Type a hlavné F-testy
- opiera sa o: §8 Human Evaluation, Results
- locator: Adaptive-VP Findings of ACL 2025 PDF, p. 2326-2327, §8 Results
- kontrolný excerpt:
  > "Omnibus tests revealed a significant main effect of Condition for both Role Fidelity, F(1, 25.4) = 4.52, p = .043, η²p = 0.151, and Conversational Realism, F(1, 24.7) = 8.421, p = .008, η²p = 0.254. Dynamic VPs were rated significantly higher than Static VPs on both dimensions ... no significant main effect of Patient Type was found, indicating perceived realism was consistent across scenarios."
- parafráza: Lineárny mixed-effects model s fixnými efektmi Condition × Patient Type a random intercept pre subject ID ukázal signifikantný hlavný efekt Condition pre obe dimenzie — Role Fidelity (F = 4.52, p = .043) a Conversational Realism (F = 8.421, p = .008), pričom Dynamic VPs boli hodnotené vyššie a typ pacienta nemal signifikantný efekt.
- use: priamy metodický precedens pre náš analytický plán (LMM s nested ratings v `analysis/scripts/thesis_rating_pipeline.R`) a empirická opora pre H1-H5 — štruktúrujúce klinické usmernenie reálne posúva expertné hodnotenie realizmu virtuálneho pacienta

### Blok 9 — kvalitatívna spätná väzba: rigid VP demoralizuje stážistu
- opiera sa o: §8 Human Evaluation, open-ended feedback
- locator: Adaptive-VP Findings of ACL 2025 PDF, p. 2327, §8 (citáty D6, S2, S9)
- kontrolný excerpt:
  > "If my responses are efficient, the patient should calm down, but they don't." (S2) ... "If the patient never calms down, it might discourage novice nurses." (S9) ... "The VP felt very realistic. I've heard similar responses from real patients before. This will be really useful for novice nurses." (D6)
- parafráza: Sestry v Static podmienke kritizovali, že VP na ich efektívne reakcie neodpovedá zmenou tónu, čo môže demoralizovať novice sestry, zatiaľ čo sestry v Dynamic podmienke porovnávali výpovede s reálnymi pacientmi a videli vysoký tréningový potenciál.
- use: silný kvalitatívny argument v 1.2 alebo 1.3 — naratívne podporuje, prečo „statický" plain LLM bez clinically grounded usmernenia nestačí; v Discussion ako paralela k tomu, čo by sa mohlo objaviť aj v našich kvalitatívnych poznámkach raterov

### Blok 10 — Limitations: Korean kontext, malá vzorka, len text-only, bez behaviorálneho outcome
- opiera sa o: §10 Limitations
- locator: Adaptive-VP Findings of ACL 2025 PDF, p. 2328, §10 Limitations
- kontrolný excerpt:
  > "First, our application and validation focused on the Korean context ... this emphasis may limit the generalizability of our findings to other healthcare systems ... our human evaluation involved a relatively small sample of nursing students and professionals based in South Korea ... our framework primarily utilized Claude 3.5 Sonnet ... Another limitation of our approach is its exclusive focus on generating textual dialogue, which constrains the multimodal realism of VP-based training ... our evaluation prioritized the realism of patient utterances over directly measuring the training effectiveness of newly hired nurses ... realistic patient dialogue is a foundational prerequisite for effective simulation-based training."
- parafráza: Autori sami uznávajú päť limitov — kultúrnu viazanosť na južnokórejský kontext, malú a demograficky úzku vzorku, závislosť od jedného konkrétneho LLM (Claude 3.5 Sonnet), text-only interakciu bez non-verbálnych modalít a fakt, že hodnotia realizmus výpovedí, nie dlhodobé tréningové outcomes — zároveň však argumentujú, že realistický pacientský dialóg je nutná podmienka pre akýkoľvek tréningový benefit.
- use: priame zrkadlo pre naše vlastné Limits v `50_discussion.md` — môžeme citovať Lee a kol. ako etablovaný precedens pre obhajobu „realizmus výpovedí ako foundational outcome" namiesto behaviorálneho skill outcome; navyše ich „prioritized realism over training effectiveness" je takmer doslovne náš dizajn

## Limity alebo pozor
- doména je tréning ošetrovateľskej komunikácie, nie psychiatria ani depresia, takže prenos do nášho kontextu treba formulovať opatrne — ich mechanika je prenosná, ale symptom fidelity pre MDD tu nie je overovaná
- ide o Findings-of-ACL paper (nie main track); pri silnejších tvrdeniach v rukopise treba tento status rešpektovať
- ich design je between-subjects s n = 14 v každej podmienke, kým náš dizajn predpokladá within-rater porovnanie viacerých simulovaných pacientov — pri prenose metodiky treba reflektovať tento posun

## Kľúčové citovateľné miesto
- Adaptive-VP Findings of ACL 2025 PDF, p. 2321-2322, §3 — štyri moduly architektúry (Evaluation, Dynamic Adaptation, Dialogue Generation, Safety Monitoring)
- Adaptive-VP Findings of ACL 2025 PDF, p. 2326, §8 — 28 sestier, EFA s dvoma faktormi (Role Fidelity α = 0.96, Conversational Realism α = 0.97)
- Adaptive-VP Findings of ACL 2025 PDF, p. 2326-2327, §8 Results — F testy z LMM (Role Fidelity F = 4.52, p = .043; Conversational Realism F = 8.421, p = .008)
- Adaptive-VP Findings of ACL 2025 PDF, p. 2328, §10 Limitations — Korean kontext, malá vzorka, text-only, realism-as-prerequisite

## Tagy
- llm / methods / seeding

## Status použitia
- must-cite / checked
