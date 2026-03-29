# Hypotézy H1–H6

**H1.** Rozhovory generované s aktívnym guardrailom (`guardrail = 1`) budú hodnotené vyššie v klinickej plausibilite než rozhovory bez guardrailu (`guardrail = 0`), a to na úrovni `plausibility_index` aj položiek `G1`, `G3` a `G4`.

**H2.** Rozhovory generované s aktívnym guardrailom budú vykazovať nižšiu mieru defektov než rozhovory bez guardrailu, a to na úrovni `defect_index` aj položiek `R1–R5`.

**H3.** Rozvinutejší realizačný profil (`R3`) bude spojený s vyššou prirodzenosťou jazyka a štýlu odpovedí než baseline (`R2`) a rezervovanejší profil (`R1`), a to najmä na položke `G2`.

**H4.** Medzi guardrailom a realizačným profilom bude interakčný efekt tak, že pozitívny efekt guardrailu na klinickú plausibilitu a zníženie defektov bude výraznejší pri profile `R3` než pri profiloch `R1` a `R2`.

**H5.** Rozhovory generované s aktívnym guardrailom budú presnejšie zodpovedať seed anchorom, teda budú mať nižšiu priemernú absolútnu chybu na `A1–A9`, `S1` a `S2` než rozhovory bez guardrailu.

**H6.** Vyššia klinická plausibilita a nižšia miera defektov budú spojené s vyššou tréningovou použiteľnosťou rozhovoru (`G5`) a s nižšou pravdepodobnosťou, že bude rozhovor označený ako `ai_generated`.
