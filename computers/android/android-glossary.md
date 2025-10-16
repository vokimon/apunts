# Android Glossary [CA]

https://github.com/codepath/android_guides/wiki/

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
    - ↓onCreate↓ ↑onDestroy↑
- Parada: Carregada en memòria pero no visible
    - ↓onStart↓ ↑onStop ↑
- Visible: Visible a l'usuari, pero sense interacció
    - ↓onResume↓ ↑onPause↑
- Active: Pot rebre la interacció del usuari.

## Fragment

Un fragment és una disposició d'elements d'interficie
que es pot reutilitzar en diferents activitats.
Aporta estructura, modularitat i reús.

Es defineix en xml i amb codi semblant a com es defineix una activitat.


## Views

Les _vistes_ son elements que componen una UI.
En Qt, Widgets. En React, Components.

## Widgets

Son views autocontingudes.

- `android.widget.TextView`:	Displays text
- `android.widget.EditText`:	Input field
- `android.widget.Button`:	Clickable button
- `android.widget.ImageView`:	Displays an image
- `android.widget.CheckBox`:	Toggle checkbox
- `android.widget.Switch`:	On/off toggle
- `android.widget.ProgressBar`:	Shows loading
- `android.widget.SeekBar`:	Slider input

## View Groups

Els _grups de vistes_ són vistes que serveixen per contindre altres vistes.
Els grups organitzen com es veuen les vistes contenides.

- `android.widget.LinearLayout`	Arranges views in a row or column
- `android.widget.RelativeLayout`	Positions views relative to each other (older)
- `androidx.constraintlayout.widget.ConstraintLayout`	Modern flexible layout
- `android.widget.FrameLayout`	Simple stacking layout
- `androidx.recyclerview.widget.RecyclerView`	Efficient list/grid container
- `android.widget.ScrollView`	Makes content scrollable vertically



## Atributs comuns de les vistes

- `android:orientation`
    (Container)
    Defineix quin és l'eix principal. L'altre eix serà el de creuament.
    Valors: `vertical` o `horizontal`
    Equivalent CSS: `flex-direction`
- `android:gravity`
    (Container) Cap a on 'cauen' els fills
    Valors: Es poden combinar un valor verticals amb un d'horitzontal amb una `|`
    - `left`, `right`, `start`, `end`, `center_horizontal`, `fill_horizontal`    
    - `top`, `bottom`, `center_vertical`, `fill_vertical`
    - `center`, `fill` afecten als dos eixos.
    - Per exemple, en un layout linial, no tè efecte en l'eix principal.
    - Equivalent al `align-items` del css flexbox
- `android:layout_gravity`
    (Children) Bescanvia el gravity del container per aquest fill en concret.
    - Equivalent al `item-align` del css flexbox
- `android:layout_weight`
    Es fa servir quan al contenidor hi ha espai per expandir més enllà del mínim.
    De l'espai disponible a aquesta vista se li asignarà la mateixa proporció
    que la que hi ha entre aquest pes i la suma dels pesos dels germans.
- `android:layout_height/width`
    - `wrap_content`: ajusta al tamany requerit pels fills
    - `adapt_parent`: expandeix al tamany del pare
    - `0dp`: 
- `android:gravity`
    Donde se colocaran los hijos. Como el align o el text-align del css.
- `android:layout_gravity`
    Equivalent al `self-align` del css.
    En un LinearLayout només affecta al cross axis.

### Coses

`post` es un metode de View que crida el block paràmetre després
de l'actual cicle de dibuixat, evitant que es recalculin coses
en mig del dibuixat.

`dp` es una unitat de pixel virtual independent de la densitat
que correspon a un pixel en una densitat de 160 dpi (`normal`).

`sp` es una unitat de pixel virtual independent per a fonts,
que no només inclou la densitat sinó que contempla les
preferències d'usuari pel tamany de font.

`px` representa pixels físics i no es recomana fer-ho servir.


## Source layout

El codi font d'un projecte Gradle per Android s'organitza en mòduls i els mòduls en conjunts de fonts (source sets)

    project_root/<module>/src/<source-set>/

**Mòdul:**
És un conjunt de fonts (codi i recursos) que es pot construir independentment.
Normalment esdevé a una aplicació (APK/AAB), una llibreria (AAR), extensió (???)...

Els mòduls poden dependre entre ells però només unidireccionalment.

**Source set:**
Es un conjunt de fonts que s'inclouen en un mòdul si es compleixen certes condicions.

- `main`: s'inclou sempre
- `debug`: només en mode desenvolupament
- `release`: només al build d'usuari
- `androidTest`: testos d'instrumentació (executats a un dispositiu Android)
- `test`: testos locals (executats a la maquina de desenvolupament)
- `paid`, `free`, `demo`...: varietats, sabors o flavors del mòdul

Quedant una estructura semblant a aquesta:
    
    project_root/
        gradle.build # defineix els moduls
        module1/
            gradle.build # defineix els source-sets
            src/
                main/
                debug/
                release/
                test/
                androidTest/
                flavor1/
                flavor2/
        module2/

**Build type:**
Defineix com es genera el component.
Es defineixen a la clau `buidTypes {}` de `gradle.build`
i per defecte son `debug` i `release`.
A cada build type li correspon el seu source set.

**Varietat (flavor):**
Literalment sabors (com als iogurts!).
Es fa servir per diferents versions del programari que volem publicar.
Per exemple, una demo, una versió shareware, una versió premium,
una versió especial nadal...

**Variant:** Combinació de diferents source sets.
Ho fa el gradle, no hem de crear source-sets
per les combinacions.
Exemple: paidRelease

**Dimensions de varietats (flavor dimensions):**
Per defecte les varietats son mutuament exclusives.
Si volem combinar-les, cal definir dimensions.
Les varietats d'una dimensió segueixen sent mutuament exclusives entre elles,
però, podem combinar varietats de diferents dimensions.

Per exemple, podem tenir una dimensió de 'region' (eu, us),
una altre 'monetization' (free, paid, premium),
una altre 'holidays' ('none', 'halloween', 'easter', 'christmas')...

Es defineixen al `gradle.build`. Per exemple:

```groovy
flavorDimensions "monetization", "holiday"

productFlavors {
    free { dimension "monetization" }
    paid { dimension "monetization" }
    easter { dimension "holiday" }
    christmas { dimension "holiday" }
}
```

Produeixen les variants `freeEasterDebug`, `paidChristmasRelease`...


## Sistema de recursos

Els recursos d'una aplicació s'identifiquen,
dins d'un _mòdul_
per un _tipus_ i un _id_ i poden tenir versions
específiques per diferents configuracions de dispositiu
identificades per un conjunt de _qualificadors_,
que corresponen a idioma, resolució...

La potència dels recursos es que li demanem al sistema un recurs per (modul), tipus i id,
i el sistema ens retorna la versió del recurs que millor s'adapta a la nostra configuració.
Ens estalviem aquesta lògica de selecció.

### Referint recursos

Per referenciar un recurs dins del codi,
fem servir el paquet `R` dins del namespace
del projecte (`import com.example.myapp.R`)

    R.type.id
    R.mipmap.ic_launcher

Si és un recurs d'un altre mòdul podem explicitar el mòdul:

    explicit.module.R.type.id

El mòdul R retorna un enter que representa un id numèric intern pel recurs
que nosaltres hauriem de fer servir de forma transparent.
Normalment per fer servir el recurs farem servir funcions que reben aquest enter
i el recuperen segons el tipus de recurs.

Des d'un xml es referencia com `@type/id` si es al mateix mòdul
o sinó, `@explicit_module:type/id`.
 
TODO: `explicit_module` es defineix com namespace o es un dot separated path?

### Creant versions dels recursos

https://developer.android.com/guide/topics/resources/providing-resources#AlternativeResources

Una versió d'un recurs estarà,
dins d'un mòdul a:
`<modul>/res/<tipus>[-<qualificador1>[-<qualificador2>]]/<id>.<extensio>`

Per exemple la icona d'aplicació (launcher icon),
es un recurs de tipus `mipmap` amb id `ic_launcher`.
Podem aportar diferents versions segons densitat de pantalla i versió d'Android.

    res/mipmap-xxxhdpi/ic_launcher.xml # Per dispositius
    res/mipmap-anydpi-v26/ic_launcher.xml # Per dispositius suportant 


Els qualificadors poden ser, per prioritat:

- **País i xarxa mobil:** (`mcc`/`mnc`) (Mobile Country Code i Mobile Network Code) Exemple `mcc208-mnc00` Vol dir a Francia fent servir xarxa d'Orange
- **Idioma:** `ca`, `ca-rFR`
- **Direcció de lectura:** (layoutDirecxpiton API 17) `ldltr` `ldrtl` (layout direction)
- **Dimensió mes petita:** (smallestWidthDp API 13) El tamany més estret d'altura o amplada `sw<N>dp`
- **Mínima amplada o altura:** (screenWidth/HeightDp API 13) `w<N>dp` o `h<N>dp` aplica a dimensions majors o igual que l'especificada
- **Mínim tamany de pantalla:** (screenLayout API 4) `small` 320x426, `normal` 320x470, `large` 480x640, `xlarge` 720x960 (API 9)
- **Aspecte de la pantalla:** (screenLayout API 4) `long`, `notlong` Si es pantalla ampla > 4/3
- **Pantalla rodona:** (isScreenRound API 23) `round`, `notround` Per rellotges i similars.
- **Gamut de color ample:** (isScreenWideColorGamut API 26) `widecg`, `nowidecg`
- **Interval dinamic ample (HDR):** (isScreenHdr) `highdr`, `lowdr`
- **Orientació de la pantalla:** (orientation) `port`, `land`
- **Mode d'interficie:** (uimode) `car` `desk` `television` `appliance` `watch` `vrheadset`
- **Mode nocturn:** `night` `notnight`
- **Densitat de pixels:** `ldpi`.  `mdpi`, `hdpi`, `xhdpi`, `xxhdpi`, `xxxhdpi`, `nodpi`, `tvdpi`, `anydpi`, `<nnn>dpi`
- **Touch screen:** (`touchscreen`)  `notouch`, `finger`
- **Keyboard available:** `keysexposed`, `keyshidden`, `keyssoft`
- **Hardware Keyboard:** `nokeys`, `qwerty`, `12key`
- **Navigation kayes available:** `navexposed`, `navhidden`
- **Non touch navigation:** `nonav`, `dpad`, `trackball`, `wheel`
- **Platform version:** `v<N>` Apply for API N or higher


### Selecció de la versió apropiada

- Primer filtra les versions del recurs amb qualificadors incompatibles
- Després fins que només quedi un, per a tot tipus de qualificador per ordre de prioritat
    - Si una versió te el qualificador, es descarten els que no el tinguin
    - En el cas concret de la Densitat, descarta també les que funcionin pitjor




Les icones d'aplicació (launcher icons)
son recursos de tipus `mipmap` amb el nom `ic_launcher`.
Per suportar diferentes versions es col·loquen a diferents
directoris `res/mipmap-qualifier1-qualifier2`.

Per les icones els qualificadors típics son
densitat de pixels (`xhdpi`)
i minim api level (`v23`)
pero també pot afegir-se idioma, regio, tamany de pantalla, orientació de pantalla...
Els qualificadors han d'anar ordenats.


https://developer.android.com/guide/topics/resources/providing-resources#BestMatch

Si un mateix id es troba en directoris amb qualificadors, el sistema de recursos:

- elimina els directoris amb qualificadors que no apliquen
- per ordre de prioritat de qualificadors, 

In code:

`R.type.id` like in `R.mipmap.ic_launcher`



## Icones d'aplicació (launcher icons)

### Criteris de disseny

- Dissenyats a 108 pixels.
- Zona util de 66

### Sistema de recursos

Els recursos de 
En codi `R.type.id`, per exemple `R.mipmap.ic_launcher`.
A un xml `@type/id`

Les icones d'aplicació (launcher icons)
son recursos de tipus `mipmap` amb el nom `ic_launcher`.
Per suportar diferentes versions es col·loquen a diferents
directoris `res/mipmap-qualifier1-qualifier2`.

Per les icones els qualificadors típics son
densitat de pixels (`xhdpi`)
i minim api level (`v23`)
pero també pot afegir-se idioma, regio, tamany de pantalla, orientació de pantalla...
Els qualificadors han d'anar ordenats.

El sistema de recursos:

- elimina els qualificadors que no apliquen

### Desplegament

A partir d'Android 1.0 (API 1) es suporten les **icones rasters**
cal posar-les en diferent densitat:
ldpi x0.75, mdpi x1, hdpi x1.5, xhdpi x2, xxhdpi x3, xxxhdpi x4
La resolució de referència es mdpi,
Per el launcher la referència es de 48.
No es recomana ficar la resolució ldpi.

```
res/mipmap-mdpi/ic_launcher.png # 48
res/mipmap-hdpi/ic_launcher.png # 72
res/mipmap-xhdpi/ic_launcher.png # 96, API 8
res/mipmap-xxhdpi/ic_launcher.png # 144, API 16
res/mipmap-xxxhdpi/ic_launcher.png # 192, API 18
```

A partir d'Android 4.0 (API 14) via llibreria `VectorDrawableCompat`
i a partir d'Android 5.0 (API 21) de forma nativa,
es suporten **els VectorDrawables, vectorials**.
Són molt semblats a svg's pero més limitats
i amb funcionalitats específiques.
La resolució base del launcher deixa de ser 48 dp i passa a ser 108 dp.

```
res/mipmap-anydpi/ic_launcher.xml
```

https://developer.android.com/guide/topics/resources/drawable-resource

A partir d'Android 8.0 (API 26) es suporten les **icones adaptatives**
que es defineixen per capes `background` pel fons i
`foreground` pel motiu principal.
Això permet fer alguns efectes animant les capes per separat.

Si cal suportar versions anteriors:

```
res/mipmap-anydpi-v26/ic_launcher.xml
```

Si no a:

```
res/mipmap-anydpi/ic_launcher.xml
```

```
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@mipmap/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>
```

Les capes referenciades poden ser raster o vectorials,
s'escullen seguint les mateixes normes.

A partir d'Android 13 (API 33) es suporten les **icones themables**,
que afegeixen una nova capa `monochrome` a una tinta
que permet adaptarla al tema del sistema o de l'aplicació.

Si cal suportar versions anteriors:

```
res/mipmap-anydpi-v33/ic_launcher.xml
```

Si no a:

```
res/mipmap-anydpi/ic_launcher.xml
```

```
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@mipmap/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
    <monochrome android:drawable="@mipmap/ic_launcher_monochrome"/>
</adaptive-icon>
```



 


    





