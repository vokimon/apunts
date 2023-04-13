# Branching Patterns

Un resum de  _Patterns for Managing Source Code Branches_ by Martin Fowler

https://martinfowler.com/articles/branching-patterns.html

## Patrons generals

### Patró _Source Branching_ (Ramificant el codi)

- **Problema:** Com treballar amb canvis paral·lels fets fer diferents persones?
- **Solució:** Crea diferents copies del codi i enregistra els canvis que es fan a cadascuna

**Conceptes:**

- Commit (confirmació): un canvi enregistrat
- Codeline: una seqüència de canvis confirmats (el terme _branca_ s'evita per significa coses diferents en diferents sistems de control de versions)
	- Una codeline és més que una branca de git: Alice i Bob poden tenir diferents codelines en local de la mateixa branca `master` de git i poden diferir de la d'`origin`.
- Tip/Head (cap): la darrera comissió d'una codeline
- To branch (ramificar): generar una copia del codi a partir de la qual generar una nova sequència de commissions
- To merge (fusionar): aplicar els canvis d'una codeline a una altra
- Conflictes: Fusionar sovint implica conflictes
	- Conflictes textuals: Quan les dues branques han modificat les mateixes linies.
		El control de versions ho detecta però requereix resolució manual.
	- Conflictes semàntic: Quan les dues branques, tot i no incòrrer en conflicte textual interfereixen en la seva lògica. 
		El control de versions no ajuda a detectar-ho però si ens ajuda tenir bons testos.

**Forces:**

- Ramificar és fàcil, fusionar costa.
- Ramificant evitem temporalment el conflicte que seria estar tothom canviant el codi.
- Tard o d'hora cal pagar els deutes (amb interessos).
- La fusió és més costosa com més canvis acomulen.

### Patrò _Mainline_ (Linia principal)

- **Problema:** Quan tenim diverses branques, quin és l'estat actual del projecte?
- **Solució:** Considerar una única branca compartida l'estat actual del producte

#### Conceptes

- La branca fa de referencia per:
	- Saber de quin punt he d'arrencar la meva branca
	- Saber quins canvis dels companys he d'incorporar
	- Saber d'on treure una versió a desplegar a producció
- Usualment la branca esta a un servidor compartit

#### Forces

- Alternativa: Release Train


### Patrò _Healthy Branch_ (Branca sana)

- **Problema:** Amb tanta gent aplicant canvis a l'hora, com puc refiar-me de que la branca principal funciona?
- **Solució:** Executar automaticament comprovacions per cada commit que es fa a la branca

**Forces:**

- Important que el codi s'auto-comprovi
- Hi ha tensió entre el cost de les proves i la freqüència i profundintat de les proves
	- Jerarquia de testos: Els ràpids primer per donar feedback aviat
- Ajuda el patro _Pre-Integration Review_
- Important a la branca principal, pero tambè a les branques de features o personals

## Patrons d'integració


### Patrò _Mainline Integration_

S'integra el codi a la branca principal


### Patrò _Feature Branching_ (Ramificat per funcions)

- **Problema:** Com integrar els canvis?
- **Solució:** Tots els canvis associats amb una funció van a una branca i s'integra quan està acabada

Alternativa: _Integració continua_

**Forces:**

- :-) La qualitat de tot codi de la funció es comprova com a unitat
- :-) El codi de la funció s'incorpora integrament o no, només quan la funció és completa
- :-( La fusió és menys freqüent
	- Més conflictes textuals i semantics
	- Por al merge
	- Branques zombie
- :-) Introdueix un punt de peer-review de tercers (fora del pair programming)
- :-( Els refactorings no relacionats es veuen aliens a una brancha de funció
- :-) Es un mode de funcionament popular a l'open source (pull request), on els desenvolupadors son contribuidors i cal review dels programadors principalsa

### Patrò _Continuous Integration_ (Integració contínua)

- **Problema:** Com integrar els canvis?
- **Solució:** Els desenvolupadors integren amb mainline tan d'hora com s'arriba a una branca sana de compartir, normalment dintre del dia

Com?

- Redueix la por d'integració per branca llarga
- Requereix Integració Continua
- Compromís d'arribar frequentment a punts de integració sana, amb una feature, si cal, parcialment construïda
- Com integrar features parcialment construides:
	- Feature flags: Que la feature estigui desactivada amb un flag
	- Keystone Interface: No exposar la interficie a l'usuari fins que tot lo de darrera està fet (Keystone interface, la interficie es la pedra final)
- Obrir una feature branch es opcional:
	- Si s'obre, s'integra freqüentment
	- També es pot treballar sense ella: Si es passa la CI i hi ha manera de desactivar la feature parcial a producció

Alternativa: _Feature branch_

**Forces:**

- :-( Requereix compromís de tenir la branca sana (integració continua)
- :-) Integració més freqüent que la duracio del desenvolupament d'una funció
	- :-) Redueix el temps de detecció dels conflictes
	- :-) Fusións més petites
- :-) Més natural fer refactorings no relacionats amb la funció
- :-) Cientificament comprovat que augmenta el delivery (Fowler dixit)
- :-( Codi condicional que un cop a producció caldria treure


### _Pre-integration review_ (Revisió previa a la integració)

- ***Problema:*** Com assegurar la qualitat del mainline?
- ***Solució:*** Tota integració amb la mainline ha de estar revisada per iguals abans d'acceptar-se

Una Pull request es una combinació dels patrons _Feature Branch_ i _Pre-integration review_

**Forces:**

- :-( El pair programming ja aporta peer-review i més rápida
- :-) Assegura un mínim de qualitat quan els equips no són equilibrats
- :-) Aporta peer review quan no s'esta fent pair programming
- :-( Introduceix latència en el delivery
- :-( Complicada de fer a cada integració si hi ha integració contínua
- :-( Amb _Feature Branch_ els reviews arriben al final del desenvolupament principal implicant refer coses per arribar a la qualitat desitjada

DGG: Pot servir per fer extensiu el que s'està fent si el desenvolupament ha estat molt concentrat en poques persones

### Patrò: _Ship-show-ask_ (Entrega, mostra o pregunta)

> No es un patrò de l'article pero en Fowler comenta que,
> en un entorn equilibrat ell prefereix fer refactorings un cop comitejat,
> que exigir-los a una revisió pre-commit.
> 
> https://martinfowler.com/articles/ship-show-ask.html

Adaptar l'estrategia al tipus de canvi.

- Ship
	- Com la integració contínua, sense branca
	- Casos:
		- Funció afegida seguint protocols ja establerts
		- Arregla un bug obvi
		- Documentació
		- Millora codi basat en el feedback rebut
- Show
	- Crees una PR i s'integra un cop es passen els checks automatics, hi ha conversa sobre el codi
	- Obre espai per comunicar el que s'ha fet i rebre feedback, preguntes...
	- Discusio post mortem
	- Casos:
		- M'agradaria qualsevol tipus de feedback per millorar el codi
		- Mireu aquesta nova aproximació de fer les coses
- Wait
	- Crees una PR, i esperes al feedback abans de fusionar
	- Casos:
		- Això funcionaria?
		- No estic segur de com he resolt el tema
		- Necessito ajuda per millorar això
		- Ja integraré demà, que avui no arribo

**Regles:**

- Per fusionar no es requereix review
- Els autors decideixen quin tipus de cas
- Els autors son els que fusionen
- Les branques tenen vida curta i les rebasem a master sovint

**Forces:**

- Un cop proposada una solució es dur proposar alternatives
- No es substitut de parlar amb les companyes abans de començar
- Que no obrir una PR pugui ser tampoc una forma d'evitar la discussió sobre com es fan les coses


### Aspectes claus dels patrons d'integració

- Freqüència d'integració: Baixa freqüència permet desenvolupament tranquil, 
- Fricció d'integració:
	- tot el que posem en mig de fer la integració: formularis, conflictes, reviews...
	- si hi ha molta dificulta la integració continua
	- plantejar: aporta un valor clar?
	- Factors culturals: confiança entre desenvolupadors, equilibri de 
- Modularitat


## Patrons d'entrega

### Patró _Release Branch_
### Patró _Maturity Branch_
### Patró _Long Lived Release Branch_
### Patró _Environment Branch_
### Patró _Hotfix Branch_
### Patró _Release Train Branch_
### Patró _Release-Ready Mainline_


## Altres patrons

### Patró _Experimental Branch_
### Patró _Future Branch_
### Patró _Collaboration Branch_
### Patró _Team Integration Branch_

## Branching Policies

### Git-flow
### Github flow
### Trunk based development



 

















### 


















