# Geef de docent geen tijd terug, maar een beter gesprek

*Deel 2 van twee. [Deel 1](artikel-1-criteria-nl.md) ging over wat een opleiding moet vastleggen voordat AI iets zinnigs kan bouwen. Dit deel gaat over wat het de docent oplevert.*

De pitch voor AI in het onderwijs is bijna altijd tijdwinst. Nakijken gaat sneller, toetsen maken gaat sneller, feedback komt eerder terug.

Dat is de zwakste versie van het argument, en de zaal wantrouwt hem terecht. Want tijdwinst op nakijken maakt het eindgesprek met een student geen millimeter beter. Je komt met dezelfde vragen aan tafel als vorig jaar, alleen eerder op de dag. En docenten voelen feilloos aan wat er onder die belofte ligt: als het werk zo routineus is dat een machine het overneemt, hoe lang duurt het dan voordat iemand vraagt of de docent er nog bij moet.

Wat zou AI dan wél moeten opleveren?

Iets wat je zonder die AI niet had gekund. Niet hetzelfde gesprek, sneller, maar een ander gesprek: met vragen die je anders niet had gesteld, omdat je niet wist dat ze er lagen. De winst hoort cognitief te zijn, niet administratief.

De schermen hieronder komen uit een module die ik dit jaar heb herbouwd. Studenten werken er in teams, leveren per fase een checkpoint in, en dat werk gaat langs twee poorten voordat de volgende fase opengaat: een Socratische AI-tutor en een peer-partnerteam. Wat de docent daarvan te zien krijgt, is waar dit stuk over gaat. Drie dingen, en ze staan los van elkaar.

## De docent houdt het laatste woord, en moet zich verantwoorden

De eerste vraag die elke docent bij een AI-poort stelt: wie beslist er nu eigenlijk?

![](figures/fig-04-dashboard.png)

**Figuur 4.** (1) Ook dit scherm staat in demo-toestand en zegt dat er zelf bij. Wat eronder ligt is wel gebouwd: de route bestaat, en met een echte klas geeft hij echte cijfers terug. (2) "Verborgen score": het cijfer dat de student nergens ziet en de docent wel. Niet omdat het per ongeluk zo uitpakte, maar omdat het rapport aan het team structureel geen veld heeft waar een score in past. (3) De docent kan de poort van de AI overrulen. De server legt elke override vast in een auditspoor, en weigert er een zonder opgegeven reden: een override die niemand later kan uitleggen is precies wat een student er wel over zou vragen.

De docent beslist. Hij kan de poort openzetten die de tutor dicht hield. Maar niet stilletjes, en niet zonder reden.

Dat de override een verplichte toelichting vergt, is geen nette gedachte achteraf. Het staat in de eisen, dus weigert de server een override zonder. En hier wordt het aardig: de knop erboven bereikt die server op dit moment niet eens door een fout in de koppeling. De regel geldt dus al voordat de functie werkt. Zo'n volgorde krijg je alleen als iemand het eerst heeft opgeschreven; bouw je andersom, dan is er tegen de tijd dat het scherm er staat niemand meer die een reden heeft om die weigering toe te voegen.

Let ook op de tweede aanwijzing. Het cijfer bestaat wel, en de docent ziet het, maar het team niet. Dat is geen instelling die iemand per ongeluk zo heeft gelaten: het rapport dat naar het team gaat heeft domweg geen veld waar een score in past. Een cijfer kan er niet in terechtkomen, ook niet als een model dat zou willen.

## De docent krijgt geen oordeel, maar bewijs

Voor het eindassessment zou je een samenvatting met een aanbeveling verwachten. "Dit team scoort zwak op procesanalyse, let daarop." Dat is precies wat dit systeem niet levert.

![](figures/fig-05-dossier.png)

**Figuur 5.** (1) Het scherm staat hier in zijn demo-toestand en zegt dat er zelf bij: het start met vastgelegde voorbeelddata en laadt pas echte gegevens na een handeling. De data is dus een voorbeeld. De regel eronder niet. (2) "Geen cijfer, oordeel of aanbeveling. Dit overzicht wijst de docent ergens op; het oordeelt niet. Elk punt hierboven toont zijn bron zichtbaar; een punt zonder geldige bron wordt door de tool zelf al geweigerd." Dat is geen disclaimer achteraf: de server schrapt een punt zonder geldige bronverwijzing daadwerkelijk, voordat het scherm het te zien krijgt. (3) Elke vraagsuggestie draagt een klikbare bronverwijzing naar de gebeurtenis in de tijdlijn waar hij uit volgt. De docent kan dus altijd terug naar het bewijs.

Wat de docent krijgt is een informatiepakket: de vragen die de tutor stelde, en aandachtspunten die elk terugwijzen naar de gebeurtenis waar ze uit volgen. Hij kan dus altijd doorklikken naar het moment zelf.

Dat verschil is groter dan het lijkt. Een samenvatting met een oordeel neemt het denkwerk over en levert een docent op die het oordeel van een model komt bevestigen. Een pakket met bronnen doet het omgekeerde: het wijst je op dingen die je zelf niet had teruggevonden, en laat de conclusie waar hij hoort. Het gesprek wordt niet korter. Het wordt scherper.

En weer die weigering: een punt zonder geldige bron haalt het scherm niet eens. Dezelfde beweging als bij de override, op een heel ander onderdeel, om dezelfde reden.

## De tijd die vrijkomt gaat terug in het materiaal

De derde opbrengst is de enige die op tijdwinst lijkt, en hij werkt alleen als je die tijd ergens in stopt.

Wat mij betreft in actueel materiaal bovenop het boek: een casus van vorige maand, een cijfer uit een sector die nu beweegt. Toen ik aan deze module begon kon dat niet. De wiki was bewust alleen-lezen, het systeem las eruit en schreef er nooit in. Dat was een eis die ik zelf had opgeschreven, en hij zat me in de weg.

Dus heb ik hem herzien. Niet door het verbod te schrappen, maar door op te schrijven wat er dan wél moet gelden. Drie vraagniveaus in plaats van zes: begrijpen, analyseren, evalueren, met de reden erbij waarom de andere drie afvallen. Onthouden beantwoord je door omhoog te scrollen. Toepassen vraagt een procedure die dit materiaal niet levert. Creëren is wat het checkpoint zelf al eist. Verder: de vragen dragen hun niveau niet als etiket, want het werkwoord hoort dat te verraden. Nooit een oordeel. Nooit het antwoord. Altijd Nederlands, ook bij een Engelstalige video.

Daarna plakte ik een YouTube-link in een docentscherm en vinkte vijf hoofdstukken aan.

![](figures/fig-06-vragen.png)

**Figuur 6.** (1) "Leg uit hoe..." Begrijpen: kan de student navertellen wat de spreker beweert? (2) "Vergelijk... met de vier perspectieven uit dit hoofdstuk." Analyseren: hier ontmoet de video het boek. (3) "Beoordeel in hoeverre..." Evalueren: een oordeel vellen, en kunnen zeggen op welke gronden. De niveaus staan er niet bij; het werkwoord verraadt ze. Dat is precies wat de opdracht eiste.

Die pagina staat nu in de wiki, tussen de hoofdstukken waar hij bij hoort.

Twee dingen ontbreken er nog, en allebei bewust. Het systeem schrijft het bestand maar publiceert het niet: een wijziging doorvoeren in een andere repository vraagt een sleutel die deze dienst niet heeft, dus een mens drukt op de knop. En de docent kiest de video. Niemand leidt uit een tutorgesprek af dát er iets ontbreekt. Dat is de volgende stap, en hij is niet gezet.

Maar let op wat er niet is gebeurd. Ik heb de agent niet overgehaald. Ik heb geen formulering gevonden die het verbod omzeilde. Ik heb één criterium herzien en opgeschreven wat ervoor in de plaats komt, en toen bouwde hij het. Dat is dezelfde eigenschap die hem eerst liet weigeren.

## Wat een docent hieraan overhoudt

Drie dingen, die geen van alle over tijd gaan. Hij beslist nog steeds, maar moet zijn afwijking kunnen uitleggen. Hij krijgt bewijs in plaats van een oordeel, en gaat het eindgesprek in met vragen die hij zelf niet had gevonden. En het materiaal dat hij toevoegt komt terug bij de student, op de plek waar het volgens het boek hoort.

Dat is een andere belofte dan tijdwinst, en een eerlijkere. Een uur dat je terugkrijgt en meteen weer uitgeeft is geen winst. Een gesprek waarin je een vraag stelt die je vorig jaar niet had kunnen stellen, dat is er wel een.
