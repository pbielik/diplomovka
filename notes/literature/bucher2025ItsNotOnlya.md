# bucher2025ItsNotOnlya

## Plná citácia
Bucher, A., Egger, S., Vashkite, I., Wu, W., & Schwabe, G. (2025). *“It’s Not Only Attention We Need”: Systematic review of large language models in mental health care*. JMIR Mental Health, 12, e78410. https://doi.org/10.2196/78410

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.2196/78410`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02 LLM – mental health / psychiatry`
- Overený attachment: [Bucher 2025 PDF](/Users/pavol.bielik/Zotero/storage/4SFA5MPG/Bucher%20et%20al.%20-%202025%20-%20%E2%80%9CIt%E2%80%99s%20Not%20Only%20Attention%20We%20Need%E2%80%9D%20Systematic%20Review%20of%20Large%20Language%20Models%20in%20Mental%20Health%20Care.pdf)

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- should-read

## Typ zdroja
- systematický review / framework paper

## Hlavná myšlienka
- Bucher review je silný bridge medzi čisto technickými review paper-mi a klinicko-dizajnovou debatou: ukazuje, že pole LLM v mental health je dnes prevažne feasibility-driven, safety a real-world outcome evidence sú slabé a ďalší vývoj má ísť smerom integrovaných modelov starostlivosti, nie iba single-user chatbotov.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, `manuscript/50_discussion.md`
- funkcia: high-level syntéza poľa, opora pre argument „feasibility nestaci“, rámec pre safety, design a AI-blended therapy

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "A systematic literature review was conducted across PubMed, IEEE Xplore, JMIR, ACM, and AIS databases, yielding 807 studies. After multiple evaluation steps, 55 studies were included. ... Most studies assessed technical feasibility, whereas only a few examined the impact of LLMs on therapeutic outcomes. ... most applications focused on single-user contexts, overlooking opportunities for integrated care environments, such as artificial intelligence–blended therapy."
- parafráza: Už abstrakt dáva pre diplomovku dôležitý verdict: korpus je relatívne široký, ale stále dominujú technické feasibility štúdie, zatiaľ čo reálne terapeutické outcomes, safety a integrované modely starostlivosti sú podskúmané.
- use: úvodný synthesize paragraph pre stav poľa LLM v mental health

### Blok 2
- opiera sa o: Overview of the Analyzed Studies
- locator: PDF p. 5-6, `Overview of the Analyzed Studies`
- kontrolný excerpt:
  > "Most (37/55, 67%) studies have focused on the technical feasibility of using LLMs in mental health care, followed by meta-studies (14/55, 26%) ... only a few studies (4/55, 7%) actually assessed the impact of LLMs on therapeutic measurements and treatment-related outcomes ... only 2 studies included diagnosed patients in their evaluation."
- parafráza: Paper dáva veľmi presný pomer medzi tým, čo je dnes v poli technická demonštrácia, a tým, čo je reálne klinické testovanie. Toto je silná opora proti príliš optimistickému čítaniu literatúry.
- use: argument v úvode aj diskusii, prečo treba byť opatrný pri tvrdeniach o klinickej pripravenosti

### Blok 3
- opiera sa o: LLM Tasks + Table 2 summary
- locator: PDF p. 8-9, `LLM Tasks` + `Table 2`
- kontrolný excerpt:
  > "LLMs’ generative capabilities were primarily used for providing information about mental health disorders or treatment options, for conducting counseling dialogues, or even to simulate encounters with patients. ... Only a few studies evaluated hallucination or safety rates in generated mental health advice, and reasoning beyond CoT remains largely unexplored. ... smaller nonautoregressive LLMs, such as MentalBERT or MentalRoBERTa, can still outperform many larger LLMs, such as GPT-4, on many discriminative tasks."
- parafráza: Review je užitočný aj tým, že nerozpráva len všeobecne o „LLM v psychiatrii“, ale ukazuje konkrétne typy taskov a zároveň upozorňuje, že pri diskriminačných úlohách môžu menšie domain-tuned modely fungovať lepšie než veľké generatívne modely.
- use: presnejšie členenie LLM use-case vetiev v úvode; opora pre odlíšenie simulácie, detekcie a counseling taskov

### Blok 4
- opiera sa o: Psychoeducation + Exercising
- locator: PDF p. 13, `Psychoeducation` + `Exercising`
- kontrolný excerpt:
  > "there appeared to be factual discrepancies within answers. For example, ChatGPT-3.5 offered 2 different mortality rates for a specific disorder and cited the same source ... LLMs might also expose users to medical misinformation, known as hallucinations. This includes inappropriate or dangerous advice ... Anthropomorphizing LLMs ... can further catalyze this issue, as users may overrely on their advice while downplaying their limitations."
- parafráza: Bucher paper prepája dve rizikové línie, ktoré sa ti hodia do diplomovky: faktické chyby a halucinácie na jednej strane a na druhej strane dizajnovo podporené preceňovanie AI výstupu.
- use: safety / limitations sekcia; opora pre non-autonomous framing AI simulovaného pacienta

### Blok 5
- opiera sa o: Discussion of current limitations
- locator: PDF p. 16, `However, the analysis of current research...`
- kontrolný excerpt:
  > "A recurring concern is the fact that LLMs hallucinate and spread misinformation ... Central to these issues are concerns about the underlying training data of LLMs, which commonly comprise data from websites such as Reddit or Wikipedia and not scientifically validated sources ... human oversight is still needed to ensure safe and reliable interactions."
- parafráza: Tu paper explicitne pomenúva slabý základ mnohých modelových výstupov: tréningové dáta nemajú klinický status samy osebe, takže bez dohľadu nemožno z výstupu robiť bezpečný klinický nástroj.
- use: diskusia o limitoch a argument pre expertné hodnotenie kvality rozhovoru namiesto slepej dôvery v model

### Blok 6
- opiera sa o: Single-User Systems Versus Integrated Care Systems
- locator: PDF p. 16-17, sekcia `Single-User Systems Versus Integrated Care Systems`
- kontrolný excerpt:
  > "the fragmented, single-user orientation of current approaches leads to numerous challenges ... there is a need to better integrate LLM assistance with human care and oversight. ... AI-blended therapy is a model of care in which AI tools are integrated into but do not replace human-delivered therapy sessions. Because of human oversight, therapeutic alliances can be formed and manifested, and the risk of hallucinations and misinformation can be mitigated."
- parafráza: Toto je pre tvoju prácu veľmi použiteľný konceptuálny bod: užitočný smer nie je „AI namiesto človeka“, ale AI-blended therapy, kde je AI vložená do ľudsky vedeného procesu a tým sa znižuje riziko halucinácií a overreliance.
- use: pojmový rámec pre bezpečné zasadenie AI simulácií do tréningového alebo podporného kontextu

### Blok 7
- opiera sa o: Ethical and Safety Considerations + Practical Implications
- locator: PDF p. 17-18, `Ethical and Safety Considerations Across the Morphological Layers` + `Practical Implications and Recommendations`
- kontrolný excerpt:
  > "Constructs such as accuracy or acceptance, played a critical role in the evaluation of such solutions. ... the users’ safety must have priority ... Future work should therefore adapt and extend these approaches to the sensitive context of mental health care ... clinicians, health care organizations, and policymakers should ensure that LLM-based mental health interventions are introduced with clear governance structures, onboarding protocols, and AI literacy training."
- parafráza: Review nekončí len všeobecnou etikou. Dáva aj praktický smer: guardrails, fact-checking, governance, onboarding a AI literacy majú byť súčasťou deploymentu, nie dodatočný afterthought.
- use: discussion / ethics / governance framing

## Kľúčová definícia / výsledok / argument
- Bucher review podopiera tvrdenie, že súčasný stav poľa je prevažne feasibility-first a že klinicky zmysluplný ďalší krok je presun od izolovaných single-user chatbotov k dohliadaným integrovaným modelom starostlivosti.

## Limity alebo pozor
- Review je široký a mieša rôzne typy aplikácií, od klasifikácie po counseling a psychoeducation, takže pri citovaní treba dávať pozor, ktorú podvetvu poľa práve opisuješ.
- Paper je skôr mapovací a konceptuálny než outcome-heavy; hodí sa na framing a gap argument, menej na tvrdé efektové tvrdenia.

## Kľúčové citovateľné miesto
- PDF p. 1 pre high-level verdict a 3-layer framework
- PDF p. 5-6 pre pomer feasibility vs outcome evidence
- PDF p. 16-18 pre AI-blended therapy, hallucinations a governance odporúčania

## Tagy
- llm / ethics / seeding

## Status použitia
- discussion / checked
