# jakobsson2005ordinalagreement

## Plná citácia
Jakobsson, U., & Westergren, A. (2005). *Statistical methods for assessing agreement for ordinal data*. Scandinavian Journal of Caring Sciences, 19(4), 427-431. https://doi.org/10.1111/j.1471-6712.2005.00368.x

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1111/j.1471-6712.2005.00368.x`, PMID `16324069`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `04.4 Ordinal models`
- Overený attachment: [Jakobsson 2005 PDF](/Users/pavol.bielik/Zotero/storage/F3W7T54J/Jakobsson and Westergren - 2005 - Statistical methods for assessing agreement for ordinal data.pdf)

## Klaster z literature map
- `04 Metóda, štatistika a analytický dizajn`

## Priorita podľa literature map
- must-read

## Typ zdroja
- metodologický článok / review

## Hlavná myšlienka
- Pri ordinal data nemožno zamieňať asociáciu za zhodu. Weighted kappa je v mnohých prípadoch najužitočnejšia metrika zhody, ale jej interpretácia závisí od prevalencie kategórií, počtu kategórií a zvoleného systému váh.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/30_method.md`, prípadne `manuscript/50_discussion.md`
- funkcia: metodické ukotvenie pre ordinal agreement a opatrné narábanie s koeficientmi zhody

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 5 (article abstract), `ABSTRACT`
- kontrolný excerpt:
  > "Such data need to be analysed with correct statistics, or the results and conclusions may be misleading. ... Both acceptable and unacceptable methods were found ... When choosing among various methods for agreement the weighted Kappa coefficient is probably the most useful for ordinal data, but several issues of concern arise and need to be taken into consideration ..."
- parafráza: Hlavná message paperu je dvojitá: pri ordinal ratings záleží na správnej metrike a weighted kappa je silný kandidát, ale nie bez výhrad.
- use: high-level metodický anchor pre agreement vetvu

### Blok 2
- opiera sa o: Introduction + Aim
- locator: PDF p. 6 (article p. 428), `INTRODUCTION` + `AIM`
- kontrolný excerpt:
  > "Agreement between observers ... can be measured in different ways, and some methods may be regarded as more accurate than other. Depending on which method one uses, one can obtain quite different values. ... The Kappa coefficient ... was originally proposed to measure agreement by classifying subjects in nominal scales, but it has since been extended to the classification of ordinal data as well."
- parafráza: Autori explicitne upozorňujú, že rôzne agreement metódy môžu na tých istých dátach dávať dosť odlišné hodnoty, preto výber metriky nie je formálny detail.
- use: zdôvodnenie, prečo treba v metodike pomenovať metric choice a jej dôsledky

### Blok 3
- opiera sa o: Review findings
- locator: PDF p. 7-8 (article p. 429), `THE REVIEW OF THE LITERATURE`
- kontrolný excerpt:
  > "A total of 183 articles were reviewed and 9 (4.9%) of the articles were found to analyse agreement for ordinal data ... The most common analyses ... were (unweighted) Kappa ... and weighted Kappa ... Other methods were percent of agreement ... Spearman rank-order correlation ... paired Student's t-test ... and another unknown 'inter-rater reliability' analysis."
- parafráza: Review ukazuje, že prax v publikovaných štúdiách je nekonzistentná a nie vždy metodicky čistá. To je dobrý argument pre explicitné zdôvodnenie agreement analytiky v tvojej práci.
- use: metodická opora pre transparentnosť analytic choices

### Blok 4
- opiera sa o: Measures of agreement
- locator: PDF p. 8-10 (article p. 429-430), `MEASURES OF AGREEMENT`
- kontrolný excerpt:
  > "Correlation is sometimes also used as a measure of agreement. However, correlation ... is a measure of association and does not satisfactorily measure agreement. ... The unweighted Kappa gives zero weight to all disagreement cells. This is an important issue when calculating agreement of ordinal data ... To 'solve' this problem a weighted Kappa coefficient can be calculated ..."
- parafráza: Pre ordinal ratings paper jasne odlišuje association od agreement. Korelácia ani chi-square nemajú nahrádzať agreement metriku a unweighted kappa ignoruje veľkosť nesúladu medzi susednými vs vzdialenými kategóriami.
- use: obhájenie, prečo nestačí reportovať len korelačné alebo jednoduché reliability čísla

### Blok 5
- opiera sa o: Measures of agreement + Conclusions
- locator: PDF p. 10-14 (article p. 430-431), end of `MEASURES OF AGREEMENT` + `CONCLUSIONS`
- kontrolný excerpt:
  > "The Kappa coefficient depends upon the prevalence in the cells as well as the number of categories in the variable, which makes it difficult to compare results from different studies. ... The intra-class correlation is probably best suited for continuous data. ... The weighted Kappa coefficient is probably the most useful measure for agreement in ordinal data. ... comparison of the studies is difficult" when different weights are used.
- parafráza: Weighted kappa paper odporúča, ale zároveň obmedzuje jej interpretáciu: výsledok sa mení s prevalenciou, počtom kategórií a weighting scheme, takže porovnávanie naprieč štúdiami treba robiť opatrne.
- use: discussion note pre limity agreement koeficientov a prečo treba transparentne reportovať nastavenie

## Kľúčová definícia / výsledok / argument
- Pri ordinal hodnoteniach treba rozlišovať association od agreement; weighted kappa je často najvhodnejšia, ale jej hodnota je citlivá na distribúciu kategórií a zvolenú schému váh.

## Limity alebo pozor
- Je to krátky metodologický článok, nie kompletný moderný tutorial k ordinal mixed models alebo ICC.
- Paper favorizuje weighted kappa, ale zároveň pripomína situácie, kde sa výsledky ťažko porovnávajú naprieč štúdiami.

## Kľúčové citovateľné miesto
- PDF p. 5 pre abstrakt a high-level verdict
- PDF p. 8-10 pre rozdiel association vs agreement a weighted kappa logiku
- PDF p. 14 pre záverečné caveats k prevalencii, počtu kategórií a weighting methods

## Tagy
- methods / analysis

## Status použitia
- method / checked
