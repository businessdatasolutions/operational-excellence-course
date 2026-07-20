# Een agent bouwt alleen wat je hebt opgeschreven

Elke opleiding experimenteert inmiddels met AI. Dat is geen gok meer, dat is de stand van zaken. Er zijn pilots, er zijn werkgroepen, er is een kaderdocument, er zijn docenten die op zaterdagochtend iets in elkaar zetten wat maandag in de les kan. De vraag of we het gaan doen is voorbij.

Alleen: kijk naar wat eruit komt. Een generator die meerkeuzevragen maakt bij een hoofdstuk. Een simulatie die los van alles staat. Een demo-appje dat het goed doet op een studiemiddag en daarna nooit meer opstart. Twee jaar experimenteren, en de onderwijskwaliteit is geen millimeter opgeschoven. De toets gaat sneller de deur uit, het gesprek met de student is hetzelfde gesprek als in 2019.

Wat ontbreekt er?

Niet de techniek, en ook niet de bereidheid. Wat ontbreekt, zijn de ontwerpcriteria: expliciet opgeschreven en machineleesbaar. Een AI-agent kan alleen bouwen wat je hebt opgeschreven. Het hoger onderwijs heeft nooit opgeschreven wat goed onderwijs is. Dus krijgt het toetsgeneratoren terug.

## Microtaken zijn geen strategie, maar een symptoom

Ik heb inmiddels genoeg van die opbrengsten gezien om een patroon te herkennen. MC-generatoren, stand-alone simulaties, chatbots die de studiegids kunnen citeren. Ze hebben iets gemeen dat zelden benoemd wordt: ze vragen alleen criteria over zichzelf.

Neem die toetsgenerator. Vraag een model om tien meerkeuzevragen bij een hoofdstuk en je krijgt tien vragen waarvan de afleiders doorzichtig zijn, waarvan er twee hetzelfde toetsen, en waarvan het juiste antwoord verdacht vaak het langste is. Bruikbaar wordt het pas als je opschrijft wat een goede vraag is: één verdedigbare sleutel, afleiders die een echte denkfout van studenten representeren, geen aanwijzingen in de formulering, geen vraag die je zonder het hoofdstuk ook kunt beantwoorden. Doe je dat, dan werkt het. Dan komen er vragen uit die je zonder schamen in een toets zet.

En let op waar die regels vandaan moesten komen: ze stonden nergens. Wat een goede afleider is, hoe je een sleutel verdedigbaar houdt, waarom een vraag die je zonder het hoofdstuk kunt beantwoorden geen vraag is: dat zat allemaal in de hoofden van de mensen die al twintig jaar toetsen construeren. We hebben het nooit opgeschreven, omdat we op hun vakmanschap vertrouwden. Dat was ook terecht. Pas toen we het aan een machine wilden uitleggen, bleek dat we het niet hádden.

Dat is dit hele artikel in het klein. Die generator werkt precies omdat iemand impliciete kennis expliciet heeft gemaakt. En hij blijft klein omdat we dat alleen voor de vraag hebben gedaan.

Kijk namelijk wat voor criteria dat zijn. Ze gaan allemaal over de vraag zelf. Ze zeggen niets over waarom dit concept in week 3 staat en niet in week 7, welke voorkennis het veronderstelt, welk misverstand studenten hier standaard hebben, of hoe het antwoord samenhangt met wat er in het eindassessment gebeurt. Je kunt een onberispelijke meerkeuzevraag maken over een hoofdstuk dat in het verkeerde blok staat.

Daar zit de hele zaak. De criteria die je meegeeft bepalen het plafond van wat je terugkrijgt. Geef je regels over vraagkwaliteit, dan krijg je goede vragen: precies dat, en niets erboven. Over samenhang, volgorde en opbouw krijg je niets terug, en niet omdat de agent het niet zou kunnen. Omdat niemand het heeft opgeschreven. De microtaak is dus geen bescheiden eerste stap op weg naar iets groters. Het is het plafond van de criteria die je had.

Voor de duidelijkheid: die generator is niet slecht. Hij doet wat hij belooft. Alleen belooft hij niets over onderwijskwaliteit, en we behandelen hem alsof hij dat wel doet.

## Ontwerpcriteria zijn het werk, en het studieboek is er een bron van

Hier komt de wending die ik in de meeste AI-gesprekken in het onderwijs mis. We doen alsof ontwerpcriteria nog geschreven moeten worden, en alsof dat een academisch project van drie jaar is. Terwijl een deel ervan al op je bureau ligt.

Een goed studieboek is geschreven door iemand die drie dingen weet. Wat er relevant is binnen een kennisgebied en wat niet. Hoe de onderdelen samenhangen. En in welke volgorde je ze bestudeert, zodat het tweede begrip op het eerste kan rusten. Sla de inhoudsopgave open: dat is volgorde plus samenhang, en dat zijn ontwerpcriteria. Daar komt de rest bovenop. De didactische aanwijzingen bij een hoofdstuk. De voorbeeldcasussen, gekozen omdat ze een specifiek onderscheid scherp maken. De discussievragen achterin, die vaak preciezer zijn opgeschreven dan de leerdoelen in onze eigen modulehandleiding.

Wie het boek wegzet als een dure contentdrager maakt dezelfde fout als wie een demo-appje laat bouwen. Beiden gooien weg wat expliciet was en houden alleen de tekst over. Het boek is niet duur vanwege het papier. Het is duur vanwege de ordening, en juist die ordening is het enige wat een agent kan lezen.

Voordat ik verder ga, iets wat je moet weten om de rest te kunnen wegen. Het systeem dat je hierna ziet is niet door een ontwikkelteam gebouwd. Het is ontworpen en geschreven door een AI-coding-agent. Mijn werk was de aansturing: eerst een Learner Requirement Document, het onderwijskundig ontwerp, voordat er één regel code bestond. Daarna leverde ik achtergrondmateriaal, ideeën en correcties, en hakte ik knopen door waar dat document zweeg. De agent bouwde wat erin stond. Dat is geen anekdote bij dit artikel. Het is het bewijs eronder.

En kort wat je dan voor je krijgt, want ik ga er straks losse schermen uit lichten. Het systeem heeft vier delen. Een **wiki** met de kennisbasis, geordend naar de hoofdstukken van het boek. Geen interne database, maar een echte openbare wiki met een eigen adres, die ik met een AI-agent bijwerk: businessdatasolutions.github.io/oe-wiki. Een **studentportaal** waar teams per fase een checkpoint indienen. **Twee poorten** bij elk checkpoint: een Socratische AI-tutor en een peer-partnerteam. En een **docentzone** met een dashboard, een studentdossier en een kwaliteitsrapport.

Ze hangen aan één ding samen. Elke handeling wordt als feit vastgelegd: een team levert in, de tutor leest en stelt vragen, de poort gaat open of blijft dicht, het partnerteam doet hetzelfde. Staan beide poorten open, dan komt de volgende fase vrij. De docent ziet diezelfde gebeurtenissen terug, samengevat op het dashboard en uitgeschreven in het dossier. De wiki bepaalt intussen wat een team op dit moment te lezen krijgt. Vier fasen, acht poorten (vier voor de tutor, vier voor de partnerteams), één spoor van feiten eronder.

Bij ons is dat geen metafoor gebleven. De kennisbasis waar de studenten mee werken is niet thematisch geordend door iets wat zelf een indeling verzon. Hij volgt de hoofdstukken van het boek en toont wat past bij waar het team op dat moment staat.

![](figures/fig-01-wiki.png)

**Figuur 1.** (1) De wiki is geordend naar de hoofdstukken van het studieboek, getagd als boekconcept. Die nummering is de volgorde die de auteur koos, en het systeem neemt hem over in plaats van hem opnieuw te bedenken. (2) Een concept dat de docent zelf toevoegde, zonder hoofdstuknummer. Het boek levert de structuur, de docent vult aan. (3) En deze pagina heeft het systeem zelf geschreven, uit een video die de docent aanwees. Alle drie staan hier omdat het team in deze fase zit: de wiki toont wat past bij waar ze nu staan.

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

Toen ik aan dit stuk begon, stond hier dat dat niet kon. De wiki was bewust alleen-lezen: het systeem las eruit en schreef er nooit in. Dat was een eis die ik zelf had opgeschreven, en hij zat me in de weg.

Dus heb ik hem herzien. Niet door het verbod te schrappen, maar door op te schrijven wat er dan wél moet gelden. Drie vraagniveaus in plaats van zes: begrijpen, analyseren, evalueren, met de reden erbij waarom de andere drie afvallen. Onthouden beantwoord je door omhoog te scrollen. Toepassen vraagt een procedure die dit materiaal niet levert. Creëren is wat het checkpoint zelf al eist. Verder: de vragen dragen hun niveau niet als etiket, want het werkwoord hoort dat te verraden. Nooit een oordeel. Nooit het antwoord. Altijd Nederlands, ook bij een Engelstalige video.

Daarna plakte ik een YouTube-link in een docentscherm en vinkte vijf hoofdstukken aan.

![](figures/fig-06-vragen.png)

**Figuur 6.** (1) "Leg uit hoe..." Begrijpen: kan de student navertellen wat de spreker beweert? (2) "Vergelijk... met de vier perspectieven uit dit hoofdstuk." Analyseren: hier ontmoet de video het boek. (3) "Beoordeel in hoeverre..." Evalueren: een oordeel vellen, en kunnen zeggen op welke gronden. De niveaus staan er niet bij; het werkwoord verraadt ze. Dat is precies wat de opdracht eiste.

Die pagina staat nu in de wiki, tussen de hoofdstukken waar hij bij hoort. In figuur 1 is hij te zien, onderaan, als enige kaart met het label video.

Twee dingen ontbreken er nog, en allebei bewust. Het systeem schrijft het bestand maar publiceert het niet: een wijziging doorvoeren in een andere repository vraagt een sleutel die deze dienst niet heeft, dus een mens drukt op de knop. En de docent kiest de video. Niemand leidt uit een tutorgesprek af dát er iets ontbreekt. Dat is de volgende stap, en hij is niet gezet.

Maar let op wat er niet is gebeurd. Ik heb de agent niet overgehaald. Ik heb geen formulering gevonden die het verbod omzeilde. Ik heb één criterium herzien en opgeschreven wat ervoor in de plaats komt, en toen bouwde hij het. Dat is dezelfde eigenschap die hem eerst liet weigeren.

Dat is de lus die ik wil. Het materiaal wordt rijker, de gate raakt beter geïnformeerd, het assessmentgesprek wint aan diepte, en dat levert weer aanwijzingen op over wat er aan materiaal ontbreekt. Een uur dat je terugkrijgt en in de volgende ronde stopt, is iets anders dan een uur dat je terugkrijgt.

Dus als je opleiding volgend jaar weer een AI-pilot doet, stel dan één vraag voordat er iets gebouwd wordt. Welke criteria geven we mee, en waar staan die opgeschreven? Is het antwoord "dat weten onze docenten", dan is het antwoord "nergens", en dan weet je nu al wat je terugkrijgt. Begin bij het boek dat je al hebt voorgeschreven, want daar heeft iemand het werk gedaan waar wij twintig jaar omheen zijn gelopen. Het probleem is nooit geweest dat de machine ons niet begrijpt. Het is dat wij het nooit hebben opgeschreven.
