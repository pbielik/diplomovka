# baguley2022vignettedata

## Plná citácia
Baguley, T., Dunham, G., & Steer, O. (2022). *Statistical modelling of vignette data in psychology*. British Journal of Psychology, 113(4), 1143-1163. https://doi.org/10.1111/bjop.12577

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1111/bjop.12577`, PMID `35735658`, PMCID `PMC9796090`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → metodická vetva pre vignette / rating design
- Overený attachment: [Baguley 2022 PDF](/Users/pavol.bielik/Zotero/storage/TESEUEXI/Baguley et al. - 2022 - Statistical modelling of vignette data in psychology.pdf)

## Klaster z literature map
- `04 Metóda, štatistika a analytický dizajn`

## Priorita podľa literature map
- optional

## Typ zdroja
- metodologický článok / review

## Hlavná myšlienka
- Pri vignette dátach nestačí automaticky použiť „obyčajnú regresiu“. Správny model závisí od toho, ako sú vignette rozdelené medzi participantov: striktnejšie factorial survey experimenty vedú skôr k nested dizajnu, kým experimental vignette studies často vytvárajú crossed random structure. Ako všeobecný default autori odporúčajú multilevel modelling.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/30_method.md`, prípadne metodické poznámky k analýze rating alebo vignette dát
- funkcia: štatistické ukotvenie pre vignette-like dizajny, nested vs crossed random effects a opatrnosť voči jednoduchej regresii

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "A key distinction is between factorial survey experiments ... The former leads to nested designs with a single random factor and the latter to designs with two crossed random factors. ... Multilevel models are proposed as a general approach to handling nested and crossed designs including unbalanced and fractional designs."
- parafráza: Už abstrakt vystihuje jadro paperu: pri vignette dátach je kritické rozlíšiť nested vs crossed štruktúru a multilevel model je praktický general-purpose rámec.
- use: high-level metodický anchor pre výber modelu pri vignette/rating dizajne

### Blok 2
- opiera sa o: Background
- locator: PDF p. 2-3, `BACKGROUND` + `How the design of a vignette study impacts the choice of analysis`
- kontrolný excerpt:
  > "A lack of consensus on how best to model quantitative vignette data ... The present paper outlines key characteristics of vignette studies and considers how the design of the study and vignettes impact the appropriate statistical model. ... experimental vignette studies ... relax the requirement to sample from a vignette universe defined by factorial combinations ... Unfortunately, relaxing the constraints ... changes the statistical model in important ways."
- parafráza: Paper výslovne hovorí, že vo vignette dátach rozhoduje detail dizajnu. To, čo vyzerá ako malá praktická odchýlka v alokácii vignett, môže zmeniť správny štatistický model.
- use: opora pre to, prečo treba v metóde transparentne popísať alokáciu vignett a štruktúru dát

### Blok 3
- opiera sa o: Common approaches + clustered data discussion
- locator: PDF p. 5-7, `COMMON APPROACHES TO MODELLING VIGNETTE DATA` + `Repeated measures as special cases of clustered samples`
- kontrolný excerpt:
  > "If intra-respondent correlation is ignored this always results in an incorrect statistical model. ... Ignoring the correlation among participants incorrectly treats each new observation as providing additional independent information to the model ... this leads to underestimation of the SEs. ... many published vignette studies have spuriously high statistical power."
- parafráza: Toto je kľúčový varovný bod. Ak sa ignoruje intra-respondent correlation, model sa tvári, že má viac nezávislej informácie než naozaj má, a výsledkom sú príliš optimistické štandardné chyby aj power.
- use: argument proti naivnej regresii pri opakovaných hodnoteniach vignett

### Blok 4
- opiera sa o: Incomplete or unbalanced sampling + aliasing discussion
- locator: PDF p. 7-10, `Incomplete or unbalanced sampling of the vignette universe` + `Complete confounding, fractional factorial designs and aliasing`
- kontrolný excerpt:
  > "Unbalanced designs are undesirable because they introduce partial or complete confounding of effects. ... This decreases efficiency ... It may also bias estimates relative to a completely balanced design. ... If two effects are aliased they cannot be distinguished from each other in the statistical model."
- parafráza: Baguley paper je užitočný aj v tom, že pomenúva ďalší problém nad rámec clusteringu: nevyvážená alebo frakcionálna alokácia vignett môže aliasovať efekty a znižovať efektivitu odhadov.
- use: metodická brzda pri návrhu alebo interpretácii vignette experimentu

### Blok 5
- opiera sa o: conclusion of general framework
- locator: PDF p. 3-6, repeated emphasis in `The case for a general framework for the analysis of vignette data` + later modelling sections
- kontrolný excerpt:
  > "A potential solution in the form of a general framework for the analysis of vignette data via multilevel models is proposed." ... "This allows for a general approach to handling nested and crossed designs including unbalanced and fractional designs."
- parafráza: Praktický záver paperu je, že multilevel modelling nie je len elegantný dodatok, ale robustnejší default práve preto, že vie absorbovať nested aj crossed štruktúru a lepšie znáša neideálne dáta.
- use: priame metodické odporúčanie pre výber modelu

## Kľúčová definícia / výsledok / argument
- Pri vignette dátach treba model voliť podľa alokácie vignett a clusteringu odpovedí; multilevel modely sú bezpečnejší default než jednoduchá regresia, najmä pri nested/crossed a nevyvážených dizajnoch.

## Limity alebo pozor
- Paper je písaný všeobecne pre psychology/social science vignette data, nie pre tvoju konkrétnu diplomovú schému.
- Nie je to hotový recept na jeden konkrétny model; skôr dáva princípy, podľa ktorých sa má model vybrať.

## Kľúčové citovateľné miesto
- PDF p. 1 pre nested vs crossed + multilevel summary
- PDF p. 5-7 pre riziká ignorovania intra-respondent correlation
- PDF p. 7-10 pre imbalance, aliasing a fractional designs

## Tagy
- methods / analysis

## Status použitia
- method / checked
