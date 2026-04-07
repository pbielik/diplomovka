# asgari2025hallucinationframework

## Plná citácia
Asgari, E., Montaña-Brown, N., Dubois, M., Khalil, S., Balloch, J., Yeung, J. A., & Pimenta, D. (2025). *A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation*. npj Digital Medicine, 8(1). https://doi.org/10.1038/s41746-025-01670-7

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1038/s41746-025-01670-7`, PMID `40360677`, PMCID `PMC12075489`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02.4 Risks / limitations`, `07 Ethics – AI governance`
- Overený attachment: [Asgari 2025 PDF](/Users/pavol.bielik/Zotero/storage/JFKZSCE3/Asgari%20et%20al.%20-%202025%20-%20A%20framework%20to%20assess%20clinical%20safety%20and%20hallucination%20rates%20of%20LLMs%20for%20medical%20text%20summarisation.pdf)

## Klaster z literature map
- `07 Etika a AI governance`
- sekundárne aj `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- must-read

## Typ zdroja
- článok / evaluačný framework paper

## Hlavná myšlienka
- Klinicky použiteľné hodnotenie LLM výstupov nemá končiť pri všeobecných NLP metrikách; treba sledovať hallucinations, omissions a ich potenciálny klinický dopad cez explicitný safety framework a iteratívne experimenty s promptmi a workflow.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, prípadne `manuscript/30_method.md` a `manuscript/50_discussion.md`
- funkcia: safety / governance / evaluačný rámec pre LLM output

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: opening abstract and motivation
- locator: PDF p. 1, opening abstract paragraphs
- kontrolný excerpt:
  > "We propose a framework comprising (1) an error taxonomy for classifying LLM outputs, (2) an experimental structure for iterative comparisons in our LLM document generation pipeline, (3) a clinical safety framework to evaluate the harms of errors, and (4) a graphical user interface, CREOLA, to facilitate these processes. ... We observed a 1.47% hallucination rate and a 3.45% omission rate."
- parafráza: Paper ponúka veľmi konkrétny safety-first framework: taxonómia chýb, experimentálna štruktúra, clinical safety hodnotenie a nástroj na anotáciu. To z neho robí praktickejší zdroj než všeobecné úvahy o hallucinations.
- use: jadrový anchor pre LLM safety evaluation framing

### Blok 2
- opiera sa o: critique of generic NLP metrics + study objective
- locator: PDF p. 2, background + end of introduction
- kontrolný excerpt:
  > "Automated metrics ... while useful for comparing model-generated text with expert-written examples, exhibit significant limitations when applied to the evaluation of healthcare-related content. These metrics, primarily focused on surface-level textual similarity, fail to capture the semantic nuances, contextual dependencies, and domain-specific knowledge crucial for accurate medical discourse."
  >
  > "This study aims ... by introducing a framework which has four components: (1) a clinically and technically-informed error taxonomy ... (2) an experiment structure ... (3) a clinical safety framework ... and (4) an encompassing graphical user interface."
- parafráza: Autori veľmi jasne hovoria, že ROUGE/BLEU-like metriky nestačia pre medicínske použitie. Potrebuješ klinicky informovanú evaluáciu, nie len textovú podobnosť.
- use: silná opora proti používaniu len všeobecných NLP metrík

### Blok 3
- opiera sa o: Results on hallucinations and omissions
- locator: PDF p. 4, `Hallucinations` + `Omissions`
- kontrolný excerpt:
  > "Of 12,999 sentences in 450 clinical notes, 191 sentences had hallucinations (1.47%), of which 84 sentences (44%) were major ... Of the 49,590 sentences from our consultation transcripts, 1712 sentences were omitted (3.45%), of which 286 (16.7%) ... were classified as major."
- parafráza: Dôležité je, že paper neostáva pri abstraktnom safety jazyku, ale reportuje sentence-level hallucination a omission rates aj podiel major errors. To je už priamo použiteľný safety benchmark.
- use: empirický anchor pre clinically relevant error rates

### Blok 4
- opiera sa o: iterative experiments and prompt engineering
- locator: PDF p. 5-7, iterative experiments discussion
- kontrolný excerpt:
  > "By designing prompts that addressed specific aspects of the notes (base, template and style), we were able to focus our iterations to achieve the best results. ... our results suggest that we can achieve state-of-the-art, sub-human clinical error rates by carefully engineering and subsequently validating LLMs to produce safe outputs."
- parafráza: Autori ukazujú, že prompt/workflow engineering môže safety výrazne meniť. Dôležitá pointa ale nie je len "lepší prompt", ale to, že tento efekt treba iteratívne validovať na klinických metrikách.
- use: argument pre experiment-driven safety tuning, nie ad hoc promptovanie

### Blok 5
- opiera sa o: methods taxonomy and safety framework
- locator: PDF p. 11-13, methods sections
- kontrolný excerpt:
  > "we categorise errors as either 'major' or 'minor', where major errors can impact on the diagnosis or the management of the patient if not corrected."
  >
  > "we propose to divide hallucinations into four categories: (1) fabrication ... (2) negation ... (3) causality ... and (4) contextual ..."
- parafráza: Pre tvoju prácu je veľmi užitočná aj samotná taxonómia: major/minor rozlíšenie a štyri typy hallucinations poskytujú praktický jazyk, ako hovoriť o kvalite a bezpečnosti AI výstupov.
- use: bezpečnostná taxonómia pre discussion alebo metodické poznámky

## Kľúčová definícia / výsledok / argument
- Pri LLM dokumentačných a sumarizačných úlohách treba hodnotiť nielen hallucinations, ale aj omissions a ich klinický dopad; bezpečnosť je tu vlastnosť workflowu, nie len modelu.

## Limity alebo pozor
- Paper je zameraný na medicínske text summarisation, nie na interview rating alebo psychiatrický dialogický systém.
- Viaceré experimenty sú viazané na jeden model a konkrétny pipeline setup, takže presný error rate sa nemusí preniesť na inú architektúru.

## Kľúčové citovateľné miesto
- PDF p. 1-2 pre štvorzložkový framework a limitácie generic metrics
- PDF p. 4 pre hallucination a omission rates
- PDF p. 5-7 pre iteratívne zlepšovanie cez prompting/workflow
- PDF p. 11-13 pre taxonómiu chýb a safety assessment

## Tagy
- ethics / llm / analysis

## Status použitia
- must-cite / checked
