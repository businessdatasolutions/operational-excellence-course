# Testdata

Fictieve roosters om de import mee te proberen. Geen echte personen; alleen voornamen, conform het privacymodel (LRD 1.3).

## `roster-4-klassen-S2Y26-27.csv`

89 studenten, 30 teams, 4 klassen, 3 docenten. Eén klas in Arnhem, drie in Nijmegen.

| klas | locatie | docent | studenten | teams |
|:--|:--|:--|--:|--:|
| BKA-C01 | Arnhem | Marleen | 22 | 7 |
| BKN-C01 | Nijmegen | Marleen | 22 | 6 |
| BKN-C02 | Nijmegen | Youssef | 22 | 8 |
| BKN-C03 | Nijmegen | Priya | 23 | 9 |

Teams tellen 2–4 studenten. Marleen heeft twee klassen — dat is toegestaan (één docent per klas, niet één klas per docent) en het is precies het geval dat de klas-scoping moet aankunnen.

**Waarom de docenten verschillende voornamen hebben.** Dat is geen toeval. De identiteit van een docent is `docent-<voornaam>`, dus twee docenten die allebei "Jan" heten zijn voor het systeem één persoon en zien elkaars klassen. Het privacymodel kent alleen voornamen, dus het systeem kán "één Jan met twee klassen" niet onderscheiden van "twee Jannen met elk één klas".

## De data opnieuw genereren

Het bestand is met een vaste seed gegenereerd en dus reproduceerbaar; het is bewust ingecheckt in plaats van bij elke run opnieuw gemaakt, zodat een testresultaat naar één concrete rooster verwijst.

## Importeren

Op dag één kan dit **niet via de applicatie**: `POST /api/roster-import` eist een docent-credential, en credentials komen alleen uit een import. Een leeg cohort heeft geen enkele grant, dus de eerste import moet buiten de HTTP-laag om:

```python
from admin_api import roster_import
res = roster_import.commit_import(open("roster-4-klassen-S2Y26-27.csv").read(), root=Path("lakehouse"))
# res["grants"] bevat de links ÉÉN keer -- alleen digests worden bewaard
```

Daarna werkt alles wel via het product: het admin-onderdeel → **Toegangslinks** doet preview → commit → printvel met QR per klas.

De server authenticeert tegen één cohort (`OE_COHORT`, standaard `2026-2027-oe`), dus voor dit bestand:

```
OE_COHORT=S2Y26-27 python -m admin_api.server
```
