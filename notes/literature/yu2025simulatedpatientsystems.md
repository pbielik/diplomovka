# yu2025simulatedpatientsystems

## Plná citácia
Yu, H., Zhou, J., Li, L., Chen, S., Gallifant, J., Shi, A., Sun, J., Li, X., He, J., Hua, W., Jin, M., Chen, G., Zhou, Y., Li, Z., Gupte, T., Chen, M.-L., Azizi, Z., Dou, Q., Yan, B. P., Xing, Y., Zhang, Y., Assimes, T. L., Bitterman, D. S., Ma, X., Lu, L., & Fan, L. (2025). *Simulated patient systems powered by large language model-based AI agents offer potential for transforming medical education*. Communications Medicine, 6(1), Article 27. https://doi.org/10.1038/s43856-025-01283-x

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1038/s43856-025-01283-x`, PMID `41420084`, PMCID `PMC12808140`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02.2 Simulated patients / virtual patients`, `02.3 Education / training use-cases`
- Overený attachment: [Yu 2025 PDF](/Users/pavol.bielik/Zotero/storage/8THUSBWD/Yu%20et%20al.%20-%202025%20-%20Simulated%20patient%20systems%20powered%20by%20large%20language%20model-based%20AI%20agents%20offer%20potential%20for%20transf.pdf)

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- must-read

## Typ zdroja
- článok / technologicko-edukačná štúdia

## Hlavná myšlienka
- LLM-based simulated patient systems môžu priniesť škálovateľné, realistické a konzistentné tréningové interakcie, ale ich použitie treba podoprieť explicitným hodnotením accuracy, trustworthiness, readability, robustness a educational value.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, prípadne neskôr `manuscript/50_discussion.md`
- funkcia: teória / seeding / simulated patients / methodological framing

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract + Plain Language Summary
- locator: PDF p. 1 / article p. 1, Abstract + Plain Language Summary
- kontrolný excerpt:
  > "Simulated patient systems are vital in medical education and research, providing safe, integrative training environments and supporting clinical decision-making. Progressive Artificial Intelligence (AI) technologies, such as Large Language Models (LLM), could advance simulated patient systems by replicating medical conditions and patient-doctor interactions with high fidelity and low cost. However, effectiveness and trustworthiness remain challenging."
  >
  > "A user study with medical students shows that AIPatient delivers high fidelity, usability, and educational value, matching or exceeding human-simulated patients in history-taking. Conclusions: Large language model-based simulated patient systems provide accurate, readable, and reliable medical encounters and demonstrates potential to transform medical education."
- parafráza: Autori stavajú simulated patient systems ako dôležitý tréningový nástroj a zároveň hovoria, že LLM ich môžu sprístupniť vo vysokom meradle a za nižšie náklady. Hneď v abstrakte však zdôrazňujú, že kľúčové ostávajú effectiveness a trustworthiness.
- use: silný anchor pre framing simulated patient use-case a zároveň pre potrebu opatrnej evaluácie

### Blok 2
- opiera sa o: Introduction
- locator: PDF p. 2 / article p. 2, Introduction
- kontrolný excerpt:
  > "While simulated patients are designed to be a low-risk and high-fidelity tool, there are unresolved concerns about their effectiveness and the trustworthiness. Current usability evaluation of simulated patients is usually subjective. As a result, variations of medical students’ familiarity of simulated patient systems could cause inaccuracy in SP-based medical skill evaluation."
  >
  > "While these implementations are promising, there are still various concerns in effectiveness and trustworthiness of the systems, including (1) the lack of a large, comprehensive, and diverse patient profile database, (2) the need for fact-checking mechanisms to minimize hallucinations and ensure consistency, (3) the insufficient flexibility in taking on different personalities, and (4) the absence of a thorough evaluation framework."
- parafráza: Paper presne pomenúva štyri slabé miesta doterajších LLM simulated patients: chýbajúca široká databáza profilov, fact-checking a hallucination control, slabá práca s osobnosťou a nedostatočný evaluačný rámec.
- use: opora pre tvrdenie, že simulated patient systémy treba hodnotiť širšie než len podľa subjektívneho dojmu

### Blok 3
- opiera sa o: Methods `Reasoning RAG agentic workflow` + `Evaluation and data labeling`
- locator: PDF p. 3 / article p. 3, Fig. 2 + evaluation paragraphs
- kontrolný excerpt:
  > "The key stages in the workflow include retrieval with the Retrieval Agent and the KG Query Generation Agent, reasoning with the Abstraction Agent and the Checker Agent, and generation with the Rewrite Agent and the Summarization Agent. There are three initial inputs, including the AIPatient KG, a natural language query from the user, and the Conversation History between the user and the AIPatient."
  >
  > "To evaluate performance of the AIPatient system, we focus on its effectiveness and trustworthiness. Synthesizing the metrics in previous research of simulated patient systems and adapting them to the AIPatient system, we focus on five dimensions."
- parafráza: AIPatient nie je len jeden prompt, ale viac-agentový workflow s retrieval, reasoning a generation vrstvami. Metodicky je dôležité aj to, že autori explicitne oddeľujú effectiveness a trustworthiness ako jadro evaluácie.
- use: keď bude treba ukázať, že kvalitný AI simulated patient potrebuje architektúru aj evaluačný rámec, nie len “funguje/nefunguje”

### Blok 4
- opiera sa o: Results `Investigation of system’s readability, robustness, and stability`
- locator: PDF p. 7-8 / article p. 7-8, Results
- kontrolný excerpt:
  > "GPT-4-Turbo achieves the highest overall accuracy (94.15%), followed closely by Claude-4-Opus (90.80%) and GPT-4o (89.02%). These findings underscore the superior reliability of advanced proprietary models as the backbone in handling complex question answering tasks."
  >
  > "For Readability, the AIPatient system presents Flesch Reading Ease scores ranging from 10.91 to 99.23 (median 68.77) and Flesch-Kincaid Grade Level peaking at the sixth-grade level (median grade level 6.4). Across 32 personality groups, the median data loss is 2% (range: 0–5.88%), indicating consistently low variability. These results confirm the system’s stability and consistency across diverse simulated personalities."
- parafráza: Výsledky článku sa neopierajú len o celkový dojem, ale reportujú QA accuracy, readability a stabilitu naprieč personality variants. To je dôležitý príklad, ako možno simulated patient systém hodnotiť systematickejšie.
- use: argument pre viacrozmernú evaluáciu AI interview systémov

### Blok 5
- opiera sa o: Results `Evaluation of the AIPatient system to human-simulated patients`
- locator: PDF p. 8-9 / article p. 8-9, Fig. 6 + discussion paragraphs
- kontrolný excerpt:
  > "Across most dimensions, AIPatient performs comparably or better than H-SPs. In the domain of fidelity, AIPatient scores higher in both case script adherence and alignment with the intended medical condition, with a particularly notable advantage in emotional realism. In the domain of educational effectiveness, AIPatient shows advantages in supporting diagnostic accuracy (4.27 vs. 3.87) and improving clinical reasoning skills (4.41 vs. 3.97)."
  >
  > "Our user evaluation with medical students further highlights AIPatient’s educational value. In a paired crossover study with H-SPs, AIPatient matches or outperforms H-SPs across most metrics—including emotional realism, reliability, and learner satisfaction."
- parafráza: V paired crossover evaluácii s medikmi AIPatient aspoň v tejto štúdii dosahuje porovnateľné alebo lepšie skóre než human-simulated patients v niektorých dimenziách fidelity, usability a educational effectiveness. To z neho robí silný empirický anchor pre vzdelávací potenciál simulated patients.
- use: keď budeš potrebovať empirickú oporu pre edukačnú hodnotu AI simulated patients

## Kľúčová definícia / výsledok / argument
- Dobrá simulated patient platform sa nemá hodnotiť len cez “realistický dojem”, ale cez kombináciu accuracy, readability, robustness, stability a user-facing educational value.

## Limity alebo pozor
- Štúdia je z prostredia všeobecného medicínskeho vzdelávania, nie priamo z psychologického alebo psychiatrického interview ratingu.
- Výsledky sú silné pre simulated patient framing, ale prenos do diplomovky musí byť opatrný a nesmie automaticky znamenať diagnostickú pripravenosť systému.

## Kľúčové citovateľné miesto
- PDF p. 1 pre high-level promise + trustworthiness caveat
- PDF p. 2 pre štyri hlavné slabé miesta doterajších systémov
- PDF p. 7-8 pre accuracy, readability, robustness a stability
- PDF p. 8-9 pre porovnanie s human-simulated patients

## Tagy
- llm / seeding / analysis

## Status použitia
- must-cite / checked
