# Interview protocol - AI-only runtime verzia

Status: AI-only runtime verzia interview packu pre simulované rozhovory.

Účel: pracovný interviewer sheet pre AI simulované rozhovory s prehľadom hlavných otázok, doplňujúcich otázok a záverečného PHQ-9 bloku.

Poznámka: dokument zachováva schválené otázky bez obsahového prepisu. Táto verzia je určená iba pre AI-only runtime použitie a nie je určená na reálne interview s pacientom.

## Základné pravidlá

| Parameter | Hodnota |
| --- | --- |
| Cieľová dĺžka | 22 - 28 turnov |
| Dĺžka otázky | 1, max. 2 vety |
| Pravidlo DO | Na A1 - A9 max. 1 DO |
| Neutralita | Bez hodnotenia; len neutrálne potvrdenie |

Používanie: najprv krátke otvorenie, potom blok A1 - A9 podľa toku reči simulovaného respondenta a až na záver štandardizovaný PHQ-9 dodatok.

## 1. Otvorenie

Úvodná časť má byť krátka, prirodzená a vecná.

### Q1 Otvorenie

- Hlavná otázka: „Dobrý deň. Povedzte mi, ako sa dnes máte?“
- DO: „Ako dlho sa to zhruba deje?“
- Poznámka: Doplňujúcu otázku použite len vtedy, ak sa už v úvode spontánne objavia nejaké problémy alebo ťažkosti.

### Q2 Vplyv na bežný deň

- Hlavná otázka: „Ako to vplýva na váš bežný deň?“

## 2. Blok A - symptómové domény (MDD)

Poradie domén A1 - A9 je možné meniť podľa toku reči simulovaného respondenta. Na každú doménu použite maximálne jednu doplňujúcu otázku.

### A1 Nálada

- Hlavná otázka: „Ako by ste opísali svoju náladu za posledné dva týždne?“
- DO: „Je to takto väčšinu dňa, takmer každý deň?“

### A2 Anhedónia (záujem)

- Hlavná otázka: „Všimli ste si zmenu v tom, ako vás bavia veci, ktoré ste mali radi predtým?“
- DO: „Viete uviesť konkrétny príklad?“

### A3 Spánok

- Hlavná otázka: „Ako spíte? Máte ťažkosti so zaspávaním, budením alebo spíte priveľa?“
- DO: „Zmenilo sa to oproti vášmu bežnému zvyku?“

### A4 Apetít / hmotnosť

- Hlavná otázka: „Ako je to s chuťou do jedla? Musíte sa do jedla nútiť, alebo jete viac než obvykle? Zmenila sa vaša váha?“
- DO: „Chutí vám jedlo ako obvykle, alebo sa zmenilo aj prežívanie chute?“

### A5 Psychomotorika

- Hlavná otázka: „Cítite sa byť spomalený, tak že vám veci idú ťažko, neviete sa rozhýbať do činnosti, alebo naopak vnútorne nepokojný a neviete obsedieť?“
- DO: „Všíma si to aj okolie?“

### A6 Energia / únava

- Hlavná otázka: „Ako ste na tom s energiou? Máte dostatok energie na všetko, čo potrebujete v daný deň urobiť, alebo sa unavíte rýchlejšie než obvykle?“
- DO: „Je tá únava primeraná námahe, alebo prichádza aj bez nej?“

### A7 Vina / bezcennosť

- Hlavná otázka: „Zvýraznili sa u vás za posledné obdobie pocity viny, pocity, že za niečo nestojíte, alebo myšlienky, že ste v niečom zlyhali? Máte pocit, že by ste nestáli za nič ako človek?“
- DO: „Týka sa to konkrétnej veci, alebo je to skôr všeobecný pocit?“

### A8 Koncentrácia

- Hlavná otázka: „Darí sa vám sústrediť tak ako obvykle, alebo je vaša pozornosť v poslednom období slabšia, napríklad pri práci, čítaní alebo sledovaní TV?“
- DO: „Robíte chyby, ktoré bežne nerobíte?“

### A9 Myšlienky na smrť (pasívne)

- Hlavná otázka: „V ťažkých obdobiach ľuďom niekedy napadne, že by bolo lepšie nebyť. Objavili sa u vás také myšlienky?“
- DO: „Ako často sa vracajú?“
- Poznámka: Ak simulovaný respondent uvedie plán, zámer alebo bezprostredné riziko, ukončite štandardný priebeh, transcript označte ako `safety_escalation` a pokračujte podľa interného branching pravidla simulácie. V AI-only režime ide o interné pravidlo simulácie, nie o reálny klinický zásah.

## 3. Záverečný PHQ-9 blok

PHQ-9 zaraďte až na záver rozhovoru. Prechodová veta môže znieť: „Na záver sa vás ešte spýtam niekoľko stručných štandardizovaných otázok o tom, ako ste sa cítili za posledné dva týždne.“

### Škála odpovedí

| 0 | 1 | 2 | 3 |
| --- | --- | --- | --- |
| Vôbec nie | Niekoľko dní | Viac ako polovicu dní | Takmer každý deň |

### PHQ-9 položky

| # | PHQ-9 položka | Odpoveď | Skóre |
| --- | --- | --- | --- |
| 1 | Malý záujem alebo potešenie z robenia vecí. | ______________ | __ |
| 2 | Pocit skleslosti, smútku alebo beznádeje. | ______________ | __ |
| 3 | Ťažkosti so zaspávaním, prerušovaný spánok alebo naopak spánok nadmieru. | ______________ | __ |
| 4 | Pocit únavy alebo nedostatku energie. | ______________ | __ |
| 5 | Znížená chuť do jedla alebo naopak jedenie viac než zvyčajne. | ______________ | __ |
| 6 | Zlý pocit zo seba - pocit zlyhania alebo že ste sklamali seba či iných. | ______________ | __ |
| 7 | Ťažkosti sústrediť sa, napríklad pri čítaní, práci alebo sledovaní TV. | ______________ | __ |
| 8 | Spomalenie pohybu alebo reči natoľko, že by si to mohli všimnúť iní, alebo naopak nepokoj a neschopnosť obsedieť. | ______________ | __ |
| 9 | Myšlienky, že by bolo lepšie nebyť tu, alebo že by ste si mohli nejako ublížiť. | ______________ | __ |

Bezpečnostná poznámka: Ak sa pri položke 9 objaví plán, zámer alebo bezprostredné riziko, ukončite štandardný priebeh, transcript označte ako `safety_escalation` a pokračujte podľa interného branching pravidla simulácie. V AI-only režime ide o interné pravidlo simulácie, nie o reálny klinický zásah.

## 4. Rýchly checklist pred použitím

- [ ] Otvorenie je krátke a prirodzené; nejde sa hneď mechanicky cez celý checklist.
- [ ] V bloku A1 - A9 používam na doménu najviac 1 doplňujúcu otázku.
- [ ] Odpovede nehodnotím; používam len neutrálne potvrdenie počutia.
- [ ] Poradie domén prispôsobujem toku reči simulovaného respondenta, nie rigidnému poradovníku.
- [ ] PHQ-9 zaraďujem až na záver ako samostatný štandardizovaný dodatok.
- [ ] Dokument používam na AI simuláciu, nie na reálne interview.
- [ ] Pri safety eskalácii používam interné branching pravidlo simulácie.
