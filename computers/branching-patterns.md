# Summary: Patterns for Managing Source Code Branches by Martin Fowler

https://martinfowler.com/articles/branching-patterns.html

## Glossari

## Source branching (Ramificant el codi)

- **Problema:** Com treballar amb canvis paral·lels fets fer diferents persones?
- **Solució:** Crea diferents copies del codi i enregistra els canvis que es fan a cadascuna

### Conceptes

- Commit (confirmació): un canvi enregistrat
- Codeline: la seqüència de comisións (el terme _branca_ s'evita per significa coses diferents en diferents sistems de control de versions)
	- Una codeline és més que una branca de git: Alice i Bob poden tenir diferents codelines en local de la mateixa branca `master` de git i poden diferir de la d'`origin`.
- Tip/Head (cap): la darrera comissió d'una codeline
- To branch (ramificar): generar una copia del codi a partir de la qual generar una nova sequència de commissions
- To merge (fusionar): aplicar els canvis d'una codeline a una altra
- Conflicts: Mergin usually implies conflicts
	- Textual Conflict: Both codelines have changed the same lines. Version control systems detects them, but requires manual resolution
	- Semantic Conflict: Both codelines do not necessarily affect the same lines, but interfere logically. Harder to detect without CI.

### Forces

- Ramificar és fàcil, fusionar costa.
- Ramificant evitem temporalment el conflicte que seria estar tothom canviant el codi.
- Tard o d'hora cal pagar els deutes (amb interessos).
- La fusió és més costosa com més canvis acomulen.

## Mainline (Linia principal)

- **Problema:** Quan tenim diverses branques, quin és l'estat actual del projecte?
- **Solució:** Considerar una única branca compartida l'estat actual del producte

### Conceptes

- La branca fa de referencia per:
	- Saber de quin punt he d'arrencar la meva branca
	- Saber quins canvis dels companys he d'incorporar
	- Saber d'on treure una versió a desplegar a producció

### Forces

- Alternativa: Release Train


## Healthy Branch (Branca sana)

- **Problema:** Amb tanta gent aplicant canvis a l'hora, com puc refiar-me de que la branca principal funciona?
- **Solució:** Executar automaticament comprovacions per cada commit que es fa a la branca

### Forces

- Important que el codi s'auto-comprovi
- Hi ha tensió entre el cost de les proves i la freqüència i profundintat de les proves
	- Jerarquia de testos: Els ràpids primer per donar feedback aviat
- Ajuda el patro _Pre-Integration Review_















