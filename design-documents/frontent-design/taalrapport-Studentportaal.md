## Redactierapport — Studentportaal.dc.html

**Datum redactie:** 2026-07-13

### Toelichting op de aanpak

Dit is een interactieve HTML-mockup met uitsluitend korte Nederlandse UI-labels en microcopy (geen doorlopende tekst): navigatielabels, week-/faseoverzicht, wiki-kaarten, tutor-rapporten en de review-ring-stappen. Er is alleen tekst tussen HTML-tags en in de databronnen van het script (`PHASES`/`WEEKS`/`WIKI_PAGES`/`REPORTS`/`RING_*`) gecorrigeerd; geen enkele CSS-regel, class-naam of componentlogica is aangeraakt.

### Taalwijzigingen

| # | Locatie | Origineel | Gecorrigeerd | Reden |
|:--|:--------|:----------|:-------------|:------|
| 1 | Tutor-tab, vaste notitie boven elk rapport | "Alleen Socratische vragen — nooit een score of verdict zichtbaar voor het team." | "Alleen Socratische vragen: nooit een score of verdict zichtbaar voor het team." | Speciaal teken — em-dash vervangen door dubbele punt (regel E) |
| 2 | Tutor-tab, lege status "nog niet ingediend" | "Nog niet ingediend — dien het checkpoint in om een rapport te ontvangen." | "Nog niet ingediend: dien het checkpoint in om een rapport te ontvangen." | Speciaal teken — em-dash vervangen door dubbele punt |
| 3 | Review-ring, escrow-toelichting | "...zodra jullie zelf feedback aan Team 8 hebben ingediend — wachten op andermans review levert dus niets op." | "...zodra jullie zelf feedback aan Team 8 hebben ingediend. Wachten op andermans review levert dus niets op." | Speciaal teken — em-dash vervangen door zinssplitsing (twee zelfstandige beweringen) |
| 4–7 | `PHASES`-data, `gateNote` per fase (Direct/Design/Deliver/Develop) | "Gate 1 — gehaald in week 4" (en analoog voor Gate 2/3/4) | "Gate 1: gehaald in week 4" (en analoog) | Speciaal teken — em-dash als label-toelichting vervangen door dubbele punt (4 locaties) |
| 8–23 | `WEEKS`-data, weektitels ("ChN — Titel") en gate-notities per checkpointweek | "Ch1 — Operations als functie" (en analoog voor Ch2 t/m Ch18/19, plus de vier "Gate N — checkpoint deze week"-notities) | "Ch1: Operations als functie" (en analoog) | Speciaal teken — em-dash tussen hoofdstuknummer en titel vervangen door dubbele punt (16 locaties) |
| 24 | Programma-tab, documentenlijst | "Teamcase-pagina — FlinkFiets (wiki)" | "Teamcase-pagina: FlinkFiets (wiki)" | Speciaal teken — em-dash vervangen door dubbele punt |
| 25 | Programma-tab, documentenlijst | "Lean 4.0-koppelingen — Tabel VII.pdf" | "Lean 4.0-koppelingen: Tabel VII.pdf" | Speciaal teken — em-dash vervangen door dubbele punt |
| 26–30 | `WIKI_PAGES`-data, paginatitels | "Ch10 — Voorraadbeheer", "Ch9 — Supply chain design", "IKEA — Supply chain als netwerk", "Toyota — Lean & JIT-voorraad", "FlinkFiets Bezorgdienst — teampagina" | "Ch10: Voorraadbeheer", "Ch9: Supply chain design", "IKEA: supply chain als netwerk", "Toyota: Lean & JIT-voorraad", "FlinkFiets Bezorgdienst: teampagina" | Speciaal teken — em-dash vervangen door dubbele punt (5 locaties) |
| 31 | `REPORTS`-data, Gate 1-vraag | "...kernprioriteit — wat zou een klant zeggen die net een beschadigd pakket ontving?" | "...kernprioriteit. Wat zou een klant zeggen die net een beschadigd pakket ontving?" | Speciaal teken — em-dash vervangen door zinssplitsing |
| 32 | `REPORTS`-data, Gate 2-vraag | "...routeclusters — wat gebeurt daarmee op een dag met drie keer de normale vraag?" | "...routeclusters. Wat gebeurt daarmee op een dag met drie keer de normale vraag?" | Speciaal teken — em-dash vervangen door zinssplitsing |
| 33 | `RING_RECEIVED`-data, vervalvenster-notitie | "Nog niet binnen. Vervalvenster sluit over 18 uur — daarna vervalt deze voorwaarde automatisch." | "Nog niet binnen. Vervalvenster sluit over 18 uur. Daarna vervalt deze voorwaarde automatisch." | Speciaal teken — em-dash vervangen door zinssplitsing |

**Aantal wijzigingen:** 33 (over 20 tabelregels, waarvan meerdere regels een repeterend patroon over meerdere data-items samenvatten)
**Oordeel:** Kleine correcties

### Toegepaste afwegingen (geen wijziging, ter informatie)

- **En-dashes in weekbereiken** ("Week 1–4", "Week 5–8" enz.): correct gebruik van het aaneengesloten streepje voor een cijferbereik, geen zinsscheidend gedachtestreepje — niet gewijzigd.
- **Ampersands in titels en beschrijvingen** ("Product- & dienstinnovatie", "Supply chain & Human-CPS", "Toyota — Lean & JIT-voorraad" na correctie "Toyota: Lean & JIT-voorraad", "Strategie & positionering"): niet gewijzigd. Het `&`-teken staat op een standaard QWERTY-toetsenbord en is geen doelwit van regel E; het bestand gebruikt "&" en "en" bewust naast elkaar op verschillende plekken (bijvoorbeeld wél "en" in doorlopende zinnen als "netwerk, lay-out en procestechnologie", maar "&" in korte titels), en dat bestaande patroon is hier niet aangepast om geen inhoudelijke stijlkeuze van de auteur over te nemen.
- **"checkpoint", "gate", "escrow", "dashboard"**: gangbare vaktermen/cursusjargon in deze context (operations management, de eigen gate-terminologie van dit systeem), blijven staan conform de anglicisme-regel (D).
- **"OE-Wiki", "AI-tutor", "Review-ring"**: eigennamen van de navigatietabs binnen dit systeem, ongewijzigd.
- **Dubbele haakjes in "(EOQ, (R,Q)- en periodieke systemen)"**: correcte geneste notatie voor de vaknaam "(R,Q)-systeem", geen fout.

### Structuuranalyse (advies)

Sectie J (SCQA/Pyramid Principle) is hier **niet van toepassing**. Het bestand bevat geen doorlopend betoog maar uitsluitend korte UI-microcopy verspreid over vier tabs (Programma, OE-Wiki, Socratische AI-tutor, Review-ring): navigatielabels, statuspillen, korte toelichtingen en losse tutor-vragen. Er is geen governing thought, geen opbouw van argumenten en geen SCQA-structuur te analyseren binnen een interface-mockup van dit type. Deze constatering vervangt hier de structuuranalyse.

**Structureel oordeel:** Niet van toepassing (korte UI-microcopy, geen doorlopend betoog).
