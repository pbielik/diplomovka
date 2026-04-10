# marasini2016weightedindexes

## Plna citacia
Marasini, D., Quatto, P., & Ripamonti, E. (2016). *Assessing the Inter-Rater Agreement for Ordinal Data through Weighted Indexes.* Statistical Methods in Medical Research, 25(6), 2611-2633. https://doi.org/10.1177/0962280214529560

## Identifikacia zdroja
- DOI / PMID / URL: DOI `10.1177/0962280214529560`, PMID `24740999`, URL `https://pubmed.ncbi.nlm.nih.gov/24740999/`
- Zotero polozka alebo kolekcia: `Diplomovka – AI Interview Depresia`, metodicko-statisticka vetva pre agreement pri ordinalnych datach
- Overeny attachment: `/Users/pavol.bielik/Zotero/storage/9Y3V7XUM/Marasini et al. - 2016 - Assessing the inter-rater agreement for ordinal data through weighted indexes.pdf`

## Klaster z literature map
- `04 Metoda, statistika a analyticky dizajn`

## Priorita podla literature map
- optional

## Typ zdroja
- statisticky metodicky paper / ordinal agreement

## Hlavna myslienka
- Paper je uzitocny najma ako specialisticky anchor pre problem, ze pri ordinalnych viac-rater datach nemusia Cohenove ani Fleissove kappa statistiky davat intuitivne interpretovatelny obraz zhody; autori preto navrhuju alternativu `s*` s linear weights.

## Na co to pouzijem v diplomovke
- kapitola alebo sekcia: `manuscript/30_method.md`, sekundarne metodicke limity v `manuscript/50_discussion.md`
- funkcia: analysis / agreement metrics / ordinal many-raters caveat

## Klucove evidencne bloky

### Blok 1
- opiera sa o: Abstract + Introduction
- locator: PDF p. 1-2, Abstract + start of Introduction
- kontrolny excerpt:
  > "Assessing the inter-rater agreement between observers, in the case of ordinal variables, is an important issue in both the statistical theory and biomedical applications."
  >
  > "both Cohen's and Fleiss' kappa could have a paradoxical behavior, which may lead to a difficult interpretation of their magnitude."
  >
  > "the evaluation of inter-rater agreement is particularly important to validate diagnostic tests and clinical scales, in case of absence of a gold standard."
- parafraza: Marasini stavia problem jasne: pri ordinalnych klinickych skalah je agreement centralny metodicky problem a bez gold standardu je este dolezitejsi. Zaroven upozornuje, ze kappa pristupy sa mozu spravat paradoxne.
- use: specializovany argument, preco pri ordinalnych expert ratings nestaci nekriticky siahnut po jednej agreement metrike

### Blok 2
- opiera sa o: kappa statistics exposition
- locator: PDF p. 3-5, sections `The kappa statistics`
- kontrolny excerpt:
  > "it is necessary to adjust this statistic on the basis of agreement expected by chance."
  >
  > "Fleiss generalized the use of the kappa statistic to the case of multiple observers"
  >
  > "the generalization of the notion of agreement in case of multiple observers involves the concept of pairwise agreement"
- parafraza: Paper pripomina zakladnu logiku: agreement ma byt korigovany o nahodnu zhodu a pri viacerych rateroch sa prirodzene prechadza na pairwise agreement logiku. To je dolezite pre pochopenie, preco su niektore koeficienty pre ordinal many-raters citlive alebo neintuivne.
- use: explanatory bridge pri metodickom opise agreement logiky

### Blok 3
- opiera sa o: paradox discussion
- locator: PDF p. 6-7, discussion of kappa paradoxes
- kontrolny excerpt:
  > "both Cohen's and Fleiss' kappa have an important disadvantage, given by their paradoxical behavior."
  >
  > "we expect that Fleiss' kappa would increase. Contrary to this prediction, we found a lower value of kappa"
  >
  > "this is a general problem, inherently connected with both Cohen's kappa and Fleiss' kappa"
- parafraza: Najpraktickejsi warning paperu je, ze kappa sa moze chovat protiintuitivne: aj pri zdanlivo vacsej zhode alebo po zjednoduseni kategorii moze vysledna hodnota klesnut. Preto ju treba citat opatrne.
- use: caveat do metodickych limitov alebo interpretacie agreement vysledkov

### Blok 4
- opiera sa o: weighted agreement and linear weights
- locator: PDF p. 9-10, definition of `s*` and linear weights discussion
- kontrolny excerpt:
  > "two judges who have expressed their opinion in adjacent categories can, in a natural way, be given a higher weight than two evaluators who have expressed their opinion in not-adjacent categories."
  >
  > "the new s* statistic is defined subtracting from the observed agreement the agreement due to chance, and normalizing"
- parafraza: V ordinalnom settingu paper vyuziva logiku vah: nesuhlas medzi susednymi kategoriami nema mat rovnaku penalizaciu ako nesuhlas medzi vzdialenymi kategoriami. Na tom stava navrhnuty koeficient `s*`.
- use: specializovana opora, preco ordinalne data mozu vyzadovat viac nez len neweighted agreement koeficient

### Blok 5
- opiera sa o: Conclusions
- locator: PDF p. 15-16, `Conclusions`
- kontrolny excerpt:
  > "In conclusion, we suggest the use of s* with linear weights as an alternative to Fleiss' kappa with multiple observers in the ordinal case."
  >
  > "Future direction of this work will consider the use of quadratic weights ... for their relation with the intraclass correlation coefficient"
- parafraza: Autori zaverom nehovoria, ze kappa je nepouzitelna, ale ze pre ordinalny many-raters setting moze byt `s*` s linearnymi vahami rozumnejsou alternativou. Zaujimavy je aj most k ICC cez quadratic weights.
- use: sekundarna metodicka diskusia pri interpretacii ordinalnych agreement indexov

## Klucova definicia / vysledok / argument
- Marasini je uzitocny najma tam, kde chces ukazat, ze ordinalne viac-rater data maju specificku agreement problematiku a ze interpretacia kappa typu koeficientov nie je vzdy priamo ci intuitivne prenosna.

## Limity alebo pozor
- Paper je metodicky narocny a pre hlavny text diplomovky je skor podpornospecialisticky zdroj nez centralny anchor.
- Nie je to primarny zdroj pre ICC typologiu; na ICC framing ostavaju silnejsie ine zdroje.

## Klucove citovatelne miesto
- PDF p. 1-2 pre ordinal agreement problem a absence gold standardu
- PDF p. 3-5 pre chance-corrected pairwise agreement logiku
- PDF p. 6-7 pre paradoxical behavior of kappa
- PDF p. 9-10 pre weighted ordinal logic a `s*`
- PDF p. 15-16 pre zaverecne odporucanie `s*` ako alternativy

## Tagy
- methods / analysis

## Status pouzitia
- method / checked
