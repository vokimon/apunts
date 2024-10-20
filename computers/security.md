# Security problems

DESCARREGA DE RESPONSABILITAT:
**Si us plau, no prenguis aquest document com a font de veritat.**
Conté el que vaig entenent que son aquests problemes de seguretat segons em vaig informant.
El contingut canviarà a mida que vagi entenent millor els conceptes,
partint de que, segurament, ara no els estic entenent del tot bé.
Igual que la resta d'apunts d'aquesta pàgina,
però com aquest és un tema especialment sensible, calia dir-ho.

## Glossary

- Resource origin: From its url, the combination of schema + hostname + port.
	- Ignore path, query parameters...
	- Implicit port considered (https is 443, http is 80)
	- Same origin: https://www.example.com:443/a/path and https://www.example.com/other/path
		- Cambia el path, ignorado, i el puerto, pero usa el explícito
	- Cross origin: http://sell.example.com and https://www.example.com
		- Cambia el protocolo, el puerto y el subdominio, cualquiera de los tres bastaría.
- Resource site: From its url, schema + eTLD + next domain level
	- No tiene en cuenta el subdominio ni el puerto
	- El dominio es un nivel más del eTLD
		- TLD toplevel domain .com, .org...
		- eTLD efective public domain: .co.uk, github.io...
			- Lista en: <https://publicsuffix.org/list/public_suffix_list.dat>
	- El subdominio es todo lo que valla más allá.
	- Same-site: https://sell.example.com vs https://www.example.com
	- Cross-site: https://vokimon.github.io vs https://som-eneriga.github.io
- Schemeless same-site: no tiene en cuenta el protocolo
- Se aplica
	- A transiciones de pagina: url de la original y la de destino
	- A contenido incrustado (iframes, imágenes, popups...)
	- A peticiones fetch: url del recurso que genera la peticion (js, html, css) vs a donde va la petición
	- A cookies: url del recurso que la crea, url de la petición que se hace que podria o no enviarla

## CSRF (Cross Site Request Forgery)

https://owasp.org/www-project-code-review-guide/reviewing-code-for-csrf-issues

https://scotthelme.co.uk/csrf-is-dead/


Succeeix quan un usuari té al navegador una sessió oberta amb una aplicació/servidor
i algú aliè, maliciosament, fa que el navegador faci una petició no volguda a aquesta aplicació aprofitant la sessió oberta.

Per exemple, imagina que tinc una sessió oberta al banc, `mibanco.com` i
visitant una web maliciosa faig click a un enllaç que
fa aquesta petició des del meu navegador:
```
https://mibanco.com/api/transfer/?amount=2000&targetiban=ES5512341234001234567890
```

L'enllaç li pot arribar per un correu, un xat, una web maliciossa, un QR...
Segurament estarà enmascarat com a legítim i amb un context que faci de ganxo.
De fet, no cal que sigui un enllaç ni que li faci click.
Qualsevol javascript pot fer peticions a on sigui de forma autònoma.

El que tenen en comú aquests atacs és que tot i que la petició la fa el navegador de l'usuari,
qui construeix la petició (origin, referer) no es el mateix lloc que la rep.

ACLARACIÓ: L'origin o referrer de la petició no es qui la executa (el navegador), si no el lloc que li diu que l'ha d'execturar.
Per protegir-nos d'un atac CSRF de qui hem de sospitar es d'aquest referrer si no és el site de destí.

- Origin: (domain) Referer: (pagina/url)

Per evitar aquest tipus de situacions,
hi ha diverses solucions que es poden aplicar:

- Que les accions no es resolguin automaticament, sinó que es demani algún tipus de confirmació.
	- No seria solució per API REST.
	- La resolució del segon pas no ha de tenir tota la informació i referir-se al primer pas.
		- Si no, estaríem tornant a tenir un punt d'entrada objectiu per l'atac.

- Synchronizer token pattern (CSRF tokens)
	- Cada cop que l'aplicació envia un link/formulari a l'usuari,
		l'aplicació generarà un codi aleatori (diferent cada vegada)
		que el client ha de tornar.
	- Aquests codis es guarden al servidor vinculats a la sessió de l'usuari.
	- Quan el client activa un dels enllaços, envia tambie el codi
	- El servidor confirma que el codi pertany a la sessió
	- Si no hi es, cal tancar la sessió i donar error
	- Un atacant, hauria d'esbrinar el codi cada cop... pot fer-ho si demana primer el formulari i agafa el token.
	- :-) Si posem els codis com a camps ocults dels formularis no cal JS ni similars
	- :-( Complejo en el lado del servidor pues hay que gestionar todos los tokens
	- !!:-O NO SOLUCIONA UNA MERDA!
		- JS pot demanar el formulari, agafar el csrf i fer el post

- Origin/Referrer headers:
	- El servidor limita les peticions compromeses a aquelles que el navegador confirma pels headers que venen del mateix lloc.
	- Els navegadors aporten certa protecció perque les pagines no puguin canviar els seus origin ni referer

- SameSite Cookies: Los navegadores no las envian cuando es una peticion entre dominios.
	- `SameSite: Strict` Només envia la cookie si el referer es el mateix.
		- Problema: La primera carrega de la pagina no tenim la cookie perque venim de fora i no s'envia
		- Solució: Tenir dos cookies simultanees una per les peticións fluixes i una Strict per les peticions delicades.
		- Cap problema amb les SPA perque la primera crida es per agafar l'index.html que no té res
		
	- `SameSite: Lax`: Solo se exige SameSite para metodos HTTP no seguros.
		- Considerandose seguros: GET, OPTIONS, HEAD, TRACE
		- Hay que programar la api con cuidado de que esos Metodos no tengan acceso a cosas y GET se usa mucho

	- Para SAP Strict es ideal pues se coge XS la pagina index.html, que es segura y el resto require SameSite.


## SQL Injection, Code Injection

- https://en.wikipedia.org/wiki/Code_injection
- https://en.wikipedia.org/wiki/SQL_injection


Succeeix en situacions on la informació que l'aplicació obté de l'exterior del sistema
s'integra com a part del codi a executar.
Per exemple, quan les dades que es reben d'un formulari s'incorporen

- a una consulta de la base de dades,
- o a un script que executa el servidor,
- o a l'HTML,
- o a una url, (important! no és un llenguatge de programació però també!)
- o...

Una atacant pot dissenyar aquesta informació introduïda
per sortir-se del contexte on està pensada incorporar-se
i acaban executant codi arbitrari al servidor.

Per exemple, molt sovint, dades que s'obtenen de formularis, acaben formant part
d'una consulta SQL entre cometes.
Si no inserim la dada amb cura,
una atacant pot incloure-hi unes cometes per tancar-les prematurament,
amb un punt-i-coma terminaria la nostra sentencia i a continuació,
podria incloure la nova sentencia maliciosa que vol executar al servidor.

La solució universal es processar aquestes dades entrants per, per exemple, incorporar seqüències d'escapada on toca.

El problema aquí és doble:

- Per un costat és una sitiuació molt comuna i es fa molt sovint aixó d'incorporar dades externes. És fàcil que en alguna en oblidem de d'aplicar-ho.
- O ens oblidem d'aplicar-ho bé, perque l'altre problema es que les casuístiques són complexes i depenen de cada llenguatge on inserim la dada externa.

Per això les bones pràctiques són:

- Evitar les tècniques d'inserció de dades del llenguatge de programació que construeix la cadena desti (Python, Javascript)
	- En Python, prohibit concatenar, f-strings, operador `%`, `format`
	- En Javascript, prohibit concatenar, interpolacio amb cometes invertida...
- No programar les escapades a mà, sinó fer servir les funcions d'escapada pròpies de cada llenguatge destí.
	- Els escapaments són específic de cada llenguatge destí (SQL, HTML, bash...)
	- Les llibreries existents ha sofert un procés de maduresa (s'han trobat i fixat errors) que segur que el nostre code des de zero no tindrà.
- Fer servir llibreries que facin el camí amb escapada, el camí per defecte i de menys resistència.
	- El que ha de costar es inserir coses sense escapar
	- Ex: JSX sempre escapa tot, si vols inserir codi és molt mes complicat i has d'escriure la paraula 'dangerous'
	- 

A dalt hem parlat de dades de l'exterior.
Cal entendre això de forma extensa.
Les dades que ja  tenim incorporades al sistema, perque ja estan a la base de dades,
també cal considerar-les externes, i no segures per injection perque en 


## CORS (Cross Origin Resource Sharing)

https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

La política de seguretat per defecte es que una pagina té confiança en els recursos 
La situació per defecte es que una pàgina web tè confiança en els recursos
(same-origin policy)

Succeeix quan una web maliciosa fa servir recursos (imatges, javascripts...) 

## XSS (Cross-site scripting)

Injectar contingut maliciós en un lloc web de confiança.
Normalment és contingut que el site permet afegir als usuaris,
o que s'obté d'un altre site/api,
que, en renderitzar-ho,
es converteix en codi executable, normalement al navegador.

Igual que altres injeccions la solució passa per sanejar
tot el contingut alié al codi de l'aplicació.
Normalment hi ha contingut, html, javascript,
que provenen del desenvolupador i es considera confiable,
volem que s'envii al navegador tal qual.
Seria no confiable tot el contingut que prové de l'usuari
o de fonts externes.

El problema d'aplicar sanejament a tot el contingut no confiable,
sempre acaba passant que hi ha un contingut no confiable
que ens oblidem de sanejar.

Per això els frameworks están adoptant la estratègia de sanejar per defecte,
i només en els casos que el desenvolupador especifiqui molt explícitament
que el contingut es confiable, esquivar el sanejament.

Exemple, en React, tot el contingut que s'insereix en el JSX
es sanititza per defecte sense dir res.
Si volem interpretar un cert text com a HTML, hem de fer servir
l'atribut `dangerouslySetInnerHTML` en el tag contenidor.

## JWT Flaws

https://portswigger.net/web-security/jwt

- Ficar informació personal al token
	- El token està codificat (base64), no pas xifrat.
	- La clau es per signar, no xifra pas.
	- Qualsevol pot llegir el contingut sense cap tipus de clau.
	- Per això, cal evitar posar cap informació que es pugui considerar sensible (correu)
	- Si l'identificador d'usuari és el correu, considerar algun tipus de hash
- No tenir o no comprovar la data d'expiració o que sigui massa llarga
	- Una data d'expiració curta redueix el temps d'exposició davant un token substret
	- En obtindre el token donar un segon refresh token per demanar l'actualització
- No incloure `aud` (audience) field o no validar-ho (si diversos serveis comparteixen secret)
	- Un token obtingut en un servei, es podria fer servir per accedir a l'altre si comparteixen clau
	- Pe. Dos instàncies d'una aplicació i ens oblidem de canviar la clau.
- No permetre els usuaris revocar els tokens (en sortir)
	- Es menja l'avantatge dels jwt respecte a les sessions, de que no requereix enmagatzematge de sessió al servidor
	- Es pot fer positiu (enmagatzemar només les revocades no caducades)
- Enmagatzemament insegur al client
	- Cookies caca
		- `HttpOnly`: Assegura que no està disponible des del javascript, només s'envia, evita atacs XSS per obtindre el token.
		- `Secure`: No s'envia amb http, només amb https
		- `SameSite=strict`: Només s'envia al site del contingut que ha generat la request
		- TODO: que hacer con el token de renovacion? (no hay que enviarlo cada vez, si no, pierde sentido)
	- Local storage caca
	- TODO: ¿entonces que?
- Decodificar pero no validar
	- La majoria de llibreries tenen dos accions, una per decodificar i obtindre el contingut (decode) i una altra per validar la signatura (verify).
	- Cal assegurar que estem verificant el token
- Fer servir l'algoritme que ve a l'atribut `alg` del token.
	- Alguns algoritmes no es basen en una clau privada. Notablement l'algoritme `none`.
	- Un atacant podría fabricar un token amb un d'aquests algoritmes i no es validaria la signatura.
	- Usa una llibreria que ignori aquest camp, o com a minim que permeti especificar explicitament l'algoritme i fer-ho.
	- Al final l'algoritme el definim nosaltres quan generem el token,
	- i no hi ha cap motiu per confiar en el que ens ve amb el token de l'usuari.
- Permetre claus incrustades amb jwk
	- L'estàndard JWK permet inserir la clau (`kid`, `jwk`) al propi token.
	- Un atacant podria fabricar un token amb la seva propia clau.
	- Hem d'especificar la clau de forma explicita i vigilar que la llibreria
	- fa servir la nostra i no la incrustada.
- Permetre claus linkades amb jku
	- El mateix que l'anterior pero la clau es proveeix amb un enllaç
	- L'enllaç es un json amb els jwk a dintre
- Permetre claus per id amb kid
	- kid es un id d'una clau interna pero també pot ser un path al servidor
	- si l'atacant puja, pe, un adjunt amb la clau, podria referenciar el fitxer adjunt
	- També podria fer un sql injection si l'id es un camp a la base de dades.
- Secret dèbil
	- La seguretat del jwt depén de que el secret amb el que es signa no sigui obtenible
	- `hashcat -a 0 -m 16500 <jwt> <wordlist>`


TODO: Es recomana moure el refresh token a tokens i el token a estat de l'aplicacio,
pero en aquest cas, tot i que protegim el token refresh de XSS, estariem enviat el refresh token tota l'estona.
O es que amb https, el punt debil deixa de ser la xarxa i esdeve el propi navegador?



