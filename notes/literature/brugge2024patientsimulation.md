# brugge2024patientsimulation

## Plná citácia
Brügge, E., Ricchizzi, S., Arenbeck, M., Keller, M. N., Schur, L., Stummer, W., Holling, M., Lu, M. H., & Darici, D. (2024). *Large language models improve clinical decision making of medical students through patient simulation and structured feedback: A randomized controlled trial*. BMC Medical Education, 24(1), 1391. https://doi.org/10.1186/s12909-024-06399-7

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1186/s12909-024-06399-7`, PMID `39609823`, PMCID `PMC11605890`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02.2 Simulated patients / virtual patients`
- Overený attachment: [Brügge 2024 PDF](/Users/pavol.bielik/Zotero/storage/PGWZSYAZ/Brügge et al. - 2024 - Large language models improve clinical decision making of medical students through patient simulatio.pdf)

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- should-read

## Typ zdroja
- článok / randomized controlled trial / educational intervention

## Hlavná myšlienka
- LLM-simulovaný pacient s okamžitou štruktúrovanou spätnou väzbou zlepšil klinické rozhodovanie študentov medicíny viac než samotná AI konverzácia bez feedbacku; autori to však rámujú ako doplnok, nie náhradu reálnej interakcie.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, prípadne `manuscript/50_discussion.md`
- funkcia: simulated-patient evidence, feedback framing, complement-not-replace argument

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "In our double-blind randomized design, the control group participated in simulated medical history conversations with AI patients ... while the intervention group ... also received AI-generated feedback ... evaluated by two raters (ICC = 0.924) ... After only four training sessions, the feedback group (3.60 ± 0.13) outperformed the control group (3.02 ± 0.12), F (1,18) = 4.44, p = .049 ... partial η2 = 0.198."
- parafráza: Paper dáva priamo použiteľný experimentálny dôkaz, že samotná AI simulácia nestačí rovnako ako simulácia plus štruktúrovaný feedback. Zároveň je dôležité, že výkon bol hodnotený dvoma ľudskými ratermi s vysokou zhodou.
- use: empirická opora pre tvrdenie, že feedback vrstva môže byť rozhodujúca pre edukatívnu hodnotu AI simulácie

### Blok 2
- opiera sa o: Introduction
- locator: PDF p. 2, `Introduction` + subsection `LLM-simulated CDM-training`
- kontrolný excerpt:
  > "Conversations with real patients, or simulated patients are the traditional approaches for training clinical-decision-making. ... However, training with real patients or human actors is often costly and limited ... Therefore ... LLMs may be able to simulate natural discussions with students, and be used as a cost-effective way to train CDM skills. ... there is currently a need for empirical studies that carefully design and evaluate the use of LLMs in CDM-training."
- parafráza: Úvod paperu presne pomenúva motiváciu, ktorú potrebuješ aj do diplomovky: klasické simulácie sú hodnotné, ale drahé a kapacitne limitované; LLM môžu rozšíriť dostupnosť tréningu, no treba ich empiricky testovať.
- use: úvodný framing pre simulated-patient vetvu a odôvodnenie výskumu

### Blok 3
- opiera sa o: Introduction + Methods
- locator: PDF p. 2-4, `Incorporating LLM-generated feedback` + `Study procedure` + `Prompt for feedback group`
- kontrolný excerpt:
  > "Well-founded feedback after completing a task is essential for an effective learning process. ... Among the few studies that exist on LLM-generated patient simulations [21-24], none have implemented feedback or debriefing at the time of reporting. ... the feedback group received feedback from ChatGPT after each simulated conversation ... generate three personalized suggestions for improvements in bullet points aimed at strengthening clinical reasoning skills after every patient case."
- parafráza: Autori nestavajú intervenciu len na tom, že AI hrá pacienta. Kľúčový dizajnový prvok je okamžitý task-specific feedback, ktorý reaguje na medzeru v skorších simulated-patient štúdiách bez debriefingu.
- use: opora pre argument, že hodnotenie kvality rozhovoru a spätná väzba nie sú sekundárny doplnok, ale jadro tréningovej utility

### Blok 4
- opiera sa o: Results + Discussion
- locator: PDF p. 8-9, `Results` + `Discussion`
- kontrolný excerpt:
  > "After four scenarios, participants in the feedback group ... outperformed the control group ... Specifically, the feedback group showed improvements in the CDM-subdomains creating context ... and securing information ... Furthermore, the participants in both groups rated the simulations as being highly accurate ... feasible ... and realistic."
- parafráza: Výsledok nie je len globálny. Najviac sa hýbali subdomény súvisiace s vytváraním kontextu a zabezpečovaním informácií, pričom subjektívne hodnotenie simulácie bolo vysoké aj na osi realismu a feasibility.
- use: discussion anchor pre to, čo AI simulácie môžu zlepšovať a prečo ich účastníci môžu akceptovať

### Blok 5
- opiera sa o: Discussion + Conclusion
- locator: PDF p. 9-10, subsection `LLM-simulations are a powerful "Add-On" but do not yet replace real human interactions` + `Conclusion`
- kontrolný excerpt:
  > "However ... LLM-based conversations ... may not fully replicate the complexity of real-life conversations. For example, LLM-simulation neglects non-verbal and social aspects. ... this new tool offers students a potentially unlimited opportunity ... We want to emphasize that this is intended as a supplementary training resource for medical students and not as a replacement for real-life interactions."
- parafráza: Paper je použiteľný aj ako brzdiaci zdroj. Výslovne hovorí, že AI simulácia síce škáluje počet a variabilitu tréningov, ale nezachytí neverbálne a sociálne vrstvy reálnych pacientskych rozhovorov.
- use: complement-not-replace framing pre discussion a limity

## Kľúčová definícia / výsledok / argument
- V tomto RCT mala AI simulácia s okamžitou spätnou väzbou lepší efekt než samotná AI simulácia bez feedbacku; autori ju však explicitne odporúčajú len ako doplnkový tréningový zdroj.

## Limity alebo pozor
- Nie je to psychiatriou špecifický paper; ide o širší medical education use-case.
- Malá vzorka (`n = 21`) a špecifický task limitujú generalizáciu.
- Použitý model bol ChatGPT 3.5 v konkrétnom čase a prostredí, takže reprodukovateľnosť môže driftovať s verziami modelu.

## Kľúčové citovateľné miesto
- PDF p. 1 pre hlavný výsledok, effect size a ICC
- PDF p. 2-4 pre odôvodnenie feedback vrstvy a dizajn
- PDF p. 9-10 pre limity a supplement-not-replace argument

## Tagy
- llm / methods / seeding

## Status použitia
- discussion / checked
