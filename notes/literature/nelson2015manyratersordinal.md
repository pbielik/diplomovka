# nelson2015manyratersordinal

## Plná citácia
Nelson, K. P., & Edwards, D. (2015). *Measures of agreement between many raters for ordinal classifications*. Statistics in Medicine, 34(23), 3116-3132. https://doi.org/10.1002/sim.6546

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1002/sim.6546`, PMID `26095449`, PMCID `PMC4560692`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `04.2 ICC / agreement`, `04.4 Ordinal models`
- Overený attachment: [Nelson 2015 PDF](/Users/pavol.bielik/Zotero/storage/BR7BHV5E/Nelson%20and%20Edwards%20-%202015%20-%20Measures%20of%20agreement%20between%20many%20raters%20for%20ordinal%20classifications.pdf)

## Klaster z literature map
- `04 Metóda, štatistika a analytický dizajn`

## Priorita podľa literature map
- must-read

## Typ zdroja
- článok / metodický štatistický text

## Hlavná myšlienka
- Pri many-raters ordinal dátach nestačí spoliehať sa na kappa-based summary measures; Nelson a Edwards navrhujú model-based prístup cez ordinal GLMM, ktorý lepšie škáluje na veľké rater štúdie, umožňuje generalizáciu a je menej citlivý na prevalence a marginal-distribution problémy.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/30_method.md`, prípadne neskôr interpretačný rámec pre `manuscript/40_results.md`
- funkcia: metodika / analýza / many-raters ordinal agreement framing

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, Abstract
- kontrolný excerpt:
  > "Existing summary measures of agreement rely on extensions of Cohen's kappa. These are prone to prevalence and marginal distribution issues, become increasingly complex for more than three experts or are not easily implemented. Here we propose a model-based approach to assess agreement in large-scale studies based upon a framework of ordinal generalized linear mixed models. A summary measure of agreement is proposed for multiple experts assessing the same sample of patients' test results according to an ordered categorical scale."
- parafráza: Hlavný vstup paperu je veľmi priamočiary: kappa-like miery majú pri väčšom počte raterov a ordinálnych kategóriách slabiny, preto autori presúvajú agreement problém do rámca ordinal GLMM.
- use: metodická opora, prečo ísť za hranicu jednoduchých kappa summary measures

### Blok 2
- opiera sa o: Introduction motivation
- locator: PDF p. 2, Introduction
- kontrolný excerpt:
  > "Consequently large-scale agreement studies involving many experts and ordinal classification scales are becoming increasingly common to assess levels of agreement and to investigate factors that may be linked with the observed variability between experts. ... an important advantage of our large-scale approach is the ability to generalize findings to experts and patients who typically use these diagnostic tests, if experts and subjects are randomly sampled from their populations."
- parafráza: Paper výslovne mieri na situácie, kde máš veľa expertov a ordinálne ratingy. Zaujímavé je aj to, že agreement neberie len ako technický summary index, ale ako populáciu-based inferenčný problém.
- use: opora pre framing tvojho datasetu ako many-raters ordinal setting

### Blok 3
- opiera sa o: section `Proposed Model of Agreement for Ordered Classifications`
- locator: PDF p. 4, section `3. Proposed Model of Agreement for Ordered Classifications`
- kontrolný excerpt:
  > "The class of ordinal generalized linear mixed models (GLMMs) provides a natural and appealing framework for modeling agreement in large-scale studies between experts in the population-based setting since any number (at least three) of experts and subjects can be included without increasing the complexity of the model, in contrast to many other approaches, and each expert may rate some or all of the subjects."
  >
  > "When experts and subjects included in the study are randomly sampled from their populations, results can be generalized to future users (both experts and subjects) of the diagnostic test under study."
- parafráza: Toto je jadrový metodický blok paperu: ordinal GLMM škáluje na ľubovoľný počet expertov a subjektov bez explózie modelovej zložitosti a zároveň umožňuje interpretačne čistejšiu generalizáciu.
- use: silný anchor pre prepojenie many-raters dizajnu s mixed-model logikou

### Blok 4
- opiera sa o: section `Proposed Summary Measure of Agreement`
- locator: PDF p. 6-7, sections `4. Proposed Summary Measure of Agreement`
- kontrolný excerpt:
  > "The proposed measure avoids some of the key flaws associated with Cohen's kappa and its extensions. ... the value of κm is not influenced by prevalence of the disease, which here is indicated by the percent of observations falling into each of the C categories."
  >
  > "A value of κm close to 0 is interpreted as little or no agreement, a value around 0.5 suggests a moderate amount of agreement, and a value of 1 as perfect agreement between the multiple experts, after correcting for chance agreement."
- parafráza: Autori nielen navrhujú model, ale aj novú chance-corrected agreement mieru `κm`, ktorú explicitne chránia pred prevalence efektom. To je veľmi relevantné, ak sú kategórie nerovnomerne obsadené.
- use: argument pre opatrnosť pri interpretácii prevalence-sensitive agreement metrík

### Blok 5
- opiera sa o: Discussion + empirical examples
- locator: PDF p. 12 + p. 22-23, `Discussion` + Tables IV-V
- kontrolný excerpt:
  > "The proposed approach flexibly can accommodate large numbers of experts and subject test results without increasing complexity as the number of experts increases, while allowing for missing data. ... Our approach allows agreement between all the experts to be assessed in one unified approach, lending power and efficiency to the study of agreement between the multiple experts when assumptions are met."
  >
  > "Model-based Kappa κm 0.484 ... Fleiss’ kappa κF 0.569 ... Cohen's GLMM-based kappa κGLMM 0.526."
- parafráza: V diskusii aj príkladoch paper ukazuje, že unified model-based prístup vie viesť k iným agreement odhadom než tradičné kappa varianty. To znamená, že výber metriky tu nie je kozmetická voľba, ale mení záver o sile zhody.
- use: opora pre metodickú disciplínu pri výbere agreement metrík

## Kľúčová definícia / výsledok / argument
- Many-raters ordinal agreement má byť modelovaný ako population-based ordinal mixed-model problém, nie redukovaný na jednoduché kappa rozšírenia bez ohľadu na prevalence a marginal distributions.

## Limity alebo pozor
- Ide o štatistický metodický paper; priamy prepis do diplomovky musí byť opatrný a skôr konceptuálny než rovnicový.
- Paper navrhuje vlastnú mieru `κm`, ale aj keď ju priamo nepoužiješ, je veľmi užitočný ako argument proti nekritickému spoliehaniu sa na kappa family.

## Kľúčové citovateľné miesto
- PDF p. 1-2 pre problém kappa extensions a motiváciu
- PDF p. 4 pre ordinal GLMM framework
- PDF p. 6-7 pre `κm` a prevalence argument
- PDF p. 12 a p. 22-23 pre diskusiu a rozdiely oproti tradičným kappa metrikám

## Tagy
- analysis / methods

## Status použitia
- method / checked
