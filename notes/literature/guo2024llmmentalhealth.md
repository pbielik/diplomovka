# guo2024llmmentalhealth

## Plná citácia
Guo, Z., Lai, A., Thygesen, J. H., Farrington, J., Keen, T., & Li, K. (2024). *Large language models for mental health applications: Systematic review*. JMIR Mental Health, 11, e57400. https://doi.org/10.2196/57400

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.2196/57400`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02 LLM – mental health / psychiatry`
- Overený attachment: [Guo 2024 PDF](/Users/pavol.bielik/Zotero/storage/W84CLISW/Guo et al. - 2024 - Large Language Models for Mental Health Applications Systematic Review.pdf)

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- should-read

## Typ zdroja
- systematický review

## Hlavná myšlienka
- Guo review dáva širší mental-health rámec než čisto psychiatry-focused prehľady: sumarizuje text-based screening, conversational agents aj klinické použitia LLM a zároveň explicitne ukazuje, že pri dnešnom stave poľa riziká v klinickom nasadení často prevyšujú prínosy.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, `manuscript/50_discussion.md`
- funkcia: broad mental-health LLM review, prehľad use-case vetiev a opora pre safety / ethics / human-oversight framing

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 1, `Abstract`
- kontrolný excerpt:
  > "In total, 40 articles were evaluated, including 15 (38%) articles on mental health conditions and suicidal ideation detection through text analysis, 7 (18%) on the use of LLMs as mental health conversational agents, and 18 (45%) on other applications and evaluations of LLMs in mental health. LLMs show good effectiveness in detecting mental health issues and providing accessible, destigmatized eHealth services. However, assessments also indicate that the current risks associated with clinical use might surpass their benefits."
- parafráza: Už abstrakt dáva použiteľný high-level verdict: pole je dosť široké, ale autori priamo hovoria, že pri klinickom použití dnes riziká často prevyšujú benefity.
- use: opening synthesis pre širší LLM-in-mental-health landscape

### Blok 2
- opiera sa o: Introduction
- locator: PDF p. 2, `Introduction`
- kontrolný excerpt:
  > "LLMs present new possibilities for enhancing the delivery and effectiveness of mental health care. ... conversational agents (CAs) powered by LLMs are valued for their nonjudgmental listening and effective problem-solving advice. ... authorities such as the World Health Organization have developed ethical guidelines for artificial intelligence (AI) research in health care, emphasizing the importance of data privacy; human oversight; and the principle that AI tools should augment, rather than replace, human practitioners."
- parafráza: Guo review je vhodný na balanced framing: na jednej strane prístupnosť, stigma-reduction a digitálna dostupnosť, na druhej strane explicitná väzba na human oversight a augment-not-replace princíp.
- use: intro anchor pre benefit/risk framing bez techno-optimismu

### Blok 3
- opiera sa o: Results overview + Mental health conditions and suicidal ideation detection through text
- locator: PDF p. 7-8, `Results` + `Mental Health Conditions and Suicidal Ideation Detection Through Text`
- kontrolný excerpt:
  > "We classified the included articles into 3 broad categories: detection of mental health conditions and suicidal ideation through text (15/40, 38%), LLMs’ use for mental health CAs (7/40, 18%), and the other applications and evaluation of the LLMs in mental health (18/40, 45%). ... Most training data ... comprised social media posts ... In addition, 5 (12%) of the 40 studies used datasets consisting of clinical transcripts and patient interviews, providing deeper insights into LLM applications in clinical mental health settings."
- parafráza: Review prirodzene delí pole na tri hlavné vetvy a zároveň ukazuje, že veľká časť evidencie stále stojí na textových alebo social-media dátach, kým klinické dáta sú zatiaľ menšia časť korpusu.
- use: štruktúrovanie prehľadu literatúry a opatrnosť pri prenose na klinický kontext

### Blok 4
- opiera sa o: Conversational agents / high-risk scenarios
- locator: PDF p. 8, section o CA reliability v high-risk scenarios
- kontrolný excerpt:
  > "Meanwhile, the reliability of LLM-driven CAs in high-risk scenarios remains a concern. An evaluation of 25 CAs found that in tests involving suicide scenarios, only 2 included suicide hotline referrals during the conversation [96]. This suggests that while these CAs can detect extreme emotions, few are equipped to take effective preventive measures."
- parafráza: Pri high-risk situáciách review ukazuje veľmi konkrétny limit: CA môžu zachytiť extrémnu emóciu, ale často nezvládnu zmysluplnú preventívnu reakciu.
- use: bezpečnostná opora pre non-diagnostic framing a human escalation

### Blok 5
- opiera sa o: Other applications and evaluation of the LLMs in mental health
- locator: PDF p. 9, `Other Applications and Evaluation of the LLMs in Mental Health`
- kontrolný excerpt:
  > "However, the direct deployment of LLMs, such as ChatGPT, in clinical settings carries inherent risks. The outputs of LLMs are heavily influenced by prompt engineering, which can lead to inconsistencies that undermine clinical reliability. ... ChatGPT typically provided helpful advice and recommended seeking expert consultation, it occasionally produced inappropriate medication suggestions."
- parafráza: Guo paper je silný aj preto, že nejde len po abstraktnej etike. Dáva aj praktický argument, že prompt sensitivity sama osebe podkopáva klinickú spoľahlivosť výstupu.
- use: discussion anchor pre prompt-dependence a nekonzistentnosť odpovedí

### Blok 6
- opiera sa o: Discussion
- locator: PDF p. 10-11, `Discussion`
- kontrolný excerpt:
  > "Although previous research has highlighted the potential of LLMs in mental health, it is evident that they are not yet ready for clinical use due to unresolved technical risks and ethical issues. ... Another critical concern is the “black box” nature of LLMs ... These ethical concerns include ... the potential for overreliance on LLMs by both physicians and patients."
- parafráza: Záverečná diskusia paperu dáva použiteľný súhrn hlavných brzdiacich faktorov: technické limity, black-box problém a riziko prehnanej dôvery zo strany profesionálov aj pacientov.
- use: silná opora pre limitation/ethics sekcie

### Blok 7
- opiera sa o: Conclusions
- locator: PDF p. 12-13, `Conclusions`
- kontrolný excerpt:
  > "Despite the potential of LLMs, challenges such as the production of hallucinatory or harmful information, output inconsistency, and ethical concerns remain. Nevertheless, as technology advances and ethical guidelines improve, LLMs are expected to become increasingly integral and valuable in mental health services."
- parafráza: Guo review nekončí odmietnutím, ale opatrným dual verdictom: dnešné limity sú reálne, no pri lepšom governance a technickom dozretí môže mať táto technológia užitočnú podpornú rolu.
- use: balanced closing sentence pre introduction alebo discussion

## Kľúčová definícia / výsledok / argument
- V mental-health literatúre už existuje pestré spektrum LLM aplikácií, ale current evidence podporuje skôr podpornú a striktne dohliadanú rolu než autonómne klinické nasadenie.

## Limity alebo pozor
- Review je široký a mieša screening, chatboti, social media aj klinické použitia; nie je to čisto psychiatry-only korpus.
- Veľká časť zahrnutej evidencie je heterogénna a stojí na rôznych datasetoch, benchmarkoch a modelových verziách.

## Kľúčové citovateľné miesto
- PDF p. 1 pre 40 štúdií a hlavný risk-benefit verdict
- PDF p. 7-8 pre tri use-case kategórie a typy dát
- PDF p. 10-11 pre black box, overreliance a not-ready-for-clinical-use framing

## Tagy
- llm / ethics / seeding

## Status použitia
- discussion / checked
