## Redactierapport — documentatie Main Task 30

**Datum redactie:** 16 juli 2026
**Scope:** uitsluitend de tekst die Main Task 30 toevoegde: LRD sectie 6.23 + de 6.14-bullet + rijen FR-46/FR-47/NFR-18/AC-22; TDD 6.7 (herschreven alinea's), 9.6, Deel 15, de nieuwe Deel 14-rijen en de matrixrijen; buildplan Main Task 30 en 31 + de overzichts- en golventabelregels.
**Niet in scope:** de bestaande tekst van de drie documenten. Zie de signalering onderaan.

### Taalwijzigingen

| # | Locatie | Origineel | Gecorrigeerd | Reden |
|:--|:--------|:----------|:-------------|:------|
| 1 | LRD 6.23, TDD 9.6/Deel 15, buildplan Task 30/31 (26 exemplaren) | Em-dash als zinsscheider, bv. "weinig betekenen — welk model leest je checkpoint" | Dubbele punt, komma, haakjes of zinssplitsing, afhankelijk van de grammaticale functie op die plek | Speciaal teken (em-dash), sectie E/I.2 |
| 2 | Buildplan, koppen Main Task 30 en 31 | "## Main Task 30: Transparantie-SSOT — één bron voor…" | "## Main Task 30: Transparantie-SSOT (één bron voor…)" | Speciaal teken (em-dash in kop), conform de eerdere behandeling van "Kop Main Task 5" in `taalrapport-buildplan.md` |
| 3 | Buildplan, subkoppen 30.3/30.5/30.4-30.6 | "**30.3 — waarom `shared/models.py` weg is…**" | "**30.3: waarom `shared/models.py` weg is…**" | Speciaal teken (em-dash) |
| 4 | TDD Deel 15.1 | "een belofte die geen test controleert, is een comment" | "…is een opmerking in de code" | Anglicisme ("comment" heeft een gangbaar, niet-houterig Nederlands equivalent) |
| 5 | TDD Deel 15.2 | "waar cross-cutting config logischer oogt" | "waar overkoepelende configuratie logischer oogt" | Anglicisme |
| 6 | TDD Deel 15.4, buildplan Task 30 + overzicht | "een Python-test die `.tsx` greppt" | "…die `.tsx` doorzoekt" | Niet-bestaand woord ("greppen" is geen Nederlands werkwoord) |
| 7 | Buildplan Task 31 | "Dit is daarom geen \"nice to have\" maar het sluitstuk van FR-47" | "Dit is daarom geen extraatje maar het sluitstuk van FR-47" | Anglicisme + onnodige aanhalingstekens (I.1) |
| 8 | Buildplan, golventabel | "\| 17–20 \| **Tasks 26–29** \| — \|" | "\| … \| (n.v.t.) \|" | Speciaal teken (em-dash als celvulling) |

**Aantal wijzigingen:** 8 categorieën, 33 tekstplaatsen (26 em-dashes + 7 overige).
**Oordeel:** Kleine correcties.

Behouden, met reden:
- **En-dash in bereiken** ("17–20", "9.1–9.5", "2–4 argumenten"): correcte typografische bereik-notatie, geen zinsscheider. Expliciet uitgezonderd in `taalrapport-buildplan.md`.
- **Ingeburgerde vaktermen** (`guard`, `commit`, `dry-run`, `endpoint`, `build`, `wheel`, `tier`): gangbaar in deze documenten en zonder houterig Nederlands alternatief; bovendien zijn het namen van concrete artefacten.
- **`—` binnen codevoorbeelden en bestandsnamen**: niet van toepassing, komt niet voor.

### Structuuranalyse (advies)

Geen wijzigingen aangebracht.

**SCQA-opening:** LRD 6.23 en TDD 15.1 volgen de volgorde herkenbaar. Situation: een student levert een semester lang werk in bij een AI-tutor. Complication: de onboarding vertelde niet wélke AI, en er was geen bron om dat uit te halen. Question (impliciet): hoe voorkom je dat zo'n tekst stil onwaar wordt? Answer: één bestand dat tegelijk configureert en informeert. De Answer staat in beide gevallen in de tweede alinea, niet in de slotalinea.

**Governing thought en supporting arguments:** de governing thought is in beide secties expliciet en vroeg ("de eis is niet 'er staat een privacytekst', maar 'die tekst kan niet onwaar worden'"). Drie supporting arguments, conform de regel-van-drie: de tweeledige bron (15.2), het verwijderen van de override (15.3), en de guard (15.4). Elk draagt eigen evidence (respectievelijk de laagscheiding en het packaging-argument, de `quality_advisor`-bug, en de zes testcategorieën plus de tegenproef).

**Horizontale en verticale logica:** de opsomming in 15.4 is na correctie parallel gestructureerd (elk item opent met een zelfstandignaamwoordgroep plus punt, gevolgd door de toelichting); vóór correctie mengden vier items een em-dash-constructie met twee die een punt gebruikten. De argumenten in 15.2–15.4 staan in causale volgorde (bron → override → afdwinging), niet willekeurig.

**Holle conclusies / gebrek aan nuance (I.3):** geen aandachtspunten. 15.5 ("Wat dit deel niet oplost") is geen samenvattende slotalinea maar voegt drie nieuwe, concrete beperkingen toe: de tier, de ontbrekende purge en Google's misbruiklogs. Datzelfde geldt voor LRD 6.23's slotalinea, die de scope afbakent tegenover DPIA/verwerkingsregister.

**Concrete suggesties:** geen.

**Structureel oordeel:** Volgt het Pyramid Principle.

### Signalering buiten scope: de em-dash-conventie is repo-breed teruggeregresseerd

Tijdens deze redactie viel op dat de drie documenten op 13 juli 2026 volledig zijn geredigeerd, waarbij álle em-dashes zijn verwijderd (LRD 298, buildplan 359; zie `taalrapport-lrd-operational-excellence.md` en `taalrapport-buildplan.md`, die de kop-variant expliciet meenamen). Sindsdien zijn ze teruggekomen in tekst die ná die datum is toegevoegd:

| Document | Em-dashes nu | Stand na de redactie van 13-07 |
|:--|--:|--:|
| `lrd-operational-excellence.html` | 35 | 0 |
| `tdd-operational-excellence.html` | 74 | 0 |
| `buildplan.md` | 148 | 0 |

Deze 257 exemplaren komen uit Main Tasks 22 tot en met 29 en vallen buiten de scope van dit rapport; de 26 die Main Task 30 zelf introduceerde, zijn hierboven gecorrigeerd. De observatie is dezelfde categorie als LRD 6.22/NFR-17: zonder een controle die meeloopt, groeit een handmatig doorgevoerde conventie terug bij de volgende ronde. Een guard-test op ` — ` in `design-documents/*` zou dit afvangen op dezelfde manier waarop `test_wiki_no_week_numbers.py` de weeknummers afvangt. Dat is een aparte opdracht en een keuze van de auteur, niet van de redacteur.
