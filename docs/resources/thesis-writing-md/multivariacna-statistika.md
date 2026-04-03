# Multivariacna statistika

## Jednoduchá lineárna regresia

## CIELE

- Zistiť percento vysvetlenej variancie závislej premennej
- Predikcia – akú hodnotu bude mať závislá premenná Y, ak budeme vedieť hodnotu nezávislej premennej X?

## Podmienky

- 1. Vzťah medzi premennými je lineárny.
- 2. Závislá premenná je kardinálna.
- 3. Distribúcia dát je gaussovská.
- 4. Nezávislá premenná je kardinálna alebo nominálna – dichotomická.
- 5. Rozptyl jednej premennej by mal byť rovnaký pre každú kategóriu nezávislej premennej (homoskedasticita).

## Výsledky regresnej analýzy môžu byť skreslené:

- 1. Nelinearitou vzťahu
- 2. Odľahlými hodnotami
- 3. Prítomnosťou subpopulácií – heterogenitou súboru

## Postup

- Opíšeme vzťah medzi premennými, a to nájdením priamky, ktorá najlepšie vystihuje priebeh vzťahu.

## Regresná rovnica:

- Y = b0 + b1 x X
- Y = závislá premenná
- b0 – v akom bode priamka pretína vertikálnu os Y
- b1 – regresný koeficient – o koľko sa zmení hodnota Y, ak sa X zmení o 1
- X – nezávislá premenná

## Slide 7

_No visible text found._

## Výstupy

- R – korelačný koeficient
- R2 koeficient determinácie
- Sig. – štatistická významnosť
- Parametre:
- Konštanta – Constant - b0 – priesečník s osou Y
- Neštandardizované koeficienty - Unstandardized Coefficients – B – sklon priamky – o koľko sa zmení hodnota závislej premennej, ak hodnota nezávislej premennej vzrastie o 1

## Viacnásobná lineárna regresia

## Vzťah medzi sadou nezávislých premenných a jednou závislou premennou

- Y = b0 + b1 x X1 + b2xX2 + b3xX3+ ... bn x Xn

## Ciele

- Vysvetliť varianciu závislej premennej
- Zistiť hodnotu neštandardizovaných koeficientov B
- Zistiť relatívnu váhu nezávislých premenných (štandardizované koeficienty)
- Predikcia hodnôt závislej premennej

## Predpoklady

- 1. Závislá premenná musí byť kardinálna
- 2. Nezávislé premenné sú kardinálne alebo nominálne – dichotomické
- 3. Medzi nezávislými premennými by nemal existovať silný vzťah
- 4. Linearita vzťahu
- 5. Homoskedasticita

## Počet participantov

- 10 participantov na prediktor (+konštanta)
- 20 participantov na prediktor (+konštanta)
- 104 + k (počet prediktorov)

## Multikolinearita

- hodnoty korelačných koeficientov
- variačný inflačný faktor VIF (nemal by byť 5 a viac)
- tolerancia (nemala by byť menšia ako 0,2)

## Metóda Enter

- Metóda Stepwise
- Metóda hierarchická – v blokoch

## Parametre

- Konštanta – Constant - b0 – priesečník s osou Y
- Neštandardizované koeficienty - Unstandardized Coefficients – B – sklon priamky – o koľko sa zmení hodnota závislej premennej, ak hodnota nezávislej premennej vzrastie o 1
- Štandardizované koeficienta Beta – relatívna váha premenných
- ∆R2 - zmena v hodnote koeficienta R2
- Adj. R2 – populačný odhad

## Klastrová analýza

- K-Means

## Charakteristika metódy

- nehierarchická metóda
- heuristická metóda

## Postup

- 1. Výber centier klastrov + priradenie objektu k zhluku
- 2. Prepočítavanie a opakovanie algoritmu
- 3. Optimálne riešenie

## Nevýhody

- Princíp výpočtu (aritmetický priemer)
- Metóda je citlivá na jednotky merania
- Riziko „stigmatizácie“
- Nemožnosť zovšeobecnenia

## https://www.naftaliharris.com/blog/visualizing-k-means-clustering/
