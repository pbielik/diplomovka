# Literárne medzery a coverage risks

Toto je pracovný gap memo. Drží to, čo ešte treba doplniť, aby bola metodická a argumentačná línia práce obhájiteľná.

## Prehľad medzier

| ID | Gap | Čo chýba | Prečo to potrebuješ | Priorita |
| --- | --- | --- | --- | --- |
| `A` | klinické jadro MDD | formálny klinický referenčný bod pre symptomatiku a diferenciálnu diagnostiku | seed konštrukcia, symptom domény, exclusion/safety | `P1` |
| `B` | expert validation rating nástroja | CVI, expert panel, Delphi-lite alebo podobný paper | obrana položiek G, A, R a pilotnej validity | `P1` |
| `C` | simulated patients framing | 1–2 zdroje priamo k simulated patients alebo virtual patients | framing práce ako simulation/training artifact | `P1` |
| `D` | safety a non-diagnostic framing | explicitné high-stakes a oversight zdroje | etika, limity, diskusia, obrana pri obhajobe | `P1` |
| `E` | agreement metrics pre ordinálne ratingy | weighted kappa alebo iný ordinal agreement zdroj | presnejšia metodická obrana | `P2` |

---

## Gap A: formálny klinický zdroj pre MDD

Momentálne máš symptom anchors, PHQ a Eurostat, ale chýba ti aspoň jeden klinický referenčný bod pre samotnú depresívnu symptomatiku.

**Doplniť:**
- DSM-5-TR alebo ekvivalentný kvalitný review k MDD symptomatike
- ideálne článok o diferenciácii MDD vs. grief / anxiety / bipolarity / psychosis features

**Načo to potrebuješ:**
- obhájenie seed konštrukcie
- obhájenie A1–A9 domén
- obhájenie exclusion/safety pravidiel

---

## Gap B: zdroj k tvorbe expertového rating instrumentu

COSMIN je silný základ, ale ešte chýba niečo bližšie k tomu, ako sa robí expert judgement scale alebo content validation panel pri novo vytvorenom nástroji.

**Doplniť:**
- CVI paper
- expert-panel validation paper
- prípadne Delphi alebo modified Delphi paper

**Načo to potrebuješ:**
- obhájiť, prečo sú položky G, A, R zostavené takto
- ukázať, ako prebiehal refine otázok
- vysvetliť, prečo je nástroj pilotne validovaný a nie plne validovaný

---

## Gap C: simulated patients / AI patients mimo všeobecného LLM health review

Máš blízky Nature/Communications Medicine smer, ale ešte by sa hodili 1–2 zdroje priamo na:
- simulated patients
- virtual standardized patients
- AI patient training
- medical alebo psychological education use-case

**Načo to potrebuješ:**
- ukotviť prácu nie ako „AI chatbota“, ale ako „simulation/training artifact“

---

## Gap D: high-stakes limitations / safety

Máš etiku všeobecne, ale potrebuješ aj explicitný argument, že:
- toto nie je diagnostický nástroj,
- ide o výskumno-tréningové použitie,
- human expert judgement ostáva rozhodujúci filter.

**Načo to potrebuješ:**
- etika
- limity
- diskusia
- obrana pred kritikou typu „AI nemôže robiť kliniku“

---

## Gap E: interrater agreement pri ordinálnych expert ratingoch

ICC je dobrý základ, ale ak budeš mať veľa ordinálnych položiek, môže sa zísť aj zdroj k:
- weighted kappa
- ordinal agreement metrics
- prípadne argument, prečo si zostal pri ICC alebo mixed models

**Načo to potrebuješ:**
- presnejšia metodická obrana
- posudok a obhajoba
