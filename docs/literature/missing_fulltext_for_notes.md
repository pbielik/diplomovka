# Missing Fulltext For Notes

> Posledna aktualizacia: 2026-04-10
> Ucel: priebezny blocker log pre citekeye, pri ktorych nejde spravit evidence-first note, lebo v Zotere chyba lokalny `PDF` alebo `snapshot`, alebo je lokalny fulltext pritomny, ale nie je strojovo citatelny.

## Ako tento subor pouzivat

- Ak pri dalsom batchi chybaju lokalne fulltexty, citekey sa zapise sem skor, nez sa praca na note zastavi.
- Ked PDF alebo snapshot doplnis do Zotera, polozku odtialto vyhod a az potom sa ma robit plnohodnotny note.
- Ak je lokalny fulltext pritomny, ale nejde z neho spolahlivo vytiahnut text alebo locator, polozka sa presunie do sekcie `OCR / extraction blocker`.
- Dated checklisty typu `fulltext_checklist_2026-04-08.md` ostavaju snapshot artefakty; tento subor je zivy operativny prehlad.

## Missing local fulltext a note este nie je hotovy

| Citekey | Priorita | Dovod / planned use | Co doplnit |
| --- | --- | --- | --- |
| ziadne | - | vsetky doteraz logovane local fulltext blockery boli doplnene | - |

## OCR / extraction blocker

| Citekey | Priorita | Stav | Co doplnit |
| --- | --- | --- | --- |
| `lynn1986contentvalidity` | `should-read` | lokalny PDF uz existuje, ale aktualny subor je scan bez textovej vrstvy; `pypdf` vracia prazdne strany a v Zotero storage nie je `.zotero-ft-cache` | doplnit searchable PDF alebo OCR verziu, az potom sa ma robit plnohodnotny evidence-first note |
