# kim2024MindfulDiaryHarnessingLarge

## Plná citácia
Kim, T., Bae, S., Kim, H. A., Lee, S.-W., Hong, H., Yang, C., & Kim, Y.-H. (2024). *MindfulDiary: Harnessing large language model to support psychiatric patients' journaling*. In *Proceedings of the CHI Conference on Human Factors in Computing Systems* (pp. 1-20). ACM. https://doi.org/10.1145/3613904.3642937

## Identifikácia zdroja
- DOI / PMID / PMCID / URL: DOI `10.1145/3613904.3642937`
- Zotero položka alebo kolekcia: `Diplomovka – AI Interview Depresia` → `02 LLM – mental health / psychiatry`
- Overený attachment: [Kim 2024 MindfulDiary PDF](/Users/pavol.bielik/Zotero/storage/PM2SHULZ/Kim%20et%20al.%20-%202024%20-%20MindfulDiary%20Harnessing%20Large%20Language%20Model%20to%20Support%20Psychiatric%20Patients%27%20Journaling.pdf)

## Klaster z literature map
- `02 LLM, mental health a psychiatria`

## Priorita podľa literature map
- should-read

## Typ zdroja
- HCI / field deployment paper

## Hlavná myšlienka
- MindfulDiary je zaujímavý tým, že nejde len o benchmark alebo simulation paper. Ukazuje konkrétne patient-facing použitie LLM v klinicky blízkom kontexte: journaling, sumarizácia a následné využitie psychiatrom pri konzultácii.

## Na čo to použijem v diplomovke
- kapitola alebo sekcia: `manuscript/20_introduction.md`, `manuscript/50_discussion.md`
- funkcia: opora pre clinically adjacent LLM use-case, pre human-in-the-loop dizajn a pre argument, že kontrola a workflow integrácia sú rovnako dôležité ako samotný model

## Kľúčové evidenčné bloky

### Blok 1
- opiera sa o: Abstract
- locator: PDF p. 2, `Abstract`
- kontrolný excerpt:
  > "MindfulDiary takes a state-based approach to safely comply with the experts' guidelines while carrying on free-form conversations. Through a four-week field study involving 28 patients with major depressive disorder and five psychiatrists ... MindfulDiary supported patients in consistently enriching their daily records and helped clinicians better empathize with their patients ..."
- parafráza: Už abstrakt je silný, lebo prepája tri veci: safety-oriented conversational design, reálnych pacientov s MDD a použitie v kontakte s psychiatrom.
- use: patient-facing LLM use-case pre introduction alebo discussion

### Blok 2
- opiera sa o: Introduction
- locator: PDF p. 3, `Introduction`
- kontrolný excerpt:
  > "journaling helps people describe experiences and express emotions ... journals frequently capture patients' daily experiences, symptoms, and other contextual data that are challenging to gather during brief hospital visits ... writing about one's past feelings and thoughts can be a complex process ..."
- parafráza: Paper ukotvuje journaling ako užitočný, ale náročný proces, ktorý môže zachytiť to, čo sa do krátkej ambulantnej návštevy nezmestí.
- use: opora pre argument, že LLM môže byť skôr facilitátor zberu a štruktúrovania dát než autonómny poradca

### Blok 3
- opiera sa o: clinical design rationale
- locator: PDF p. 5, section o controllability
- kontrolný excerpt:
  > "human oversight and moderation are critical when using LLMs in clinical settings ... the chatbot operates using state-based prompting ... By simplifying the model prompts, we intended the generated responses to safely and reliably comply with the MHP's guidelines for interacting with the patients."
- parafráza: Toto je kľúčový design point: namiesto úplne voľného generovania autori zaviedli state-based prompting, aby bol model viac kontrolovateľný a zladený s odbornými guidelines.
- use: opora pre safe-by-design LLM workflow

### Blok 4
- opiera sa o: system description
- locator: PDF p. 2-3, Figure 1 + introduction
- kontrolný excerpt:
  > "MindfulDiary consists of two components: the patient interface and the expert interface ... a mobile conversational AI with which patients can converse about daily experiences and thoughts and (2) a web dashboard that allows MHPs to review their patients' dialogue history with the AI."
- parafráza: Systém je dôležitý aj architektonicky: nie je to len chatbot, ale dvojica pacientsky interface + klinický dashboard, teda explicitný human-in-the-loop model.
- use: argument, že klinické použitie LLM má byť workflow-level, nie len model-level

### Blok 5
- opiera sa o: field deployment summary
- locator: PDF p. 18, conclusion section
- kontrolný excerpt:
  > "We conducted a field deployment study with 28 patients over 4 weeks. We found that the versatility, narrative-building capability, and diverse perspectives provided by MindfulDiary assisted patients in consistently enriching their daily records. The enriched records from MindfulDiary provided psychiatrists with deeper insights, enhancing their understanding and empathy toward their patients."
- parafráza: Toto je najpraktickejší výsledok paperu: prínos nebol v "nahradení" psychiatra, ale v tom, že pacienti vytvárali bohatšie záznamy a psychiatri z nich získali lepší pohľad na každodenný kontext pacienta.
- use: discussion anchor pre supportive, augmentative rolu LLM

### Blok 6
- opiera sa o: utilization in clinic
- locator: PDF p. 15-16, `Utilization of MindfulDiary in Clinic` + `Perceived Benefits`
- kontrolný excerpt:
  > "psychiatrists reviewed the journal entries ... 5 to 10 minutes per patient ... After checking trends primarily through PHQ-9 in the clinician dashboard, psychiatrists read summaries about events and documented emotions." ... "MindfulDiary helped them gain a deeper understanding and empathy about their patients."
- parafráza: Reviewovanie dát malo konkrétnu ambulantnú podobu: psychiatri používali dashboard pred návštevou, sledovali PHQ-9 trendy a súhrny udalostí/emócií, čo im pomohlo prísť do konzultácie lepšie pripravení.
- use: opora pre klinicky realistické workflow využitie

### Blok 7
- opiera sa o: perceived benefits outside visits
- locator: PDF p. 16, `Insights from Everyday Perspectives Outside Clinical Visits`
- kontrolný excerpt:
  > "Usually, when patients come for a consultation, they talk about bad experiences ... But I was happy to see that there were many positive statements in these records ..." ... "the diary" could help understand "reasons" for medication acceptance or decline.
- parafráza: Paper pekne ukazuje, že priebežný záznam vie vytiahnuť aj pozitívne zážitky a jemnejšie detaily adherencie či reakcie na liečbu, ktoré v bežnej konzultácii často nezaznejú.
- use: discussion anchor pre added clinical context, nie pre autonómne rozhodovanie modelu

## Kľúčová definícia / výsledok / argument
- Dobre navrhnutý LLM systém môže v mental-health kontexte fungovať ako facilitátor denného záznamu a klinického prehľadu, ak je pevne zasadený do human-in-the-loop workflow a drží sa odborných pravidiel interakcie.

## Limity alebo pozor
- Ide o field deployment v konkrétnom journaling use-case a s pomerne malou vzorkou; nemožno to čítať ako dôkaz všeobecnej klinickej pripravenosti LLM.
- Paper sám rieši controllability a expert guidelines, čo naznačuje, že voľné open-ended nasadenie bez guardrails by bolo rizikové.

## Kľúčové citovateľné miesto
- PDF p. 2 pre state-based approach a `28` pacientov / `5` psychiatrov
- PDF p. 5 pre human oversight a controllability
- PDF p. 15-18 pre konkrétne klinické workflow a perceived benefits

## Tagy
- llm / methods / analysis

## Status použitia
- discussion / checked
