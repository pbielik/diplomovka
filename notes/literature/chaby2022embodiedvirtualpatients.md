# chaby2022embodiedvirtualpatients

## Plná citácia
Chaby, L., Benamara, A., Pino, M., Prigent, E., Ravenet, B., Martin, J.-C., Vanderstichel, H., Becerril-Ortega, R., Rigaud, A.-S., & Chetouani, M. (2022). *Embodied virtual patients as a simulation-based framework for training clinician-patient communication skills: An overview of their use in psychiatric and geriatric care*. Frontiers in Virtual Reality, 3, 827312. https://doi.org/10.3389/frvir.2022.827312

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.3389/frvir.2022.827312`, URL `https://www.frontiersin.org/articles/10.3389/frvir.2022.827312/full`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02.2 Simulated patients / virtual patients`
- Overený attachment: open access na Frontiers, plné PDF (19 strán, Frontiers in Virtual Reality 2022, vol. 3, art. 827312) prečítané z `/tmp/pdf-extracts/chaby2022embodiedvirtualpatients.txt` a evidence blocky doplnené nižšie

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- must-read

## Typ zdroja
- narratívny prehľad / pedagogický framework paper

## Hlavná myšlienka
- Chaby a kol. argumentujú, že embodied virtual patients — simulovaní pacienti s rendrovaným telom a non-verbálnym správaním — sú legitímny tréningový nástroj pre psychiatrické a geriatrické prostredie, kde kliniciko-pacientska komunikácia kladie vysoké nároky na čítanie non-verbálnych symptómov.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md` (1.2 Klinický rozhovor a simulovaní pacienti; pred-LLM pivot ku novším LLM virtual patients)
- funkcia: teória / seeding / historický most medzi klasickými virtual patients a LLM-based simulated patients

## Kľúčová definícia / výsledok / argument
- Virtual patients sú v psychiatrii používané na tréning komunikačných zručností v témach ako depresia, suicidálne riziko či PTSD, pričom embodied agenty pomáhajú adresovať non-verbálne aspekty kontaktu, ktoré sú inak v tréningu ťažko zachytiteľné.

## Evidenčné bloky

### Blok 1 — použitie v psychiatrii a príklady
- opiera sa o: Abstract
- locator: Frontiers článok, `Abstract`, URL ako vyššie
- kontrolný excerpt:
  > "VP simulation tools are used in psychiatry (e.g. depression, suicide risk, PTSD)"
- parafráza: Autori explicitne uvádzajú, že virtual patient tréningové nástroje sa už používajú v psychiatrii, pričom medzi príklady patria depresia, suicidálne riziko a PTSD.
- use: priamy zdroj pre tvrdenie, že virtual patients už majú psychiatrické tréningové aplikácie, a že depresia patrí medzi ne — kotva pre pre-LLM baseline v 1.2

### Blok 2 — non-verbálne symptómy ako hlavný dôvod pre psychiatrické VP
- opiera sa o: Introduction
- locator: Frontiers článok, `Introduction`
- kontrolný excerpt:
  > "In the psychiatric or geriatric field, clinicians are expected to interpret specific non-verbal cues associated with patients' psychological and behavioral symptoms"
- parafráza: V psychiatrickom a geriatrickom kontexte sa od klinikov očakáva, že budú interpretovať špecifické non-verbálne indície spojené s psychologickými a behaviorálnymi symptómami pacientov, čo je jeden z hlavných dôvodov pre nasadenie embodied VP.
- use: argument pre to, prečo sa klasické textové virtual patients prirodzene posúvali k embodied variantom, a prečo je ďalší posun k LLM-based simulovaným pacientom logickým krokom

### Blok 3 — etický princíp „never the first time on a patient"
- opiera sa o: Introduction
- locator: Frontiers článok, `Introduction`
- kontrolný excerpt:
  > "embodied virtual agents" are used "in order to respect the fundamental ethical principle of 'never the first time on a patient'"
- parafráza: Autori ukotvujú embodied virtual agents v etickom princípe „never the first time on a patient", čo je štandardná simulačno-tréningová justifikácia.
- use: etický framing v úvode (1.2) — odôvodnenie, prečo je simulácia legitímny medzistupeň pred reálnou praxou; podpora pre discussion section o bezpečnostnom rozmere tréningu

### Blok 4 — potreba: bežné klinické prostredie neponúka dostatok tréningových stretnutí
- opiera sa o: Introduction (súhrn)
- locator: Frontiers článok, `Introduction`
- kontrolný excerpt:
  > "training and evaluating non-verbal communication ... is challenging, often intrusive ... or can require extensive resources"
- parafráza: Tréning a evaluácia non-verbálnej komunikácie sú v bežnom klinickom prostredí ťažko realizovateľné — bývajú časovo a zdrojovo náročné, niekedy aj invazívne voči pacientom — čo je jeden z praktických dôvodov pre prechod k simulačným nástrojom.
- use: argument v 1.2 pre potrebu simulačných nástrojov v psychiatrii ako praktickej alternatívy klasických supervízovaných stretnutí

### Blok 5 — anotovaný prehľad 14 VP nástrojov v psychiatrii a geriatrii (Table 1)
- opiera sa o: §2 + Table 1
- locator: Chaby et al. 2022 Frontiers PDF, p. 5, Table 1
- kontrolný excerpt:
  > "Overview of annotated attributes in our selected list of articles presented on Section 2. The annotation procedure captures the user and the VP characteristics in simulation tools for clinician-patient communication in the field of psychiatry and geriatrics. ... Carpenter et al. (2012) ... Depressive child; ... Shah et al. (2012) ... Major depression; Cordar et al. (2014) ... Major depression; ... Dupuy et al. (2020) ... Depressive symptoms; ... Pantziaras et al. (2014, 2015) ... PTSD refugee"
- parafráza: Autori v Table 1 systematicky anotujú 14 VP simulačných nástrojov pre kliniko-pacientsku komunikáciu v psychiatrii a geriatrii podľa atribútov používateľa (komunikačné kompetencie, typ scenára, evaluácia) aj podľa atribútov virtuálneho pacienta (verbálne/non-verbálne správanie, simulačný model, hodnotenie nástroja, typ patológie); medzi 14 zaradenými prácami sú minimálne štyri zamerané na depresívnu symptomatiku (Carpenter 2012, Shah 2012, Cordar 2014, Dupuy 2020).
- use: priamy dôkaz v 1.2, že virtual patients pre depresiu nie sú izolované jednotlivosti, ale že existuje aspoň 4-položková predLLM tradícia priamo zameraná na depresívnu symptomatiku, ktorú náš LLM-based dizajn metodicky kontinualne rozvíja

### Blok 6 — Carpenter 2012 SAMHT a O'Brien 2019 PeopleSim: VP pre suicidálne riziko
- opiera sa o: §2.3 VP-Simulation for Clinician-Patient Communication in Psychiatry
- locator: Chaby et al. 2022 Frontiers PDF, p. 6
- kontrolný excerpt:
  > "One of the first use cases of VPs in the field of psychiatry was designed as a web-based platform to train clinicians to assess suicide risk in youth (Carpenter et al., 2012). The Suicidal Avatars for Mental Health Training (SAMHT) platform allows the user to face a VP who can move, speak and is embodied as a child suffering from depressive symptoms. ... More recently, another work (O'Brien et al., 2019) tested the acceptability and benefit of VP simulation, using The PeopleSim® technology, to train mental health practitioners to interact effectively with individuals at risk for suicide."
- parafráza: Chaby a kol. dokumentujú, že prvými systematickými použitiami VP v psychiatrii boli platformy SAMHT (Carpenter 2012, dieťa s depresívnymi symptómami a suicidálnym rizikom) a PeopleSim® (O'Brien 2019, 20-ročná pacientka so suicidálnymi myšlienkami) — obe využívali predefinované zoznamy otázok a rozhodovacie stromy, nie generatívny model.
- use: argument v 1.2 a 1.3 pre to, že pred-LLM tradícia VP v psychiatrii sa explicitne zaoberala práve depresívno-suicidálnou témou, ale bola limitovaná pevnou stromovou logikou — náš LLM-based dizajn nadväzuje na rovnakú motiváciu, ale využíva flexibilnejší generatívny mechanizmus

### Blok 7 — Shah/Cordar Cynthia Young VP pre major depression v The Sims
- opiera sa o: §2.3 (str. 6-7)
- locator: Chaby et al. 2022 Frontiers PDF, p. 6-7
- kontrolný excerpt:
  > "Using The Sims video game, other studies have focused on the use of VPs to enhance the empathy and interpersonal communication skills of medical students during interactions with a 21-year-old virtual patient (Ms. Cynthia Young) suffering from major depressive episodes (Shah et al., 2012; Cordar et al., 2014). ... A limitation of these studies is that, in the limited environment of 3D virtual world games, VPs are not able to converse in a realistic manner, nor respond to dialogues with human-like non-verbal behaviors or emotions."
- parafráza: Shah a Cordar postavili VP Ms. Cynthia Young, 21-ročnú pacientku s veľkou depresívnou epizódou, postavenú v hre The Sims; trénujú empatiu a interpersonálne komunikačné zručnosti medicínskych študentov, no autori sami priznávajú, že herné prostredie nedovolí realistickú konverzáciu ani human-like non-verbálne reakcie.
- use: presný pred-LLM analóg pre nás dôležitej kombinácie (depresia + tréning empatie + virtuálny pacient) — v 1.2 priamy dôkaz, že téma „LLM simulovaný pacient s depresiou\" má etablovaného predchodcu, ktorému však chýba flexibilita prirodzeného jazyka

### Blok 8 — Dupuy 2020: 35 študentov, MDD, multimodálne non-verbálne hodnotenie
- opiera sa o: §2.3 (str. 8)
- locator: Chaby et al. 2022 Frontiers PDF, p. 8
- kontrolný excerpt:
  > "More recently, a study focused on improving the empathic communication skills of medical students during realistic psychiatric interviews with a middle-aged VP with affective disorders (Dupuy et al., 2020). Interestingly, the simulation was not exclusively text-based or speech-based as in previous studies, but also addressed the VP's non-verbal behavior as well as the trainees' non-verbal and empathic behavior. The interaction, based on a predetermined question-answer scenario, was designed as a 35-min psychiatric interview requiring 35 students (medical, psychiatric) to conduct interviews with a middle-aged VP with major depressive disorder and to extract semiology"
- parafráza: Dupuy a kol. (2020) realizovali doposiaľ najbohatšie pred-LLM riešenie pre náš kontext: 35 medicínskych a psychiatrických študentov uskutočnilo 35-minútový psychiatrický rozhovor so stredne starým virtuálnym pacientom s veľkou depresívnou poruchou, pričom systém zachytával non-verbálne správanie pacienta aj študenta (mimika, gestá, prozódia) a využíval rozpoznávanie reči a mimiky.
- use: najdôležitejší pred-LLM precedens pre náš dizajn — v 1.2 a v Discussion priamy benchmark („n = 35, MDD VP, expert evaluation\"), ktorý ukazuje, že naša ratingová štúdia s LLM-based simulovaným pacientom s MDD je metodicky kontinuálna voľba, nie izolovaný experiment

### Blok 9 — Discussion: 5 z 14 nástrojov nepodporuje realistickú konverzáciu, chýba evaluácia stážistu
- opiera sa o: Discussion (str. 11)
- locator: Chaby et al. 2022 Frontiers PDF, p. 11, `DISCUSSION`
- kontrolný excerpt:
  > "Among the 14 tools (17 articles) using VP simulation presented in this overview, five used simulation models (e.g., prerecorded videos associated with text-based interfaces) that do not allow for realistic human-like conversations (Carpenter et al., 2012; O'Brien et al., 2019; Shah et al., 2012; Cordar et al., 2014; Pantziaras et al., 2014, 2015). By contrast, four tools offer immersive experiences using VPs displayed on human-sized screens and interacting in natural language ... In addition, our overview reveals a lack of interest in evaluating the learner."
- parafráza: V syntéze Chaby a kol. priamo pomenúvajú dve hlavné limitácie celej pred-LLM VP literatúry v psychiatrii a geriatrii — že 5 zo 14 nástrojov používa predefinované video/text rozhrania bez realistickej konverzácie a že väčšina štúdií neinvestuje do evaluácie samotného stážistu (verbálne ani non-verbálne správanie).
- use: silný argument pre náš framing v 1.2/1.3 — LLM-based simulovaní pacienti s expertným ratingom adresujú presne tie dva nedostatky, ktoré pred-LLM literatúra explicitne identifikuje (chýbajúca konverzačná flexibilita + chýbajúca evaluácia kvality klinikovej inquiry); v Discussion sa môžeme oprieť o tento záver ako o motiváciu pre práve tie dva piliere našej štúdie

## Limity alebo pozor
- ide o narratívny prehľad, nie o systematický review, takže nemá meta-analytické effect sizes ako kononowicz2019virtualpatients
- zameranie je na embodied VP (virtual avatars, VR), nie na textové LLM-based simulovaných pacientov; v úvode preto slúži ako pred-LLM most, nie ako priama empirická validácia LLM prístupov
- plný PDF (19 strán) bol prečítaný a zapracovaný do blokov 5-9; pôvodný `needs manual check` status na ďalšie evidenčné bloky je tým vyriešený

## Kľúčové citovateľné miesto
- Frontiers článok `Abstract` (psychiatrické use-cases: depresia, suicide risk, PTSD)
- Frontiers článok `Introduction` (non-verbálne cues, „never the first time on a patient", nedostatok reálnych tréningových možností)
- Chaby et al. 2022 Frontiers PDF, p. 5, Table 1 — anotovaný prehľad 14 VP nástrojov v psychiatrii/geriatrii, z toho min. 4 zamerané na depresiu
- Chaby et al. 2022 Frontiers PDF, p. 6-7, §2.3 — Carpenter SAMHT, O'Brien PeopleSim, Shah/Cordar Cynthia Young Sims-based MDD VP
- Chaby et al. 2022 Frontiers PDF, p. 8, §2.3 — Dupuy 2020: 35 študentov, 35-min psychiatrický rozhovor s VP s veľkou depresívnou poruchou, multimodálne non-verbálne hodnotenie
- Chaby et al. 2022 Frontiers PDF, p. 11, `DISCUSSION` — 5 z 14 nástrojov bez realistickej konverzácie, lack of interest in evaluating the learner

## Tagy
- llm / methods / seeding

## Status použitia
- must-cite / checked
