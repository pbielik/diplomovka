# mitani2017ordinalsummarymeasures

## Plná citácia
Mitani, A. A., Freer, P. E., & Nelson, K. P. (2017). *Summary measures of agreement and association between many raters' ordinal classifications*. Annals of Epidemiology, 27(10), 677-685.e4. https://doi.org/10.1016/j.annepidem.2017.09.001

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1016/j.annepidem.2017.09.001`, PMID `29029991`, PMCID `PMC5687310`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → metodická vetva pre agreement / ordinal ratings
- Overený attachment: [Mitani 2017 PDF](/Users/pavol.bielik/Zotero/storage/AXQAQDT9/Mitani et al. - 2017 - Summary measures of agreement and association between many raters' ordinal classifications.pdf)

## Klaster z literature map
- `04 Metóda, štatistika a analytický dizajn`

## Priorita podľa literature map
- optional

## Typ zdroja
- metodologický článok

## Hlavná myšlienka
- Pri ordinal expert ratingoch s viacerými ratermi nestačí mechanicky reportovať Cohenovo kappa alebo ICC. Mitani paper systematicky ukazuje rozdiel medzi agreement a association, limity klasických metrík pri mnohých rateroch, missing/unbalanced dátach a pri extrémnej prevalencii, a obhajuje model-based prístup ako robustnejší rámec.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/30_method.md`, `manuscript/40_results.md`
- funkcia: obhájenie rozdielu agreement vs association pri ordinálnych ratingoch a metodická opora pre diskusiu o limitoch kappa-like metrík

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "However, using traditional measures of agreement in some studies is challenging due to the presence of many raters, the use of an ordinal classification scale and unbalanced data. ... Some measures were influenced by the underlying prevalence of disease and raters’ marginal distributions and/or were limited in use to balanced data sets where every rater classifies every subject. ... Model-based measures provide a flexible approach for calculating agreement and association and are robust to missing and unbalanced data as well as the underlying disease prevalence."
- parafráza: Abstrakt veľmi priamo pomenúva jadro problému: mnoho raterov, ordinálna škála a nevyvážené dáta lámajú jednoduché agreement metriky a model-based prístup je voči tomu robustnejší.
- use: high-level metodický argument pre ordinal many-rater dizajn

### Blok 2
- opiera sa o: Introduction
- locator: PDF p. 2-3, `Introduction`
- kontrolný excerpt:
  > "Measures of agreement focus on assessing the levels of exact concordance ... while measures of association also take into account the degrees of disagreement among raters’ classifications. ... many agreement studies report the average or the range of pairwise Cohen’s kappas and weighted kappas when assessing the agreement and association respectively among more than two raters. This can lead to complexities in interpretation and is infeasible in studies with a large number of raters."
- parafráza: Paper je užitočný aj konceptuálne: odlišuje exact agreement od association pri ordinálnych kategóriách a upozorňuje, že pri väčšom počte raterov sa pairwise kappa prístup stáva ťažko interpretovateľný.
- use: vysvetlenie, prečo v texte odlišovať agreement a association

### Blok 3
- opiera sa o: Methods, model-based kappa statistic
- locator: PDF p. 4-6, `2.1.3 Model-based kappa statistic` + `2.2 Measures of association`
- kontrolný excerpt:
  > "An ordinal GLMM with a probit link and a crossed random effect structure can be used to model the cumulative probability ... There are several advantages in using a model-based measure of agreement over simpler summary statistics. One is the ability to accommodate missing or unbalanced data ... Another is the option to include covariates in the GLMM to evaluate the effects of raters’ or subjects’ characteristics ..."
- parafráza: Metodické jadro paperu je GLMM-based rámec, ktorý vie naraz absorbovať subject aj rater heterogenitu, missingness a prípadné kovariáty.
- use: obhájenie modernejšieho many-rater ordinal frameworku

### Blok 4
- opiera sa o: Example One (AIM) + Example Two (Gonin and Lipsitz)
- locator: PDF p. 9-10, `3.1 Example One (AIM)` + `3.2 Example Two (Gonin and Lipsitz)`
- kontrolný excerpt:
  > "The average pairwise Cohen’s kappa and Fleiss’ kappa yielded similar agreement measures ... Nelson’s model-based approach produced a kappa estimate that was slightly lower ... Nelson’s model-based approach yielded a much smaller measure of association ... In this data set, not all subjects were rated by J = 119 raters. Therefore, we had to use a subset ... In [the DIDS] study ... Cohen’s kappa, Fleiss’ kappa, the ICC and Mielke’s method all require data to be balanced ... This is an example where only model-based measures of agreement and association can be applied due to the highly unbalanced nature of the data set."
- parafráza: Praktická hodnota článku je v ukážkach, že rôzne metriky dávajú reálne odlišné výsledky a že pri sparse/unbalanced many-rater dátach môžu byť niektoré klasické prístupy úplne nepoužiteľné.
- use: opora pre interpretáciu a limitácie agreement metrík vo výsledkoch

### Blok 5
- opiera sa o: Simulation study
- locator: PDF p. 11-12, `3.4 Simulation study`
- kontrolný excerpt:
  > "Nelson’s model-based approach remained unchanged and was robust to varying disease prevalence. The other two measures of agreement (Cohen’s kappa and Fleiss’ kappa) overestimated the agreement for more extreme levels of prevalence ... Nelson’s model-based measure for association was also unaffected by the changes in level of disease prevalence whereas the average Cohen’s weighted kappa and the ICC were impacted by the underlying disease prevalence and generally overestimated the association ..."
- parafráza: Simulácia je dôležitá, lebo ukazuje mechanizmus problému: pri extrémnej prevalencii môžu kappa/ICC-like súhrny systematicky nadhodnocovať agreement alebo association.
- use: methodological caution pri interpretácii ordinal agreement indexov

### Blok 6
- opiera sa o: Discussion + recommendations
- locator: PDF p. 13-14, `4. Discussion`
- kontrolný excerpt:
  > "An important limitation of the more commonly used measures of agreement and association (Cohen’s kappa, Fleiss’ kappa, and the ICC) is that they cannot be applied to unbalanced data sets where not all raters classify each subject. ... We recommend that researchers estimate the disease prevalence in their study ... If the subjects’ test results are unequally distributed across the ordinal categories ... we recommend Nelson and Edwards’ model-based approach to measure agreement. When measuring association in large-scale studies, we would generally recommend the use of a model-based summary measure ..."
- parafráza: Záverečné odporúčanie paperu je pre tvoju metodickú argumentáciu veľmi použiteľné: najprv skontrolovať prevalenciu a balance dát a pri nevyvážených ordinal ratings preferovať model-based summary measures.
- use: priama opora pre metodické rozhodovanie a diskusiu limitov

## Kľúčová definícia / výsledok / argument
- Pri many-rater ordinálnych dátach treba oddeliť agreement od association a zohľadniť balance/prevalence; model-based miery sú robustnejšie než jednoduché kappa/ICC súhrny.

## Limity alebo pozor
- Paper rieši všeobecné screening-test settings a nehovorí priamo o tvojej konkrétnej škále či dizajne rozhovorov.
- Odporúča model-based prístup, ale nie je to automaticky argument, že v každom kontexte musíš reportovať presne tie isté metriky ako autori.

## Kľúčové citovateľné miesto
- PDF p. 1 pre summary problémov: many raters, ordinal scale, unbalanced data
- PDF p. 4-6 pre GLMM/model-based framework
- PDF p. 11-14 pre simulation + praktické odporúčania podľa prevalence a balance dát

## Tagy
- methods / analysis

## Status použitia
- method / checked
