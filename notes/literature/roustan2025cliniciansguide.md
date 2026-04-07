# roustan2025cliniciansguide

## Plná citácia
Roustan, D., & Bastardot, F. (2025). *The clinicians' guide to large language models: A general perspective with a focus on hallucinations*. Interactive Journal of Medical Research, 14, e59823. https://doi.org/10.2196/59823

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.2196/59823`, PMID `39874574`, PMCID `PMC11815294`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `07 Ethics – AI governance`
- Overený attachment: [Roustan 2025 PDF](/Users/pavol.bielik/Zotero/storage/VBJHU79U/Roustan and Bastardot - 2025 - The Clinicians’ Guide to Large Language Models A General Perspective With a Focus on Hallucinations.pdf)

## Klaster z literature map
- `07 Etika a AI governance`

## Priorita podľa literature map
- must-read

## Typ zdroja
- viewpoint / clinical guidance

## Hlavná myšlienka
- Pre klinickú prax nie je hlavný problém len to, že LLM môžu „niekedy“ halucinovať, ale že pri nesprávnom použití môžu systematicky posúvať diagnostické a terapeutické uvažovanie nesprávnym smerom. Bez znalosti datasetu, testovania variability odpovedí a lokálnej governance vrstvy nie sú spoľahlivým klinickým nástrojom.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, `manuscript/50_discussion.md`
- funkcia: clinician-facing guidance k hallucinations, governance a praktickým safeguards

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "A significant risk associated with the use of LLMs is their potential to create hallucinations. ... The implications for clinical practice range from the generation of inaccurate diagnostic and therapeutic information to the reinforcement of flawed diagnostic reasoning pathways ... To reduce this risk, we developed a general technical framework ..."
- parafráza: Roustan paper je priamy klinický safety zdroj: hallucinations nevedú len k jednej zlej odpovedi, ale môžu upevňovať chybný reasoning pathway.
- use: discussion anchor pre clinical risk pri LLM use

### Blok 2
- opiera sa o: Overview of Hallucinations
- locator: PDF p. 2, `Overview of Hallucinations`
- kontrolný excerpt:
  > "Hallucinations ... refer to the generation of false or fabricated information. ... Another major cause of hallucinations stems from the very way certain LLMs are programmed. Indeed, most LLMs are auto-regressive ... factual accuracy is not the end goal. Rather, accuracy is inferred from a high probability of adequate token prediction ..."
- parafráza: Dôležitý prínos paperu je, že halucinácie nevysvetľuje len ako „zlý tréningový dataset“, ale aj ako vlastnosť autoregresívnej generácie, kde cieľom nie je pravda, ale pravdepodobný ďalší token.
- use: presnejšie vysvetlenie mechanizmu hallucinations

### Blok 3
- opiera sa o: Implications for Clinical Medicine
- locator: PDF p. 2-3, `Implications for Clinical Medicine`
- kontrolný excerpt:
  > "LLMs may erroneously attribute clinical, biological, or radiological characteristics to certain diseases ... This flaw, in combination with anchoring and confirmation bias, may unknowingly lead the clinician down an erroneous diagnostic or therapeutic pathway. ... LLMs may also make false claims about diagnostic accuracy for diagnostic procedures."
- parafráza: Tento paper dobre prepája technický problém hallucinations s reálnou klinickou kogníciou: LLM chyba sa vie spojiť s anchoringom a confirmation bias a tým posilniť nesprávne rozhodovanie.
- use: opora pre practical safety risk framing

### Blok 4
- opiera sa o: Mitigating Hallucinations in Clinical Practice
- locator: PDF p. 3-4, `Mitigating Hallucinations in Clinical Practice` + Textbox 1
- kontrolný excerpt:
  > "Understanding the model's origins, version, training database content, and strengths as well as drawbacks are essential prerequisites ... user input should be carefully crafted ... model accuracy and hallucination prevalence should be assessed before being put into practice, through iterative testing and evaluation. ... consistency, as well as variability in the answers, should be evaluated by regenerating the LLM's responses multiple times."
- parafráza: Roustanov najpraktickejší príspevok je tento clinician checklist: poznať pôvod modelu, vedieť čo je v datasete, cielene promptovať a pred použitím iteratívne testovať aj variabilitu odpovedí.
- use: priamo použiteľný safeguard framework

### Blok 5
- opiera sa o: Prospects + Conclusions + Textbox 2
- locator: PDF p. 4-6, `Prospects`, `Conclusions`, Textbox 2
- kontrolný excerpt:
  > "Institutional governance is key to their implementation for everyday use." ... "specific tasks for which the LLM should be used" ... "Ensuring a human has the final word in the decision-making process" ... "training procedures and certifications required for health care professionals to use the tool."
- parafráza: Paper nejde len po individuálnom kritickom myslení klinika. Explicitne volá po inštitucionálnej governance: scope of use, human-in-the-loop, tréning, accountability a quality control.
- use: governance a implementation framing pre discussion

## Kľúčová definícia / výsledok / argument
- LLM majú klinický potenciál, ale bez testovania hallucination risku, variability odpovedí a bez inštitucionálnej governance nie sú bezpečným decision-support nástrojom.

## Limity alebo pozor
- Ide o viewpoint, nie o systematický review alebo prospektívnu validačnú štúdiu.
- Viaceré odporúčania sú frameworkové a pragmatické, nie kvantitatívne validované cez jednu štúdiu.

## Kľúčové citovateľné miesto
- PDF p. 1-2 pre hallucination definition a clinical implications
- PDF p. 3-4 pre mitigation checklist
- PDF p. 5-6 pre institutional governance a human-in-the-loop argument

## Tagy
- ethics / llm / seeding

## Status použitia
- must-cite / checked
