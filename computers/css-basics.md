# CSS: Conceptes bàsics


## Què es CSS

No és un llenguatge de programació.
Es un llenguatge d'estilat:
diu com han de presentar-se els elements d'un HTML.

<div style="
	text-align: center;
	color: #ff6;
	padding-block: 30px;
	background-image: linear-gradient(150deg, transparent, black);
	margin-inline: auto;
	background-color: #770;
	border-radius: 5px;
	border-top: 20px #fa3 solid;
	font-weight: 900;
	font-size: 230%;
	box-shadow: 1px 2px 10px blanchedalmond;
	letter-spacing: 12px;
">
Hola món
</div>

De fet és aplicable a tots els formats XML,
això inclou, per exemple, l'SGV per gràfics vectorials,
o les interfícies de Flutter o Qt.

<svg viewBox="0 0 1220 100" xmlns="http://www.w3.org/2000/svg">
	<style>
		g {fill: red}
		rect { fill: #727; }
		rect.wide { fill: #dd9 }
		rect[rx='15'] { fill: #962; }
		rect[rx='50'] { fill: #277; }
	</style>
<g>
	<rect class="wide"  y="50" x="20" width="1100" height="10" />
	<rect width="100" height="100" />
	<rect x="120" width="100" height="100" rx="15" />
	<rect x="1100" width="100" height="100" rx="50" />
</g>
</svg>

Aquest document explica els conceptes bàsics sobre CSS

- Quina sintaxi general segueixen
- Cóm fer-los servir des de l'HTML
- Cóm seleccionar les dianes dels estils amb selectors
- Regles d'aplicació: Cascada, Herència i Especificitat
- Enumeració de
	- at-rules
	- pseudo-classes
	- pseudo-elements
	- unitats

Altres apunts expliquen altres aspectes:

- [Novetats](css.md)
- [Principis de dissen](css-design-principles.md)


## Anatomia d'un full d'estil

```css
/* comentari */
selector {
	propietat: valor; /* <- regla */
	propietat: valor;
} /* <- block */
```

- **Selector:** Selecciona a què elements s'apliquen les regles
- **Regla:** Representa un canvi del valor d'un atribut
- **Attribut:** Quelcom que volem canviar de la presentació: el color, el marge...
- **Valor:** Depenent de la propietat podem assignar diferents tipus de valor: distancies, colors...
- **Bloc (de regles):** un seguit de regles agrupades i encapçalades per un selector

Llevat dels blocks normals, també hi podem trobar regles `@`.
Les regles `@` comencen per `@keyword` on `keyword` especifica quin tipus de regla és.

```css
@regla-inline capcelera ... ;

@regla-de-block capcelera ... {
  block
}
```

## Inserció

### Inline: `style` attribute

A dintre dels elements html a l'atribut `style`.
No posem ni el selector ni les claus, només les regles.
El selector es implícit perque l'element afectat serà
l'element que té l'atribut.

```html
<p style="color: red; background-color: lightgrey">Hola món</p>
```
<p style="color: red; background-color: lightgrey">Hola món</p>

No es recomana fer-ho servir.
Va bé per provar coses ràpides, inclús editant a les eines de desenvolupament del navegador.
Però es molt poc mantenible, tendeix a la repetició de codi 

També és l'única manera que alguns clients de correu permeten estilar emails html.
Per aquest escenari, hi ha eines que converteixen els fulls d'estils a atributs `style`.

###  `<style>` element

```html
<style>
	h1 { color: red }
</style>
```

### External file: `<link>`


```html
<head>
  <link rel="stylesheet" href="mystyle.css" />
</head>
```

## Selectors bàsics

Els més comuns:

### Selector d'`element`

S'apliquen als elements amb aquest nom de tag html.

```css
/* Aplica color vermell a tots els elements h1 del document */
h1 {
	color: red;
}
```

```html
<h1>Aquest títol es veurà vermell</h1>
```


### Selector de `.classe`

Selecciona tots els elements l'atribut `class` dels quals
conté el nom de la clase que va després del punt.
L'atribut `class` pot tenir més d'una classe separades per espais.
Es el selector més comú i el recomanat de fer servir normalment.

```css
.myclass {
	color: purple;
}
```

```html
<div class="myclass otherclass">some text</div>
```

Els selectors de classe son més específics que els selectors d'element.
Quan a un element apliquen dos regles pel mateix attribut,
si un selector es d'element i l'altre és de classe, s'aplica el de classe.

Per exemple, en el següent html, si tenim activades les dos anteriors regles,
la de `h1` i la de `myclass`, com colisionen en l'atribut `color`,
s'aplica la de `myclass`.

### Selector d'`#identificador`

Seleccionen elements amb l'atribut `id`
amb el valor especificat darrera del signe `#`.

```css
#my-identifier {
	color: purple;
}
```

```html
<p id="my-identifier">title</p>
```

Tenen més especificitat que els selectors de classe.
Com que només pot haver un identificador igual a tot el document,
no és gaire comú ni aconsellable fer servir aquest tipus de selector.


### Selector de `::pseudo-element`

Seleccionen una **part interna** dels elements que no es un element per si mateix.
Per exemple, el punt que precedeix els elements `li` d'una llista `ul` s'accedeix amb `::marker`.
Van precedits per `::` i només poden ser certs valors
definits en l'estàndard dels quals no tots s'apliquen a tots els elements.

Tenen la mateixa especificitat que els selectors d'elements.

```css
/* Pinta la primera lletra de cada element en taronja */
::first-letter {
	color: orange;
}
/* pinta tots els punts de les llistes com a signes > */
::marker {
	color: purple;
	content: '> ';
}
```


Tenen molta importancia `::before` i `::after` que representen
uns components virtuals en tot element que estan just davant i darrera
d'ell i serveixen per inserir abans o despres contingut extra.


### Selector de  `:pseudo-classe`

Els selectors de pseudo-classe seleccionen els elements en certs **estats**.
Van precedits per `:`. Vigila que no son `::` com els pseudo-elements.
També estàn definits per l'estandard.

Tenen la mateixa especificitat que els selectors de classe.


### Selector d'`[attribut]`

Podem fer servir **els corxets `[]`** per seleccionar
elements pels seus attributs altres que `class` i `id`.

- `[my-attribute]` que té l'atribut
- `[my-attribute="value"]` que l'atribut coincideix exactament amb aquest valor
- `[my-attribute*="value"]` que l'atribut conté aquest valor
- `[my-attribute~="value"]` que l'atribut conté paraules separades per espais una de les quals es aquest valor
- `[my-attribute^="value"]` que l'atribut comença amb aquest valor
- `[my-attribute$="value"]` que l'atribut acaba amb aquest valor
- `[my-attribute|="value"]` que l'atribut és aquest valor o comença per ell i el segueix un guio (per matxar idiomes `ca` pero tambe `ca-ES`)

Té la mateixa especificitat que els selectors de classe.

### Selector universal `*`

Els selectors universals coincideixen amb tots els elements.
Normalment els farem servir en combinació amb altres
o per regles molt concretes d'abast global.

### Regles `@`

Si al lloc d'un selector ens trobem una `@`,
no és un selector, és una construcció especial, [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/At-rule).
Es fan servir per coses com ara:

- Condicionar regles:
	- `@media`:  segons [característiques](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries) del **dispositiu**: dimensions, capacitats...
	- `@support`: segons funcionalitats css supportades pel navegador
	- `@container`: segons dimensions de l'element contenidor
- Definir objectes especials:
	- `@keyframes`: punts clau d'una animació
	- `@counter-style` comptador per seccions, figures, teoremes...
	- `@color-profile` perfil de color `icc`
	- `@font-face`: d'on obtenir un tipus de lletra
	- `@property`: variables amb tipus i valor per defectea
- `@import`: inclusions (condicionades) des d'altres fitxers
- `@page`: format de pàginat
- `@namespace`: espai de noms xml per poder referenciar-los al css
- `@charset`: codificació de caracters del full d'estil.
- ...


## Combinacions de selectors

### Llista (`,`)

Quan separem selectors **amb comes**,
vol dir que la regla es donarà si **qualsevol**
dels selectors coincideix.

```css
selector1, selector2 { ... } /* les regles s'aplican a ambos selectors */
```

Seria equivalent en duplicar les regles per cada selector per separat.

```css
selector1 { ... }
selector2 { ... }
```

Poder especificar els selectors junts, redueix redundància al codi.

### Concurrents (sense separació)

Quan juntem selectors **sense espais entre ells**,
tots els selectors han de donar-se en el mateix element per seleccionar-ho.

::: columns
	::: column
		```css
		/* Tots els h1 que a més tinguin la class 'appendix' */
		h1.apendix { color: orange  }
		```
		```html
		<div class="apendix">classe sense h1</div>
		<h1>h1 sense classe</h1>
		<h1 class="apendix">h1 amb classe</h1>
		```
	::: column exemple-concurrents
		<style>
		.exemple-concurrents {
		  h1.apendix { color: orange  }
		}
		</style>
		<div class="apendix">classe sense h1</div>
		<h1>h1 sense classe</h1>
		<h1 class="apendix">h1 amb classe</h1>


### Descendents (<space>)

Quan **separem selectors amb espais**,
per exemple, `ancestor descendant`
estem seleccionant els elements seleccionats per `descendant`
que tingui com ancestre algun element seleccionat per `ancestor`.

No és necessari que siguin pare i fill directes.

::: columns
	::: column
		```css
		/* All p descendant of a section */
		.ancestor p { color: orange }
		```

		```html
		<p>Fora de section, no es seleccionarà</p>
		<div class="ancestor">
		  <p>Aquest es selecciona</p>
		  <div>
		    <p>Aquest, que no és directe, també</p>
		  </div>
		</div>
		```
	::: column exemple-descendants
		<!-- Fem trampa perque markdown ho trenca tot -->
		<style>
		.exemple-descendants {
		  .ancestor p { color: orange }
                }
		</style>
		<p>Fora de section, no es seleccionarà</p>
		<div class="ancestor">
		  <p>Aquest es selecciona</p>
		  <div>
		    <p>Aquest, que no és directe, també</p>
		  </div>
		</div>

En general, es desaconsella fer servir anidaments,
donat que quan la nostra fulla d'estils creix,
genera interaccions entre les regles complexes d'entendre,
i fa complex el manteniment.

### Fills (`>`)

Si separem dos selectors amb un `>`,
per exemple `selector_pare > selector_fill`,
seleccionem els elements que coincideixin amb el `selector_fill`
sempre se siguin fills directes d'elements seleccionats amb el `selector_pare`.

::: columns
	::: column
		```css
		.pare > p { color: orange }
		```

		```html
		<p>Aquest no està dintre del pare</p>
		<div class="pare">
		  <p>Seleccionarà aquest que és fill</p>
		  <div>
		    <p>Però no pas aquest que és un net</p>
		  </div>
		<section>
		```
	::: column exemple-fills
		<!-- Fem trampa perque markdown trenca el > -->
		<style>
		.exemple-fills {
		  .trampa { color: orange }
		}
		</style>
		<p>Aquest no està dintre del pare</p>
		<p class="trampa">Seleccionarà aquest que és fill</p>
		<p>Però no pas aquest que és un net</p>


Tot i que els seus efectes estan més controlats que el descendant,
també dona problemes de manteniment perque acoblem el css a l'estructura de l'html.
Si el fill deixa de ser directe, si interposem un contenidor en mig,
el selector deixarà de ser valid.


### Successor (`+`)

Quan separem els selectors amb **un signe  `+`**,
per exemple, `predecessor + successor`,
estem indicant que volem seleccionar
els elements que seleccioni `successor`
inmediatament després com a germans del mateix pare,
de un element que seleccioni `predecessor`.


<style>
.columns { display: flex; flex-direction: row; gap: 2rem; }
.column { flex: 1;}
</style>

::: columns
	::: column
		```css
		<style>
		.marcat + div { color: blue }
		</style>
		```
		```html
		<div class="marcat">Aquest es el marcat</div>
		<div>Aquest sera blau</div>
		<div>Però aquest germà ja no</div>
		```
	::: column exemple-successor
		<style>
		.exemple-successor {
			.marcat + div { color: orange }
		}
		</style>

		<div class="marcat">Aquest es el marcat</div>
		<div>Aquest serà taronja</div>
		<div>Però no pas aquest</div>


### Posterior (`~`)

L'operador posterior és al successor,
com el descendent al pare.
Es un germà posterior pero no ha de ser inmediatament el següent.

::: columns exemple-posterior
	::: column
		```css
		.marcat ~ div { color: orange }
		```

		```html
		<div class="marcat">Aquest es el marcat</div>
		<div>Aquest serà taronja</div>
		<div>I aquest també</div>
		```
	::: column
		<style>
		.exemple-posterior {
		.marcat ~ div { color: orange }
		}
		</style>

		<div class="marcat">Aquest es el marcat</div>
		<div>Aquest serà taronja</div>
		<div>I aquest també</div>

### Anidament `&`

L'anidament de blocs ens estalvia codi repetit i agrupa regles conceptualment.
Simplement cal definir un bloc dintre de les claus d'un altre:

Per defecte selector pare i fill generen un selector descendent.
Respon a l'estructura que s'espera a l'html

::: columns
	::: column

		```css
		.pare {
		  .fill {
			...
		  }
		}
		```
	::: column

		```css
		/* Equivalent a */
		.pare .fill { ... }
		```

Però si el selector fill conté `&`,
llavors el selector fill resultant es construeix
substituint el `&` per el selector pare.

::: columns
	::: column

		```css
		.pare {
		  &.fill1 { ...  } /* sense espai! */
		  & .fill2 { ...  } /* igual que sense & */
		  & > .fill2 { ...  }
		  .avi & { ...  } /* ordre invertit */
		}
		```
	::: column
		```css
		/* Equivalent a */
		.pare.fill1 { ... }
		.pare .fill2 { ... }
		.pare > .fill3 { ... }
		.avi .pare  { ... }
		```



## Resolució css, la cascada

### L'algoritme

Resol quines regles s'acaban aplicant.
A de cada passa, si encara hi ha selectors en conflicte, es es considera la següent passa.

- Relevancia: Primer es mira quines regles s'apliquen o no a una diana segons el selector
- Origen e importància:
	- Navegador-Autor-Usuari-Keyframes-Importants(Usuari-Autor-Navegador)-Transitions
	- Els importants no només s'imposen, sino que inverteix la prioritat dels origens
	- Les animacions de keyframes s'imposen a les regles normals
	- Les animacions de transició s'imposen a totes les regles.
- Capes: Si l'origen és el mateix, capes
	- Capa1-Capa2-..-Sense Capa-Inline-Important(Sense Capa-...-Capa2-Capa1-Inline)
	- Les capes en ordre d'aparicio, després les que no tenen capa
	- Important s'imposa invertint la prioritat de les capes i sense capa
	- Inline sempre s'imposa dintre de les importants i dintre de les no importants
- Especificitat: La que té major vector d'especificitat, es queda
- Scoping proximity (No Firefox 2024): S'imposa la regla l'scope de la qual es un ancestre més proper
	- L'scope per defecte es `:root`
	- Podem definir un nou scope amb `@scope(selector) { blocks de regles }`
- Ordre d'aparició: La darrera regla que apareix és la que queda

### Especificitat

Quan apliquem les regles a un element es prioritzen,
primer, per especificitat i,
si coincideixen en especificitat, després per l'ordre en que estan (ordre de cascada).
L'especificitat es un vector multi component que depén del selector que ha fet aplicar la regla.

Els estils posats inline tenen una especificitat especial de 4art nivell.
Només els podem sobrescriure amb regles `important!` que puja l'especificitat a nivel 4,
cosa totalment no recomanada.

Cada subselector que composa el selector incrementa o no una de les components.
La primera component es menys específica.


- No pujen especificitat
	- Selector universal `*`
- Pujen la 1a component
	- **elements**
	- pseudo-elements
- Pujen la 2a component
	- **class**
	- pseudo-class
	- atribut
- Pujen la 3a component
	- **identificador**

- Aquestes funcions adopten l'especificitat del subselector més específic entre parèntesis
	- `:is()` i tot el que tingui a dintre de la funció
	- `:has()`


### Herència

Què passa quan les regles no assignen explícitament un valor a una propietat?

- L'especificació de cada propietat diu si és heretada (ex `color`) o no ho és (ex. `border`).
- Si ho és, agafa el valor del pare (equivalent a `inherit`).
- Si no ho és, o és l'element arrell (`:root`) agafarà el valor per defecte (`initial`).
- El valor especial `unused` és equivalent a no tenir-ne especificat valor (`inherit` o `initial` segons s'escaigui)

Procés de càlcul

- Herencia/Initial -> Cascada -> Specified Value
- Canvis especificats -> **Computed Value** (ex. L'especificació diu que si un span en mode absolut, canvia el seu display a block)
- Aplicació dels layouts -> **Used Value** (ex. Molts valors es dedueixen d'aplicar els layouts)
- Limitacions del entorn -> **Actual value** (ex. Discretització a pixel o a les fonts disponibles)


## At-rules

Les at-rules son sentencies especials que podem introduir en el full d'estils per diferents funcions.

### `@import`

Aquest regla permet organitzar les fulles d'estils en diferents fitxers.
En el seu ús més bàsic és:

```css
@import './file.css';
@import url(./file.css);
```

També és útil per evitar carregar regles innecessàries
condicionant la càrrega a situacións específiques:

- Les funcionalitats que soporta el navegador: `supports (not (display: grid) and (selector(:has(a))`
- El tipus de mitjà: `screen` o `paper`, `orientation(landscape)`, `(max-width: 400px)`...



```css
@import './file.css' supports(not (display: grid) and (selector(:has(a))) screen ;
```

### `@support`

Define de forma condicional bloques de reglas o reglas
si el navegador soporta las funcionalidades indicadas.

```css
@support supports (not (display: grid) and (selector(:has(a)) {
	:has(p) {
		...
	}
}
```

### `@media`

Tambien llamadas media-queries.
Define de forma condicional bloques de reglas o reglas
si el medio tiene las características descritas.

### Altres

- `@media` -- declaració condicional de regles depenent de les dimensions format i tecnologia (print, screen) del mitjà
- `@container` -- declaració condicional de regles depenent del tamany contenidor (similar que les media queries, pero més útil, i menys suportat)
- `@support` -- declaració condicional de regles depenent de les funcionalitats que suporta el navegador
- `@page` -- defineix el format de pàgina a medis paginats
- `@keyframes` -- defineix animacions de propietats via punts claus
- `@counter-style` -- defineix un tipus de numeració (figures, llistes, seccions...)
- `@property` -- (poc suportat) permet definir una propietat personalitzada (com les variables pero animables)
- `@color-profile` --
- ...

## Llistats

### Pseudo-elements

Parts internes dels elements que es poden estilar independentment.

#### Generals

- `::before`: aplica a un element virtual que està just abans de cada element
- `::after`: aplica a un element virtual que està just darrera de cada element
- `::first-line`: aplica a la primera linia del contingut
- `::first-letter`: aplica a la primera lletra del contingut
- `::selection`: aplica al text seleccionat

#### Altres molt més específics (pel elements específics): 

- `::placeholder`: aplica a el text substitutori a alguns camps de formulari.
- `::marker`: aplica a la gorguilla
- `::file-selector-button`: aplica al botó de l'input de selecció de fitxers.
- `::spelling-error`: aplica al contingut editable que conté errors d'ortografia
- `::grammar-error`: aplica al contingut editable que conté errors de gramàtica
- `::cue`: aplica als subtítols d'un element `video`
- `::backdrop`: aplica a l'element que tapa el fons quan es mostra un element `dialog`

### Pseudo-classes

Representen situacions o estats dels elements.

#### Structural

- `:root`: l'arrel del document, normalment `html`
- `:empty`: element que com a molt conté espais
- `:nth-child()` fill a la posició, permet formules de n com `2n+1` per agafar els imparells, també `odd` o `even`
- `:nth-last-child()` comptant pel final
- `:nth-of-type()` i `:nth-last-of-type()`: nomes compten els selecciontat per la resta de selectors
- `:first-child`: equival a `nth-child(1)`
- `:last-child`: equival a `nth-last-child(1)`
- `:only-child`: si no té germans (equival a `:first-child:last-child`)

#### Interacció

- `:hover` el ratoli passa per damunt
- `:active` l'usuari està interactuant (pe. fent click)
- `:focus` l'element té el focus de teclat
- `:focus`: quan l'element te el focus de teclat
- `:focus-within`: quan l'element o algun fill té el focus de teclat

#### Visualització

- `:fullscreen`: quan l'element esta en mode pantalla complerta
- `:modal`: quan l'element (dialeg, popup...) exclou la interacció amb la resta d'elements
- `:picture-in-picture`: quan l'element, normalment un video, està extret a una subfinestra de reproducció fora de la pàgina

#### Controls

- `:enabled` camp amb interaccio habilitada
- `:disabled` camp amb la interacció deshabilitada
- `:read-only` quan no es pot modificar el valor
- `:read-write` quan si es pot modificar el valor
- `:blank`: camp sense contingut (no confondre amb `:empty`
- `:placeholder-shown`: si el control mostra el placeholder (normalment perque està buit, pero no sempre)
- `:autofil`: camp ha estat omplert pel navegador
- `:default`: camp (checkbox, radio, select option) seleccionada inicialment.
- `:required`: camp requerit
- `:optional`: camp no requerit
- `:valid`: camp valid
- `:invalid`: camp invalid
- `:user-valid`: camp valid després que l'usuari interactui
- `:user-invalid`: camp invalid després que l'usuari interactui
- `:in-range`: camp amb limitacio d'abast, dintre de l'abast
- `:out-range`: camp amb limitacio d'abast, dintre de l'abast
- `:checked`: radio o checkbox marcat
- `:indeterminate`: radio o checkbox en estat indeterminat

#### Funcionals

- `:is()`: concorda a qualsevol dels selectors dintre dels parèntesis (separats per comes)
- `:has()`: Com el descendant pero queda seleccionat el pare no el descendant.
- `:where()`: concorda amb el contingut igual que si no hi hagues el where però, no puja l'especificitat
- `:not()`: concorda amb tot el que no concordi amb el selector a dintre dels parèntesis

