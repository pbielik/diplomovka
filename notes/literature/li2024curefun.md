# li2024curefun

## Plná citácia
Li, Y., Zeng, C., Zhong, J., Zhang, R., Zhang, M., & Zou, L. (2024). *Leveraging large language model as simulated patients for clinical education* (arXiv:2404.13066). arXiv. https://doi.org/10.48550/arXiv.2404.13066

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.48550/arXiv.2404.13066`, URL `https://arxiv.org/abs/2404.13066`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02.2 Simulated patients / virtual patients` + `02.5 Use of LLM`
- Overený attachment: arXiv preprint v2 (25 Apr 2024, 14 strán), plné PDF prečítané z `/tmp/pdf-extracts/li2024curefun_raw.pdf` a evidence blocky doplnené nižšie

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- must-read

## Typ zdroja
- arXiv preprint / metodický framework paper

## Hlavná myšlienka
- CureFun je model-agnostický framework, v ktorom LLM hrajú rolu simulovaných pacientov pre klinické vzdelávanie, facilitujú rozhovor so študentom, automaticky vyhodnocujú dialóg a poskytujú spätnú väzbu zameranú na klinickú inquiry.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md` (1.3 LLM simulovaní pacienti a nová generácia); čiastočne aj `manuscript/30_method.md` (rámcovanie premennej „štruktúrujúce klinické usmernenie" / `guardrail`)
- funkcia: teória / seeding / empirická opora pre H1–H5 (plausibility, vernosť symptómov, efekt guardrail-u)

## Kľúčová definícia / výsledok / argument
- CureFun ukazuje, že LLM môžu fungovať ako simulovaní pacienti nielen pasívne, ale v integrovanom pipeline, ktorý okrem dialógu hodnotí kvalitu klinickej inquiry a dáva študentom suggestie — čiže presne ten druh štruktúrujúceho klinického usmernenia, ktoré v našej práci operacionalizujeme ako `guardrail`.

## Evidenčné bloky

### Blok 1 — hlavný príspevok: integrovaný framework
- opiera sa o: Abstract
- locator: arXiv:2404.13066, `Abstract`, URL ako vyššie
- kontrolný excerpt:
  > "we present an integrated model-agnostic framework called CureFun that harnesses the potential of LLMs in clinical medical education."
- parafráza: Autori predstavujú CureFun ako integrovaný a model-agnostický framework, ktorý využíva LLM v klinickom medicínskom vzdelávaní a nie je viazaný na jeden konkrétny model.
- use: priamy dôkaz, že LLM-as-simulated-patient nie je len chat demo, ale štruktúrovaný tréningový pipeline; opora pre 1.3 a pre odlíšenie od pred-LLM éry v 1.2

### Blok 2 — facilitácia dialógu + automatická evaluácia inquiry
- opiera sa o: Abstract
- locator: arXiv:2404.13066, `Abstract`
- kontrolný excerpt:
  > "facilitates natural conversations between students and simulated patients, evaluates their dialogue, and provides suggestions to enhance students' clinical inquiry skills."
- parafráza: CureFun umožňuje prirodzený rozhovor medzi študentom a simulovaným pacientom, pričom automaticky vyhodnocuje priebeh dialógu a poskytuje odporúčania zamerané na zlepšenie klinickej inquiry.
- use: empirický precedens pre premennú „štruktúrujúce klinické usmernenie" (`guardrail` v našom experimente); pomáha argumentovať, prečo v našom dizajne testujeme efekt prítomnosti/absencie takéhoto usmernenia na plausibility a defect indexy

### Blok 3 — kvalita SP-scenáru a porovnanie s inými LLM chatbotmi
- opiera sa o: Abstract
- locator: arXiv:2404.13066, `Abstract`
- kontrolný excerpt:
  > "Through comprehensive evaluations, our approach demonstrates more authentic and professional SP-scenario dialogue flows"
- parafráza: Autori tvrdia, že CureFun pri komplexnej evaluácii generuje autentickejšie a profesionálnejšie SP-scenár dialógy než iné LLM-based chatboti.
- use: podpora pre hypotézu H1/H2 (že štruktúrujúce usmernenie zlepšuje plausibility ratingy) a pre framing, že jednoduché GPT-4 chat nie je hornou hranicou toho, čo sa dá dosiahnuť

### Blok 4 — LLM ako „virtuálny doktor" a obmedzenia
- opiera sa o: Abstract (záverečná časť)
- locator: arXiv:2404.13066, `Abstract`
- kontrolný excerpt:
  > "several medical LLMs and discuss the possibilities and limitations of using LLMs as virtual doctors from the perspective of their diagnostic abilities."
- parafráza: V práci tiež testujú viacero medicínskych LLM ako „virtuálnych lekárov" a diskutujú možnosti aj limity takéhoto použitia z hľadiska diagnostických schopností.
- use: opora pre úvahu v diskusii — systém by mohol byť zneužitý ako pseudo-diagnostický nástroj, čo je presne to, pred čím naša práca varuje (non-diagnostic framing, limitations sekcia)

### Blok 5 — formálny argument: existujúce LLM často „flipnú do role doktora" alebo halucinujú
- opiera sa o: §1 Introduction (str. 2)
- locator: CureFun arXiv preprint v2 PDF, p. 2, §1 Introduction
- kontrolný excerpt:
  > "One notable issue is hallucinations, which can result in the generation of fictional information and factual errors, thereby reducing the realism of clinical training. While existing LLMs primarily aim to align with the perspective of healthcare advisors to provide helpful responses in addressing users' concerns, they often struggle to accurately portray an actual patient, leading to problems such as role flipping in SP conversations."
- parafráza: Autori explicitne pomenúvajú dve typické zlyhania plain LLM v roli simulovaného pacienta: halucinácie (vymýšľanie klinických detailov) a role flipping — model spadne z roly pacienta do roly „nápomocného radcu", pretože RLHF zarovnanie ho k tomu predisponuje.
- use: priamy precedens pre náš A1-A9 codebook a pre `defect_index` — keď budeme v Discussion argumentovať, čo presne vlastne expertné ratingy zachytávajú, môžeme citovať Li a kol. ako etablovaný zoznam typov chýb plain LLM simulovaného pacienta

### Blok 6 — graph-driven context-adaptive ERRG architektúra
- opiera sa o: §3.2 Graph-Driven Context-Adaptive SP Chatbot (str. 7-8)
- locator: CureFun arXiv preprint v2 PDF, p. 7-8, §3.2
- kontrolný excerpt:
  > "we propose the integration of a graph-driven context-adaptive mechanism into the LLM-based chatbot ... Extract, Retrieve, Rewrite, and Generate (ERRG). In the 'Extract' step, the chatbot extract the core entities and possible relations from the user's input ... In the 'Retrieve' step, the chatbot utilizes the LLM to generate a formal query based on the extracted entities and relations, then executes the query on the case graph ... In the 'Rewrite' step, the chatbot transforms the retrieved subgraph into natural language form ... in the 'Generate' step, the chatbot generates an optimal response by considering the retrieved evidence, the current dialogue context, and the user's input."
- parafráza: CureFun nie je voľná promptová architektúra — pacientske odpovede prechádzajú cez štyri kroky (Extract → Retrieve → Rewrite → Generate), pričom každá odpoveď je ukotvená v retrievovanom podgrafe z prípadového grafu a tým sa kontroluje obsah, ktorý sa môže v dialógu objaviť.
- use: silný precedens pre náš `guardrail` ako technickú kategóriu — môžeme v 1.3 a 1.5 ukázať, že „štruktúrujúce klinické usmernenie" nie je vágna kategória, ale sa v komunite operacionalizuje ako konkrétna RAG/graph architektúra; v Discussion ako paralela pre to, prečo naše guardrails reálne menia kvalitu výstupu

### Blok 7 — kontrolovaná konfabulácia pre missing entities
- opiera sa o: §3.2 (str. 8)
- locator: CureFun arXiv preprint v2 PDF, p. 8, §3.2
- kontrolný excerpt:
  > "in the setting of open-world dialogue, SP case scripts cannot contain all the information that the user may ask. In this situation, the chatbot needs to fabricate rational attributes and entities to maintain the dialogue coherence. For preventing the inconsistency response about fictional information, and to prevent the potential conflict between the generated information and the known information in the case graph, which may lead to hallucinations, we introduce a controlled fictional information generation approach."
- parafráza: Autori formálne pomenúvajú netriviálny problém: SP scenár nikdy nepokryje všetky otázky študenta a model musí niečo dofabulovať — preto navrhujú „controlled fictional information generation" a perzistujú nový atribút späť do case graph-u, aby sa rovnaká odpoveď neopakovala inak v ďalších turn-och.
- use: priame použitie v Discussion — náš `defect_index` (vrátane „inconsistency v naratíve") má presne v tomto svoju oporu; môžeme citovať Li a kol. ako precedens pre to, že ide o známy a riešený problém, nie o náš artefakt

### Blok 8 — empirický výsledok: framework reálne zlepšuje plain LLM (B-ELO +250.18 pre GPT-3.5)
- opiera sa o: §2.2 Generation Quality (str. 4)
- locator: CureFun arXiv preprint v2 PDF, p. 4, §2.2 + Table 1
- kontrolný excerpt:
  > "it is noteworthy that our framework consistently and significantly improved performance across all backbone LLMs (Figure 3b; P < 0.05, one-sided Wilcoxon's rank-sum test). Specifically, integrating our framework into GPT-3.5-Turbo resulted in a 250.18-point increase in B-ELO score for the SP role-playing capacity, signifying a substantial advancement."
- parafráza: V pairwise porovnaní (Bootstrap ELO, GPT-4 ako sudca) CureFun framework signifikantne zlepšuje výkon všetkých testovaných backbone LLM (p < 0.05) — pre GPT-3.5-Turbo dosahuje zisk +250.18 B-ELO bodov v úlohe hrať SP rolu.
- use: priama empirická opora pre H1/H2 — štruktúrujúce klinické usmernenie reálne posúva expertne hodnotenú plausibility plain LLM ďaleko nad baseline; v Discussion ako kvantitatívny benchmark pre porovnanie nášho efektu

### Blok 9 — vysoká korelácia automatického a expertného hodnotenia (Spearman ~0.81)
- opiera sa o: §2.3 Evaluate Assessment (str. 5)
- locator: CureFun arXiv preprint v2 PDF, p. 5, §2.3 + Table 2
- kontrolný excerpt:
  > "we employed two correlation measures: Spearman's rank correlation and Pearson correlation ... Overall, both Spearman's rank correlation and Pearson correlation coefficients are consistently closed to 1 (on average 0.81 and 0.85, respectively), suggesting a high degree of agreement between the two sets of scores. And the p-values associated with both correlation tests were found to be less than 0.05 for each group of cases."
- parafráza: V samostatnej validačnej štúdii Li a kol. porovnávajú LLM-as-judge automatický scoring s ratingmi ľudského experta a ukazujú priemerné Spearmanovo ρ ≈ 0.81 a Pearsonovo r ≈ 0.85, pričom všetky 8 prípadov sú signifikantne korelované (p < 0.05).
- use: precedens pre náš pilotný validation step — pri obhajobe v `30_method.md` môžeme argumentovať, že úroveň korelácie ~0.8 medzi automatikou a expertom je v tejto oblasti benchmarkovo dobrá; aj keď my ostávame pri experte ako primárnom zdroji, máme tým podloženú kontextovú referenciu

### Blok 10 — limit: SP a VD úlohy nie sú dokonale paralelné
- opiera sa o: §2.4 Evaluate LLMs as VDs (str. 7)
- locator: CureFun arXiv preprint v2 PDF, p. 7, §2.4
- kontrolný excerpt:
  > "It's worth noting that SPs and VDs, considered complementary tasks, do not align perfectly in real-world scenarios, as confirmed by our diagnostic evaluation of various LLMs. Highly performing LLMs in diagnostic QA benchmarks do not meet expectations in our VSP setting. Firstly, SPs are primarily designed for education and rely on standardized examinations, prioritize comprehensive and standardized communication, while real patient interactions prioritize efficiency and flexibility."
- parafráza: Autori v záverečnej poznámke explicitne priznávajú, že LLM, ktoré dobre skórujú v diagnostických QA benchmarkoch, nemusia dobre fungovať v SP role — pretože SP úloha je optimalizovaná na edukačnú štandardizáciu, kým reálny pacient prioritizuje efektivitu a flexibilitu.
- use: priamy argument pre náš non-diagnostic framing — môžeme v Limits citovať, že aj v komunite je rozdiel medzi „LLM ako diagnostický nástroj" a „LLM ako simulovaný pacient pre tréning" formálne uznaný, takže náš framing je podporený existujúcou literatúrou

## Limity alebo pozor
- ide o arXiv preprint, nie o peer-reviewed publikáciu — vhodné označiť v diskusii ako „preprint" a neopierať sa oň pri silne normatívnych tvrdeniach
- zameranie na čínsku medicínu (8 čínskych SP scenárov, ERNIE-Bot najsilnejší kvôli Chinese-language tuningu) — pri prenose do nášho slovenského/anglického MDD kontextu je to skôr framework precedens než priame empirické porovnanie
- ich SP úloha je široká all-purpose medical history (gastric, diabetes, COPD, COVID...), nie psychiatricky špecifická — preto obsahovo nemôže nahradiť psychiatrické VP literatúru ako wang2024patientpsi alebo kim2025mindvoyager

## Kľúčové citovateľné miesto
- CureFun arXiv preprint v2 PDF, p. 2, §1 — formálne pomenovanie role flipping a halucinácií ako typických zlyhaní plain LLM v SP role
- CureFun arXiv preprint v2 PDF, p. 4, §2.2 + Table 1 — B-ELO zlepšenie +250.18 pre GPT-3.5-Turbo a signifikantný hlavný efekt CureFun frameworku
- CureFun arXiv preprint v2 PDF, p. 5, §2.3 + Table 2 — Spearmanovo ρ ≈ 0.81 / Pearsonovo r ≈ 0.85 medzi automatickým a expertným hodnotením
- CureFun arXiv preprint v2 PDF, p. 7-8, §3.2 — ERRG (Extract-Retrieve-Rewrite-Generate) graph-driven architektúra a kontrolovaná konfabulácia
- CureFun arXiv preprint v2 PDF, p. 7, §2.4 — explicitné rozlíšenie SP úlohy od VD úlohy a obhajoba non-diagnostic framingu

## Tagy
- llm / methods / seeding

## Status použitia
- must-cite / checked
