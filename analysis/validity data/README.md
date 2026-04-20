# analysis/validity data

Tento priečinok drží surový validačný export pre pilotný expert review pass.

Pravidlá:
- `data.xlsx` je source of truth.
- `data.csv` je len raw export snapshot a môže byť technicky poškodený.
- clean analytické vstupy patria do `analysis/data_clean/`, nie sem.

Aktuálny stav:
- `data.csv` má hlavičku so 164 stĺpcami, ale aspoň dva riadky obsahujú 191 polí.
- problém vzniká tým, že workbook nesie aj trailing stĺpce bez použiteľnej hlavičky; pri CSV exporte sa preto do riadku dostanú nadbytočné hodnoty navyše.
- workflow skript `analysis/scripts/build_expert_review_outputs.py` číta primárne `data.xlsx` a pri čítaní z workbooku berie len pomenované stĺpce.

Ak potrebuješ opravený CSV snapshot:

```bash
python3 analysis/scripts/repair_validation_csv.py
```

To vytvorí `data_repaired_trimmed.csv` s riadkami orezanými na šírku hlavičky. Tento repaired CSV je pomocný artefakt pre import/archív; nemení fakt, že source of truth ostáva `data.xlsx`.
