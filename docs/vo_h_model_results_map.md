# Mapa blokov, VO, hypotéz a Results

> Pracovná pomôcka pre drafting, kontrolu logiky IMRaD a obhajobu.
> Cieľ: mať na jednom mieste zhrnuté, ako sa bloky výskumných otázok (`VO`), hypotéz (`H`), outcome premenných, modelov a sekcií Results navzájom prekrývajú.

## Hlavná mapa

| Blok | Funkcia bloku | VO | H | Hlavné premenné / outcome-y | Model / postup | Sekcie vo Results | Krátka veta na obhajobu |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Blok A` | globálna kvalita interview | `VO1` | `H1`, `H2`, `H5` | index klinickej vierohodnosti = priemer `G1`, `G3`, `G4`; položky `G2`, `G5`; deskriptívne aj `G1`–`G5` | frekvencie + mediány/IQR pre položky, `LMM` pre index, `ordinal mixed models` pre `G2`, `G5` | `3.2`, `3.3`, `3.5.1`, `3.5.2`, `3.5.5` | Najprv ukazujem, ako kvalitne rozhovory pôsobia celkovo, a potom testujem, či `guardrail` zvyšuje priemernú úroveň vierohodnosti a posúva distribúciu prirodzenosti a použiteľnosti k vyšším skóre. |
| `Blok A` | symptom fidelity voči seedu | `VO2` | `H4` | `symptom_error_mean` = priemerná absolútna chyba `A1`–`A9`; doplnkovo `severity_error`, `impact_error`, deskriptívne `S1`, `S2` | deskriptíva a transcript-level model pre `symptom_error_mean`, `severity_error`, `impact_error`; doplnkovo `CLMM` pre `S1`, `S2` | `3.2`, `3.3`, `3.5.4` | Tu nejde len o to, či rozhovor znie dobre, ale či zodpovedá zamýšľanému klinickému profilu seedu; jadro je rozdiel v priemernej chybe, nie voľný dojem. |
| `Blok B` | efekt `profile` na globálnu kvalitu | `VO3` | `H6`, `H7` | index klinickej vierohodnosti = priemer `G1`, `G3`, `G4`; položky `G2`, `G5` | `LMM` pre index, `ordinal mixed models` pre `G2`, `G5` | `3.6.1`, `3.6.2` | Tento blok ukazuje, či zdržanlivejší alebo rozvinutejší štýl odpovedania mení priemernú úroveň vierohodnosti a distribúciu prirodzenosti a použiteľnosti. |
| `Blok B` | efekt `profile` na symptom fidelity a red flags | `VO4` | `H8` + bez samostatnej hypotézy pre zvyšné outcome-y | `symptom_error_mean`, `severity_error`, `impact_error`, `defect_index` | transcript-level model pre error vetvu, `LMM` pre index defektov; doplnkovo `CLMM` pre `S1`, `S2` | `3.6.3` | `H8` pokrýva jadro transcript-level symptom fidelity; ostatné outcome-y ostávajú inferenčnou odpoveďou na `VO4`, nie samostatnými smerovými hypotézami. |
| `Blok C` | interakcia `guardrail × profile` | `VO5` | `H9` | index klinickej vierohodnosti, index defektov, doplnkovo `symptom_error_mean`, `severity_error`, `impact_error` | interakčné členy v `LMM`, transcript-level error modeli a doplnkových ordinálnych modeloch | `3.6.4` | Tu sa pýtam, či `guardrail` pomáha rovnako vo všetkých profiloch, alebo výraznejšie pri niektorých štýloch odpovedania. |
| `Blok C` | zhoda hodnotiteľov | `VO6` | bez hypotézy | `ICC` pre `plausibility_index`, `defect_index`, `S1`, `S2` | `ICC` | `3.4` | Toto je merací blok: najprv potrebujem vedieť, či sa experti zhodujú, až potom má zmysel silnejšie interpretovať inferenčné výsledky. |
| `Blok C` | vnímaný pôvod rozhovoru | `VO7` | bez hypotézy, exploračné | `guessed_origin`, `guess_confidence` | frekvencie, exploratórny logistický alebo ordinálny model | `3.7.1` | Toto nie je jadro testu kvality, ale doplnkový signál, či rozhovory pôsobia zjavne strojovo alebo nie. |
| `Blok C` | otvorené komentáre | `VO8` | bez hypotézy, exploračné | `comment` | stručné tematické kódovanie | `3.7.2` | Komentáre vysvetľujú, prečo boli niektoré rozhovory hodnotené lepšie alebo horšie, a dopĺňajú kvantitatívny obraz. |

## Praktické pravidlá

- Ak má blok priradené hypotézy, ide o konfirmačný blok.
- Ak blok nemá hypotézu, ide buď o merací blok (`VO6`), alebo o exploračný blok (`VO7`, `VO8`).
- V poradí reportovania drž logiku `Blok A -> Blok B -> Blok C`.
- Pri `VO4` nepodsúvaj v texte, že existovali samostatné hypotézy pre `S1`, `S2` a `defect_index`; tieto výstupy sú súčasťou odpovede na otázku, ale nie samostatne hypotetizované.
- `severity_error` a `impact_error` sú po zarovnaní seed anchors na `1-5` priame error skóre voči `S1_anchor` a `S2_anchor`; môžu sa reportovať ako sekundárna vetva, ale netvoria jadro `VO/H`.

## Najkratšia verzia na obhajobu

- `Blok A`: overujem, či sú rozhovory kvalitné a či sedia na seed.
- `Blok B`: overujem, čo s kvalitou robí štýl odpovedania simulovaného pacienta.
- `Blok C`: overujem interakciu, zhodu expertov a doplnkové signály o pôvode a komentároch.
