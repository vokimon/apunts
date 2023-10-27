# Security problems

DESCARREGA DE RESPONSABILITAT:
**Si us plau, no prenguis aquest document com a font de veritat.**
Conté el que vaig entenent que son aquests problemes de seguretat segons em vaig informant.
El contingut canviarà a mida que vagi entenent millor els conceptes,
partint de que, segurament, ara no els estic entenent del tot bé.
Igual que la resta d'apunts d'aquesta pàgina,
però com aquest és un tema especialment sensible, calia dir-ho.

## CSRF (Cross Site Request Forgery

https://owasp.org/www-project-code-review-guide/reviewing-code-for-csrf-issues

Succeeix quan un usuari té una sessió oberta al navegador
i algú, maliciosament, li fa clickar un enllaç que fa una acció a l'aplicació.

Per exemple, imagina que tenim sessió oberta al banc i li fem clickar aquest enllaç:
```
https://mibanco.com/api/transfer/?amount=2000&targetiban=ES5512341234001234567890
```

L'enllaç li pot arribar per un correu, un xat, una web maliciossa, un QR...
I pot estar enmascarat amb un text legítim.

Per evitar aquest tipus de situacions,
hi ha diverses solucions que es poden aplicar:

- Que les accions no es resolguin automaticament, sinó que es demani algún tipus de confirmació.
	- No seria solució per API REST.
	- El resultat de la confirmació, no pot ser un altre punt atacable, el que envia la confirmació es una referència a la acció anterior.

- CSRF Tokens:
	- Cada cop que l'aplicació envia un link/formulari a l'usuari,
		l'aplicació generarà un codi aleatori (diferent cada vegada)
		que el client ha de tornar.
	- Aquests codis es guarden al servidor vinculats a la sessió de l'usuari.
	- Quan el client activa un dels enllaços, envia tambie el codi
	- El servidor confirma que el codi pertany a la sessió
	- Si no hi es, cal tancar la sessió i donar error
	- Un atacant, hauria d'esbrinar el codi cada cop... pot fer-ho si 



## SQL (or other) Injection

Succeeix quan la informació obtinguda de l'exterior del sistema
(la introdueix l'usuari o 




