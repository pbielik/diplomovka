# chen2023SoulChatImprovingLLMs

## Plná citácia
Chen, Y., Xing, X., Lin, J., Zheng, H., Wang, Z., Liu, Q., & Xu, X. (2023). *SoulChat: Improving LLMs' empathy, listening, and comfort abilities through fine-tuning with multi-turn empathy conversations*. In *Findings of the Association for Computational Linguistics: EMNLP 2023* (pp. 1170-1183). Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.findings-emnlp.83

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.18653/v1/2023.findings-emnlp.83`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02 LLM – mental health / psychiatry`
- Overený attachment: [Chen 2023 SoulChat PDF](/Users/pavol.bielik/Zotero/storage/ZPMVF5DT/Chen%20et%20al.%20-%202023%20-%20SoulChat%20Improving%20LLMs%E2%80%99%20Empathy%2C%20Listening%2C%20and%20Comfort%20Abilities%20through%20Fine-tuning%20with%20Multi-t.pdf)

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- should-read

## Typ zdroja
- conference paper / dataset + model paper

## Hlavná myšlienka
- SoulChat paper je dôležitý pre LLM vetvu preto, že veľmi explicitne ukazuje rozdiel medzi "rozumnou radou" a skutočne empatickou odpoveďou. Namiesto generických rád stavia na multi-turn empathy datasete a fine-tuningu, ktorý posúva model viac k listening/comfort štýlu.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, `manuscript/50_discussion.md`
- funkcia: opora pre rozdiel medzi advice-giving a empatickou interakciou; dataset/model anchor pre empathic conversation design

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "When users seek psychological support, they need to gain empathy, trust, understanding and comfort, rather than just reasonable advice. To this end, we constructed a multi-turn empathetic conversation dataset of more than 2 million samples ... Experiments have shown that the empathy ability of LLMs can be significantly enhanced when finetuning ..."
- parafráza: Hlavný argument paperu je pre tvoju prácu veľmi užitočný: v mental-health kontexte nestačí "správna" rada; dôležité sú aj trust, comfort a empatický priebeh rozhovoru.
- use: opora pre to, že kvalita rozhovoru nie je redukovateľná len na informatívnosť

### Blok 2
- opiera sa o: Introduction
- locator: PDF p. 1, `Introduction`
- kontrolný excerpt:
  > "ChatGPT tends to provide repetitive and standardized responses ... is inclined to provide suggestions rather than ask questions or listen ... Users who seek emotional support usually expect empathy support such as listening, understanding and comfort."
- parafráza: Autori veľmi presne pomenúvajú zlyhanie baseline LLM v psychologickej podpore: príliš rýchlo radia, málo sa pýtajú a málo počúvajú.
- use: limitations framing pre generic LLM counseling

### Blok 3
- opiera sa o: dataset construction
- locator: PDF p. 3, `SoulChatCorpus Collection`
- kontrolný excerpt:
  > "we first constructed 215,813 different psychological counseling questions about 12 topics and 619,725 answers ... we obtained a multi-turn empathy conversation dataset, named SoulChatCorpus, with 2,300,248 samples. To our knowledge, it is the first million-scale multi-turn empathy conversation dataset in the field of mental health or emotional support."
- parafráza: Toto je silná dátová opora: paper nestojí len na malej curated sade, ale na veľmi veľkom multi-turn empathy korpuse, ktorý cieli presne na štýl psychologickej podpory.
- use: dataset anchor pre empatické modelovanie rozhovoru

### Blok 4
- opiera sa o: privacy-aware data cleaning
- locator: PDF p. 3 a p. 5, `SoulChatCorpus Collection` + `Ethics Statement`
- kontrolný excerpt:
  > "Rule-based cleaning, manual rewriting and human proofreading are applied to ensure that there is no sensitive or privacy-related content in the dataset." ... "we removed 105,134 low-quality samples" ... "Any text related to privacy has been rewritten or removed."
- parafráza: Paper je užitočný aj metodicky: pri mental-health datasetoch explicitne rieši privacy a safety cleaning, nie len výkon modelu.
- use: opora pre etickú opatrnosť pri práci s mental-health konverzačnými dátami

### Blok 5
- opiera sa o: Results and Analysis
- locator: PDF p. 4-5, `3.3 Results and Analysis`
- kontrolný excerpt:
  > "Three individual experts majoring in Psychology were asked to evaluate the generated responses in terms of content naturalness, empathy level, helpfulness and safety ... Generally, SoulChat outperforms ChatGLM-6B, ChatGPT and MeChat in both automatic evaluation metrics and Emp. metric ... the results on SMILECHAT demonstrates SoulChat's excellent zero-shot performance."
- parafráza: Zmysluplné je aj to, že evaluation nejde len cez automatické skóre; autori pridali psychológov a oddelili naturalness, empathy, helpfulness a safety.
- use: argument pre multi-dimensional hodnotenie LLM odpovedí

### Blok 6
- opiera sa o: Conclusion and Limitations
- locator: PDF p. 5, `Conclusion and Future Work` + `Limitations`
- kontrolný excerpt:
  > "using this dataset to finetune LLMs leads to high-level empathy ability when users try to seek emotional support from LLMs. Future work needs to further consider user attributes, such as personality, gender ..." 
- parafráza: Paper nekončí triumfalisticky; uznáva, že aj empatický model treba ďalej prispôsobovať podľa používateľa a kontextu.
- use: balanced discussion anchor pre personalization a residual limits

### Blok 7
- opiera sa o: Ethics Statement
- locator: PDF p. 5, `Potential Risks of the Model`
- kontrolný excerpt:
  > "there are inevitably answers that may pose harm to users ... it is necessary to inform the users in advance that the answers they see are generated by the AI model and are for reference only."
- parafráza: Dôležitý safety point je, že ani lepší empatický fine-tuned model sa nemá prezentovať ako autoritatívna klinická odpoveď.
- use: ethics / disclosure framing

## Kľúčová definícia / výsledok / argument
- Fine-tuning na veľkom multi-turn empathy korpuse vie LLM posunúť od generických rád k viac empatickému, počúvajúcemu štýlu, ale bezpečnosť a transparentná disclosure zostávajú nutné.

## Limity alebo pozor
- Ide o čínsky kontext a jazykovo špecifický dataset; generalizácia na iné jazyky a kultúrne prostredia nie je automatická.
- Paper je orientovaný na empatický štýl odpovede, nie na plnú klinickú validitu alebo terapeutický outcome.

## Kľúčové citovateľné miesto
- PDF p. 1 pre "empathy vs advice" framing
- PDF p. 3 pre `2,300,248` samples a dataset construction
- PDF p. 4-5 pre psychology-expert evaluation a safety/disclosure limits

## Tagy
- llm / methods / seeding

## Status použitia
- discussion / checked
