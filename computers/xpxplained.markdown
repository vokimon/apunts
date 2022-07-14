# El problema


## Riscos del programari

- Objectiu: evitar els riscos del programari
- En concret:
	- Fora de termini: Hem de dir al client que no arribem a data
	- Cancel·lació del projecte: tants terminis fora al final es cancela abans d'entrar a producció
	- Programari feixuc: El sistema es feixuc de mantenir i corregir
	- Programari defectuós: Alta tasa de falles
	- Negoci malentés: No s'ha entés el negoci i no soluciona el problema
	- Negoci canviant: El negoci canvia i quan entra a producció el sistema ja és vell
	- Sobredisseny: S'han implementat funcionalitats divertides de programar, inútils pel client
	- Fugida de cervells: Els programadors bons, s'agobien del projecte i s'en van a d'altres més engrescadors 
- Solucions XP:
	- Fora de termini:
		- Cicles curts, d'abast limitat
		- Tasques comprehensibles i detallades
		- Prioritzacio amb el client
	 	- Les tasques que queden fora son les menys prioritaries
	- Cancel·lació del projecte:
		- El client escull quin és el conjunt mínim de funcionalitats que poden fer una release útil.
		- Això màximitza el valor de la feina des de l'inici
	- Programari feixuc:
		- Test unitaris cobrint el programari
		- S'executen continuament
		- No s'acomula el codi brossa
	- Programari defectuós:
		- Programadors testejen a baix nivell
		- Clients defineixen testos a nivell de funcionalitat
	- Negoci malentés:
		- El client s'integra en l'equip
		- L'especificació es refina amb l'aprenentatge dels desenvolupadors
	- Negoci canviant:
		- Cicles curts redueixen la possibilitat de que canviin mentres ho fem
		- El client és benvingut a canviar l'especificacio del que s'esta fent al cicle
		- Això fa que l'equip treballi amb requeriments nous com si fossin vells.
	- Sobredisseny:
		- Només es fa el que es decideix que és prioritari
	- Fugida de cervells:
		- Programaires prenen la responsabilitat de estimar i finalitzar el seu treball
		- Aprenen de les seves estimacions
		- No se li demanen terminis impossibles i fustrants
		- Força interacció amb companys i clients, reduint la solitud
		- Formació contínuada incoorporada al treball

## El dia a dia

- Parelles de programaires programen junts
- Desenvolupament dirigit per testos
	- Primer fas el test, després el codi que el fa passar (no codi sense test)
	- Quan no pots pensar un test que falli, ja estàs (no sobretesteix)
- Refactoring:
	- En paral·lel als testos que afegeixen funcionalitat, modifiquen el codi per millorar el disseny
	- El codi que toca una parella no està restringit en abast
- Integració contínua:
	- La integració es fa seguidament del codi
	- Test d'integració inclosos


## Economia del programari

- Generar beneficis el més abans possible, generar costos el més tard possible
- Allargar la vida productiva del projecte per arribar a amortitzar-ho

- Opcions:
	- Abandonar: Millor si podem obtindre valor d'un projecte tot i abandonar-ho
	- Dredreçar: Millor com més sovint i violentament podem redreçar el projecte
	- Retardar: Millor si podem retrasar la inversió sense perdre l'oportunitat d'invertir
	- Creixer: Millor si podem escalar amb més inversió si hi ha més demanda

- Valor de les opcions:
	- Inversió requerida
	- Benefici obtingut
	- Valor actual del benefici obtingut
	- Finestra temporal on es viable
	- Incertesa sobre el valor del benefici en el futur
- Normalment domina la incertesa en el valor

## 4 variables dels projectes

- Cost, Temps, Qualitat, Abast (agafa'n 3... o 2... o 1)

- Cost:
	- Ha de ser suficient, pero massa diners massa d'hora no sol ser bo
	- No sempre els diners aconsegueixen reduir el temps
		- 9 dones no fan un nen en un mes
	- Es pot invertir en millors eines, infrastructura o especialistes
- Time:
	- Amb més temps pots incrementar la qualitat i l'abast.
	- Massa temps sense arribar a producció, no rebem feedback i pot tenir impacte a la qualitat
	- No donar suficient va en detriment de les altres
	- Sovint es una restriccio externa
- Quality:
	- No paga controlar el projecte amb aquesta variable
	- Podem reduir el temps reduint qualitat pero a la llarga ho paguem.
	- Sovint exigint mes qualitat els projectes acaben abans: testing, coding standards...
	- A vegades les restriccions de qualitat es poden relaxar
	- Treure coses amb qualitat dona moral
- Abast:
	- Tenint cobertes les necessitats ens permet controlar molt be el temps i els costos amb alta qualitat


- Focalitzar en l'abast
	- Amb un abast més curt els clients poden reaccionar, al començament, potser les idees no estan clares
	- La indefinició dels requeriments es una oportunitat, no un problema
	- El definim poc a poc, maximitzant les altres variables
	- Definim l'scope donades les altres tres variables
	- Ho fem amb el client al costat per maximitzar el valor
	- Com evitar defraudar al client
		- El client prioritza les funcionalitats que vol ficar
		- Anar aprenent a estimar per definir quant entra, per minimitzar les funcionalitats que cauen
		- Dintre de la iteració fer primer les tasques prioritaries, si cal deixar caure, que sigui lo menys important


## Cost del canvi

- Quant costa fer un canvi?
- Teoria clasica:
	- model cascada: Analisis-Disseny-Implementacio-Testeig-Implantacio
	- el cost dels canvis implica revisar decissions previes, creix exponencialment
- Actualitat
	- Hi ha eines (tecnologies, pràctiques) per controlar el cost dels canvis
	- Orientacio a objectes per abstreure i desacoblar implementacions
	- Disseny el més simple possible que fa la funcionalitat
	- Tests de regressió per fer canvis amb confiança 
	- Constant refactoring to improve the design

## Els quatre valors

### Comunicació

- Els problemes als projectes sovint es poden reseguir fins a algu no parlant amb algu altres
	- Un canvi en el disseny no comunicat
	- Un desenvolupador no preguntant alguna cosa al client
	- Un gestor fent la pregunta equivocada als programadors i obtenint un informe de progrés erroni
	- ...

- Coses que minen la comuniciació
	- Un programador dona males notítices al seu cap i el cap li castiga, això fa que les males notícies futures no arribin a temps en el futur
	- Un desenvolupador ignorant alguna cosa que li ha dit el client
	- ...

- XP força la comunicació introduint práctiques que requereixen comunicació entre desenvolupadors, clients i gestors.
- XP introdueix la figura 


### Simplicitat

- Quina es la solució més simple que funciona
- Com no avançar-se als problemes de demà si ens han acollonit amb el cost exponencial dels projectes
- XP fa una aposta:
	- Millor invertir poc ara i asumir cost del canvi posterior
	- que invertir molt ara i arriscar-se a que no sigui útil demà

### Realimentació

- "No m'ho preguntis a mi, pregunta-ho al sistema"
- Es posa en valor tenir una visió real de l'estat del sistema (testos, progres, estimacions...)
- Les pràctiques XP donen resposta a les accions que fem:
	- Els testos sobre els canvis que anem fent al codi
	- La planificacio sobre el progres de les tasques
	- El planning game sobre el cost de les funcionalitats
	- Testos funcionals per cada història (cas d'us simplificat) 
	- Posar d'hora les funcionalitats a producció 

### Coratge

- Els altres valors permeten tenir coratge per fer coses que sense elles no en tindries
- Però de fet, sovint els temors heredats a fer segons quines coses ens dominen, cal tenir coratge
- Exemples:
	- Començar a implementar sense tenir una visió completa del problema
	- Tirar codi que ja no es fa servir
	- Intentar una solucio que simplifica el sistema

### Interaccions positives entre els valors

- (Com->Sim) Com més _comuniqueu_, millor veieu el que cal i el que no cal en un sistema i podeu _simplificar_
- (Sim->Com) Com més _simple_ és el sistema, més fàcil és _comunicar_
- (Com->Cor) Si _comuniqueu_ bé, aquests canvis els podeu fer amb més confiança, més _coratge_
- (Com->Cor) Quan _comuniquem_ bé obrim la porta al _coratge_ perque podem comunicar més obertament a idees d'experiments que tenim que suposen alt risk i alta recompensa.
- (Sim->Cor) Quan la solució és _simple_ també, tindreu més _coratge_ per fer canvis.
- (Fb->Cor) Quan tenim feedback ens permet ser coratjosos perque si la caguem ens adonem d'hora i podem tirar enrera
- (Fb->Com) Quan tenim molt feedback es molt més fàcil comunicar: Si detectes un flaw en un codi, fas un test
- (Com->Fb) Si comuniques efectivament saps que testejar i quines metriques calen
- (Sim->Fb) Simple systems are easier test (_feedback_)
- (Fb->Sim) Having test _feedback_ let's you focus on how to _simplify_ the system.



## Principis

- Els valors ens donen una idea de que valorar en un bon projecte
- Són massa difusos per establir unes pràctiques 

1. Feedback rapid:
	- Cal poder incorporar ràpid la informació que ofereix el feedback sobre l'acció que fem
	- El temps entre l'acció i la reacció és clau per l'aprenentatge
2. Asumir la simplicitat:
	- Tractar cada problema com si es pogués resoldre amb una simplifitat ridícula
	- Molt difícil d'empassar pels programadors:
		- No planegis el futur
		- Confia en que pots afegir complexitat en el futur si la necessites
	- L'economia del software com a opcions ho recolza
3. Canvi incrementals:
	- Els grans canvis mai funcionen i menys a la primera
	- Disseny es canvia poc a poc
	- La planificació canvia poc a poc
	- L'equip canvia poc a poc
	- Fins i tot, l'adopcio de XP es fa poc a poc
4. Canvi és benvingut
	- Accepta el canvi com a motor de tot
5. Trabajo de calidad
	- Ningú treballa a gust fent xapuses
	- Tothom es sent bé fent un bon treball
	- La qualitat no ha de ser una de les variables de controlar.
	- Els únics valors possibles són _excel·lent_ o _malaltisament excel·lent_ en cas de que en depenguin vides.


- Altres menys primaris


1. Ensenya aprenent:
	- En comptes de ensenyar amb doctrines
	- planificar camins d'aprenentatge
	- Que cadascú trobi les seves pròpies respostes
2. Inversio inicial petita
	- Massa recursos a l'inici del projecte es recepta pel fracàs
	- Si no hi ha recursos per resoldre un problema interessant, el projecte no és interessant
3. Jugar para ganar
	- No para no perder
	- Si juegas para no perder te ciñes al libro, no porque tenga sentido sino para que nadie pueda culparte del fracaso
	- Ceñirse al libro son reuniones, documentacion inutiles que se hacen porque tocan, no porque ayude al exito.
4. Experiments concrets
	- Davant d'una decissió, testejar-la
	- El resultat de les sessions de disseny no és un disseny acabat sinó un conjunt de coses a comprovar.
	- El resultat d'una sessió d'anàlisis de requeriments ha de ser també un conjunt d'experiments a fer.
5. Comunicació oberta i honesta
	- Hem de poder dir els problemes que veiem en el codi dels altres
	- Hem de poder expresar les pors i demanar auxili
	- Hem de poder donar males notícies als clients i als caps
	- Fer-ho com abans millor i sense castigs
6. Treballar amb els instints de les persones no en contra d'ells
	- A les persones els agrada:
		- guanyar, apendre, interactuar amb altres persones, ser part d'un equip, rebre confiança, fer un bon treball, tenir un software funcionant... 
	- A la gent no li agrada:
		- procediments, burocracia, castigs...
7. Responsabilitat aceptada:
	- No s'asigna responsabilitats a les persones
	- Son les persones les que accepten la responsabilitat
	- Si l'equip arriba a la conclusio de que cal fer una tasca algu asumira la responsabilitat
8. Local adaptation
	- Cada pais, organitzacio, equip és diferent
	- Les receptes d'XP no son regles absolutes
	- Cal pero evaluar els canvis i les seves conseqüències
	- Es un procés progressiu
9. Viatja lleuger
	- No ens podem moure àgilment si portem molt d'equipatge
	- Artefactes: pocs, simples i valuosos
	- Cultura nòmada llestos per canviar de lloc
		- Si el client decideix pendre un altre camí
		- Si decidim portar el disseny per un camí no anticipat
		- Si l'entorn del negoci canvia
		- Si una nova tecnologia esdevé interessant
10. Mètriques honestes
	- Si hi ha incertesa no interessa tant una estimació amb molts decimals sinó un rang o un ordre de magnitud
	- No fer servir mètriques que no es correlin amb el progrés
	- ie. LoC no tè sentit si simplificar ho redueix


## Activitats bàsiques

Quins son les activitats bàsiques que necessitem?

### Codificar

- El codi és el producte principal, el que has d'acabar generant
- Pots voler dir una altra cosa, pero el que está escrit hi queda
- El codi comunica sense retorica
	- Si m'expliques una idea, la puc malinterpretar
	- Si la codifiquem junts, precissament  el que volies dir (en un test o en un Sut)
- Aquesta comunicació esdevé aprenentatge al temps que evolucionem el codi
- Com és lo bàsic, ho farem servir per el que poguem
	- Comunicar
	- Especificació operacional (testos autocomprovats)

### Testejar

- Molt de programari es fa sense testos automatics, perque seria essencial?
	- Llarg: Mante el programari viu més temps
		- Pots fer canvis durant més temps
		- La confiança en el sistema es manté, millor modificar el que hi ha que refer-ho tot de nou perque no ens atrevim a tocar-ho
	- Curt: Es mes divertit amb test (lo curt es el que va a favor de l'instint)
- Dos nivells:
	- Unitaris: Els codi fa el que els programadors volen que faci 
	- Funcionals: El codi fa el que els clients volen que faci


### Escoltar

- Els programadors no saben res (que els interessi a la gent de negoci)
- Els testos recullen saber de negoci capturat pels programadors
- D'on el treuen? d'escoltar al client
- Els programadors tambe ajuden al client a entendre el que es complicat i el que es fàcil
- Cal una bona estructura de comunicació per a que això funcioni


### Dissenyar

- Si escoltem, testejem i codifiquem arribara un moment que l'entropia no ens deixarà avançar
- Cal reorganitzar el codi, dissenyar
- Disseny bo:
	- Un canvi a una part no implica un canvi a un altra part (baix acoblament)
	- Cada peça de logica es troba a un sol lloc (no duplicació)
	- La lògica és a prop de les dades que modifica (cohesió)
	- Extensions al sistema es poden fer canviant-ho a un sol lloc (extensibilitat)
- La forma de dissenyar també és incremental
- No es fa un disseny d'entrada sinó que es va evolucionant
- Refactorings: canvis en el codi per millorar el disseny
- El procés de disseny separat de l'afegir funcionalitats





