# Een agent bouwt alleen wat je hebt opgeschreven

Elke hoegschool, academie en opleiding experimenteert inmiddels met AI. Er zijn pilots, er zijn werkgroepen, er is een kaderdocument, er zijn docenten die op zaterdagochtend iets in elkaar zetten wat maandag in de les kan.

Alleen: kijk naar wat eruit komt. Een generator die meerkeuzevragen maakt bij een hoofdstuk. Een simulatie die ergens verloren, zonder verdere context in het LMS is geplaatst. Een demo-appje dat het goed doet op een studiemiddag en daarna nooit meer opstart. De toets gaat sneller de deur uit, maar de kwaliteit en vorm van toetsing blijft hetzelfde. Twee jaar experimenteren, en de onderwijskwaliteit is geen millimeter opgeschoven.

Wat ontbreekt er?

Niet de techniek, en ook niet de bereidheid. Wat ontbreekt, zijn de ontwerpcriteria: gedocumenteerd en machineleesbaar. Een AI-agent kan alleen bouwen wat expliciet is vastgelegd. Vaak hebben opleidingen nooit opgeschreven wat goed onderwijs is.

## Microtaken zijn geen strategie, maar een symptoom

Ik heb inmiddels genoeg van die opbrengsten gezien om een patroon te herkennen. MC-toetsgeneratoren, stand-alone simulaties, chatbots die de studiegids kunnen citeren. Ze hebben iets gemeen dat zelden benoemd wordt: het zijn precies de taken die geen ontwerpcriteria nodig hebben.

Om een meerkeuzevraag te genereren hoef je niet te weten waarom dit concept in week 3 staat en niet in week 7. Je hoeft niet te weten welk misverstand studenten hier standaard hebben, of welke voorkennis de vraag veronderstelt, of hoe het antwoord samenhangt met wat er in het eindassessment gebeurt. Je hebt een stuk tekst nodig en een vraagvorm. Meer niet.

En dat is geen toeval. Het is de enige soort taak die een agent zonder criteria kan doen. Wie geen criteria aanlevert, krijgt onvermijdelijk het soort werk terug dat zonder criteria kan. De microtaak is dus geen bescheiden eerste stap op weg naar iets groters. Het is waar je onvermijdelijk op uitkomt als je stap één hebt overgeslagen. Dat verklaart ook waarom opschalen niet werkt: honderd microtaken naast elkaar zijn nog steeds honderd microtaken. De ontbrekende schakel schaalt niet mee, want hij is er niet.

Voor de duidelijkheid: die generator is niet slecht. Hij doet wat hij belooft. Alleen belooft hij niets over onderwijskwaliteit, en we behandelen hem alsof hij dat wel doet.

## Ontwerpcriteria zijn het werk, en het studieboek is er een bron van

Hier komt de wending die ik in de meeste AI-gesprekken in het onderwijs mis. We doen alsof ontwerpcriteria nog geschreven moeten worden, en alsof dat een academisch project van drie jaar is. Terwijl een deel ervan al op je bureau ligt.

Een goed studieboek is geschreven door iemand die drie dingen weet. Wat er relevant is binnen een kennisgebied en wat niet. Hoe de onderdelen samenhangen. En in welke volgorde je ze bestudeert, zodat het tweede begrip op het eerste kan rusten. Sla de inhoudsopgave open: dat is volgorde plus samenhang, en dat zijn ontwerpcriteria. Daar komt de rest bovenop. De didactische aanwijzingen bij een hoofdstuk. De voorbeeldcasussen, gekozen omdat ze een specifiek onderscheid scherp maken. De discussievragen achterin, die vaak preciezer zijn opgeschreven dan de leerdoelen in onze eigen modulehandleiding.

Wie het boek wegzet als een dure contentdrager maakt dezelfde fout als wie een demo-appje laat bouwen. Beiden gooien weg wat expliciet was en houden alleen de tekst over. Het boek is niet duur vanwege het papier. Het is duur vanwege de ordening, en juist die ordening is het enige wat een agent kan lezen.

Voordat ik verder ga, iets wat je moet weten om de rest te kunnen wegen. Het systeem dat je hierna ziet is niet door een ontwikkelteam gebouwd. Het is ontworpen en geschreven door een AI-coding-agent. Mijn werk was de aansturing: eerst een Learner Requirement Document, het onderwijskundig ontwerp, voordat er één regel code bestond. Daarna leverde ik achtergrondmateriaal, ideeën en correcties, en hakte ik knopen door waar dat document zweeg. De agent bouwde wat erin stond. Dat is geen anekdote bij dit artikel. Het is het bewijs eronder.

En kort wat je dan voor je krijgt, want ik ga er straks losse schermen uit lichten. Het systeem heeft vier delen. Een **wiki** met de kennisbasis, geordend naar de hoofdstukken van het boek. Een **studentportaal** waar teams per fase een checkpoint indienen. **Twee poorten** bij elk checkpoint: een Socratische AI-tutor en een peer-partnerteam. En een **docentzone** met een dashboard, een studentdossier en een kwaliteitsrapport.

Ze hangen aan één ding samen. Alles wat er gebeurt wordt als gebeurtenis weggeschreven: een team levert in, de tutor leest en stelt vragen, de poort gaat open of blijft dicht, het partnerteam doet hetzelfde. Staan beide poorten open, dan komt de volgende fase vrij. De docent ziet diezelfde gebeurtenissen terug, samengevat op het dashboard en uitgeschreven in het dossier. De wiki bepaalt intussen wat een team op dit moment te lezen krijgt. Vier fasen, acht poorten (vier voor de tutor, vier voor de partnerteams), één spoor van feiten eronder.

Bij ons is dat geen metafoor gebleven. De kennisbasis waar de studenten mee werken is niet thematisch geordend door iets wat zelf een indeling verzon. Hij volgt de hoofdstukken van het boek en toont wat past bij waar het team op dat moment staat.

![](figures/fig-01-wiki.png)

**Figuur 1.** (1) De wiki is geordend naar de hoofdstukken van het studieboek, getagd als boekconcept. Die nummering is de volgorde die de auteur koos, en het systeem neemt hem over in plaats van hem opnieuw te bedenken. (2) Het systeem filtert die pagina's op waar het team nu staat: het eigen checkpoint en de eigen fase. Ernaast staat een toegevoegd concept, zonder hoofdstuknummer: het boek levert de structuur, de docent vult aan.

Zodra je die criteria uitschrijft in een vorm die een machine kan lezen, gebeurt er iets wat de microtaak nooit oplevert. In ons systeem bepaalt één JSON-bestand welk model welke rol vervult, en diezelfde regel is de tekst die de student op het scherm leest. Niet twee bronnen die uit elkaar kunnen lopen: één bron, twee lezers.

![](figures/fig-02-transparantie.png)

**Figuur 2.** (1) Eén JSON-bestand bepaalt welk model welke rol vervult. Diezelfde regel is hier de tekst die de student leest. (2) "Deze lijst is geen momentopname die iemand handmatig bijhoudt: het is exact de configuratie waarmee het systeem draait. Verandert er een model, dan verandert deze tabel mee, anders start het systeem niet."

Dat principe geldt breder dan compliance. Als je opschrijft dat kwaliteit op meerdere momenten in de leerroute ontstaat en niet op één eindmoment, dan is dat geen visiepraat meer. Dan zijn het vier poorten, elk op hun eigen moment, die een agent kan bemensen.

En dan is er de vraag die je pas kunt stellen als de criteria zijn opgeschreven. Niet alleen de uitvoering wordt toetsbaar, maar het ontwerp zelf. Dekken de checkpoints de concepten die het boek als kern aanmerkt? Zit er een concept in week 6 dat nergens in een opdracht terugkomt? Dat is geen vraag over studenten. Dat is een vraag over mij.

Mijn systeem rekent dat overigens niet voor me uit. Die analyse heb ik niet gebouwd, en ik wil niet suggereren van wel. Maar de vraag is nu stelbaar, omdat er eindelijk iets is om hem tegenaan te houden. Vijf jaar geleden was er niets: niet omdat het niet mocht, maar omdat het antwoord in de hoofden van veertien docenten zat.

## De opbrengst is cognitief, niet administratief

De pitch voor AI in het onderwijs is bijna altijd tijdwinst. Dat is de zwakste versie van het argument, en bovendien de versie die de zaal terecht wantrouwt.

De AI-tutor bij ons is de eerste gate, niet de docentvervanger. Hij leest een ingediend checkpoint en schrijft één rapport. Meer niet: het is nadrukkelijk geen chatbot, er is geen dialoog en de student kan er niet op terugpraten. Dat is geen tekortkoming die we nog moeten wegwerken. Het is opgeschreven, omdat een tutor waarmee je kunt onderhandelen geen poort meer is.

![](figures/fig-03-tutor.png)

**Figuur 3.** (1) De vier fasen, elk met een eigen gate. Design is afgerond, Direct staat nog open: kwaliteit wordt op meerdere punten getoetst, niet op één eindmoment. (2) "Alleen Socratische vragen: nooit een score of verdict zichtbaar voor het team." Die regel staat niet in een handleiding maar boven het gesprek, en het rapport eronder houdt zich eraan. (3) Een echte vraag van de tutor over de Ryanair-casus van dit team. De tutor vraagt door op wat het team zelf heeft opgeschreven, en geeft nergens het antwoord.

Het opvallendste aan dat rapport is wat er niet in staat. Geen cijfer, geen oordeel, geen "goed gedaan, let nog even op". Alleen vragen die teruggrijpen op de woorden die het team zelf heeft ingeleverd: de omkeertijd van 25 minuten, de punt-tot-punt-vluchten, zijn eigen bewering over Industry 5.0. Dat is een Socratische tutor die zich aan zijn definitie houdt, en die definitie stond in het ontwerpdocument voordat er een model aan te pas kwam.

Wat het team terugkrijgt, zijn dus de vragen, plus of de gate open staat of niet. Een cijfer krijgt het team niet te zien: de rubriekscore blijft verborgen en gaat naar de docent.

![](figures/fig-04-dashboard.png)

**Figuur 4.** (1) Ook dit scherm staat in demo-toestand en zegt dat er zelf bij. Wat eronder ligt is wel gebouwd: de route bestaat, en met een echte klas geeft hij echte cijfers terug. (2) "Verborgen score": het cijfer dat de student nergens ziet en de docent wel. Niet omdat het per ongeluk zo uitpakte, maar omdat het rapport aan het team structureel geen veld heeft waar een score in past. (3) De docent kan de poort van de AI overrulen. De server legt elke override vast in een auditspoor, en weigert er een zonder opgegeven reden: een override die niemand later kan uitleggen is precies wat een student er wel over zou vragen.

Daar staat het antwoord op de vraag die elke docent bij een AI-poort stelt: wie heeft het laatste woord? De docent. Hij kan de gate openzetten die de tutor dicht hield. Maar niet stilletjes, en niet zonder reden. Dat de override een verplichte toelichting vergt, is geen nette gedachte achteraf: het staat in de eisen, dus weigert de server een override zonder. De knop erboven bereikt die server nog niet eens, en de regel geldt al.

Voor het eindassessment krijgt die docent geen samenvatting met een aanbeveling, maar een informatiepakket: de vragen die de tutor stelde, en aandachtspunten die elk terugwijzen naar de gebeurtenis waar ze uit volgen. Daarmee voert hij een ander gesprek dan hij anders had gevoerd.

![](figures/fig-05-dossier.png)

**Figuur 5.** (1) Het scherm staat hier in zijn demo-toestand en zegt dat er zelf bij: het start met vastgelegde voorbeelddata en laadt pas echte gegevens na een handeling. De data is dus een voorbeeld. De regel eronder niet. (2) "Geen cijfer, oordeel of aanbeveling. Dit overzicht wijst de docent ergens op; het oordeelt niet. Elk punt hierboven toont zijn bron zichtbaar; een punt zonder geldige bron wordt door de tool zelf al geweigerd." Dat is geen disclaimer achteraf: de server schrapt een punt zonder geldige bronverwijzing daadwerkelijk, voordat het scherm het te zien krijgt. (3) Elke vraagsuggestie draagt een klikbare bronverwijzing naar de gebeurtenis in de tijdlijn waar hij uit volgt. De docent kan dus altijd terug naar het bewijs.

Twee schermen verder is het dezelfde beweging: een punt zonder geldige bron haalt het scherm niet eens. Zo'n weigering krijg je er achteraf nooit meer in. Tegen de tijd dat het scherm er staat en de demo gepland is, heeft niemand nog een reden om hem toe te voegen.

Het gesprek wordt dus niet korter, het wordt scherper. En de tijd die vrijkomt wil ik in iets stoppen waar hij verschil maakt: in actueel materiaal bovenop het boek. Een casus van vorige maand, een cijfer uit een sector die nu beweegt.

Daar wil ik heen, en daar ben ik nog niet. De wiki uit figuur 1 is bewust alleen-lezen: geen enkele agent schrijft erin. Materiaal toevoegen is handwerk van docenten, en reflectievragen laten genereren bestaat bij ons niet.

Dat is geen gat dat ik vergeten ben. Het is een eis die ik zelf heb opgeschreven, en die me nu in de weg zit. En hier wordt het interessant: de agent die dit systeem bouwde heeft zich eraan gehouden, ook toen ik die lus wilde. Hij bouwt wat er staat, ook wanneer dat een verbod is. Dat is dezelfde eigenschap die hem bruikbaar maakt en die hem hier laat weigeren. Wil ik die lus, dan moet ik mijn eigen criterium herzien en opschrijven waarom alleen-lezen niet langer klopt. Ik kan er niet omheen door het te vergeten, en dat is precies de bedoeling.

Dat is de lus die ik wil. Het materiaal wordt rijker, de gate raakt beter geïnformeerd, het assessmentgesprek wint aan diepte, en dat levert weer aanwijzingen op over wat er aan materiaal ontbreekt. Een uur dat je terugkrijgt en in de volgende ronde stopt, is iets anders dan een uur dat je terugkrijgt.

Dus als je opleiding volgend jaar weer een AI-pilot doet, stel dan één vraag voordat er iets gebouwd wordt. Welke criteria geven we mee, en waar staan die opgeschreven? Is het antwoord "dat weten onze docenten", dan is het antwoord "nergens", en dan weet je nu al wat je terugkrijgt. Begin bij het boek dat je al hebt voorgeschreven, want daar heeft iemand het werk gedaan waar wij twintig jaar omheen zijn gelopen. Het probleem is nooit geweest dat de machine ons niet begrijpt. Het is dat wij het nooit hebben opgeschreven.
