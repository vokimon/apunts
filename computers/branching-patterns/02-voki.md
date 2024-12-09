# Patrons de base

## Patrons de base

Tota la resta es basen en aquests:

- Source Branching
- Main Line
- Healthy Branching

## Source Branching

- Problema: Moltes persones treballant a la mateixa base de codi
- Solució: Crear una còpia del codi i registrar els canvis successius que se li fan
- Branch-Codeline-Branca: Seqüència de commits 
- Commit: Agrupa conjunt de canvis respecte la versió anterior
- Head-Tip-Cap: La darrera versión de la branca
- **Còm reintegrar els canvis a la branca original**

## Source Branching (Forces)

Forces: Ramificar és fàcil. Fusionar no tant.

Les branques es distancien, generant deute que es paga a la fusió

_La caiguda està bé, si no fos perquè acaba_

Git ajuda a integrar les versions textualment

Git detecta **conflictes textuals**

Compte amb els **conflictes semàntics**

## Main line

Problema: Amb tantes branques, com sé quin és l'estat actual actual del producte

Solució: Establir una branca única i compartida que actua com a estat actual del producte

Repositori central vs Repositoris locals

"La branca `master` del repositori de github"

`master` local no és `master` en github

Alternativa: **Release train**


## Healthy branching

Problema: Tot l'equip depèn de l'estabilitat de les branques compartides

Estableix comprovacións automatitzades a fer a cada commit, per assegurar que no hi ha defectes en la branca

Automatitzat: estil (linters), funcionalitat (unittest), desplegabilitat (deploys)...

No todos los problemas se detectan en la automatización -> **Pre-integration review**



# Patrons d'integració


## Patrons d'integració

Cóm resoldre el problema de la integració de branques

- Mainline Integration
- Feature branching
- Integration Frequency
- Continuous Integration
- Pre-integration Review
- Integration friction
- Modularity


## Mainline Integration

Problema 


# Patrons de Camí a Produció




