# Security problems

DESCARREGA DE RESPONSABILITAT:
**Si us plau, no prenguis aquest document com a font de veritat.**
Conté el que vaig entenent que son aquests problemes de seguretat segons em vaig informant.
El contingut canviarà a mida que vagi entenent millor els conceptes,
partint de que, segurament, ara no els estic entenent del tot bé.
Igual que la resta d'apunts d'aquesta pàgina,
però com aquest és un tema especialment sensible, calia dir-ho.

## CSRF (Cross Site Request Forgery)

https://owasp.org/www-project-code-review-guide/reviewing-code-for-csrf-issues

Succeeix quan un usuari té una sessió oberta al navegador
i algú, maliciosament, li fa clickar un enllaç que fa una acció a l'aplicació.

Per exemple, imagina que tenim sessió oberta al banc i li fem clickar aquest enllaç:
```
https://mibanco.com/api/transfer/?amount=2000&targetiban=ES5512341234001234567890
```

L'enllaç li pot arribar per un correu, un xat, una web maliciossa, un QR...
Segurament estarà enmascarat com a legítim i amb un context que faci de ganxo.

Per evitar aquest tipus de situacions,
hi ha diverses solucions que es poden aplicar:

- Que les accions no es resolguin automaticament, sinó que es demani algún tipus de confirmació.
	- No seria solució per API REST.
	- La resolució del segon pas no ha de tenir tota la informació i referir-se al primer pas.
		- Si no, estaríem tornant a tenir un punt d'entrada objectiu per l'atac.

- Synchronizer token pattern
	- Cada cop que l'aplicació envia un link/formulari a l'usuari,
		l'aplicació generarà un codi aleatori (diferent cada vegada)
		que el client ha de tornar.
	- Aquests codis es guarden al servidor vinculats a la sessió de l'usuari.
	- Quan el client activa un dels enllaços, envia tambie el codi
	- El servidor confirma que el codi pertany a la sessió
	- Si no hi es, cal tancar la sessió i donar error
	- Un atacant, hauria d'esbrinar el codi cada cop... pot fer-ho si
	- :-) Si posem els codis com a camps ocults dels formularis no cal JS ni similars
	- :-( Complejo en el lado del servidor pues hay que gestionar todos los tokens


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









