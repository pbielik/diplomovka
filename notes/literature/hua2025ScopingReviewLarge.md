# hua2025ScopingReviewLarge

## Plná citácia
Hua, Y., Na, H., Li, Z., Liu, F., Fang, X., Clifton, D., & Torous, J. (2025). *A scoping review of large language models for generative tasks in mental health care*. npj Digital Medicine, 8(1), 230. https://doi.org/10.1038/s41746-025-01611-4

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1038/s41746-025-01611-4`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02 LLM – mental health / psychiatry`
- Overený attachment: [Hua 2025 PDF](/Users/pavol.bielik/Zotero/storage/PQGNALLM/Hua%20et%20al.%20-%202025%20-%20A%20scoping%20review%20of%20large%20language%20models%20for%20generative%20tasks%20in%20mental%20health%20care.pdf)

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- should-read

## Typ zdroja
- scoping review

## Hlavná myšlienka
- Hua review je silný argument proti rýchlym záverom o pripravenosti generatívnych LLM pre mental health: ukazuje malý a heterogénny korpus, slabú štandardizáciu hodnotenia, časté ad-hoc škály a zanedbané safety/privacy/fairness vrstvy.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, `manuscript/50_discussion.md`
- funkcia: scoping syntéza generatívnych mental-health aplikácií, opora pre argument o potrebe štandardizovanej evaluácie a prepojenia s klinickými mierami

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "A systematic search identified 726 unique articles, of which 16 met the inclusion criteria. ... the evaluation methods were often non-standardized, with most studies relying on ad-hoc scales that limit comparability and robustness. A reliance on prompt-tuning proprietary models ... raises concerns about transparency and reproducibility. As current evidence does not fully support their use as standalone interventions, more rigorous development and evaluation guidelines are needed."
- parafráza: Už abstrakt hovorí priamo to, čo sa hodí do tvojho framingu: generatívne LLM v mental health majú zaujímavý potenciál, ale evidencia je malá, metodicky nejednotná a zatiaľ nepodporuje autonómne standalone použitie.
- use: balanced opening pre review of generative LLM studies

### Blok 2
- opiera sa o: Results - Mental disorders, conditions, and subconstructs
- locator: PDF p. 2-3, `Mental disorders, conditions, and subconstructs`
- kontrolný excerpt:
  > "eight studies out of the sixteen reviewed included validated measures for mental health constructs ... while nine relied only on ad-hoc approaches ... Across both groups, depression was the most frequently studied mental health construct. The Patient Health Questionnaire-9 (PHQ-9) ... were adopted as inclusion criteria and outcome measures ... However, not all studies ... provided specific criteria."
- parafráza: Review jasne ukazuje, že ani pri často skúmaných témach ako depresia nie je používanie validovaných mier samozrejmosť. Práve tento metodický chaos je dôležitý pri interpretácii súčasnej evidencie.
- use: opora pre metodologickú opatrnosť a potrebu explicitných ratingových kritérií

### Blok 3
- opiera sa o: Applications and model information
- locator: PDF p. 5, `Applications and model information`
- kontrolný excerpt:
  > "Existing generative applications of LLMs in mental health care can be categorized into six main types ... Clinical Assistant, Counselling, Therapy, Emotional Support, Positive Psychology Intervention, and Education. ... In Education, LLMs have been employed to train medical students in communication skills, providing a realistic and positive simulated patient experience."
- parafráza: Hua paper je užitočný aj na taxonómiu generatívnych použití. Pre tvoju tému je obzvlášť cenné, že education a simulated-patient vetva tu stojí vedľa counseling a therapy, nie mimo hlavného poľa.
- use: členenie literatúry v úvode; umiestnenie simulated-patient použitia do širšieho generative-LLM landscape

### Blok 4
- opiera sa o: Pyramid framework of evaluation constructs
- locator: PDF p. 5-6, `Pyramid framework of evaluation constructs`
- kontrolný excerpt:
  > "This framework categorizes constructs into three levels: (1) Safety, Privacy, and Fairness; (2) Trustworthiness and Usefulness; and (3) Design and Operational Effectiveness. ... Foundational areas like 'Safety, Privacy, and Fairness' are rarely evaluated, highlighting key gaps in critical aspects such as 'Accountability,' 'Transparency,' and 'Security'."
- parafráza: Review ponúka veľmi použiteľný evaluačný rámec: bezpečnosť, súkromie a férovosť majú byť spodná vrstva pyramídy, ale presne tieto oblasti sú dnes v mental-health LLM štúdiách najslabšie pokryté.
- use: pre ethics / governance framing aj pre argument, prečo expert-based validation nestačí bez safety vrstvy

### Blok 5
- opiera sa o: Discussion
- locator: PDF p. 6, `Discussion`
- kontrolný excerpt:
  > "the current evidence regarding their task performance and clinical effectiveness is limited and varies across studies. Many studies lack rigorous clinical validation, standardized outcome measures, and adequate sample sizes ... With the majority of studies using non-well-established ad-hoc scales without addressing their validity and reliability ... safety and privacy should be the foundation of any evaluation."
- parafráza: Jadrový prínos tohto paperu je, že nedostatky nevidí len v modeloch, ale v samotnej kvalite evaluácie. Bez validovaných škál, adekvátnych vzoriek a safety-first rámca je klinická interpretácia slabá.
- use: metodologická opora pre vlastnú orientáciu na explicitné hodnotiace kritériá a validizačné úvahy

### Blok 6
- opiera sa o: Discussion - clinician engagement, proprietary models, APIs
- locator: PDF p. 6-7, `Discussion`
- kontrolný excerpt:
  > "the focus of current LLMs today is directed more at patients and less at clinicians ... clinician engagement is required for more sustained and impactful patient use ... dependence on proprietary models ... raises concerns about transparency and customization ... Research should be conducted using the API, where hyperparameters such as the 'temperature' can be controlled, ensuring replicability of the results."
- parafráza: Hua review dobre pomenúva dve praktické slabiny poľa: prevažuje patient-facing logika bez pevného klinického ukotvenia a zároveň sa príliš často skúma cez closed web interface bez kontroly parametrov a reprodukovateľnosti.
- use: discussion anchor pre reproducibility, clinician-in-the-loop a výskumný dizajn

### Blok 7
- opiera sa o: Future directions
- locator: PDF p. 7, `Future directions for LLMs in mental health care`
- kontrolný excerpt:
  > "studies should prioritize the development of standardized evaluation guidelines ... validated and reliable scales ... APIs and locally deployable models that allow for control over hyperparameters should be used ... Incorporating ethical considerations and addressing privacy and safety concerns in study designs will also enhance the trustworthiness of LLM applications in mental health care."
- parafráza: Autori dávajú veľmi konkrétny next-step agenda: štandardizovať evaluáciu, používať validované škály, kontrolovateľné modelové rozhrania a od začiatku zahrnúť privacy/safety požiadavky.
- use: closing synthesis pre gap statement a odporúčania pre budúci výskum

## Kľúčová definícia / výsledok / argument
- Hua review podopiera tvrdenie, že generatívne LLM aplikácie v mental health sú dnes výskumne heterogénne a že bezpečná klinická integrácia bude vyžadovať oveľa štandardizovanejšie a transparentnejšie evaluačné postupy.

## Limity alebo pozor
- Review zahŕňa len 16 štúdií a je cielený na generatívne tasky, takže nepopisuje celé širšie pole mental-health AI.
- Časť textu pracuje s interdisciplinárne voľnejšími definíciami konštruktov; pri citovaní treba rozlišovať medzi klinicky validovanými a len voľne pomenovanými outcome-mi.

## Kľúčové citovateľné miesto
- PDF p. 1 pre search size a hlavný verdict
- PDF p. 2-3 pre validated vs ad-hoc measures a častosť depresie / PHQ-9
- PDF p. 5-7 pre pyramid framework, proprietary-model limits a odporúčania na štandardizáciu

## Tagy
- llm / ethics / analysis

## Status použitia
- discussion / checked
