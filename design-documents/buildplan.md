# Operational Excellence Gate-systeem — Build Plan

> **Voor uitvoerende agents:** dit document is de **enige bron van waarheid voor voortgang**. Vink een taakvakje (`- [ ]` → `- [x]`) pas af nadat de bijbehorende test gate daadwerkelijk is uitgevoerd en geslaagd — nooit vooruitlopend. Twee hookify-rules in `.claude/` herinneren je hieraan bij elke `git commit`/`git push` en bij elke stop: `hookify.require-tests-before-commit.local.md` en `hookify.check-test-gate-on-stop.local.md`.
>
> **Volgorde-regel:** een main task mag pas beginnen nadat de **vorige main task in dezelfde afhankelijkheidsketen** succesvol gecommit én gepusht is (zie "Parallelisatie-overzicht" hieronder voor welke tasks wél gelijktijdig mogen). Binnen één main task: subtasks in volgorde, geen enkele commit vóór de test gate van die main task geslaagd is.

**Doel:** de architectuur uit `tdd-operational-excellence.html` bouwen tot een werkend gate-systeem: Socratische AI-gate, peer-review-gate, review-ring, wiki-kwaliteitspunten, instructor-dashboard, admin-onderdeel en studentdossier — precies zoals gespecificeerd in de LRD (`lrd-operational-excellence.html`, FR-01–FR-24) en het TDD.

**Architectuur (samenvatting, zie TDD Deel 2 voor het volledige plaatje):** vier lagen — wiki/content (ongewijzigd, `wiki-template`), data (`small-medium-data-lake`-patroon, per-team/ring/klas lakehouses), agentic services (Google ADK 2.0, `adk2-blueprint`-patroon), frontend (React + Vite, net-new). Alle nieuwe code voor de laatste drie lagen leeft in een **nieuwe, aparte repository** — voorlopige naam `oe-gate-system` — naast (niet ín) deze documentatierepository. De wiki blijft in haar eigen `wiki-template`-fork, ongewijzigd (NFR-02).

**Tech stack:** Python 3.11+ (data-laag, agents — `google-adk[a2a,db,eval]~=2.0`, DuckDB/DuckLake, pytest), TypeScript/React + Vite (frontend), Quartz v4/Node (wiki, ongewijzigd), Cloud Run + managed Postgres (deployment, `europe-west4`).

## Globale randvoorwaarden (gelden voor élke main task)

Deze eisen zijn projectbreed en worden niet in elke task herhaald — een subtask die ze schendt is per definitie niet af:

- **Privacy (LRD Deel 1.3, TDD Deel 9):** uitsluitend `first_name` + `team_id` + `klas_id` + `cohort` als identifiers. Nooit een studentnummer, e-mailadres, achternaam of ander HAN-systeemveld in enig datamodel, log of API-response.
- **Never-invents-garanties (TDD Deel 4.4, 5.1, 5.3, 5.7, 5.8):** elke agent-tool die cijfers, duplicaat-oordelen, citatie-geldigheid of aandachtspunten produceert, doet dat op basis van deterministische data — nooit een ongestaafde LLM-claim. Waar het TDD een `source_ref`- of vergelijkbaar traceerbaarheidsveld eist, is dat een schema-eis, geen instructie die genegeerd kan worden.
- **OKF-conformantie (FR-11, NFR-07):** elk nieuw concept-type heeft verplicht `type` in de frontmatter en volgt `design-documents/SPEC.md` §9.
- **KISS (LRD Deel 5.1):** geen functionaliteit bouwen die niet direct aan een FR/NFR uit de LRD te koppelen is. Twijfel je? Citeer het FR/NFR-nummer in je subtask; kun je dat niet, bouw het niet.
- **Elke main task levert een mens-testbaar artefact op** (zie "Test Gate" per task) — niet alleen groene automatische tests. Een developer of de opdrachtgever moet het resultaat kunnen dráaien en met eigen ogen kunnen zien werken, vóórdat de task als afgerond geldt.
- **Blueprint-herkomst respecteren:** waar het TDD een component labelt als hergebruik van `wiki-template`/`small-medium-data-lake`/`adk2-blueprint`, begin je met dat blueprint kopiëren/forken — schrijf het niet from scratch.
- **Python: altijd een virtualenv, nooit globaal installeren.** Elk `pip install`-commando in dit plan is `.venv/bin/python -m pip install ...` (na `python3 -m venv .venv` in Task 0.6), nooit kaal `pip install` — dat installeert in de globale Python-omgeving en kan andere projecten op dezelfde machine breken (gebeurde tijdens het bouwen van Task 0 zelf; zie de les hieronder in Task 0.6).
- **Niet elke FR is een build-task:** FR-02 (kwaliteitscriteria-tekst), FR-12 (jaarlijkse Ingest-ronde), FR-16 (optionele KPI-laag) en FR-17 (DMAIC-capstoneformat), en NFR-06 (criteria wijzigen niet binnen een cohort) zijn content-/procesvereisten die docenten rechtstreeks in de wiki (Task 1) of het configuratiepad (Task 3.6) invullen — geen aparte software-subtask. Ze zijn hier expliciet benoemd zodat ze niet stilzwijgend verdwijnen, niet omdat ze genegeerd mogen worden.

---

## Parallelisatie-overzicht

Main tasks zijn genummerd in de volgorde van de kernketen (0→7). Tasks 8, 9 en 10 zijn **additief** (TDD Deel 13) en niet op het kritieke pad.

| Golf | Main tasks | Mag starten zodra | Kan als aparte subagent-opdracht |
|---|---|---|---|
| 1 | **Task 0** (scaffolding) | direct | — (eenmalig, blokkeert alles) |
| 2 | **Task 1** (wiki) + **Task 2** (data-laag) | Task 0 gepusht | Ja — twee onafhankelijke subagents, geen gedeelde bestanden |
| 3 | **Task 3** (Socratische tutor) + **Task 4** (Review-Ring + dashboard) + **Task 8** (Wiki Quality Check) + **Task 9** (admin) | Task 2 gepusht (Task 3 heeft ook Task 1 nodig) | Ja — vier onafhankelijke subagents; elk raakt een eigen submap (`agents/socratic_tutor/`, `agents/review_ring_coordinator/`, `agents/wiki_quality_check/`, `frontend/src/routes/admin/` + admin-API) |
| 4 | **Task 5** (volledige cyclus, integratie) | Task 3 én Task 4 gepusht | Nee — integratietaak, raakt bestanden van beide vorige tasks |
| 4b | **Task 10** (studentdossier) | Task 4 én Task 8 gepusht | Ja — parallel aan Task 5, eigen submap (`agents/dashboard_query/` uitbreiding + `frontend/src/routes/instructor/dossier/`) |
| 5 | **Task 6** (kalibratie) | Task 5 gepusht | Nee — vereist pilotdata uit Task 5 |
| 6 | **Task 7** (deployment hardening) | Task 6 gepusht (scaffolding uit 7.1–7.2 mag al eerder starten, parallel aan golf 3–5) | Deels — Dockerfile/CI-CD-scaffolding (7.1, 7.4) kan een aparte subagent zijn zodra Task 0 klaar is; de uiteindelijke smoke-test (7.6) niet |

**Vuistregel voor de orkestrerende agent:** als twee main tasks in dezelfde golf staan én geen gedeelde bestanden aanraken (zie de submap-hints), spawn ze als aparte subagents/teammates. Laat elke subagent zijn eigen main task volledig afsluiten (incl. test gate + commit + push) vóórdat de volgende golf begint.

---

## Main Task 0: Repository- en projectscaffolding

**Waarom eerst:** alle volgende tasks hebben een plek nodig om code neer te zetten. Zonder deze task is er geen "junior developer kan dit uitvoeren" mogelijk — er is nog geen repo.

**Bestanden:**
- Create (nieuwe repo `oe-gate-system`): `README.md`, `.gitignore`, `data/`, `agents/`, `frontend/`, `infra/` (lege mappen met `.gitkeep`)

- [x] **0.1** Maak een nieuwe, lege GitHub-repository `oe-gate-system` aan. ✅ Aangemaakt onder `businessdatasolutions` (privé), zelfde org als de documentatierepository: https://github.com/businessdatasolutions/oe-gate-system
- [x] **0.2** Maak de mapstructuur aan: `data/smdl/`, `data/tests/`, `agents/shared/`, `agents/tests/`, `frontend/src/`, `frontend/tests/`, `infra/`.
- [x] **0.3** Schrijf `README.md` met: doel van de repo, link naar `lrd-operational-excellence.html` en `tdd-operational-excellence.html` in de documentatierepository, en de mapstructuur hierboven met één zin uitleg per map.
- [x] **0.4** Schrijf `.gitignore` voor Python (`__pycache__/`, `.venv/`, `*.pyc`) én Node (`node_modules/`, `dist/`) — beide lagen leven in dezelfde repo.
- [x] **0.5** Voeg een minimale `data/smdl/__init__.py` en `agents/shared/__init__.py` toe zodat de package-structuur importeerbaar is.
- [x] **0.6** Voeg een `pyproject.toml` toe met de kernafhankelijkheden: `duckdb`, `pydantic`, `google-adk[a2a,db,eval]~=2.0`, `pytest`, `pytest-asyncio`. Maak daarna **eerst** een virtualenv (`python3 -m venv .venv`) vóór je iets installeert — `pip install` zonder venv installeert in de globale Python-omgeving en kan andere projecten op dezelfde machine breken. ⚠️ **Dit gebeurde daadwerkelijk tijdens het bouwen van deze task**: een kale `pip install -e .` upgradede/downgradede globale pakketten (`openai`, `fastapi`, `pydantic`, `cryptography`, `opentelemetry-*`, e.a.). Gecorrigeerd door alsnog een `.venv` aan te maken en daarin te herinstalleren; de globale pakketten zijn op verzoek van de opdrachtgever ongewijzigd gelaten (geen bekende afhankelijkheid van de oude versies). Zie de bijgewerkte, venv-verplichte instructie hierboven en in `README.md`.
- [x] **0.7** Voeg een minimale `frontend/package.json` toe (`npm create vite@latest . -- --template react-ts`) met React + Vite + TypeScript.

### Test Gate — Task 0
- **Automatisch:** ✅ `python3 -m venv .venv && .venv/bin/python -m pip install -e ".[dev]"` slaagde zonder fouten (pytest 9.1.1 geïnstalleerd, geïsoleerd); `cd frontend && npm install` slaagde zonder fouten (27 packages, 0 vulnerabilities).
- **Mens-testbaar artefact:** ✅ `npm run dev` gestart, `curl -I http://localhost:5173` gaf `HTTP/1.1 200 OK` — Vite-devserver draaide en serveerde de React-startpagina. Devserver na verificatie weer gestopt.

### Commit & push — Task 0
- [x] `git add -A && git commit -m "Scaffold oe-gate-system repo structure"` — commit `7947ad8`.
- [x] `git push origin main` — gepusht naar https://github.com/businessdatasolutions/oe-gate-system
- [x] **Main Task 0 afgerond** (12 juli 2026).

---

## Main Task 1: Wiki-content-laag operationeel

*(Kan parallel aan Task 2 — golf 2, aparte subagent, raakt geen bestanden uit Task 2.)*

**Bestanden:** een fork van `wiki-template` (aparte repo, blijft altijd apart van `oe-gate-system` — TDD Deel 3.1/10.1) — geen wijzigingen aan `oe-gate-system` in deze task.

- [ ] **1.1** Fork/clone `https://github.com/witoldtenhove/wiki-template` als de cursus-wiki-repo. Draai lokaal `npm install && npm run serve` en bevestig dat de bestaande demo-content rendert op `localhost:8080`.
- [x] **1.2** Zet de 19 boekconcept-pagina's (Ch1–Ch19) op in `wiki/concepts/`, elk met OKF-frontmatter: verplicht `type: boek-concept`, plus `stage` (direct|design|deliver|develop) en hoofdstuktag (`ch01`…`ch19`) per de mapping in LRD Deel 8 (ná de 10e-editie-correctie: Ch15=Operations improvement, Ch16=Lean operations, Ch5="The structure and scope of supply"). ✅ 19/19 pagina's aangemaakt (`wiki/concepts/ch01-*.md`..`ch19-*.md`); stage-mapping exact volgens LRD Deel 8 (Direct=Ch1–4, Design=Ch5–8, Deliver=Ch9–14, Develop=Ch15–19); Ch1 en Ch2 bevatten de verbatim "key questions" uit de 77-pp preview-PDF (Ch1 volledig gelezen, Ch2 t/m de flexibiliteitssectie), Ch3–19 gebaseerd op de LRD's eigen Deel-8-hoofdstukbeschrijving. Elke pagina citeert Slack, Brandon-Jones & Burgess (2022), 10e editie, met hoofdstuknummer.
- [x] **1.3** Zet de bedrijfscase-bibliotheek op in `wiki/sources/` — begin met de vijf in LRD Deel 1.1 genoemde voorbeelden (IKEA, Toyota, Ryanair, Michelin, Amazon) als concrete eerste batch, elk `type: bedrijfscase-bron`. ✅ Alle 5 aangemaakt, alle 5 **echte content, geen stubs**: de 77-pp preview-PDF bleek bij inspectie te stoppen medio Ch2 (voor de IKEA-case-study aan het eind van dat hoofdstuk), dus geen van de vijf company-boxen zat in de preview. Alle vijf zijn in plaats daarvan gevonden via een gerichte, doelgerichte read van de volledige epub (IKEA Ch2-case-study volledig; Toyota Ch16 + Ch4; Michelin Ch9; Ryanair Ch10; Amazon Ch13+Ch15+Ch16 — drie boxen). Elke pagina is een eigen samenvatting met korte, aangehaalde citaten (bewust geen bulk-verbatim-reproductie van het auteursrechtelijk beschermde tekstboek op een publiek GitHub Pages-adres), geciteerd naar exact hoofdstuk en boxtitel.
- [x] **1.4** Zet de 23 Lean-tool↔Industrie-4.0-referentiepagina's uit Gomaa (2025) Tabel VII op in `wiki/concepts/`, `type: concept`, getagd `[lean-tool, industrie4.0]` — gebruik de gecorrigeerde chapter-tags uit LRD Deel 6.2 (Kaizen→ch15, Kanban→ch16, beide `stage: develop`). ✅ 23/23 pagina's; Tabel VII (en de ondersteunende Tabel I) integraal gelezen uit de Gomaa-PDF (20 pagina's, volledig). Kaizen→ch15/develop en Kanban→ch16/develop bevestigd exact zoals gespecificeerd; de overige 21 chapter-tags zijn elk met een 1-zins-redenering op de pagina zelf onderbouwd (bv. Poka-Yoke→ch17 i.p.v. ch16 omdat het een conformance-tool is, Hoshin Kanri→ch03 omdat het strategie-implementatie is). **Bekende beperking, niet stilzwijgend weggelaten:** FR-14 noemt ook een losse "Lean 4.0-paradoxen"-pagina; die staat niet in de letterlijke tekst van deze subtaak (die alleen de 23 Tabel-VII-pagina's noemt) en is daarom niet gebouwd — open punt voor een vervolgtaak als volledige FR-14-dekking gewenst is.
- [x] **1.5** Zet de 19 vooraf geselecteerde AI-Wiki-contentmap-pagina's (FR-19) op, per de fase-mapping in LRD §8.1. ✅ 19/19 pagina's (`wiki/concepts/ai-wiki/`); fase-tags herleid uit LRD §8.1's eigen tabel (opgeteld: Direct 4 + Design 2 + Deliver 5 + Develop 8 = 19 ✓). Elke pagina citeert de echte query-trace (nu ook geacquireerd als raw-bron: `raw/reports/2026-07-11-operational-excellence-course-content-map-query-trace.md`) en is expliciet een pointer-/contentmap-pagina — geen gefabriceerde kopie van de externe, niet-publieke AI-Wiki's paginabodies.
- [x] **1.6** Bouw of hergebruik de bestaande Quartz-extensiecomponent voor het 4D "je-bent-hier"-diagram (FR-13) op elke week-landingspagina — het huidige thema gemarkeerd, exact zoals het cirkeldiagram in het bronboek. ✅ Nieuwe extensie `extensions/inject-stage-diagram.ts` gebouwd (transformer/htmlPlugin-patroon van `inject-confidence-badge.ts` — geen client-side JS, puur build-time uit frontmatter); structureel gemodelleerd naar Figure 1.13 uit het bronboek (vier stage-nodes rond een centrale "Operations management"-hub, cyclisch verbonden, huidige fase gemarkeerd + "je bent hier"-label), toegankelijk via `role="img"` + dynamische `<title>`. Gestileerd in `quartz/styles/custom.scss` (theme-reactieve CSS-variabelen, licht/donker-modus-bestendig). 4 week-landingspagina's (`wiki/weeks/{direct,design,deliver,develop}.md`) als scaffolding — bewust geen volledig 15-weekprogramma. Build-output geverifieerd: elke pagina markeert in de gerenderde HTML exact de eigen `stage`.
- [x] **1.7** Controleer dat `.github/workflows/deploy.yml` (al aanwezig in `wiki-template`) ongewijzigd werkt: push naar `main` bouwt en publiceert naar GitHub Pages. ✅ Workflow ongewijzigd gelaten (generiek `npx quartz build -d wiki` + `actions/deploy-pages`, geen repo-specifieke aannames die zouden breken). Wel gecorrigeerd: `quartz.config.ts`/`quartz.layout.ts` bevatten nog `wiki-template`-placeholders (`baseUrl: example.github.io/llm-wiki`, `pageTitle: "LLM Wiki"`, footer-GitHub-link) die de daadwerkelijke deploy naar het verkeerde adres zouden laten verwijzen — nu gezet op `businessdatasolutions.github.io/oe-wiki`.

### Test Gate — Task 1
- **Automatisch:** ✅ nieuw script `scripts/lint-wiki-batch.mjs` (hergebruikt `scripts/lint-page.mjs`'s patroon/rule-engine per pagina — roept het letterlijk aan via dezelfde stdin-payload als de PostToolUse-hook — plus een eigen OKF-§9-non-empty-`type`-check en recursieve walk) liep over alle 70 nieuwe pagina's uit 1.2–1.6: **0 OKF-fouten, 0 lint-page.mjs-waarschuwingen**. `npm run build`, `npm run check` (tsc --noEmit) en `npm test` (69 bestaande unit tests) slagen alle drie zonder fouten.
- **Mens-testbaar artefact:** ✅ `npm run serve` gestart op `localhost:8080`. Als uitvoerende agent zonder browser is dit geverifieerd via `curl` + directe HTML-inspectie (de dichtstbijzijnde controleerbare gelijkwaardige stap, zoals gevraagd): alle 4 week-landingspagina's (`weeks/{direct,design,deliver,develop}`) gaven `HTTP 200` met het 4D-diagram waarin exact de eigen `stage` de `stage-diagram-node--active`-klasse en het "je bent hier"-label draagt (de SVG's `<title>` bevestigt bv. "Huidige fase: Design" op `weeks/design`); 3 boekconcept-pagina's (Ch1, Ch9, Ch16) en 3 bedrijfscase-pagina's (IKEA, Toyota, Ryanair) gaven `HTTP 200` met de juiste `<title>` en `type`-tag in de gerenderde HTML (plus 2 bonus-steekproeven: een Lean-tool- en een AI-Wiki-contentmap-pagina); een niet-bestaande URL gaf correct `HTTP 404` (negatieve controle die bevestigt dat de 200's betekenisvol zijn); alle 55 `[[wikilinks]]` in de nieuwe pagina's resolven naar een bestaande pagina (0 broken links, apart geverifieerd). Exacte curl-commando's en resultaten staan in de commit-boodschap/PR-beschrijving zodat een mens dit met eigen ogen kan herhalen door `npm run serve` te draaien en dezelfde URL's in de browser te openen.

### Commit & push — Task 1
- [x] Commit met boodschap die refereert aan FR-11/FR-13/FR-14/FR-19. ✅ Commit `9c133dd` in `oe-wiki`: "Wiki-content-laag operationeel: boekconcepten, bedrijfscases, Lean-tool-referenties, AI-Wiki-contentmap, 4D-diagram (FR-11/FR-13/FR-14/FR-19)".
- [x] Push naar de wiki-repo's `main`. ✅ Gepusht naar https://github.com/businessdatasolutions/oe-wiki (`main`, `89ab0b4..9c133dd`).
- [x] Vink af: **Main Task 1 afgerond** (12 juli 2026).

---

## Main Task 2: Data-laag + OKF-bundelconventie per team

*(Kan parallel aan Task 1 — golf 2, aparte subagent.)*

**Bestanden (in `oe-gate-system`):**
- Modify: `data/smdl/storage.py`, `data/smdl/okf.py`, `data/smdl/ducklake.py`
- Create: `data/smdl/ingest_csv.py`, `data/tests/test_okf_concepts.py`, `data/tests/test_ducklake_tables.py`

- [x] **2.1** Kopieer `storage.py`, `okf.py`, `ducklake.py`, `query.py`, `ingest_excel.py`, `ingest_pdf.py`, `service.py` uit `small-medium-data-lake` naar `data/smdl/`. ✅ Alle zeven bestanden overgenomen als startpunt en aangepast: het generieke financiële/ontologie-specifieke deel van `query.py` (synoniemresolutie tegen `ontology.py`) en `service.py`/`ingest_excel.py`/`ingest_pdf.py` (XAF-ingester, financiële Table/Document/Entity-concepten) is vervangen door dit systeem's eigen `instructor-document`/`uploaded_tables`-patroon (TDD 4.7) — `ontology.py` en `ingest_xaf.py` bewust niet meegenomen (geen FR/NFR-koppeling, KISS).
- [x] **2.2** Pas `Lakehouse` in `storage.py` aan: vervang `client_id` door `team_id` + `cohort` (team-niveau), en voeg twee extra constructor-varianten toe voor ring-niveau (`ring_id` + `cohort`) en klas-niveau (`klas_id` + `cohort`) — drie soorten lakehouse-paden per TDD Deel 4.1/4.6: `lakehouse/<cohort>-team-<team_id>/`, `lakehouse/<cohort>-ring-<ring_id>/`, `lakehouse/<cohort>-klas-<klas_id>/`. ✅ Geïmplementeerd als `Lakehouse.for_team`/`for_ring`/`for_klas`, plus twee bonus-constructors `for_admin` (TDD 4.9, cohortbreed) en `for_system` (TDD 4.8, cohort-onafhankelijk, huisvest `action_log`) — alle vijf paden handmatig geverifieerd.
- [x] **2.3** Implementeer in `okf.py` de acht concept-schema's uit TDD Deel 7.1, elk als een `Concept`-subklasse of Pydantic-model met exact de velden uit het TDD: `checkpoint-submission`, `gate-pass-event`, `escrow-state`, `reviewring-assignment`, `klas-roster`, `instructor-document`, `wiki-quality-check`, `course-period`, `team-roster`, `assessment-schedule`. Kopieer de veldnamen letterlijk uit de YAML-voorbeelden in het TDD — geen eigen veldnamen verzinnen. Het `checkpoint-submission`-schema bevat verplicht een kritische-lens-sectie (FR-15) als onderdeel van hetzelfde antwoord, geen apart veld of aparte indiening. ✅ Alle **tien** concept-types (de lijst in deze subtask-tekst noemt er tien, ondanks "acht" hierboven) als Pydantic-modellen geïmplementeerd, veldnamen 1-op-1 uit de TDD-YAML overgenomen. `CheckpointSubmission.create()` vereist `kritische_lens` als verplicht keyword-argument — structureel onmogelijk een submission te bouwen zonder FR-15-antwoord.
- [x] **2.4** Implementeer in `ducklake.py` schrijfhelpers voor de zeven tabellen uit TDD Deel 7.2: `gate_events`, `rubric_scores`, `reviewring_log`, `override_log`, `uploaded_tables`, `action_log`, `wiki_quality_log` — kolomnamen exact zoals in het TDD. ✅ Alle zeven, elk met een Pydantic-rijmodel + `write_*`/`query_*`-paar; nieuwe `ducklake.append_rows()` (INSERT, niet de blueprint's REPLACE-`write_table`) zodat deze append-only logs elkaar niet overschrijven.
- [x] **2.5** Schrijf `data/smdl/ingest_csv.py`: een deterministische ingester naar het patroon van `ingest_excel.py` (TDD Deel 4.7) — CSV inlezen, output als DuckLake-tabel + `instructor-document`-concept. ✅ Geschreven en handmatig end-to-end getest (zie testverslag in de agent-rapportage).
- [x] **2.6** Voeg `.csv` toe aan de routeringstabel in `service.py` (naast de bestaande `EXCEL_EXTS`/`PDF_EXTS`). ✅ `CSV_EXTS = {".csv"}` toegevoegd naast `EXCEL_EXTS`/`PDF_EXTS`.
- [x] **2.7** Schrijf `data/tests/test_okf_concepts.py`: voor elk van de acht concept-types uit 2.3 een test die een instance aanmaakt, naar een tijdelijke lakehouse schrijft, terugleest, en velden vergelijkt. ✅ Alle tien concept-types + 3 aanvullende structurele tests (type-dispatch, non-empty-type-afdwinging) — 13 tests, allemaal geslaagd.
- [x] **2.8** Schrijf `data/tests/test_ducklake_tables.py`: voor elk van de zeven tabellen uit 2.4 een test die een rij schrijft en via een `SELECT`-query terugleest. ✅ Alle zeven tabellen + 3 aanvullende tests (append-only-gedrag, foutuitkomst, SUM-query over `wiki_quality_log`) — 10 tests, allemaal geslaagd.
- [x] **2.9** Schrijf een smoke-test-CLI-script `data/smdl/cli.py` met een `inspect <team_id>`-commando dat een team-lakehouse's OKF-bundle-inhoud en DuckLake-tabelrijen naar de terminal print (mens-leesbaar, geen JSON-dump). ✅ Geïmplementeerd en handmatig geverifieerd — zie Test Gate hieronder voor de daadwerkelijke output.
- [x] **2.10** Schrijf `agents/shared/action_log.py`: een herbruikbare decorator `@log_action(layer=...)` (NFR-08, TDD Deel 5.6) die elke functie waarop hij wordt toegepast omhult — bij succes een `action_log`-regel met `outcome=success`, bij een exception `outcome=error` + foutdetail, altijd met een `correlation_id` uit de aanroepende sessie/workflow-context. Elke volgende agent-task (3, 4, 8, 10) past deze decorator toe op zijn eigen tools — bouw hem hier één keer, generiek genoeg voor hergebruik. ✅ Werkt op zowel sync als async functies, genereert zelf een `correlation_id` indien niet meegegeven, geeft de oorspronkelijke exception altijd door (logt, slikt nooit in), en forwardt de reserved kwargs (`correlation_id`/`actor_type`/`actor_id`/`target_type`/`target_id`/`lakehouse`) nooit naar de gewrapte functie zodat elke bestaande functiesignatuur ermee te wrappen is — 6 eigen tests in `agents/tests/test_action_log.py` (niet vereist door de test gate hieronder, wel gedraaid en geslaagd).
- [x] **2.11** Implementeer in `service.py` de distributiescope-routering uit TDD Deel 4.6/4.7 (FR-20): een functie `route_instructor_document(scope: Literal["team","ring","klas"], scope_id, cohort, file) -> Lakehouse` die het juiste lakehouse-pad kiest op basis van `scope` (scope `"everyone"` wordt hier expliciet **niet** afgehandeld — dat pad gaat via Task 1's wiki-terugschrijfmechaniek, niet via de data-laag). ✅ Geïmplementeerd; `scope="everyone"` en een onbekende bestandsextensie geven allebei een expliciete `ValueError` met duidelijke boodschap — handmatig geverifieerd (zie agent-rapportage).

### Test Gate — Task 2
- **Automatisch:** ✅ `.venv/bin/python -m pytest data/tests/ -v` — **23/23 geslaagd** (alle tests uit 2.7/2.8; `pytest -v` over de hele repo, incl. de niet-verplichte `agents/tests/test_action_log.py`, geeft 29/29 geslaagd).
- **Mens-testbaar artefact:** ✅ `rm -rf lakehouse && .venv/bin/python -m smdl.demo_seed && .venv/bin/python -m smdl.cli inspect team-07` daadwerkelijk gedraaid. Output toont de teamnaam (`team-07`, cohort `2026-2027-oe`), het `checkpoint-submission`-concept (titel "Checkpoint 1 — Direct", stage/hoofdstuk, bedrijfscase Ryanair, teamleden, en een leesbare preview van het FR-15-kritische-lens-antwoord), het `gate-pass-event`-concept én de bijbehorende `gate_events`-DuckLake-rij, en een aparte "Gate status summary"-sectie (`direct Gate A: OPEN`) — mens-leesbaar, geen JSON-dump.

### Commit & push — Task 2
- [x] Commit met boodschap die refereert aan FR-01/FR-07/FR-09/FR-11/FR-20/FR-21/FR-22. Commit `c46301f`.
- [x] Push naar `oe-gate-system` `main`. ✅ Gepusht naar https://github.com/businessdatasolutions/oe-gate-system (`b201cd8..c46301f`).
- [x] Vink af: **Main Task 2 afgerond** (12 juli 2026).

---

## Main Task 3: Socratische Tutor Agent + evalharnas (alleen Gate 1)

*(Golf 3, parallel aan Task 4/8/9 — vereist Task 1 én Task 2 gepusht.)*

**Bestanden:**
- Create: `agents/socratic_tutor/agent.py`, `agents/shared/session.py`, `agents/socratic_tutor/socratic_tutor.evalset.json`, `agents/tests/test_socratic_tutor_component.py`

- [ ] **3.1** Kopieer `shared/models.py` en `shared/session.py` uit `adk2-blueprint` naar `agents/shared/`.
- [ ] **3.2** Scaffold `agents/socratic_tutor/agent.py` als `task`-modus `Agent` (patroon uit `adk2-blueprint/agents/collector/`).
- [ ] **3.3** Implementeer de tool `query_wiki(query: str) -> list[dict]` die de gepubliceerde wiki (Task 1) doorzoekt (hergebruik het `qmd`-hybride-zoekpatroon uit `wiki-template`, TDD Deel 5.1).
- [ ] **3.4** Implementeer de tool `read_team_history(team_id: str, stage: str) -> list[dict]` die alle eerdere `checkpoint-submission`-vervolgconcepten van dat team uit de data-laag (Task 2) leest.
- [ ] **3.5** Implementeer de tool `write_report(team_id, stage, team_transcript, instructor_report, rubric_score, gate_a_status)` die **twee gescheiden schrijfacties** doet: een teamgericht antwoord-schema zónder scoreveld, en een docentgericht schema mét `rubric_score` — exact de structurele scheiding uit TDD Deel 5.1/6.3. Schrijf een test die aantoont dat het teamgerichte schema geen `score`-attribuut heeft (structurele controle, niet alleen een lint-regel).
- [ ] **3.6** Schrijf de Socratische systeeminstructie (nooit een verdict, altijd voortbouwen op eerdere geschiedenis, FR-03) in een apart, module-eigenaar-only-schrijfbaar configuratiebestand `agents/socratic_tutor/prompts/system_instruction.md`.
- [ ] **3.7** Koppel `DatabaseSessionService` (uit `shared/session.py`) met één sessie per team-per-checkpoint.
- [ ] **3.8** Schrijf `agents/socratic_tutor/socratic_tutor.evalset.json` met minimaal vijf cases die controleren dat geen enkel teamgericht antwoord scoretaal bevat ("goed", "fout", een cijfer) — AC-03.
- [ ] **3.9** Schrijf `agents/tests/test_socratic_tutor_component.py`: een in-memory-`Runner`-test die een mock-checkpoint-inzending door de agent stuurt en controleert dat er precies één rapport per kanaal wordt geschreven.
- [ ] **3.10** Pas de `@log_action`-decorator uit Task 2.10 toe op `query_wiki`, `read_team_history` en `write_report` (NFR-08).

### Test Gate — Task 3
- **Automatisch:** `pytest agents/tests/test_socratic_tutor_component.py -v` slaagt; `pytest agents/socratic_tutor/ -m eval` (AgentEvaluator tegen het evalset) slaagt 100% op de never-scores-check (AC-03).
- **Mens-testbaar artefact:** start `adk web` lokaal, open de dev-UI in de browser, voer een mock-Direct-fase-checkpoint in, en bevestig met eigen ogen dat de tutor uitsluitend Socratische vragen terugstuurt — nooit "dat is goed" of een cijfer.

### Commit & push — Task 3
- [ ] Commit met boodschap die refereert aan FR-03/FR-10.
- [ ] Push naar `oe-gate-system` `main`.
- [ ] Vink af: **Main Task 3 afgerond**.

---

## Main Task 4: Review-Ring Coordinator + Instructor Dashboard

*(Golf 3, parallel aan Task 3/8/9 — vereist Task 2 gepusht.)*

**Bestanden:**
- Create: `agents/review_ring_coordinator/workflow.py`, `agents/dashboard_query/agent.py`, `frontend/src/routes/instructor/Dashboard.tsx`, `agents/tests/test_review_ring.py`

- [ ] **4.1** Scaffold `agents/review_ring_coordinator/workflow.py` als deterministische ADK `Workflow` (patroon uit `adk2-blueprint/agents/approval/`) — **geen LLM-call**.
- [ ] **4.2** Implementeer ringtoewijzing bij cohortstart: elk team krijgt een A→B→C→A-positie (FR-07), geschreven als `reviewring-assignment`-concept (Task 2).
- [ ] **4.3** Implementeer fallback-herconfiguratie (FR-08): een functie `reconfigure_ring(ring_id, departed_team_id)` die alleen de betrokken posities aanpast.
- [ ] **4.4** Implementeer de escrow-onthulling met het `RequestInput`/resume-patroon (FR-18): team A's zicht op ontvangen feedback blijft gepauzeerd tot het event "eigen review ingediend" binnenkomt.
- [ ] **4.5** Implementeer het `/check-lapses`-endpoint (FR-04): een los aan te roepen functie die `escrow-state`-concepten met een verstreken `lapse_deadline` (Task 2, 48u) detecteert en de "ontvangen"-voorwaarde laat vervallen.
- [ ] **4.6** Scaffold `agents/dashboard_query/agent.py`: de tool `query_dashboard(cohort)` die `gate_events`/`rubric_scores` aggregeert via DuckDB-SQL (nooit een LLM-samenvatting van getallen, TDD Deel 4.4).
- [ ] **4.7** Bouw `frontend/src/routes/instructor/Dashboard.tsx`: per-team statuskaart (fase, gate A/B-status), override-knop die naar een `POST /override`-endpoint schrijft dat een `gate-pass-event` met `actor: instructor` aanmaakt (FR-06) en in `override_log` landt.
- [ ] **4.8** Schrijf `agents/tests/test_review_ring.py`: tests voor ringtoewijzing, fallback-herconfiguratie, en dat escrow-onthulling pas plaatsvindt ná de eigen-review-submit-event.
- [ ] **4.9** Pas de `@log_action`-decorator uit Task 2.10 toe op de workflow-transities in `review_ring_coordinator/workflow.py` en op `query_dashboard` (NFR-08).

### Test Gate — Task 4
- **Automatisch:** `pytest agents/tests/test_review_ring.py -v` slaagt; een test bevestigt expliciet dat vroegtijdig lezen van andermans feedback vóór eigen inzending onmogelijk is (FR-18).
- **Mens-testbaar artefact:** `npm run dev` in `frontend/`, dashboard-route openen, en met gemockte data (uit Task 2's `demo_seed.py`, uit te breiden met 3 mock-teams) met de klok meelopen of een mens binnen 1 minuut de status van elk team kan beoordelen (NFR-03/AC-04) — noteer de gemeten tijd in de commit-boodschap.

### Commit & push — Task 4
- [ ] Commit met boodschap die refereert aan FR-04/FR-06/FR-07/FR-08/FR-18/NFR-03.
- [ ] Push naar `oe-gate-system` `main`.
- [ ] Vink af: **Main Task 4 afgerond**.

---

## Main Task 5: Volledige cyclus — alle vier gates live + teamfrontend

*(Golf 4 — integratietaak, niet parallelliseerbaar; vereist Task 3 én Task 4 gepusht.)*

**Bestanden:**
- Modify: `agents/socratic_tutor/agent.py` (verwijder Gate-1-only-restrictie), `agents/review_ring_coordinator/workflow.py`
- Create: `frontend/src/routes/team/CheckpointView.tsx`, `agents/tests/test_full_cycle_integration.py`

- [ ] **5.1** Verwijder elke Gate-1-only-restrictie uit Task 3; bevestig dat de agent voor alle vier D-fasen werkt met dezelfde tools.
- [ ] **5.2** Bouw `frontend/src/routes/team/CheckpointView.tsx`: het team-facing scherm — Socrates-chatkaart, Gate A/B-statuskaarten, peer-partnerkaart, footer zonder scoreveld (mapping uit TDD Deel 6.1).
- [ ] **5.3** Implementeer het server-side "geen cijfer zichtbaar"-contract (TDD Deel 6.3): het teamgerichte API-response-schema bevat structureel geen scoreveld — voeg een contract-test toe die faalt als iemand per ongeluk een scoreveld toevoegt aan dat schema.
- [ ] **5.4** Implementeer het binaire gate-signaal (FR-05): een functie `combine_gate_signal(gate_a_status, gate_b_status) -> Literal["open","dicht"]`, voor het team alleen zichtbaar als open/dicht.
- [ ] **5.5** Breid het evalset uit Task 3 uit met AC-05-cases (voortbouw-op-vorig-rapport-check voor gate 2–4).
- [ ] **5.6** Schrijf `agents/tests/test_full_cycle_integration.py`: één test die één mock-team door alle vier checkpoints stuurt (submit → Gate A → Gate B → volgende fase) en op elk punt de juiste status controleert.

### Test Gate — Task 5
- **Automatisch:** `pytest agents/tests/test_full_cycle_integration.py -v` slaagt; uitgebreide evalset (AC-05) slaagt.
- **Mens-testbaar artefact:** volledige handmatige doorloop door een mens: als team door één D-fase heen (checkpoint indienen → Socratische chat → peer-review simuleren → beide gates open zien gaan) in de draaiende frontend — geen enkele stap overgeslagen, geen cijfer zichtbaar op enig moment.

### Commit & push — Task 5
- [ ] Commit met boodschap die refereert aan FR-05/AC-03/AC-05.
- [ ] Push naar `oe-gate-system` `main`.
- [ ] Vink af: **Main Task 5 afgerond**.

---

## Main Task 6: Kalibratie

*(Golf 5 — vereist Task 5 gepusht en pilotdata.)*

**Bestanden:** Create: `data/calibration/report.md`, `data/calibration/threshold_analysis.py`

- [ ] **6.1** Schrijf `data/calibration/threshold_analysis.py`: leest pilot-cohort-data uit `rubric_scores`/`override_log`/`reviewring_log`, berekent AC-05/AC-07/AC-08-percentages.
- [ ] **6.2** Kalibreer de verborgen-rubriekdrempel op basis van de uitkomst; documenteer de gekozen waarde en de reden in `data/calibration/report.md`.
- [ ] **6.3** Kalibreer de embedding-similariteitsdrempel voor duplicaatdetectie (Task 8) op dezelfde manier, tegen AC-13.
- [ ] **6.4** Werk TDD Deel 14 en LRD Deel 12 bij (in de documentatierepository) met de definitieve, gekalibreerde waarden — dit vervangt de "nog te kalibreren"-vermeldingen.

### Test Gate — Task 6
- **Automatisch:** `threshold_analysis.py` draait zonder fouten en produceert reproduceerbare cijfers uit de pilotdata.
- **Mens-testbaar artefact:** `data/calibration/report.md` is leesbaar voor de module-eigenaar en bevat expliciete voor/na-drempelwaarden met onderbouwing — de docent kan het rapport lezen en de keuze beoordelen zonder de code te hoeven lezen.

### Commit & push — Task 6
- [ ] Commit (in beide repo's: `oe-gate-system` voor de code, documentatierepository voor de LRD/TDD-updates).
- [ ] Push beide.
- [ ] Vink af: **Main Task 6 afgerond**.

---

## Main Task 7: Deploymenthardening

*(7.1/7.4 mogen als scaffolding al vanaf golf 2 parallel starten; 7.6 pas ná Task 6.)*

**Bestanden:** Create: `infra/Dockerfile`, `infra/cloudrun.yaml`, `.github/workflows/deploy-gate-system.yml`

- [ ] **7.1** Schrijf `infra/Dockerfile`: multi-stage build voor de Python-agentic-/data-laag (mag parallel starten zodra Task 0 klaar is).
- [ ] **7.2** Configureer Cloud Run (regio `europe-west4`) met een gemount volume of GCS-object-storage-koppeling voor de DuckLake-bestanden (TDD Deel 10.2 — expliciet niet in de container zelf laten).
- [ ] **7.3** Configureer een managed Postgres-instantie (zelfde regio) voor `DatabaseSessionService`.
- [ ] **7.4** Schrijf `.github/workflows/deploy-gate-system.yml`: aparte workflow van de wiki-pijplijn, bouwt en deployt bij wijzigingen in `oe-gate-system` (mag parallel starten zodra Task 0 klaar is).
- [ ] **7.5** Bevestig dat Cloud Logging automatisch stdout/stderr van de container opvangt naast het eigen `action_log` (TDD Deel 10.6) — geen extra configuratie nodig, wel te verifiëren.
- [ ] **7.6** Draai een smoke-test tegen de gedeployde omgeving: health-check-endpoint + één volledige gate-cyclus (hergebruik het scenario uit Task 5's integratietest, nu tegen de live URL).

### Test Gate — Task 7
- **Automatisch:** CI/CD-pipeline is groen op een test-PR; smoke-test-script tegen de live URL slaagt.
- **Mens-testbaar artefact:** een mens bezoekt de gedeployde frontend-URL in een browser en doorloopt handmatig één checkpoint-indiening tegen de echte, gedeployde omgeving (niet lokaal).

### Commit & push — Task 7
- [ ] Commit met boodschap die refereert aan NFR-02/NFR-04/Deel 10.
- [ ] Push naar `oe-gate-system` `main`.
- [ ] Vink af: **Main Task 7 afgerond**.

---

## Main Task 8: Wiki Quality Check Agent (additief, parallelliseerbaar)

*(Golf 3, parallel aan Task 3/4/9 — vereist Task 2 gepusht.)*

**Bestanden:** Create: `agents/wiki_quality_check/agent.py`, `agents/wiki_quality_check/wiki_quality_check.evalset.json`, `agents/tests/test_wiki_quality_check.py`

- [x] **8.1** Implementeer de tool `extract_contribution(synthesis_text) -> ContributionCandidate` (LLM-stap, gestructureerde output: concepten/entiteiten/bronnen/relaties). ✅ Gemini-structured-output (`gemini-2.5-flash-lite`, `response_schema=ContributionCandidate`) wanneer `GEMINI_API_KEY`/`GOOGLE_API_KEY` beschikbaar is, anders een deterministische heuristische markdown-parser (zelfde graceful-degradation-vorm als `data/smdl/ingest_pdf.py`) — deze omgeving had geen API-key, dus de heuristische fallback is wat daadwerkelijk is uitgevoerd/getest.
- [x] **8.2** Implementeer de tool `check_duplicates(candidate) -> DuplicateResult` — deterministisch: exacte titelmatch + embedding-similariteit (Gemini text-embedding-model) tegen een instelbare drempel (placeholder-waarde, kalibratie volgt in Task 6). ✅ Exacte titelmatch (via `smdl.storage.slugify`) tegen de échte `oe-wiki/wiki/`-inhoud (66 pagina's gescand: 19 boekconcepten + 5 bedrijfscases + 23 Lean-tool-referenties + 19 AI-Wiki-pagina's). Similariteitscheck: Gemini `text-embedding-004` wanneer een API-key beschikbaar is (wél gebouwd, hier ongebruikt), anders een dependency-vrije TF-IDF/cosinus-fallback — **expliciet een placeholder, niet de definitieve aanpak** (TDD Deel 14): zowel de drempelwaarde (0,55) als de embeddingmodelkeuze wachten op kalibratie in Task 6/AC-13.
- [x] **8.3** Implementeer de tool `validate_citations(candidate) -> CitationResult` — deterministisch: elke bron moet auteur/jaar/titel/uitgever-of-URL bevatten (gestructureerde invoer, geen vrije-tekst-parsing). ✅ Werkt uitsluitend op de al-gestructureerde `SourceCandidate`-velden; ontbrekende bron → `missing_citation`, onvolledige bron → `invalid_citation`.
- [x] **8.4** Implementeer de tool `compute_points(candidate, duplicate_result, citation_result) -> PointsBreakdown` — 1 punt/concept, 1 punt/entiteit, 1 punt/bron, 0,5 punt/relatie (LRD 6.11); schrijft naar `wiki_quality_log` (Task 2), nooit een los bijgehouden totaal. ✅ `points_total` is een `@computed_field` (pydantic), afgeleid van de vier ruwe tellingen — structureel niet instelbaar/overschrijfbaar, exact consistent met TDD Deel 7.1's eigen uitgewerkte voorbeeld (tellingen 2+1+3+1 → totaal 6.5 klopt alleen als de 0,5-wegingsfactor bij het lezen wordt toegepast, niet in de opgeslagen telling zelf). Bonus-helper `query_team_points_total` herberekent het team-totaal altijd via een live SQL-`SUM`-query, nooit een gecachete teller.
- [x] **8.5** Koppel de agent-aanroep in de Synthesize-pijplijn: vlak vóór de git-commit die een teamcase publiceert (TDD Deel 3.6), ná gate A/B — geen invloed op gate-status. ✅ `run_quality_check()` in `agent.py` ketent de vier tools in de vaste volgorde als één aanroepbare eenheid, met een docstring die exact documenteert waar de (nog niet gebouwde) Review-Ring Coordinator dit zou aanroepen — vlak vóór de `wiki/syntheses/`-git-commit, ná gate A/B, zonder invloed op gate-status.
- [x] **8.6** Schrijf `agents/wiki_quality_check/wiki_quality_check.evalset.json` met cases voor: exact duplicaat (afwijzen), inhoudelijk duplicaat (afwijzen), ontbrekende bronvermelding (afwijzen), volledig geldige bijdrage (accepteren + correcte puntentelling). ✅ Alle vier cases aanwezig (inhoudelijk-duplicaat-case is een zwaar geparafraseerde, deels verbatim-overlappende versie van de echte Toyota-pagina, scoort 0,61 tegen de 0,55-drempel). Primair geverifieerd via een deterministisch testharnas (geen live modelaanroep nodig — consistent met de never-invents-eis); een aparte `@pytest.mark.eval`-test speelt hetzelfde bestand af via de echte `AgentEvaluator` en skipt netjes zonder API-key.
- [x] **8.7** Pas de `@log_action`-decorator uit Task 2.10 toe op alle vier tools uit 8.1–8.4 (NFR-08). ✅ Toegepast en functioneel geverifieerd (niet alleen `__wrapped__`-aanwezigheid): elke tool-aanroep schrijft een `action_log`-regel, en één volledige pijplijn-run deelt één `correlation_id` over alle vier de stappen (TDD 4.8/5.6).

### Test Gate — Task 8
- **Automatisch:** ✅ `.venv/bin/python -m pytest agents/tests/test_wiki_quality_check.py -v` — **33/33 geslaagd, 1 geskipt** (de live-`AgentEvaluator`-test, correct geskipt zonder `GEMINI_API_KEY`/`GOOGLE_API_KEY`). Volledige repo-testsuite: 126 geslaagd, 1 geskipt.
- **Mens-testbaar artefact:** ✅ `agents/wiki_quality_check/demo_submit.py` daadwerkelijk drie keer gedraaid met drie verschillende testbijdragen: `--scenario exact-duplicate` (hergebruikt de titel "Toyota", exact zoals in `wiki/sources/toyota.md`) → **REJECTED / reject_reason=duplicate / 0 punten**; `--scenario missing-citation` → **REJECTED / reject_reason=missing_citation / 0 punten**; `--scenario valid` → **ACCEPTED / 5,5 punten** (2 concepten + 1 entiteit + 2 bronnen + 1 relatie×0,5) — alle drie de afwijzingsredenen/puntentotalen kloppend in de daadwerkelijke terminal-output gecontroleerd.

### Commit & push — Task 8
- [x] Commit met boodschap die refereert aan FR-21/AC-13. Commit `e9ba394`.
- [x] Push naar `oe-gate-system` `main`. ✅ Gepusht naar https://github.com/businessdatasolutions/oe-gate-system (`c46301f..e9ba394`).
- [x] Vink af: **Main Task 8 afgerond** (12 juli 2026).

---

## Main Task 9: Admin-onderdeel voor cursusvoorbereiding (additief, parallelliseerbaar)

*(Golf 3, parallel aan Task 3/4/8 — vereist Task 2 gepusht.)*

**Bestanden:** Create: `agents/admin_api/routes.py`, `frontend/src/routes/admin/CoursePeriod.tsx`, `frontend/src/routes/admin/Teams.tsx`, `frontend/src/routes/admin/Assessments.tsx`, `frontend/src/routes/admin/DocumentUpload.tsx`, `agents/tests/test_admin_crud.py`

- [ ] **9.1** Implementeer CRUD-endpoints voor `course-period` (TDD Deel 4.9/7.1): create/read/update in het cohort-brede admin-lakehouse.
- [ ] **9.2** Implementeer CRUD-endpoints voor `team-roster`: teams aanmaken/wijzigen/verwijderen, studenten (voornamen) koppelen/ontkoppelen.
- [ ] **9.3** Implementeer CRUD-endpoints voor `assessment-schedule`: datum/tijdslot/locatie/docent per CBI.
- [ ] **9.4** Koppel `team-roster`-wijzigingen aan het bestaande fallback-mechanisme uit Task 4.3 (een teamwissel ná cohortstart wordt behandeld als ring-uitval, geen apart pad).
- [ ] **9.5** Bouw de drie admin-frontendschermen (`CoursePeriod.tsx`, `Teams.tsx`, `Assessments.tsx`) — pure formulieren, geen agent-aanroep.
- [ ] **9.6** Schrijf `agents/tests/test_admin_crud.py`: create/read/update/delete-tests voor alle drie de concept-types.
- [ ] **9.7** Implementeer het upload-endpoint voor instructeur-documenten (FR-20, TDD Deel 6.4): accepteert PDF/Excel/CSV + een scope-keuze (team/ring/klas/iedereen), roept bij team/ring/klas de routering uit Task 2.11 aan; bij scope "iedereen" commit het endpoint het geconverteerde bestand naar de wiki-repo (Task 1) via een git-commit, niet via de data-laag.
- [ ] **9.8** Bouw `frontend/src/routes/admin/DocumentUpload.tsx`: bestandskiezer + scope-selector; toont vóór bevestiging expliciet welke teams het zullen zien, met een aparte, zwaardere bevestigingsstap bij scope "iedereen" (LRD 6.10, onomkeerbaar publiek).
- [ ] **9.9** Pas de `@log_action`-decorator uit Task 2.10 toe op de admin-CRUD-endpoints en het upload-endpoint (NFR-08).

### Test Gate — Task 9
- **Automatisch:** `pytest agents/tests/test_admin_crud.py -v` slaagt.
- **Mens-testbaar artefact:** een mens doorloopt handmatig in de draaiende admin-UI: een cohortperiode instellen, een team aanmaken met twee voornamen, één assessment plannen met datum/tijdslot/locatie, én één testdocument uploaden met scope "team" — en ziet alle vier correct terug ná een refresh (dus daadwerkelijk persistent weggeschreven, niet alleen in front-end state); bij een tweede upload met scope "iedereen" verschijnt de aparte, zwaardere bevestigingsstap (9.8) daadwerkelijk in de UI.

### Commit & push — Task 9
- [ ] Commit met boodschap die refereert aan FR-20/FR-22/NFR-08.
- [ ] Push naar `oe-gate-system` `main`.
- [ ] Vink af: **Main Task 9 afgerond**.

---

## Main Task 10: Studentdossier + AI-CBI-voorbereiding (additief, parallelliseerbaar)

*(Golf 4b, parallel aan Task 5 — vereist Task 4 én Task 8 gepusht.)*

**Bestanden:** Create: `agents/dashboard_query/prep_agent.py` (uitbreiding van Task 4.6's agent), `frontend/src/routes/instructor/StudentDossier.tsx`, `agents/tests/test_assessment_prep.py`

- [ ] **10.1** Implementeer de tool `build_student_timeline(first_name, team_id) -> list[TimelineEvent]` — deterministisch: query's over `gate_events`, `wiki_quality_log`, `reviewring_log`, gesorteerd op tijdstempel, met gebruik van DuckLake's snapshot-tijdreizen (TDD Deel 4.3).
- [ ] **10.2** Implementeer de tool `generate_prep_summary(timeline) -> list[PrepPoint]` — LLM-stap; elk `PrepPoint` heeft een **verplicht** `source_ref`-veld (bv. `gate_events#<id>`). Een `PrepPoint` zonder geldig `source_ref` wordt binnen de tool zelf weggefilterd vóórdat het wordt teruggegeven — schema-afdwinging, geen instructie.
- [ ] **10.3** Bouw `frontend/src/routes/instructor/StudentDossier.tsx`: tijdlijnweergave + voorbereidingsoverzicht, elk `PrepPoint` toont zijn `source_ref` als klikbare/zichtbare referentie (NFR-10 moet zichtbaar zijn, niet alleen intern aanwezig).
- [ ] **10.4** Bevestig instructor-only-toegang: dezelfde toegangsscheiding als `rubric_scores` — geen teamgericht kanaal geeft ooit toegang tot dit dossier.
- [ ] **10.5** Schrijf `agents/dashboard_query/prep_agent.evalset.json`: elke gegenereerde `PrepPoint` in de evalset-cases moet een geldig `source_ref` hebben, anders faalt de test (AC-14).
- [ ] **10.6** Schrijf `agents/tests/test_assessment_prep.py`: test dat een `PrepPoint` zonder `source_ref` nooit de tool-output bereikt.
- [ ] **10.7** Implementeer `export_student_history(first_name, team_id) -> bytes` (FR-09): rendert de volledige tijdlijn uit 10.1 (gate-geschiedenis, iteraties, feedback) naar PDF of doc, ten behoeve van het criterion-based interview (LRD Deel 9) — hergebruikt de append-only `log.md`/tijdlijndata, geen apart bijgehouden exportformaat.
- [ ] **10.8** Pas de `@log_action`-decorator uit Task 2.10 toe op `build_student_timeline`, `generate_prep_summary` en `export_student_history` (NFR-08).

### Test Gate — Task 10
- **Automatisch:** `pytest agents/tests/test_assessment_prep.py -v` slaagt; evalset slaagt 100% op source_ref-aanwezigheid (AC-14).
- **Mens-testbaar artefact:** een docent (of een mens die de docentrol test) opent het dossier voor één mock-student met een gevulde gate-geschiedenis, leest het gegenereerde voorbereidingsoverzicht, en controleert handmatig dat elke aandachtspunt/vraagsuggestie daadwerkelijk klopt met het brondatapunt waarnaar `source_ref` verwijst.

### Commit & push — Task 10
- [ ] Commit met boodschap die refereert aan FR-09/FR-23/FR-24/NFR-08/NFR-10/AC-14.
- [ ] Push naar `oe-gate-system` `main`.
- [ ] Vink af: **Main Task 10 afgerond**.

---

## Voortgangsoverzicht (samenvatting — werk bovenstaande secties bij, dit is alleen een snelle scan)

- [x] Main Task 0 — Repository- en projectscaffolding ✅ https://github.com/businessdatasolutions/oe-gate-system
- [x] Main Task 1 — Wiki-content-laag operationeel ✅ 70 pagina's (19 boekconcepten + 5 bedrijfscases + 23 Lean-tool-referenties + 19 AI-Wiki-contentmap-pagina's + 4 week-landingspagina's) + 4D-diagramextensie, 0 OKF-lintfouten, commit `9c133dd`
- [x] Main Task 2 — Data-laag + OKF-bundelconventie ✅ tien OKF-concepttypes + zeven DuckLake-tabellen + team/ring/klas/admin/system-lakehouses, commit `c46301f`
- [ ] Main Task 3 — Socratische Tutor Agent (Gate 1)
- [ ] Main Task 4 — Review-Ring Coordinator + Instructor Dashboard
- [ ] Main Task 5 — Volledige cyclus, alle vier gates
- [ ] Main Task 6 — Kalibratie
- [ ] Main Task 7 — Deploymenthardening
- [x] Main Task 8 — Wiki Quality Check Agent ✅ vier deterministische tools (extract/check_duplicates/validate_citations/compute_points) + evalset (4 cases, deterministisch geverifieerd) + `demo_submit.py` (3 scenario's handmatig gedraaid) — similariteitscheck gebruikt een TF-IDF-placeholder (embedding-pad wél gebouwd, ongebruikt zonder API-key), kalibratie volgt in Task 6/AC-13, commit `e9ba394`
- [ ] Main Task 9 — Admin-onderdeel
- [ ] Main Task 10 — Studentdossier + AI-CBI-voorbereiding

**Traceerbaarheid:** elke main task citeert de FR/NFR/AC-nummers die hij dekt (zie de commit-boodschap-eisen per task). Voor de volledige matrix, zie TDD Deel 8.
