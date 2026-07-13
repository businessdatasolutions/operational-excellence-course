## Redactierapport — buildplan.md

**Datum redactie:** 13 juli 2026
**Bestand:** `design-documents/buildplan.md` (Operational Excellence Gate-systeem — Build Plan)
**Omvang:** 639 regels, ca. 16.140 woorden vóór redactie (ca. 15.830 ná redactie)
**Methode:** het document is voor deze redactie in vijf inhoudelijke fragmenten verdeeld langs de bestaande Main Task-scheidingen (regels 1–135, 137–264, 266–381, 383–486, 488–639), elk onafhankelijk geredigeerd volgens dezelfde procedure, en vervolgens samengevoegd en geverifieerd tot dit ene document.

### Uitgangspunten die zijn gerespecteerd

- Checkbox-markers (`- [ ]` / `- [x]`) zijn **niet gewijzigd**: 170 `[x]` en 58 `[ ]` vóór en ná de redactie, exact gelijk in aantal én in positie.
- Alle taaknummers (`0.1`…`20.6`) zijn ongewijzigd: identieke verzameling vóór/na.
- Alle FR-/NFR-/AC-codes zijn ongewijzigd: identieke verzameling vóór/na (FR-01 t/m FR-31, NFR-01 t/m NFR-12, AC-01 t/m AC-16).
- Alle 1.344 inline-code-fragmenten (bestandsnamen, paden, commando's, commit-hashes, packagenamen e.d. tussen backticks) zijn byte-voor-byte identiek gebleven vóór en na de redactie.
- Markdown-structuur (koppen, tabellen, horizontale lijnen, lijsten) is intact; alle tabellen hebben nog exact hetzelfde aantal kolommen per rij.

### Taalwijzigingen

**A. Woordniveau-correcties** (spelling, anglicismen, zinsstructuur, lidwoorden)

| # | Locatie | Origineel | Gecorrigeerd | Reden |
|:--|:--------|:----------|:-------------|:------|
| 1 | Globale randvoorwaarden | "schrijf het niet from scratch" | "schrijf het niet vanaf nul" | Anglicisme |
| 2 | Task 1.3 | "gerichte, doelgerichte read van de volledige epub" | "gerichte, doelgerichte lezing van de volledige epub" | Anglicisme |
| 3 | Task 1.3 | "het auteursrechtelijk beschermde tekstboek" | "het auteursrechtelijk beschermde studieboek" | Anglicisme (calque van "textbook") |
| 4 | Task 1.4 | "de gecorrigeerde chapter-tags" (2×) | "de gecorrigeerde hoofdstuktags" (2×) | Anglicisme |
| 5 | Task 1.6 | "op elke week-landingspagina — het huidige thema gemarkeerd, exact zoals..." | "op elke week-landingspagina, waarbij het huidige thema wordt gemarkeerd, exact zoals..." | Zinsstructuur (elliptische bijzin zonder werkwoord hersteld tot volledige bijzin) |
| 6 | Test Gate Task 1 | "lint-page.mjs`'s patroon" | "lint-page.mjs`' patroon" | Spelling (genitief van een op s-klank eindigend woord neemt in het Nederlands alleen een apostrof, geen extra -s) |
| 7 | Test Gate Task 1 | "alle 55 [[wikilinks]] ... resolven naar" | "... resolveren naar" | Spelling (onvervoegbare stam "resolven" bestaat niet; correcte infinitief is "resolveren") |
| 8 | Task 2.9 | "een team-lakehouse's OKF-bundle-inhoud" | "een team-lakehouses OKF-bundle-inhoud" | Spelling (Nederlandse genitief van een gewoon zelfstandig naamwoord gebruikt geen Engelse apostrof-s) |
| 9 | Task 3.7 | "deze devomgeving heeft geen" | "deze dev-omgeving heeft geen" | Spelling (samenstelling met Engels leenwoord vereist koppelteken) |
| 10 | Task 4.1 | "een throwaway smoke-workflow" | "een tijdelijke smoke-workflow" | Anglicisme |
| 11 | Main Task 11 (introtekst) | "is laat toegevoegd" | "is later toegevoegd" | Spelling (tikfout) |
| 12 | Test Gate Task 12 | "6 aanvankelijk gemiste stale weekverwijzingen" | "... verouderde weekverwijzingen" | Anglicisme |
| 13 | Task 13.5 | "kan eerder interleaven dan" | "kan eerder verweven worden dan" | Anglicisme |
| 14 | Task 16.1 | "geen nieuw datamodel nodig ... — default `False` zodat elk" | "... , met `False` als standaardwaarde zodat elk" | Anglicisme ("default" als bijvoeglijk gebruikt) |
| 15 | Task 17 (bestandenlijst) | "read-only query — niet instructor-only" | "read-only query, dus niet instructor-only" | Zinsstructuur (ontbrekend verband tussen twee bijstellingen verduidelijkt) |
| 16 | Task 19.1 | "aanbeveling: GoatCounter — bevestig bij kickoff of dit de definitieve keuze blijft" | "aanbeveling: GoatCounter, te bevestigen bij kickoff of dit de definitieve keuze blijft" | Zinsstructuur (grammaticaal onvolledige infinitiefconstructie na een dubbele punt) |
| 17 | Slotzin (Traceerbaarheid) | "de FR/NFR/AC-nummers die hij dekt" | "... die ze dekt" | Zinsstructuur (antecedent-congruentie: "main task"/"taak" is een de-woord, vereist "ze", niet "hij") |
| 18 | Kop Main Task 5 | "Volledige cyclus — alle vier gates live + teamfrontend" | "Volledige cyclus (alle vier gates live + team-frontend)" | Speciaal teken + Spelling (em-dash in kop vervangen; "teamfrontend" krijgt koppelteken als samenstelling) |
| 19 | Task 5.2 | "het team-facing scherm" | "het teamgerichte scherm" | Anglicisme |
| 20 | Task 5.5 | "Breid het evalset uit" | "Breid de evalset uit" | Lidwoord (elders in het document consequent "de evalset"; hier stond het inconsistente "het") |

**Aantal woordniveau-correcties:** 20 (excl. de losse lidwoord-/koppen-fix die in rij 18 is meegeteld)

**B. Speciale tekens — em-dash-verwijdering (sectie E/I.2)**

Het originele document bevatte 359 em-dashes (—), doorgaans gebruikt als zinsscheidingsteken in een stijl die kenmerkend is voor AI-gegenereerde/geredigeerde tekst ("em-dash-manie", sectie I.2). Dit is **stelselmatig gecorrigeerd**: elke em-dash-als-zinsscheider is vervangen door een komma, dubbele punt, punt (zinssplitsing) of haakjes, afhankelijk van wat de zin nodig had. Normale koppeltekens in samenstellingen (bv. "AI-systeem", "4D-diagram") en getallenreeksen met een en-dash (bv. "FR-01–FR-24", "13:00–14:30") zijn ongemoeid gelaten — die zijn geen zinsscheidingstekens maar correcte typografische bereik-notatie.

Resultaat: van 359 em-dashes zijn er **351 vervangen**; 8 blijven bewust staan (zie hieronder). Het en-dash-gebruik (39 gevallen) bleek in dit document uitsluitend correcte bereik-notatie (getallen-/taakreeksen, tijden) en is volledig ongewijzigd gebleven.

Overzicht van het aantal em-dash-correcties per sectie:

| Sectie | Em-dashes vóór | Representatief voorbeeld (vóór → na) |
|:--|:--|:--|
| Intro/Doel/Architectuur/Tech stack/Scope-uitbreiding | 8 | "...admin-onderdeel en studentdossier — precies zoals..." → "...admin-onderdeel en studentdossier, precies zoals..." |
| Globale randvoorwaarden | 6 | "...niet in elke task herhaald — een subtask..." → "...niet in elke task herhaald; een subtask..." |
| Parallelisatie-overzicht (tabel) | 15 | "Ja — twee onafhankelijke subagents..." → "Ja: twee onafhankelijke subagents..." |
| Main Task 0 | 8 | "### Test Gate — Task 0" → "### Test Gate: Task 0" |
| Main Task 1 | 16 | "Zet de bedrijfscase-bibliotheek op in `wiki/sources/` — begin met..." → "..., begin met..." |
| Main Task 2 | 21 | "...kolomnamen exact zoals in het TDD" (dash vóór bijzin verwijderd, komma) |
| Main Task 3 | 24 | "...**geen LLM-call**." (dash vóór toelichting → dubbele punt) |
| Main Task 4 | 20 | "...die niemand de tijd had — nu gecombineerd..." (voorbeeld uit context, komma/splitsing) |
| Main Task 5 | 23 | zie rij 18/19 hierboven |
| Main Task 6 | 5 | (nog open subtaken, korte teksten) |
| Main Task 7 | 4 | (nog open subtaken, korte teksten) |
| Main Task 8 | 14 | "...vier deterministische tools... — similariteitscheck gebruikt..." → "..., een punt gevolgd door: De similariteitscheck gebruikt..." |
| Main Task 9 | 18 | "...een voornaam met een spatie wordt geweigerd — niet slechts een UI-conventie" → ", niet slechts een UI-conventie" |
| Main Task 10 | 18 | "...dezelfde toegangsscheiding als `rubric_scores` — geen teamgericht kanaal..." → "...`rubric_scores`: geen teamgericht kanaal..." |
| Main Task 11 | 33 | "...op de letterlijke mockup-pixelwaarden — 52×40-doos..." → "..., 52×40-doos..." |
| Main Task 12 | 17 | kop + "...een 'vorm'-kolom... — planning + lichte in-sessie tools..." → "...: planning + lichte in-sessie tools..." |
| Main Task 13 | 12 | "...kan eerder interleaven... — als aanbeveling, geen harde eis" → "..., als aanbeveling, geen harde eis" |
| Main Task 14 | 13 | "...bevestigd zowel in de UI-tabel... — en in `action_log`" → "..., en in `action_log`" |
| Main Task 15 | 5 | (nog open subtaken, korte teksten) |
| Main Task 16 | 13 | "...geen nieuw datamodel nodig — Eén nieuw boolean-veld..." → "...nodig. Eén nieuw boolean-veld..." |
| Main Task 17 | 5 | (nog open subtaken, korte teksten) |
| Main Task 18 | 5 | (nog open subtaken, korte teksten) |
| Main Task 19 | 22 | "...toont ontbrekende rollup-data `—`..." (letterlijke UI-weergave, bewust ongewijzigd — zie hieronder) |
| Main Task 20 | 4 | (nog open subtaken, korte teksten) |
| Voortgangsoverzicht | 30 | "Main Task 8 — Wiki Quality Check Agent ✅ ..." → "Main Task 8: Wiki Quality Check Agent ✅ ..." |
| **Totaal** | **359** | **351 gecorrigeerd, 8 bewust ongewijzigd** |

**De 8 bewust ongewijzigde em-dashes** zijn geen zinsscheidingstekens maar:
- letterlijke, geciteerde titel-/label-strings uit het systeem zelf (bv. de titel `"Checkpoint 1 — Direct"`, de mockup-tekst `"Geen cijfer hier — alleen open of dicht"`, de server-tekst `"Geen cijfer zichtbaar hier — alleen open/dicht."`) — deze citeren exacte UI-/datawaarden, geen auteursproza, en zijn behandeld als citaten (onaangeroerd, conform de regel dat citaten ongewijzigd blijven);
- een standaalone `—` in een tabelcel die "niet van toepassing" betekent (`| direct | — (eenmalig, blokkeert alles) |`), een gangbare typografische conventie voor een lege/n.v.t.-cel, geen zinsscheiding;
- twee gevallen waarin de tekst rapporteert dat de UI zelf letterlijk een `—`-teken toont aan de gebruiker (bv. "team-09 toont eerlijk `—`") — ook dit is een geciteerde weergavewaarde, geen redactionele tekst.

**Aantal speciale-teken-correcties:** 351

**Totaal aantal taalwijzigingen: 371** (20 woordniveau-correcties + 351 em-dash-correcties)
**Oordeel:** Substantiële correcties, overwegend van mechanische/typografische aard (em-dash-manie, een herkenbaar AI-slop-patroon volgens sectie I.2 van de procedure). De inhoudelijke woordniveau-correcties zijn beperkt in aantal maar verspreid door het hele document; geen enkele wijziging raakt een claim, cijfer, testresultaat of technische bewering.

Geen enkele wijziging is aangebracht in checkbox-status, taaknummers, FR-/NFR-/AC-codes, Deel-verwijzingen, of in de inhoud van code-referenties (bestandsnamen, paden, commando's, commit-hashes).

### Structuuranalyse (advies)

Dit document is geen betogende publicatie (LinkedIn-artikel, column, opiniestuk) maar een technische takenlijst/voortgangsrapportage met een vaste, verplichte structuur (checkbox → taak → ✅-verslag → Test Gate → Commit & push, herhaald per Main Task). Het **Pyramid Principle/SCQA-kader is daarom grotendeels niet van toepassing**: er is geen governing thought die het document als geheel probeert over te brengen, geen opbouw van ondersteunende argumenten, en geen lezer die overtuigd moet worden van een standpunt. Elke Main Task-sectie is in essentie een chronologisch logboek van wat is gedaan en waarom, niet een argumentatieve structuur.

**SCQA-opening:** niet van toepassing. Het document opent met een korte, functionele contextzin ("Doel", "Architectuur", "Tech stack") die direct feitelijk is, geen retorische opbouw kent en dat ook niet hoeft te kennen voor dit documenttype.

**Governing thought en supporting arguments:** niet van toepassing in de klassieke zin. Voor zover er een impliciete "governing thought" per Main Task is, is dat de taakomschrijving zelf (bv. "Main Task 11: HAN Huisstijl-ontwerpsysteem toepassen"), en de subtaken zijn geen argumenten maar uitvoeringsstappen. Dit is een passende vorm voor een buildplan en behoeft geen aanpassing.

**Horizontale en verticale logica:** de subtaken binnen een Main Task zijn overwegend chronologisch/causaal geordend (schema's eerst, dan schrijfhelpers, dan tests, dan demo) en dat patroon is consistent door het hele document — een vorm van verticale logica die hier wél passend is, ook al is het geen Minto-piramide.

**Holle conclusies / gebrek aan nuance (I.3):** geen aandachtspunten. Elke ✅-afronding citeert een concreet testresultaat, commit-hash of waarneming; er zijn geen samenvattende slotalinea's die alleen herhalen zonder nieuwe informatie. Waar iets niet is afgerond of een compromis is gemaakt (bv. Task 8's TF-IDF-placeholder in plaats van embeddings, Task 9's `PENDING_WIKI_INTEGRATION`), wordt dat expliciet en specifiek benoemd, niet weggepoetst.

**Losse observatie (niet taalkundig, niet gecorrigeerd):** bij het samenvoegen van de fragmenten is een inhoudelijke inconsistentie opgevallen tussen het "Voortgangsoverzicht" (de samenvattende bullet-lijst onderaan het document) en de hoofdsecties. Main Task 14 ("Sessie- & planningslaag") en Main Task 16 ("Onboarding-flow") zijn in hun eigen sectie volledig afgevinkt (`- [x] Vink af: Main Task 14/16 afgerond`, met datum en commit-verwijzing), maar staan in het Voortgangsoverzicht nog als `- [ ]` (open). Main Task 19 daarentegen is op beide plekken correct `[x]`. Dit is een data-integriteitskwestie in de takenlijst zelf, geen taalfout, en is dan ook **niet aangepast** — checkbox-status blijft in deze redactie onder alle omstandigheden onaangeroerd. De auteur/orkestrerende agent kan dit desgewenst apart bijwerken.

**Structureel oordeel:** past bij het documenttype; het Pyramid Principle-kader is voor een technische takenlijst met vaste sjabloonstructuur grotendeels niet van toepassing. Geen structurele aandachtspunten die aanpassing behoeven.
