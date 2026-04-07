# kim2025mindvoyager

## Plná citácia
Kim, M., Yoo, D., Hwang, Y., Kang, M., Kim, N., Gwak, M., Kwak, B., Chae, H., Kim, H., Lee, Y., Kim, M. H., Jung, D., Chung, K.-M., & Yeo, J. (2025). *Can you share your story? Modeling clients' metacognition and openness for LLM therapist evaluation* [MindVoyager]. In *Findings of the Association for Computational Linguistics: ACL 2025*. Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.findings-acl.1332

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.18653/v1/2025.findings-acl.1332`, URL `https://aclanthology.org/2025.findings-acl.1332/`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02.2 Simulated patients / virtual patients` + `02.5 Use of LLM`
- Overený attachment: open access na ACL Anthology, plné PDF (20 strán, Findings of ACL 2025, pp. 25943–25962) prečítané a evidence blocky doplnené nižšie

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- must-read

## Typ zdroja
- peer-reviewed konferenčný článok (Findings of ACL 2025)

## Hlavná myšlienka
- MindVoyager je LLM-based framework pre evaluáciu LLM terapeutov, ktorý zavádza kontrolovaný a realistický klientský simulátor; kľúčová inovácia je, že klient nezverejňuje automaticky svoje vnútorné stavy, čím sa tvorba bezpečnej terapeutickej interakcie stáva netriviálnou úlohou exploration-u, a nie iba odpovedania na priame otázky.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md` (1.3 LLM simulovaní pacienti; 1.5 Pojmový rámec — premenná „štýl odpovedania"); `manuscript/50_discussion.md` (limity plnej transparentnosti simulovaných pacientov)
- funkcia: teória / seeding / teoretická opora pre premennú `profile` (kontrola disclosure) a pre H6-H9

## Kľúčová definícia / výsledok / argument
- MindVoyager argumentuje, že klientské simulátory, ktoré otvorene odkrývajú svoje vnútorné stavy, sú nerealistické — a že kvalitný LLM terapeut má byť hodnotený podľa toho, ako dokáže odkryť myšlienky a presvedčenia klienta, ktoré nie sú explicitne vyjadrené. To je presne paralela k nášmu `profile` — štýl odpovedania kontroluje, ako otvorene simulovaný pacient zdieľa svoje symptómy.

## Evidenčné bloky

### Blok 1 — definícia MindVoyager
- opiera sa o: Abstract
- locator: ACL Anthology 2025.findings-acl.1332, `Abstract`, URL ako vyššie
- kontrolný excerpt:
  > "We introduce MindVoyager, a novel evaluation framework featuring a controllable and realistic client simulator which dynamically adapts itself based on the ongoing counseling session."
- parafráza: Autori predstavujú MindVoyager ako nový evaluačný framework postavený na kontrolovateľnom a realistickom klientskom simulátore, ktorý sa dynamicky prispôsobuje priebehu poradenského sedenia.
- use: priamy precedens pre rozlíšenie kontrolovateľnosti a realizmu v LLM klient-simulátoroch; opora v 1.3 pre to, že naše `profile` nastavenia nie sú ad hoc, ale súvisia s existujúcou debatou v literatúre

### Blok 2 — kritika „plne transparentných" klientov v predchádzajúcej práci
- opiera sa o: Abstract
- locator: ACL Anthology 2025.findings-acl.1332, `Abstract`
- kontrolný excerpt:
  > existing methods "rely on client simulators that clearly disclose internal states to the therapist, making it difficult to determine whether an LLM therapist can uncover unexpressed perspectives."
- parafráza: Autori poukazujú, že existujúce metódy sa opierajú o klientskych simulátorov, ktorí terapeutovi jasne odkrývajú svoje vnútorné stavy, a preto sa nedá posúdiť, nakoľko LLM terapeut dokáže odhaliť nevyjadrené perspektívy.
- use: silný argument v 1.5 pre to, že štýl odpovedania (`profile`) je nezávislá premenná, ktorú sa oplatí experimentálne varírovať; priamo podporuje H6/H7 o efekte „zdržanlivejšej" verzus „otvorenejšej" komunikácie simulovaného pacienta

### Blok 3 — evaluačné metriky pre exploration ability
- opiera sa o: Abstract
- locator: ACL Anthology 2025.findings-acl.1332, `Abstract`
- kontrolný excerpt:
  > "We further introduce evaluation metrics that assess the exploration ability of LLM therapists by measuring their thorough understanding of client's beliefs and thoughts."
- parafráza: Autori ďalej zavádzajú evaluačné metriky, ktoré hodnotia „exploration ability" LLM terapeutov — teda to, do akej miery dokážu porozumieť presvedčeniam a myšlienkam klienta.
- use: metodická paralela k `plausibility_index` a k expertnému posúdeniu v 1.4; potvrdzuje, že v literatúre existuje trend merať kvalitu interakcie inak než len cez povrchovú plynulosť dialógu

### Blok 4 — explicitný non-deployment disclaimer
- opiera sa o: Abstract, prvé dve vety
- locator: MindVoyager Findings of ACL 2025 PDF, p. 25943, Abstract
- kontrolný excerpt:
  > "This work does NOT advocate for the use of large language models (LLMs) in psychological counseling. Instead, we propose an assessment approach to reveal the characteristics of LLM therapists."
- parafráza: Autori v prvej vete abstractu explicitne vylučujú akýkoľvek nasadený klinický cieľ a rámcujú prácu výhradne ako evaluačný/výskumný príspevok, ktorý odhaľuje vlastnosti LLM terapeutov.
- use: priamy precedens pre náš non-diagnostic framing v Limits a v Discussion — môžeme citovať Kim a kol. ako etablovaný model, ako sa v komunite formuluje opatrný safety disclaimer pre LLM v duševnom zdraví; zapadá do gap D (high-stakes / non-diagnostic)

### Blok 5 — openness a metakognícia ako dva hlavné rozdiely od reálnych klientov
- opiera sa o: §1 Introduction
- locator: MindVoyager Findings of ACL 2025 PDF, p. 25943-25944, §1 Introduction
- kontrolný excerpt:
  > "there are two notable differences between real-world clients and simulated clients: (1) Openness – willingness to share personal information and consider alternative perspectives. Clients with high openness often disclose experiences and actively engage the exploration stage, while those with low openness tend to be guarded and reluctant to share. (2) Metacognition – awareness of their own thoughts, emotions, and cognitive processes ... A client with high metacognitive abilities can articulate themselves, whereas a client with low metacognition may struggle to recognize or verbalize their emotional states, leading to more stilted or guarded interactions."
- parafráza: Kim a kol. konceptuálne rozdeľujú klientovu komunikačnú variabilitu na dve nezávislé osy — openness (ochotu zdieľať a uvažovať o alternatívach) a metacognition (schopnosť uvedomiť si vlastné myšlienky a emócie a verbalizovať ich).
- use: priama teoretická opora pre náš `profile` (R1/R2/R3) — môžeme v 1.5 a v `30_method.md` argumentovať, že rozlišovanie „štýlu odpovedania" má etablovanú dvojrozmernú konceptualizáciu v komunite (openness × metacognition), a že naše profily sú projekciou tejto dvojrozmernej osi do pilotného setupu

### Blok 6 — empirický dôkaz, že prompt engineering pre low-openness klientov nestačí
- opiera sa o: §2.2 Limitations of LLM-based Client Simulators
- locator: MindVoyager Findings of ACL 2025 PDF, p. 25944, §2.2
- kontrolný excerpt:
  > "In our experiment, LLM-based client simulators instructed to behave as realistic clients exhibited high levels of openness and metacognition, achieving average scores of 5.0 in both traits. Even when prompted to display low openness and low metacognition, these simulators still demonstrated relatively high levels, with average scores of 4.28 and 4.15, respectively."
- parafráza: V kontrolnom experimente Kim a kol. ukazujú, že aj keď prompt explicitne inštruuje LLM klienta byť uzavretý a s nízkou metakogníciou, model stále dosahuje priemerné hodnoty 4.28 a 4.15 (z 5) — teda samotný prompt engineering nedokáže verne simulovať uzavretého reálneho klienta.
- use: silný empirický argument pre to, prečo musíme `profile` riešiť architektonicky a nie čisto promptovo; v Discussion ako precedens pre myšlienku, že „štýl odpovedania" simulovaného pacienta je netriviálny inžiniersky problém, nie len prompting trick

### Blok 7 — formatívna analýza s troma expertmi: 36 % self-awareness, 26 % openness
- opiera sa o: §2.1 Discrepancy between LLM-based Client Simulator and Real-world Clients
- locator: MindVoyager Findings of ACL 2025 PDF, p. 25944, §2.1
- kontrolný excerpt:
  > "we conduct an analysis with three experts in psychological counseling. We collect twenty counseling sessions conducted between a client simulator and an LLM therapist ... the feedback type percentages are 36.11% for self-awareness, 26.39% for openness to share experiences, 19.44% for openness to any suggestion, and 11.11% for rapid emotional transition."
- parafráza: Autori zrealizovali formatívnu kvalitatívnu analýzu s tromi expertmi v psychologickom poradenstve nad 20 sedeniami s LLM klientom; experti označili 36,11 % feedback položiek ako self-awareness, 26,39 % ako openness to share, 19,44 % ako openness to suggestion a 11,11 % ako rapid emotional transition.
- use: metodický precedens pre našu mixed-methods linku (kvantitatívne ratingy + kvalitatívne expert komentáre); v `30_method.md` to môžeme citovať ako oporu pre to, že malá expertná panel (3 ľudia) je v komunite akceptovateľná pre formatívny audit pred hlavnou štúdiou

### Blok 8 — architektúra: cognitive diagram + cognition mediator
- opiera sa o: §3.1 Components of MINDVOYAGER
- locator: MindVoyager Findings of ACL 2025 PDF, p. 25945, §3.1
- kontrolný excerpt:
  > "Our client simulator consists of two main components: (1) the cognitive diagram, a structured framework that describes how an individual's thoughts and beliefs are interconnected and influence emotions and behaviors; and (2) the cognition mediator, which controls the accessible parts of the cognitive diagram throughout the counseling session. First, we mask the cognitive diagram based on the client's metacognition and openness, then provide the masked cognitive diagram as input to an LLM to simulate a client. Throughout the counseling session, the cognition mediator evaluates the LLM therapist and progressively unmasks parts of the cognitive diagram, simulating a client gradually sharing thoughts and feelings."
- parafráza: MindVoyager má dve komponenty: cognitive diagram (štruktúrovaný popis prepojenia myšlienok a presvedčení klienta) a cognition mediator (kontrolný modul, ktorý maskuje a postupne odmaskováva časti diagramu na základe priebehu sedenia). Klient teda neodkrýva všetko naraz — disclosure je riadené samostatným modulom.
- use: analógia ku „štruktúrujúcemu klinickému usmerneniu" v našom dizajne — náš `guardrail` × `profile` je konceptuálne podobný cognitive diagram × cognition mediator; v 1.3 a 1.5 to môžeme použiť ako priamu paralelu pre obhájenie nášho dvojrozmerného dizajnu

### Blok 9 — Patient-ψ-CM ako zdroj kognitívnych anotácií
- opiera sa o: §3.1 Cognitive diagram
- locator: MindVoyager Findings of ACL 2025 PDF, p. 25945, §3.1
- kontrolný excerpt:
  > "All elements are derived from CCD, and we provide definitions and examples in Table 4. Annotations for each element come from the Patient-ψ-CM dataset (Wang et al., 2024b), which includes CCDs written by experts."
- parafráza: Autori používajú dataset PATIENT-ψ-CM (Wang a kol. 2024) ako zdroj expertami napísaných CCD anotácií, ktoré tvoria základ kognitívnych diagramov v MindVoyager.
- use: dôkaz, že v komunite existuje rastúci ekosystém — výskumníci stavajú nové LLM evaluation frameworky priamo na expertami curatovaných seed datasetoch; pre náš seed workflow je to validácia, že investícia do expertami curatovaných seedov sa vypláca aj nad rámec jednej štúdie

### Blok 10 — evaluácia 6 LLM terapeutov na troch difficulty leveloch
- opiera sa o: §4.1 Experimental Setup, §4.2 Experimental Results
- locator: MindVoyager Findings of ACL 2025 PDF, p. 25947-25948, §4 + Tables 1-2
- kontrolný excerpt:
  > "we conduct experiments with several representative LLMs (GPT-4o, GPT-4o-mini, Llama-3.1-8B, Llama-3.1-70B, and Claude-Haiku) and a LLM-based therapist model (Camel ... 7B model fine-tuned on psychological counseling data) ... we define three setups with varying difficulty levels (easy, normal and hard) based on the metacognition and openness levels of the client simulator." ... "we observe that the CDER performance of LLM therapists declines as the difficulty level progresses from easy to normal to hard."
- parafráza: V hlavnej evaluácii MindVoyager testuje šesť LLM terapeutov (5 univerzálnych + 1 fine-tuned Camel) v troch difficulty setupoch a ukazuje, že CDER (Cognitive Diagram Exposure Rate) každého modelu klesá s rastúcou náročnosťou — teda ťažší klient odhalí menej zo svojho kognitívneho diagramu.
- use: empirická opora pre H6-H9 — keď sa znižuje openness simulovaného pacienta, výkon všetkých LLM terapeutov klesá; toto je presne ten typ efektu, ktorý chceme dokumentovať aj v našom expertnom hodnotení (`profile` má merateľný vplyv na vnímanú kvalitu interakcie)

### Blok 11 — RQ4: existujúce metriky (CTRS) nestačia na meranie exploration ability
- opiera sa o: §4.2 RQ4 + Table 3
- locator: MindVoyager Findings of ACL 2025 PDF, p. 25949, §4.2 RQ4
- kontrolný excerpt:
  > "To compare the exploration ability of LLM therapists to an existing evaluation method, we utilize the cognitive therapy rating scale (CTRS), a metric used in real-world counseling (Beck, 2020) ... We can observe that those two evaluation metrics are slightly correlated to each other, but not directly related. These results show that existing evaluation approaches are not sufficient to evaluate the exploration ability of LLM therapists."
- parafráza: Autori porovnávajú svoje navrhnuté metriky (CDER, IDSS) so štandardnou klinickou škálou CTRS a ukazujú, že obe škály sú len mierne korelované — z čoho vyvodzujú, že existujúce evaluation prístupy nestačia a treba špecializované metriky pre exploration ability.
- use: priama opora pre náš argument v 1.4 a v Discussion, že nové LLM evaluation tasks vyžadujú nové dimenzie hodnotenia (analogicky aj naše A1-A9 domény + globálne škály); CTRS sám o sebe by nezachytil to, čo expert rater vidí pri detailnom posúdení interakcie

## Limity alebo pozor
- MindVoyager je evaluačný framework pre LLM terapeutov, zatiaľ čo náš rukopis hodnotí LLM simulovaných pacientov — smer evaluácie je opačný, takže citácie treba formulovať ako „inverzná, ale komplementárna úloha"
- fokus na counseling / psychoterapeutickú konverzáciu; pri prenose do diagnosticky-orientovaného interview o MDD treba byť opatrný, aby sa interpretácie nezamieňali
- ich evaluácia je primárne automatická (LLM-as-judge), nie ratingy expertov vo veľkej škále — naša expert-rated metodika je v tomto bode komplementárna a hodnotnejšia pre validáciu konkrétnych domén

## Kľúčové citovateľné miesto
- MindVoyager Findings of ACL 2025 PDF, p. 25943, Abstract — non-deployment disclaimer
- MindVoyager Findings of ACL 2025 PDF, p. 25943-25944, §1 — openness × metacognition ako dvojrozmerný konceptuálny rámec
- MindVoyager Findings of ACL 2025 PDF, p. 25944, §2.2 — empirický dôkaz, že prompt engineering pre low-openness nestačí (4.28 / 4.15)
- MindVoyager Findings of ACL 2025 PDF, p. 25945, §3.1 — cognitive diagram + cognition mediator architektúra
- MindVoyager Findings of ACL 2025 PDF, p. 25949, §4.2 RQ4 — CDER/IDSS vs. CTRS, zlá korelácia medzi novými a klasickými metrikami

## Tagy
- llm / methods / seeding

## Status použitia
- must-cite / checked
