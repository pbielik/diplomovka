# louie2024RoleplaydohEnablingDomainExperts

## Plná citácia
Louie, R., Nandi, A., Fang, W., Chang, C., Brunskill, E., & Yang, D. (2024). *Roleplay-Doh: Enabling domain-experts to create LLM-simulated patients via eliciting and adhering to principles*. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (pp. 10570-10603). Association for Computational Linguistics. https://doi.org/10.18653/v1/2024.emnlp-main.591

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.18653/v1/2024.emnlp-main.591`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02 LLM – mental health / psychiatry`
- Overený attachment: [Louie 2024 PDF](/Users/pavol.bielik/Zotero/storage/RCG7WMZ7/Louie%20et%20al.%20-%202024%20-%20Roleplay-doh%20Enabling%20Domain-Experts%20to%20Create%20LLM-simulated%20Patients%20via%20Eliciting%20and%20Adhering%20to.pdf)

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- should-read

## Typ zdroja
- conference paper / tool and evaluation study

## Hlavná myšlienka
- Louie paper je pre tvoju temu velmi relevantny, lebo riesi presne problem realistickych AI pacientov v mental-health domene bez pristupu k realnym transcriptom: pouziva expert feedback prelozeny do prirodzenych principov, ktorymi sa potom riadi simulacia pacienta.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, `manuscript/30_method.md`, `manuscript/50_discussion.md`
- funkcia: opora pre expert-in-the-loop tvorbu simulovanych pacientov, pre argument o potrebe explicitnych principov a pre limity text-only AI pacientov

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "To address this, we develop Roleplay-doh, a novel human-LLM collaboration pipeline that elicits qualitative feedback from a domain-expert, which is transformed into a set of principles, or natural language rules, that govern an LLM-prompted roleplay. ... we also introduce a novel principle-adherence prompting pipeline which shows a 30% improvement in response quality and principle following."
- parafráza: Hlavny technicky prispevok paperu je dvojity: expertnu kvalitativnu spatnu vazbu meni na prirodzenojazykove pravidla a nasledne pridava pipeline, ktora kontroluje, ci ich simulovany pacient naozaj dodrziava.
- use: opora pre metodicky argument, ze prompt samotny nestaci a treba explicitny behavior framework

### Blok 2
- opiera sa o: Introduction
- locator: PDF p. 1, `Introduction`
- kontrolný excerpt:
  > "In sensitive application domains like mental health, privacy concerns with obtaining the required data can restrict the feasibility of such methods. ... experts report that patients use colloquial language and can show resistance to help ... no system supports counseling experts ... to customize an AI patient themselves."
- parafráza: Paper velmi presne pomenovava problem tvojej domeny: fine-tuning na realnych datach naraza na privacy limity a naive simulacie zlyhavaju na jemnych, ale klinicky dolezitych znakoch, ako je kolokvialny jazyk ci odpor voci pomoci.
- use: uvodny gap statement pre AI simulated patients v mental health

### Blok 3
- opiera sa o: Tool concept
- locator: PDF p. 2, `Figure 1` + surrounding description
- kontrolný excerpt:
  > "experts customize a set of principles, or rules written in natural language that govern its behavior ... qualitative feedback ... gets transformed by an LLM into well-formulated principles ... 'Respond to encouraging words with hesitation, doubting their significance'."
- parafráza: Pre tvoju pracu je cenne, ze autori nejdu len cestou skryteho promptingu. Spravanie pacienta externalizuju do zrozumitelnych principov, ktore vie expert citat, opravovat a iterovat.
- use: konceptualna opora pre transparentnejsi design simulovaneho pacienta

### Blok 4
- opiera sa o: User Study using Roleplay-doh
- locator: PDF p. 6-7, `User Study using Roleplay-doh`
- kontrolný excerpt:
  > "we conducted a within-subjects study with 25 counseling experts ... The AI patients prompted with Scenario+Expert Principles were rated significantly higher than Scenario-Only on all measures except for role consistency ... Scenario-only AI patient lacked emotional depth ... was also too articulate and forthcoming ... too cooperative, too willing to accept."
- parafráza: Toto je velmi pouzitelny empiricky bod: bez expert principles boli AI pacienti prilis uhladeni, otvoreni a kooperativni, co znizuje realizmus. Pridanie explicitnych principov posunulo hodnotenie autenticity a treningovej pouzitelnosti.
- use: opora pre to, preco pri tvorbe simulovaneho pacienta nestaci genericka LLM persona

### Blok 5
- opiera sa o: Qualitative analysis of principles + third-party ratings
- locator: PDF p. 7, `Creating Principles with Roleplay-doh` + `Third-Party Comparison`
- kontrolný excerpt:
  > "Across the 25 Scenario+ExpertPrinciple AI patients, 123 total principles were created ... themes dictating a concise and colloquial speaking style ... show initial skepticism with the idea of seeking help ... Third-party judges rate AI Patients with expert-defined principles as more authentic, resembling typical cases, ready as a training partner, and likely recommend to novices."
- parafráza: Paper neukazuje len to, ze principy pomahaju, ale aj ake principy su dolezite: styl reci, miera otvorenosti, skepticizmus voci pomoci a fazy podporneho rozhovoru. To je velmi relevantne pre konstrukciu realistickeho depresivneho rozhovoru.
- use: inspiracia pre behavior blocks a expert rating dimensions

### Blok 6
- opiera sa o: Evaluation of Principle-Adherence
- locator: PDF p. 8, `Evaluation of Principle-Adherence`
- kontrolný excerpt:
  > "We find our [Full] method performs better than [No Critique] on M1 (W: 35%; L 10%) and on M3 (W: 35%; L 5%) ... On overall rankings, it again has the strongest performance (W: 30%; L 15%)."
- parafráza: Ked autori testovali tazke error cases, plna principle-adherence pipeline vyhravala nad jednoduchym GPT-4 baseline na konzistencii s kontextom aj na dodrziavani principov.
- use: argument pre explicitne quality-control vrstvy pri AI pacientovi

### Blok 7
- opiera sa o: Ethics and Broader Impacts Statement
- locator: PDF p. 9-10, `Ethics and Broader Impacts Statement`
- kontrolný excerpt:
  > "a risk with simulation is that counselors can become overconfident in supporting an AI patient, but may not effectively support patients with real mental health concerns. ... AI patients should be just one tool for practicing these skills."
- parafráza: Autori sami upozornuju na klucovy limit: AI pacient ma byt treningovy nastroj, nie nahrada kontaktu s realnym pacientom ani automaticka garancia pripravenosti poradcu.
- use: discussion / limitations / ethical guardrail

## Kľúčová definícia / výsledok / argument
- Realistickeho AI pacienta v mental-health domene pomaha budovat expert-in-the-loop pipeline s explicitnymi principmi; genericka LLM simulacia bez takychto pravidiel ma tendenciu byt prilis kooperativna a malo autenticka.

## Limity alebo pozor
- Ide o conference paper a AI pacienti su textovi; autori sami priznavaju, ze text-only modalita nevie zachytit nonverbalne signaly a plny counseling context.
- Vzorka zahrna 25 expertov a iba limitovany pocet vaznych klinickych scenarov; generalizacia na tazsie psychiatricke pripady je obmedzena.

## Kľúčové citovateľné miesto
- PDF p. 1-2 pre principle-based pipeline a privacy motivation
- PDF p. 6-8 pre user study, 123 principles a wins nad baseline
- PDF p. 9-10 pre overconfidence risk a curricular framing

## Tagy
- llm / methods / seeding

## Status použitia
- method / checked
