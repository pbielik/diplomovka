# Prehľad literatúry pre diplomovú prácu

**Téma:** AI-generované simulované klinické interview pri depresívnej symptomatike / odborné hodnotenie plausibility, konzistencie a symptom fidelity  
**Účel súboru:** centrálny rozcestník pre literature workflow v repo

---

## Ako tento bundle používať

Tento súbor je vstupná brána. Nemá držať všetky detaily sám. Slúži na rýchlu orientáciu:

1. pozri si tematické klastre a rozhodni, kam nový zdroj patrí,
2. otvor detailný súbor pre daný klaster alebo gap,
3. zaraď zdroj do Zotera a tagov,
4. vytvor výpiskový súbor, ak ide o `must-read` alebo metodicky kritický zdroj,
5. ak zdroj vstupuje do textu, skontroluj source map v `references/`.

Bibliografický zdroj pravdy ostáva v Zotere. Tento bundle je plánovacia a operačná vrstva medzi Zoterom, výpiskami a rukopisom.

## Súbory v tomto bundle

- [Tematické klastre a jadro literatúry](source_clusters.md)
- [Literárne medzery a coverage risks](gaps_and_missing_sources.md)
- [P1 expansion pass s konkrétnymi zdrojmi](p1_expansion_pass.md)
- [Audit Better BibTeX seed workflow](bbt_seed_audit_2026-04-06.md)
- [Zadania pre agentov](agent_tasks.md)
- [Krátky praktický plán](action_plan.md)
- [Workflow README](README.md)

## Tematické klastre

| Klaster | Primárna funkcia v práci | Stav |
| --- | --- | --- |
| `01 Depresia a MDD` | klinické ukotvenie symptomatiky, seed anchoring, Introduction a Method | `čiastočne pokryté` |
| `02 LLM, mental health a psychiatria` | všeobecný rámec AI použitia, simulated patients, Discussion | `dobre rozbehnuté` |
| `03 Validácia rating nástroja` | content validity, expert panel, pilotná validácia v Method | `čiastočne pokryté` |
| `04 Metóda, štatistika a analytický dizajn` | ICC, agreement metrics, mixed models, Results | `dobre rozbehnuté` |
| `05 Všeobecná metodológia psychologického výskumu` | terminológia, dizajn, formálne metodické opory | `pokryté` |
| `06 Kvalitatívne metódy (optional)` | len ak sa budú analyzovať otvorené komentáre | `voliteľné` |
| `07 Etika a AI governance` | non-diagnostic framing, safety, limity a etika | `čiastočne pokryté` |

Detaily, odporúčané zdroje a priority sú v [source_clusters.md](source_clusters.md).

## Otvorené medzery

| ID | Gap | Prečo je dôležitý |
| --- | --- | --- |
| `A` | klinické jadro MDD | obhájenie seed konštrukcie a symptom domén |
| `B` | content validity a expert validation | obrana rating nástroja v metóde |
| `C` | simulated patients mimo všeobecných LLM review | framing práce ako simulation/training artifact |
| `D` | high-stakes limitations a safety | etika, limity, non-diagnostic framing |
| `E` | agreement metrics pre ordinálne ratingy | metodická obrana pri posudku a obhajobe |
| `F` | epidemiologický zdroj pre depresiu (WHO fact sheet) | otváracie paragrafy Úvodu a rámcovanie významu témy |
| `G` | pred-LLM virtual patients v psychiatrickom tréningu | ukotvenie posunu od klasických VP k LLM-based VP v Úvode |
| `H` | LLM simulovaný pacient so štruktúrujúcim framework-om (CureFun / PATIENT-ψ / Adaptive-VP) | empirická opora pre H1-H5 a variable „štruktúrujúce klinické usmernenie" |
| `I` | LLM klient s metakogníciou a kontrolou disclosure (MindVoyager) | teoretická opora pre premennú „štýl odpovedania" a H6-H9 |

Detaily a očakávané využitie v práci sú v [gaps_and_missing_sources.md](gaps_and_missing_sources.md).

## Najbližšie kroky

- zosúladiť `references/zotero-thesis-seed.bib` s auditom v [bbt_seed_audit_2026-04-06.md](bbt_seed_audit_2026-04-06.md),
- zosúladiť Zotero kolekcie a tagy s klastrami v [source_clusters.md](source_clusters.md),
- doplniť `must-read` jadro pre medzery A až E,
- aktualizovať výpisky v `notes/literature/`,
- držať source mapy v `references/` v súlade s novými citekeys a kľúčovými zdrojmi.

## Jednovetové zhrnutie

Literatúrny workflow je teraz rozdelený tak, aby si sa rýchlo dostal od klastrov a medzier k výpiskom, Zotero workflow a konkrétnym agent taskom bez toho, aby jeden súbor niesol všetko naraz.
