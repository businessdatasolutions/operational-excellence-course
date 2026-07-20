# Artikel-pijplijn

Twee delen, twee talen, één beeldset, herhaalbaar. Dit bestand is de bedieningshandleiding; `manifest.json` is de waarheid.

| Bestand | Figuren | Kern |
|:--|:--|:--|
| `artikel-1-criteria-{nl,en}.md` | 1, 2, 3 | wat een opleiding moet vastleggen |
| `artikel-2-docent-{nl,en}.md` | 4, 5, 6 | wat de docent eraan heeft |

Elke figuur draagt een `artikel`-veld in het manifest; `audit.py` controleert daarop. De oude versie in één stuk staat in `archief/`.

```sh
python3 audit.py     # figuren, legenda's, em-dashes, weesbestanden -- draai dit voor publicatie
```

## Draaien

```sh
pip install -r requirements.txt
python3 -m playwright install chromium
cp .env.example .env      # vul de twee capability-links in
set -a; . ./.env; set +a

python3 shoot.py                  # alle figuren   (browser + draaiende stack nodig)
python3 shoot.py fig-06-vragen    # alleen deze    (publieke wiki: stack niet nodig)
python3 annotate.py               # figures/*.png  (alleen Pillow)
```

Drie soorten bron in één manifest:

| Veld | Betekent |
|:--|:--|
| `path` + `rol: student\|docent` | lokale stack, ingelogd met een capability-link |
| `url` + `rol: publiek` | een externe site zonder inlog (de openbare wiki) |
| `clip_range: [selA, selB]` | snijdt van de bovenkant van A tot de onderkant van B |

`clip_range` bestaat omdat een markdown-pagina geen omhullend element per sectie heeft: koppen en lijsten staan plat naast elkaar, dus er is niets om op te clippen. Twee ankers beschrijven de sectie wel exact. `measure()` verlegt bij een uitsnede de oorsprong mee, anders wijzen alle callouts op zo'n figuur naar de verkeerde plek en valt dat pas op als je het beeld opent.

De stack draait op `:5273` (SPA) en `:8811` (team_api), niet op de Vite-defaults 5173/8801. Dat is de aparte Playwright-stack uit `~/Projects/oe-gate-system`, met geseede identiteiten (Nina, student; Marleen, docent). Publicatiescreenshots horen daar te komen en niet uit een omgeving met echte studenten.

## Waarom twee scripts

`shoot.py` heeft een browser en een draaiende stack nodig. `annotate.py` heeft niets nodig en draait in een seconde. Gesplitst betekent dat: een callout bijstellen kost geen herschot, en een herschot na een UI-wijziging gooit de annotaties niet weg. Wie ze samenvoegt, betaalt dat elke iteratie terug.

## Waarom de callout-tekst niet in de PNG zit

`annotate.py` tekent genummerde badges en kaders, geen tekst. De tekst staat in `manifest.json` onder `legend.nl` en `legend.en` en gaat als legenda onder de figuur het artikel in. Tekst in pixels is niet te vertalen zonder opnieuw te renderen, niet te doorzoeken en onzichtbaar voor een schermlezer. Zo draagt één beeldset beide talen: alleen de legenda verschilt.

## Waarom callouts selectors zijn en geen coördinaten

Een callout wijst een CSS-selector aan, niet een positie. `shoot.py` meet de omhullende rechthoek op in de levende DOM en schrijft hem naast de PNG in `<id>.boxes.json`; `annotate.py` leest dat. Handgetikte coördinaten zijn niet alleen monnikenwerk, ze verlopen ook stil: verschuift de UI een blok, dan wijst het getal naar het verkeerde element zonder dat iets faalt. Een selector wijst na een herschot vanzelf weer het goede element aan, of hij knalt. Bij het bouwen wees `.source-ref-tag` inderdaad het verkeerde element aan, en de meting liet dat meteen zien.

## Valkuilen die geld hebben gekost

- **`ready` is nooit een `<h1>`.** Die rendert uit de route-params en staat er dus al terwijl de fetch nog loopt. Drie van de vijf eerste schoten waren `Laden…`. Gebruik een selector die de data zelf nodig heeft (`.wiki-item`, `.prep-point`, `.transparantie__table`).
- **Geen `networkidle`.** `CheckpointView` pollt elke 5 seconden zolang gate A op `assessing` staat, dus daar wordt het netwerk nooit stil.
- **Eén browsercontext per rol.** `sessionStorage` is per context en de app houdt bewust één credential per tab aan, ongeacht de rol (zie `auth.ts`). Twee rollen in één context overschrijven elkaars credential.
- **Het cohortveld staat standaard verkeerd.** Op `/instructor/quality-report` staat `2026-2027-oe` voorgevuld terwijl Marleen bij `S2Y26-27` hoort, dus zonder `fill` levert de klik een 403 op in plaats van een rapport. Zie het `actions`-blok.
- **De links horen niet in het manifest.** `manifest.json` gaat de git-geschiedenis in; een capability-link verleent volledige toegang als die persoon. Vandaar `.env` (gitignored) en `OE_LINK_STUDENT` / `OE_LINK_DOCENT`.

## Een artikel over een levend systeem veroudert terwijl je het schrijft

Twee dagen na het afronden van de tekst was er een video-pijplijn bijgekomen (`video_ingest` + `socratic_questions`), en daarmee was het artikel op één punt **aantoonbaar onwaar**: het beweerde dat het systeem nooit naar de wiki schrijft, terwijl `publish_draft` sindsdien een pagina van het type `video-bron` wegschrijft. Ook figuur 1 was verouderd: de wiki ging van 66 naar 70 pagina's en toont nu een gegenereerde videokaart.

Dat is geen incident, het is de normale toestand. Wat helpt:

- **Draai de figuur-audit opnieuw vóór publicatie**, niet alleen na het schrijven. Hij vangt geen verouderde inhoud, maar wel losgeraakte legenda's; hier ving hij dat ik het manifest had bijgewerkt en de artikelen niet.
- **Vergelijk de figuren met de vorige versie**, niet alleen met zichzelf. `fig-01` ging van 2912 naar 3436 px hoog; die 524 px waren de nieuwe inhoud. Een afmeting die verandert is het goedkoopste signaal dat er iets is bijgekomen.
- **Draai de feitencontrole opnieuw tegen de gewijzigde documentatie.** `git diff` op de blueprint wees hier binnen een minuut de hele wijziging aan.

Bij `fig-01-wiki` leverde dat een derde callout op (`.wiki-item:has-text('ToyotaGPT')`): de figuur toont nu in één beeld een boekhoofdstuk, een concept dat de docent toevoegde, en een pagina die het systeem zelf schreef. Precies het verschil dat argument 2 en argument 3 samen maken.

## Bevindingen voor oe-gate-system (niet opgelost, alleen gemeld)

Onderweg gevonden bij het schieten. Geen daarvan is voor dit artikel gerepareerd.

1. **`Dashboard.tsx:179` fetcht een kaal `/api/dashboard`**, niet via `adminApiBase()`, en stuurt geen `authHeaders()` mee. Dat pad gaat naar de SPA-server, die SPA-fallbackt naar `index.html` en 200 OK met HTML teruggeeft; `res.json()` klapt en het scherm valt terug op mock. Dit is exact de root-cause die in `StudentDossier.tsx::fetchExportPdf` uitvoerig staat gedocumenteerd en daar met `adminApiBase()` is opgelost. De route bestaat wel: `admin_api/server.py:773`. Met een geldige aanroep geeft hij echte data terug.
2. **`Dashboard.tsx::postOverride` post naar een kaal `/override`**, terwijl de route `POST /api/override` is (`admin_api/server.py:774`). De fallback doet "an optimistic local update only": de knop lijkt te werken en er wordt niets weggeschreven. `h_override` zelf is volledig geïmplementeerd, inclusief de weigering van een override zonder toelichting.
3. **De comments boven `fetchDashboard` en `postOverride` zijn verouderd.** Ze zeggen "No such endpoint is running yet (buildplan.md Task 4 explicitly does not require one)". Beide endpoints draaien inmiddels.
4. **`TutorHistory.tsx:50` hardcodeert `const teamId = 'team-07'`.** Dode constante: `team_api/server.py:270` leidt team en cohort af uit het credential en negeert de query. Geverifieerd, er lekt niets. Maar de code suggereert een lek dat er niet is.
5. **`/api/student-timeline` weigert team-01 voor Marleen** ("hoort niet bij een klas van deze docent"), terwijl `/api/teams?klas_id=BKA-C01` datzelfde team wél als haar klas teruggeeft. De twee scope-checks zijn het oneens.

## Herhaalbaarheid

`shoot.py && annotate.py` twee keer achter elkaar geeft **inhoudelijk** identieke bestanden, niet byte-identieke. Twee bekende bronnen van verschil, allebei onschuldig:

- **Rasterisatie.** Gemeten op `fig-05-dossier`: 2824 van 17.654.400 pixels (0,016%), maximale afwijking 61/255; bij drempel 8 blijven er 26 pixels over, allemaal op de gestreepte randen van de `.citation-link`-tags. Dat is de sub-pixelfase van een dashed border. Byte-identiteit eisen van een fontrasterizer is een verkeerde eis; controleer op inhoud.
- **Een tijdstempel.** `fig-04-dashboard` toont "gegenereerd op <datum, tijd>" en die verandert per run. Wie byte-stabiliteit wil, moet dat element maskeren; voor een artikel dat één keer gepubliceerd wordt is dat de moeite niet.

Ook gezien: **`shoot.py` is niet flake-vrij.** In één run haalde `.wiki-item` de wachttijd van 15 s niet. Opnieuw draaien loste het op. Als dit vaker gebeurt, is de wachttijd per figuur instelbaar maken de eerste stap, niet de selector veranderen.

## Workflow en parallellisme

```
FASE 0  outline + manifest.json vastzetten            [serieel; barrier]
             |
        +----+----------------+
        |                     |
   FASE 1A                 FASE 1B                    [>>> PARALLEL <<<]
   shoot.py + annotate.py  NL-draft schrijven
        |                     |
        +----+----------------+
             |
FASE 2  samenvoegen, dan twee controles               [barrier, dan PARALLEL]
        2A figuur/verwijzing-audit
        2B feitencontrole tegen de blueprint
             |
FASE 3  /taalredactie-publicatie artikel/artikel-nl.md   [serieel]
             |
FASE 3b auteur leest taalrapport en beslist              [menselijke poort]
             |
FASE 4  EN-vertaling + EN-legenda                        [serieel]
```

De echte fork is 1A naast 1B, en die werkt alleen omdat fase 0 de figuur-id's, bestandsnamen en legenda's vastlegt vóórdat er een regel geschreven of geschoten is. De schrijver zet `![](figures/fig-01-wiki.png)` neer terwijl het bestand nog niet bestaat.

Waarschuwing uit de praktijk: verandert het manifest ná de fork (hier verdween een figuur en verhuisde er een van argument 3 naar argument 2), dan moet het concept alsnog verzoend worden. De fork is dus zo betrouwbaar als het manifest waar hij op steunt. Reken op één verzoenronde in fase 2 zodra het schietspoor iets over de werkelijkheid leert dat het schrijfspoor nog niet wist.

Fase 3 en 4 zijn een keten: de EN-versie erft een geredigeerde NL-structuur, dus parallel vertalen betekent de taalredactie twee keer doen.

## Waarom het twee artikelen zijn (Minto)

Het stuk was één artikel van 2132 woorden met zes figuren. Getoetst aan Barbara Minto's Pyramid Principle vielen vijf dingen op, en twee daarvan waren structureel:

- **Er stond een "background"-sectie in**, de enige constructie die Minto met zoveel woorden verbiedt: een opsomming van *onderwerpen* (wiki, portaal, poorten, docentzone) op een ander abstractieniveau dan de argumenten eromheen. Die informatie is nu verdeeld over de plekken waar ze nodig is.
- **De opbouw was deductief**: symptoom, oorzaak, opbrengst, elk leunend op het vorige. Minto's waarschuwing daarbij is dat één weerlegd sleutelidee het hele bouwwerk meeneemt, en dat is hier twee keer gebeurd (de claim dat microtaken geen criteria vragen, en de claim dat het systeem nooit naar de wiki schrijft). Beide delen dragen nu drie **onafhankelijke** claims van dezelfde soort; weerleg er één en de rest staat nog.

Verder: argument 3 vatte zijn eigen inhoud niet meer samen (Minto's tweede groeperingsregel), de drie kopjes waren drie verschillende soorten idee (eerste regel), en 40 procent van de tekst plus vier van de zes figuren hing onder één kop.

## De figuur-audit (fase 2A)

Controleert dat elke figuur een verwijzing heeft, elke verwijzing een bestand, de nummering oploopt in leesvolgorde, elke legenda-regel letterlijk in de tekst staat en er geen weesbestanden zijn. Draai hem tegen beide talen: `legend.nl` tegen `artikel-nl.md`, `legend.en` tegen `artikel-en.md`. Hij ving in deze ronde een ontbrekende slotzin die met het oog niet opviel.

## De blinde vlek: elke controle hier is gesloten over het manifest

De grootste misser van deze ronde vond geen enkele geautomatiseerde stap. De sterkste pagina van het hele systeem, `/team/{team}/tutor` met echte Socratische output, stond niet in het manifest. Niet afgewogen en afgevallen: hij is er tijdens het plannen stilzwijgend uit gevallen, en daarna heeft de pijplijn braaf gedraaid op een onvolledige lijst.

Dat is structureel, geen slordigheid:

- de figuur-audit checkt of elke figuur in het manifest een verwijzing heeft, en kan niet weten wat er in het manifest hóórt te staan;
- de feitencontrole toetst de claims die in de tekst staan, en kan geen bewijs missen dat nergens genoemd wordt;
- de herhaalbaarheidscheck vergelijkt figuren met zichzelf.

Alle drie meten binnen de cirkel die fase 0 heeft getrokken. Er is geen check die de cirkel zelf betwist.

**Doe daarom vóór fase 0 een inventarisatie die niets overslaat.** Loop de routetabel af (`frontend/src/App.tsx`) en schiet élke route die een rol kan zien, kaal en zonder callouts. Kies daarna pas welke het manifest in gaan. Dat kost tien minuten en het is de enige stap die deze fout kan vangen. In deze ronde vond de auteur hem, door zelf de link te openen.

## De feitencontrole (fase 2B) is niet optioneel

Dit is de duurste les van deze ronde. Het eerste concept bevatte drie claims die het systeem capaciteiten toeschreven die het niet heeft, en de zwaarste daarvan droeg de slotalinea:

- *"De agent hangt dat in de wiki"* — geen enkele module schrijft naar de wiki. Alleen-lezen per NFR-02; `wiki_query/agent.py` "never write anything and never call an LLM". De ordening is handwerk van docenten.
- *"De docent volgt die conversatie mee"* — er is geen conversatie. `team_api/server.py:155`: "Het is geen chatbot." Eén inzending, één rapport.
- *"Met opgeschreven criteria wordt het ontwerp toetsbaar"* — niets in de codebase rekent dekking uit. Aspiratie, geen functie.

Geen daarvan was met het blote oog te zien; alle drie klonken plausibel en pasten in het betoog. Een artikel over een half afgebouwd systeem overclaimt vanzelf, want de auteur kent zijn bedoelingen beter dan zijn code. Laat de controle door een aparte agent doen, met opdracht om te weerleggen, en laat hem bestandspaden en regelnummers noemen.

Een tweede reden om hem te draaien: hij corrigeerde ook een fout in de *andere* richting. Het dossier bleek geen "API die nog niet live is" maar een scherm dat in demo-toestand mount (`useState(MOCK_TIMELINE)`) en pas na een handeling echte data laadt. De route bestaat en handhaaft autorisatie. Wie dat niet nakijkt, publiceert een verkeerde bewering over zijn eigen bouwstatus.

## Prompts

De prompts voor het NL-concept, de feitencontrole en de EN-vertaling staan in het plan bij dit artikel. Twee eisen die een ronde besparen:

- **Nederlands: geen em-dash en geen en-dash als zinsscheider.** `/taalredactie-publicatie` sectie E schrapt ze toch. In het Engels mogen ze wel; die regel is Nederlands.
- **Geen Oxford-komma in het Nederlands.** Dat was de meest terugkerende bevinding in het taalrapport, en een schrijfagent produceert hem standaard.
