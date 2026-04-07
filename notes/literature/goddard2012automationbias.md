# goddard2012automationbias

## Plná citácia
Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). *Automation bias: A systematic review of frequency, effect mediators, and mitigators*. Journal of the American Medical Informatics Association, 19(1), 121-127. https://doi.org/10.1136/amiajnl-2011-000089

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1136/amiajnl-2011-000089`, PMID `21685142`, PMCID `PMC3240751`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `07 Ethics – AI governance`
- Overený attachment: [Goddard 2012 PDF](/Users/pavol.bielik/Zotero/storage/R8259U8E/Goddard et al. - 2012 - Automation bias a systematic review of frequency, effect mediators, and mitigators.pdf)

## Klaster z literature map
- `07 Etika a AI governance`

## Priorita podľa literature map
- should-read

## Typ zdroja
- systematický review / health informatics / safety

## Hlavná myšlienka
- Automation bias je konzistentné riziko pri práci s decision-support systémami: keď používateľ priveľmi dôveruje automatizovanému odporúčaniu, môže nasledovať nesprávnu radu alebo si nevšimnúť, že systém nič neodporučil. Riziko rastie pri časovom tlaku, vyššej záťaži, nižšej skúsenosti a nesprávne kalibrovanej dôvere.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, `manuscript/50_discussion.md`
- funkcia: safety / ethics / over-reliance framing pre AI podporu rozhodovania a hodnotenia

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `ABSTRACT`
- kontrolný excerpt:
  > "Automation bias (AB) - the tendency to over-rely on automation - has been studied in various academic fields. ... Of 13 821 retrieved papers, 74 met the inclusion criteria. ... User factors such as cognitive style ... and task specific experience mediated AB, as did ... trust and confidence. Environmental mediators included workload, task complexity, and time constraint ... Mitigators of AB included ... training and emphasizing user accountability ..."
- parafráza: Už abstrakt dáva kompaktný rámec: automation bias nie je izolovaný glitch, ale opakovaný jav s jasnými mediátormi a praktickými mitigáciami.
- use: definícia a high-level map rizík pre AI governance časť

### Blok 2
- opiera sa o: Background
- locator: PDF p. 1, `BACKGROUND` + subsection `Automation bias and complacency`
- kontrolný excerpt:
  > "Although most decision support systems (DSS) are 80-90% accurate, it is known that the occasional incorrect advice they give may tempt users to reverse a correct decision they have already made ... AB manifests in errors of commission (following incorrect advice) and omission (failing to act because of not being prompted to do so). ... Friedman et al noticed that in 6% of cases, clinicians over-rode their own correct decisions in favor of erroneous advice from the DSS."
- parafráza: Paper dobre vysvetľuje, prečo vysoká priemerná presnosť systému nestačí. Aj relatívne zriedkavá chybná rada môže preklopiť správny ľudský úsudok na nesprávny.
- use: opora pre argument, že vysoká presnosť AI sama osebe neruší safety risk

### Blok 3
- opiera sa o: Discussion
- locator: PDF p. 3-4, subsection `The rate and extent of AB`
- kontrolný excerpt:
  > "The risk ratio was 1.26 (95% CI 1.11 to 1.44); erroneous advice was more likely to be followed in the CDSS groups than in the control groups and when in error the CDSS increased the risk of an incorrect decision being made by 26%. ... The proportion of decisions which demonstrated this ranged from 6% ... to 11% of cases in prospective empirical studies."
- parafráza: Review nejde len po teórii. Pri kontrolovaných porovnaniach ukazuje aj smer efektu: chybná rada v DSS skupine zvýšila riziko nesprávneho rozhodnutia a negatívne konzultácie sa objavovali v jednotkách až desiatkach percent.
- use: kvantitatívny safety anchor pre discussion

### Blok 4
- opiera sa o: Discussion
- locator: PDF p. 4-5, subsections `Experience`, `Confidence and trust`, `Task type`
- kontrolný excerpt:
  > "Experience may decrease over-reliance on automation ... Physicians with greater experience may be less reliant on DSS and be more likely to recognize incorrect advice. ... increased confidence in the user's own decision decreased reliance on external support, whereas trust in the DSS increased reliance. ... More complex tasks and higher workloads are posited to increase reliance ... high time pressure could bias a user toward DSS usage."
- parafráza: Pre diplomovku je dôležité, že automation bias sa nespúšťa vo vákuu. Silno súvisí s kalibráciou dôvery, skúsenosťou používateľa a s tým, ako kognitívne náročná alebo časovo stlačená je úloha.
- use: rozklad mechanizmu over-reliance, nie len pomenovanie rizika

### Blok 5
- opiera sa o: Discussion + Overall conclusion
- locator: PDF p. 5, subsections `Automation bias avoidance` + `OVERALL CONCLUSION`
- kontrolný excerpt:
  > "Research indicates that certain measures can help prevent over-reliance on decision support. ... making users aware of the DSS reasoning process increased appropriate reliance ... Increasing accountability for decisions may also prevent AB ... training may increase the likelihood of recognizing DSS error ... AB can be mitigated by decreasing the prominence of DSS output ... updating advice confidence levels, and providing supportive information rather than commands."
- parafráza: Review ponúka aj praktické mitigácie: transparentnejší reasoning, accountability, tréning a opatrnejší interface môžu znižovať nekritické nasledovanie systému.
- use: diskusná a metodická opora pre návrhy safeguards okolo AI systémov

## Kľúčová definícia / výsledok / argument
- Automation bias je tendencia nadmerne sa spoliehať na automatizované odporúčanie; prejavuje sa komisionálnymi aj omisionálnymi chybami a je zosilnená najmä dôverou, záťažou, komplexitou a časovým tlakom.

## Limity alebo pozor
- Review je široký naprieč oblasťami a nie je šitý len na LLM alebo psychologický rozhovor.
- Autori sami píšu, že časť evidencie je incidentálne reportovaná a pojem automation bias ešte nebol vtedy úplne konzistentne definovaný.

## Kľúčové citovateľné miesto
- PDF p. 1 pre definíciu AB a základné mediátory
- PDF p. 3-4 pre risk ratio `1.26` a negative consultation rates
- PDF p. 5 pre mitigácie a overall conclusion

## Tagy
- ethics / analysis / seeding

## Status použitia
- discussion / checked
