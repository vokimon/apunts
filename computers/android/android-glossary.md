# Android Glossary [CA]

## Application

Una **Aplicació** en Android és la unitat lògica d'execució.
Es correspon a un procés Linux gestionat per el sistema operatiu Android.

Empaca dintre d'un zip reanomenat APK

- codi compilat: bytecode y llibreries natives
- metadades
- recursos

A cada aplicació li és assignat un UUID (identificador únic d'usuari).
Molt semblant al que es fa amb els dimonis de sistema de Linux.
Els usuaris del sistema no son només persones sinó principalment aplicacions.
Es una primera capa d'aïllament entre aplicacions.
A més cada aplicació s'executa en un entorn virtual aïllat.

## Activity

Una _activitat_ en Android es una interfície d'usuari, una pantalla.
Es el concepte anàlog a _finestra_ o _pantalla_
en les applicacions GUI d'escriptori.
La diferència són les limitacións que s'imposen
en com l'usuari pot interaccionar amb elles.
No amb el contingut sino amb elles en si.
Les finestres les pots obrir, tancar, moure, redimensionar...
Les activitats només pots obrirles o tirar enrere.

## Task

Aquest fluxe de finestres de la mateixa applicació es el que es diu _tasca_.
Les organitza a mode de pila.
Quan arrenca l'aplicació s'obre
l'anomenada _activitat principal_
que es situa a la base de la pila.
Si la activitat principal llença una nova activitat,
la nova activitat queda com a activa al damunt
i la principal desactivada a sota.
Només quan la nova activitat es tanca,
per exemple, tirant endarrera,
que la activitat principal torna a activar-se.

## Intent

Una _intenció_ es un punt d'entrada declarat a les metadades per a una aplicació.
Es correspon amb una activitat principal y certes dades que li serán proveides
o s'especifiquen a les metadades.

La majoria d'aplicacions tenen com a mínim la _intenció_
per ser llençades des del llençador d'applicacions.
Pero poden definir-ne d'altres,
per exemple, al botó de compartir,
per obrir un cert tipus de dades,
o quan es produeix un cert esdeveniment.

Les aplicacions es poden comunicar fent servir els intents exposats

## Life cycle

Aplicacions, tasques i activitats
tenen un cicle de vida controlat pel sistema.

Per exemple, en el cas concret de les Activitats,
Android defineix crides que cadascuna pot sobrescriure
en cada transició.
Els noms dels estats no són oficials.
Android només defineix les transicions, no pas els estats.

- Apagada: No está disponible al sistema
    - ↓ onCreate onDestroy ↑
- Parada: Carregada en memòria pero no visible
    - ↓ onStart onStop ↑
- Visible: Visible a l'usuari, pero sense interacció
    - ↓ onResume onPause ↑
- Active: Pot rebre la interacció del usuari.

## Fragment

Un fragment és una disposició d'elements d'interficie
que es pot reutilitzar en diferents activitats.
Aporta estructura, modularitat i reús.

Es defineix en xml semblant a com es defineix una activitat.



