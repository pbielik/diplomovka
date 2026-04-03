# K-Means navod SPSS

Metóda K-Means je štatistická metóda, prostredníctvom ktorej zoskupujeme participantov do skupín (klastrov, zhlukov, typov) na základe ich podobnosti a rozdielnosti. Cieľom je nájsť optimálne riešenie – t.j. aby participanti boli vo vnútri zhluku čo najpodobnejší a aby sa zároveň nepodobali na participantov z iných zhlukov. Cieľom je teda rozdeliť participantov do klastrov tak, aby vzdialenosť medzi všetkými objektmi a ich centrami bola minimalizovaná.

Metóda K-Means je nehierarchická metóda – všetky vytvorené typy sú „na jednej“ úrovni. Jedná sa o heuristickú metódu. To znamená, že počet typov zadávame vopred my a hľadáme optimálne riešenie (systém nám nepovie, či máme zvoliť trojtypové alebo štvortypové riešenie – vzniknuté typy totiž interpretujeme z pohľadu psychológie).

Princíp metódy: Systém náhodne vyberie centrá klastrov a každý objekt priradí k zhluku, ktorého centrum je k nemu najbližšie (jedná sa o tzv. centroid - vektor, ktorého hodnoty sú aritmetickými priemermi hodnôt všetkých objektov zhluku). Po priradení všetkých objektov sa centrá prepočítavajú (opäť na princípe priemerov, preto sa metóda volá K-Means). Tento algoritmus sa opakuje, kým nie je nájdené optimálne riešenie (t.j. centrá sa už nemenia – najpodobnejší participanti sú zoskupení v jednom type). Analýza je tiež zastavená, ak v systéme vopred zvolíme určitý počet tzv. iterácií, čie prepočítavaní.

Nevýhoda metódy – metóda pracuje na princípe prepočítavania aritmetického priemeru – t.j. výpočet je skreslený, ak sú v súbore vybočujúce alebo extrémne hodnoty alebo ak je distribúcia negaussovská. Metóda je citlivá na jednotky merania – keďže metódy, s ktorými pracujeme, majú rôzne jednotky a rôzne teoretické rozpätia, je potrebné zrealizovať prevod hrubého skóre na štandardizované skóre – Z-skóre (prichádzame tým o určitú presnosť dát).

Práca s programom SPSS:

Transformácia skóre na Z skóre - Analyze – Descriptive Statistic – Descriptives

<img src="k-means-navod-spss-assets/media/image1.png" style="width:6.3in;height:4.87917in" />

V dialógovom boxe presunieme na pravú stranu najdôležitejšie ukazovatele v jednotlivých doménach a v dolnej časti zaškrtneme políčko Save standardized values as variables – po spustení príkazu sa v dátovom súbore vytvoria nové stĺpce, s ktorými budeme pracovať.

<img src="k-means-navod-spss-assets/media/image2.png" style="width:4.81317in;height:4.11516in" />

Metódu K- Means nájdeme v ponuke Analyze – Classify – K-Means Cluster

<img src="k-means-navod-spss-assets/media/image3.png" style="width:6.3in;height:5.37153in" />

V dialógovom boxe presunieme na pravú stranu všetky novo vytvorené premenné (Z skóre) a nastavíme počet zhlukov. V prvom prípade 3.

<img src="k-means-navod-spss-assets/media/image4.png" style="width:5.94875in;height:5.17781in" />

Stlačíme rádiové tlačidlo Save a zvolíme možnosť Cluster membership – opäť sa nám vytvorí nová premenná – Typológia, ktorá bude mať varianty jednotlivé typy – v práci s premennou môžete ďalej pracovať

<img src="k-means-navod-spss-assets/media/image5.png" style="width:2.3024in;height:1.47937in" />

Kliknutím na rádiové tlačidlo Options otvoríme nové okno, v ktorom zaškrtneme možnosť ANOVA table (zisťujeme štatistickú odlíšiteľnosť typov) a môžeme aj Cluster information for each case – uvidíme zaradenie jednotlivých participantov do typov

<img src="k-means-navod-spss-assets/media/image6.png" style="width:2.48993in;height:2.75038in" />

Výsledky

Trojtypové riešenie

Zaujíma nás „profil“ jednotlivých typov – t.j. hodnoty centier definitívnych klastrov

<table style="width:73%;">
<colgroup>
<col style="width: 47%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 8%" />
</colgroup>
<tbody>
<tr>
<td colspan="4" style="text-align: center;"><blockquote>
<p><strong>Final Cluster Centers</strong></p>
</blockquote></td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;"></td>
<td colspan="3" style="text-align: center;"><blockquote>
<p>Cluster</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(fonematicka_spolu)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,65132</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,17756</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,07163</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov zvieratá</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,03926</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,10773</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,41665</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov zelenina</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,54212</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,18570</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,13304</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov Náradie</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,00632</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,06052</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,37537</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet zapamätaných slov po 30 minútach</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,26915</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,11381</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,25360</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(spolu_a_AVLT)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,55571</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,01209</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,06376</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Kódovanie symbolov výsledné skóre</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,59648</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,91460</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,00710</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet správnych odpovedí odpredu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,86416</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,83069</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,16627</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet správnych odpovedí odzadu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>1,16418</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,52095</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,43761</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Najdlhší číselný rad odpredu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,78313</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,79784</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,13459</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Najdlhší číselný rad odzadu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>1,24599</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,52473</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,48009</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Test cesty A - celkový čas</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,49167</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,85018</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,04024</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Test cesty B - celkový čas</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,61303</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,84185</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,02775</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(fab_spolu)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,55295</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,65378</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,06273</p>
</blockquote></td>
</tr>
</tbody>
</table>

Znázornenie týchto hodnôt v grafe – graf vytvoríme tak, že vo výstupe v SPSS v predchádzajúcej tabuľke s jednotlivými Z-skóre označíme na čierno hodnoty, akoby sme ich išli skopírovať a pravým tlačidlom myši klikneme na označenú časť. V ponuke zvolíme Create Graph a Bar.

<img src="k-means-navod-spss-assets/media/image7.png" style="width:6.3in;height:5.03194in" />

<img src="k-means-navod-spss-assets/media/image8.png" style="width:6.27083in;height:5.02083in" />

Štatistická odlíšiteľnosť jednotlivých typov z hľadiska skúmaných premenných (stĺpec Sig)

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<tbody>
<tr>
<td colspan="7" style="text-align: center;"><blockquote>
<p><strong>ANOVA</strong></p>
</blockquote></td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;"></td>
<td colspan="2" style="text-align: center;"><blockquote>
<p>Cluster</p>
</blockquote></td>
<td colspan="2" style="text-align: center;"><blockquote>
<p>Error</p>
</blockquote></td>
<td rowspan="2" style="text-align: center;"><blockquote>
<p>F</p>
</blockquote></td>
<td rowspan="2" style="text-align: center;"><blockquote>
<p>Sig.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Mean Square</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>df</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Mean Square</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>df</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(fonematicka_spolu)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10,187</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,633</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>16,105</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov zvieratá</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>8,577</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,697</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>12,307</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov zelenina</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>9,481</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,661</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>14,349</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov Náradie</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>7,596</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,736</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10,319</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet zapamätaných slov po 30 minútach</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>7,647</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,734</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10,416</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(spolu_a_AVLT)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>7,495</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,740</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10,125</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Kódovanie symbolov výsledné skóre</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>6,852</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,766</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>8,945</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet správnych odpovedí odpredu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>9,438</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,662</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>14,247</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet správnych odpovedí odzadu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>14,203</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,472</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>30,098</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Najdlhší číselný rad odpredu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>8,036</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,719</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>11,184</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Najdlhší číselný rad odzadu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>16,247</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,390</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>41,648</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Test cesty A - celkový čas</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,450</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,822</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>6,630</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,003</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Test cesty B - celkový čas</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>6,373</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,785</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>8,117</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,001</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(fab_spolu)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>4,485</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,861</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>50</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,212</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,009</p>
</blockquote></td>
</tr>
</tbody>
</table>

Počet participantov v jednotlivých typoch

<table style="width:30%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><blockquote>
<p><strong>Number of Cases in each Cluster</strong></p>
</blockquote></td>
</tr>
<tr>
<td rowspan="3" style="text-align: center;"><blockquote>
<p>Cluster</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>15,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>28,000</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><blockquote>
<p>Valid</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>53,000</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><blockquote>
<p>Missing</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
</tbody>
</table>

Postup opakujeme s iným počtom klastrov

Štvortypové riešenie

<table style="width:71%;">
<colgroup>
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><blockquote>
<p><strong>Final Cluster Centers</strong></p>
</blockquote></td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;"></td>
<td colspan="4" style="text-align: center;"><blockquote>
<p>Cluster</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(fonematicka_spolu)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,67801</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,52442</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,81442</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,54557</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov zvieratá</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,10936</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,04948</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,56527</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,44514</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov zelenina</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,59065</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,33591</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,32371</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,95273</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov Náradie</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,12976</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,26700</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,81306</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,13987</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet zapamätaných slov po 30 minútach</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,27693</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,25552</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,67751</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,27715</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(spolu_a_AVLT)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,48667</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,17806</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,38786</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,51009</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Kódovanie symbolov výsledné skóre</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,59024</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,16704</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,44727</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,31419</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet správnych odpovedí odpredu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,98803</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,65512</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,31235</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,63362</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet správnych odpovedí odzadu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>1,21356</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,35204</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,67938</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,21849</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Najdlhší číselný rad odpredu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,89129</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,63994</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,43799</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,73103</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Najdlhší číselný rad odzadu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>1,24971</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,40400</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,62889</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,21225</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Test cesty A - celkový čas</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,46049</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,03938</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,00654</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>1,47834</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Test cesty B - celkový čas</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,64722</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,17728</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,29932</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>1,87389</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(fab_spolu)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,57534</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,08992</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-,38736</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>-1,07692</p>
</blockquote></td>
</tr>
</tbody>
</table>

<img src="k-means-navod-spss-assets/media/image9.png" style="width:6.27083in;height:5.02083in" />

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<tbody>
<tr>
<td colspan="7" style="text-align: center;"><blockquote>
<p><strong>ANOVA</strong></p>
</blockquote></td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;"></td>
<td colspan="2" style="text-align: center;"><blockquote>
<p>Cluster</p>
</blockquote></td>
<td colspan="2" style="text-align: center;"><blockquote>
<p>Error</p>
</blockquote></td>
<td rowspan="2" style="text-align: center;"><blockquote>
<p>F</p>
</blockquote></td>
<td rowspan="2" style="text-align: center;"><blockquote>
<p>Sig.</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Mean Square</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>df</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>Mean Square</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>df</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(fonematicka_spolu)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10,796</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,400</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>26,977</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov zvieratá</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>4,833</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,765</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>6,314</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,001</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov zelenina</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>4,387</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,793</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,536</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,002</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet slov Náradie</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,411</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,730</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>7,413</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet zapamätaných slov po 30 minútach</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,391</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,731</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>7,374</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(spolu_a_AVLT)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,740</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,710</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>8,087</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Kódovanie symbolov výsledné skóre</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,509</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,724</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>7,610</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet správnych odpovedí odpredu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>8,762</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,525</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>16,698</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Počet správnych odpovedí odzadu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>9,707</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,467</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>20,791</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Najdlhší číselný rad odpredu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>8,368</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,549</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>15,246</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Najdlhší číselný rad odzadu</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10,142</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,440</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>23,037</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Test cesty A - celkový čas</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>4,644</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,777</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,977</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,001</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore: Test cesty B - celkový čas</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>8,396</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,547</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>15,344</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Zscore(fab_spolu)</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>4,137</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,808</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>49</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,121</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,004</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:30%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><blockquote>
<p><strong>Number of Cases in each Cluster</strong></p>
</blockquote></td>
</tr>
<tr>
<td rowspan="4" style="text-align: center;"><blockquote>
<p>Cluster</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>14,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>22,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>12,000</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>4</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5,000</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><blockquote>
<p>Valid</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>53,000</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><blockquote>
<p>Missing</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,000</p>
</blockquote></td>
</tr>
</tbody>
</table>

S analýzou by sme mohli pokračovať a skúšať viac-typové riešenia, kým nenájdeme optimálne riešenie.

Dodatok

Výsledok klastrovej analýzy si môžeme overiť tzv. diskriminačnou analýzou – prostredníctvom nej zistíme, koľko participantov bolo správne zaradených do typu.

Analyze – Classify – Discriminant

<img src="k-means-navod-spss-assets/media/image10.png" style="width:6.3in;height:5.48333in" />

Ako Grouping Variable označíme vybranú typológiu a definujeme jej rozsah. Do políčka Independents zahrnieme všetky Zetkové premenné.

<img src="k-means-navod-spss-assets/media/image11.png" style="width:5.32366in;height:3.32338in" />

Klikneme na Classify a zaklikneme možnosť Summary table

<img src="k-means-navod-spss-assets/media/image12.png" style="width:4.66732in;height:3.28171in" />

Vo výstupoch nás zaujíma posledná tabuľka:

V prípade prvej typológie bolo zaradených správne 100% participantov.

<table style="width:72%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 22%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr>
<td colspan="7" style="text-align: center;"><blockquote>
<p><strong>Classification Results<sup>a</sup></strong></p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td rowspan="2" style="text-align: center;"><blockquote>
<p>Cluster Number of Case</p>
</blockquote></td>
<td colspan="3" style="text-align: center;"><blockquote>
<p>Predicted Group Membership</p>
</blockquote></td>
<td rowspan="2" style="text-align: center;"><blockquote>
<p>Total</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr>
<td rowspan="6" style="text-align: center;"><blockquote>
<p>Original</p>
</blockquote></td>
<td rowspan="3" style="text-align: center;"><blockquote>
<p>Count</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>15</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>10</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>28</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>28</p>
</blockquote></td>
</tr>
<tr>
<td rowspan="3" style="text-align: center;"><blockquote>
<p>%</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
</tr>
<tr>
<td colspan="7" style="text-align: center;"><blockquote>
<p>a. 100,0% of original grouped cases correctly classified.</p>
</blockquote></td>
</tr>
</tbody>
</table>

V druhej typológii (štvortypovej) je to 98,1% participantov – jedného participanta diskriminačná analýza „preradila“ z druhého typu do prvého.

<table style="width:72%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 22%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr>
<td colspan="8" style="text-align: center;"><blockquote>
<p><strong>Classification Results<sup>a</sup></strong></p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td rowspan="2" style="text-align: center;"><blockquote>
<p>Cluster Number of Case</p>
</blockquote></td>
<td colspan="4" style="text-align: center;"><blockquote>
<p>Predicted Group Membership</p>
</blockquote></td>
<td rowspan="2" style="text-align: center;"><blockquote>
<p>Total</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr>
<td rowspan="8" style="text-align: center;"><blockquote>
<p>Original</p>
</blockquote></td>
<td rowspan="4" style="text-align: center;"><blockquote>
<p>Count</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>14</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>14</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>21</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>22</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>12</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>12</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>4</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>5</p>
</blockquote></td>
</tr>
<tr>
<td rowspan="4" style="text-align: center;"><blockquote>
<p>%</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>1</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>2</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>4,5</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>95,5</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>3</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>4</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
<td style="text-align: right;"><blockquote>
<p>100,0</p>
</blockquote></td>
</tr>
<tr>
<td colspan="8" style="text-align: center;"><blockquote>
<p>a. 98,1% of original grouped cases correctly classified.</p>
</blockquote></td>
</tr>
</tbody>
</table>

.
