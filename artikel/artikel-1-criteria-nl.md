# Een agent bouwt alleen wat je hebt opgeschreven

*Deel 1 van twee. Dit deel gaat over wat een opleiding moet vastleggen. [Deel 2](artikel-2-docent-nl.md) gaat over wat de docent eraan heeft.*

Elke opleiding experimenteert inmiddels met AI. Dat is geen gok meer, dat is de stand van zaken. Er zijn pilots, er zijn werkgroepen, er is een kaderdocument, er zijn docenten die op zaterdagochtend iets in elkaar zetten wat maandag in de les kan. De vraag of we het gaan doen is voorbij.

Alleen: kijk naar wat eruit komt. Een generator die meerkeuzevragen maakt bij een hoofdstuk. Een simulatie die los van alles staat. Een demo-appje dat het goed doet op een studiemiddag en daarna nooit meer opstart. Twee jaar experimenteren, en de onderwijskwaliteit is geen millimeter opgeschoven. De toets gaat sneller de deur uit, het gesprek met de student is hetzelfde gesprek als in 2019.

Wat ontbreekt er?

Niet de techniek, en ook niet de bereidheid. Wat ontbreekt, zijn de ontwerpcriteria: expliciet opgeschreven en machineleesbaar. Een AI-agent kan alleen bouwen wat je hebt opgeschreven. Het hoger onderwijs heeft nooit opgeschreven wat goed onderwijs is. Dus krijgt het toetsgeneratoren terug.

Dat kan ik laten zien in plaats van beweren. De schermen in dit stuk komen uit een module die ik dit jaar heb herbouwd, en dat systeem is niet door een ontwikkelteam gemaakt. Het is ontworpen en geschreven door een AI-coding-agent. Mijn werk was de aansturing: eerst een Learner Requirement Document, het onderwijskundig ontwerp, voordat er één regel code bestond. Daarna leverde ik achtergrondmateriaal, ideeën en correcties, en hakte ik knopen door waar dat document zweeg. De agent bouwde wat erin stond. Dat is geen anekdote bij dit artikel. Het is het bewijs eronder.

## Schrijf je niets op, dan krijg je microtaken terug

Ik heb inmiddels genoeg van die opbrengsten gezien om een patroon te herkennen. MC-generatoren, stand-alone simulaties, chatbots die de studiegids kunnen citeren. Ze hebben iets gemeen dat zelden benoemd wordt: ze vragen alleen criteria over zichzelf.

Neem die toetsgenerator. Vraag een model om tien meerkeuzevragen bij een hoofdstuk en je krijgt tien vragen waarvan de afleiders doorzichtig zijn, waarvan er twee hetzelfde toetsen, en waarvan het juiste antwoord verdacht vaak het langste is. Bruikbaar wordt het pas als je opschrijft wat een goede vraag is: één verdedigbare sleutel, afleiders die een echte denkfout van studenten representeren, geen aanwijzingen in de formulering, geen vraag die je zonder het hoofdstuk ook kunt beantwoorden. Doe je dat, dan werkt het. Dan komen er vragen uit die je zonder schamen in een toets zet.

En let op waar die regels vandaan moesten komen: ze stonden nergens. Wat een goede afleider is, hoe je een sleutel verdedigbaar houdt, waarom een vraag die je zonder het hoofdstuk kunt beantwoorden geen vraag is: dat zat allemaal in de hoofden van de mensen die al twintig jaar toetsen construeren. We hebben het nooit opgeschreven, omdat we op hun vakmanschap vertrouwden. Dat was ook terecht. Pas toen we het aan een machine wilden uitleggen, bleek dat we het niet hádden.

Kijk nu wat voor criteria dat zijn. Ze gaan allemaal over de vraag zelf. Ze zeggen niets over waarom dit concept in week 3 staat en niet in week 7, welke voorkennis het veronderstelt, welk misverstand studenten hier standaard hebben, of hoe het antwoord samenhangt met wat er in het eindassessment gebeurt. Je kunt een onberispelijke meerkeuzevraag maken over een hoofdstuk dat in het verkeerde blok staat.

Daar zit de hele zaak. De criteria die je meegeeft bepalen het plafond van wat je terugkrijgt. Geef je regels over vraagkwaliteit, dan krijg je goede vragen: precies dat, en niets erboven. Over samenhang, volgorde en opbouw krijg je niets terug, en niet omdat de agent het niet zou kunnen. Omdat niemand het heeft opgeschreven. De microtaak is dus geen bescheiden eerste stap op weg naar iets groters. Het is het plafond van de criteria die je had.

Voor de duidelijkheid: die generator is niet slecht. Hij doet wat hij belooft. Alleen belooft hij niets over onderwijskwaliteit, en we behandelen hem alsof hij dat wel doet.

## Een deel staat al opgeschreven, in het boek dat je wegdoet

Hier komt de wending die ik in de meeste AI-gesprekken in het onderwijs mis. We doen alsof ontwerpcriteria nog geschreven moeten worden, en alsof dat een academisch project van drie jaar is. Terwijl een deel ervan al op je bureau ligt.

Een goed studieboek is geschreven door iemand die drie dingen weet. Wat er relevant is binnen een kennisgebied en wat niet. Hoe de onderdelen samenhangen. En in welke volgorde je ze bestudeert, zodat het tweede begrip op het eerste kan rusten. Sla de inhoudsopgave open: dat is volgorde plus samenhang, en dat zijn ontwerpcriteria. Daar komt de rest bovenop. De didactische aanwijzingen bij een hoofdstuk. De voorbeeldcasussen, gekozen omdat ze een specifiek onderscheid scherp maken. De discussievragen achterin, die vaak preciezer zijn opgeschreven dan de leerdoelen in onze eigen modulehandleiding.

Wie het boek wegzet als een dure contentdrager maakt dezelfde fout als wie een demo-appje laat bouwen. Beiden gooien weg wat expliciet was en houden alleen de tekst over. Het boek is niet duur vanwege het papier. Het is duur vanwege de ordening, en juist die ordening is het enige wat een agent kan lezen.

Bij ons is dat geen metafoor gebleven. De kennisbasis van de module is een openbare wiki met een eigen adres, en die is niet thematisch geordend door iets wat zelf een indeling verzon. Hij volgt de hoofdstukken van het boek, en toont per team wat past bij waar ze op dat moment staan.

![](figures/fig-01-wiki.png)

**Figuur 1.** (1) De wiki is geordend naar de hoofdstukken van het studieboek, getagd als boekconcept. Die nummering is de volgorde die de auteur koos, en het systeem neemt hem over in plaats van hem opnieuw te bedenken. (2) Een concept dat de docent zelf toevoegde, zonder hoofdstuknummer. Het boek levert de structuur, de docent vult aan. (3) En deze pagina heeft het systeem zelf geschreven, uit een video die de docent aanwees. Alle drie staan hier omdat het team in deze fase zit: de wiki toont wat past bij waar ze nu staan.

Let op wat het systeem hier niet doet. Het bedenkt geen eigen thematische indeling, het maakt geen samenvatting van het boek, het rangschikt niets op relevantie die het zelf heeft ingeschat. Het neemt de ordening over die een expert heeft aangebracht, en filtert daarbinnen. Dat is geen beperking die ik heb moeten accepteren. Het is de reden dat het werkt.

## Schrijf je het wél op, dan bouwt de agent het

En dan de derde claim, die de vorige twee omdraait. Zodra de criteria er wél staan, in een vorm die een machine kan lezen, gebeurt er iets wat de microtaak nooit oplevert.

In dit systeem bepaalt één JSON-bestand welk model welke rol vervult. Diezelfde regel is de tekst die de student op het scherm leest. Niet twee bronnen die uit elkaar kunnen lopen: één bron, twee lezers.

![](figures/fig-02-transparantie.png)

**Figuur 2.** (1) Eén JSON-bestand bepaalt welk model welke rol vervult. Diezelfde regel is hier de tekst die de student leest. (2) "Deze lijst is geen momentopname die iemand handmatig bijhoudt: het is exact de configuratie waarmee het systeem draait. Verandert er een model, dan verandert deze tabel mee, anders start het systeem niet."

Die laatste zin is het hele punt. Het systeem weigert te starten als de belofte aan de student en de werkelijkheid uit elkaar lopen. Dat is geen zorgvuldigheid van een programmeur, het is een eis die iemand heeft opgeschreven.

Hetzelfde geldt voor iets veel minder technisch. Als je vastlegt dat kwaliteit op meerdere momenten ontstaat en niet op één eindmoment, dan is dat geen visiepraat meer. Dan zijn het vier fasen met bij elke fase twee poorten: een Socratische AI-tutor en een peer-partnerteam dat het werk van een ander team leest.

![](figures/fig-03-tutor.png)

**Figuur 3.** (1) De vier fasen, elk met een eigen gate. Design is afgerond, Direct staat nog open: kwaliteit wordt op meerdere punten getoetst, niet op één eindmoment. (2) "Alleen Socratische vragen: nooit een score of verdict zichtbaar voor het team." Die regel staat niet in een handleiding maar boven het gesprek, en het rapport eronder houdt zich eraan. (3) Een echte vraag van de tutor over de Ryanair-casus van dit team. De tutor vraagt door op wat het team zelf heeft opgeschreven, en geeft nergens het antwoord.

Het opvallendste aan dat rapport is wat er niet in staat. Geen cijfer, geen oordeel, geen "goed gedaan, let nog even op". Alleen vragen die teruggrijpen op de woorden die het team zelf heeft ingeleverd: de omkeertijd van 25 minuten, de punt-tot-punt-vluchten, zijn eigen bewering over Industry 5.0.

Die tutor is dus geen chatbot. Er is geen dialoog en de student kan er niet op terugpraten. Dat is geen tekortkoming die we nog moeten wegwerken, het staat opgeschreven, omdat een tutor waarmee je kunt onderhandelen geen poort meer is. De agent die dit bouwde heeft zich daaraan gehouden op een plek waar niemand het zou hebben gecontroleerd.

## Wat dit betekent voor je volgende pilot

Drie dingen, en ze staan los van elkaar. Geef je geen criteria mee, dan krijg je werk terug uit de enige categorie die zonder criteria kan. Een deel van je criteria heb je al, in het boek dat je overweegt weg te doen. En schrijf je ze wél op, dan houdt een agent zich eraan, ook waar het hem in de weg zit.

Dus als je opleiding volgend jaar weer een AI-pilot doet, stel dan één vraag voordat er iets gebouwd wordt. Welke criteria geven we mee, en waar staan die opgeschreven? Is het antwoord "dat weten onze docenten", dan is het antwoord "nergens", en dan weet je nu al wat je terugkrijgt. Begin bij het boek dat je al hebt voorgeschreven, want daar heeft iemand het werk gedaan waar wij twintig jaar omheen zijn gelopen. Het probleem is nooit geweest dat de machine ons niet begrijpt. Het is dat wij het nooit hebben opgeschreven.

*In [deel 2](artikel-2-docent-nl.md): wat de docent hieraan heeft, en waarom de winst cognitief is en niet administratief.*
