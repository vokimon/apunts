# CSS: El modelo de caja

## Partes de la caja

El modelo de caja, es la base para la maquetación (layout).

Considera que cada elemento es una caja que tiene que albergar 4 niveles de espaciado:

- un contenido con un ancho y un alto
- un relleno (`padding`) alrededor del contenido
- un borde (`border`) alrededor del relleno que delimita la caja
- un margen (`margin`) alrededor del borde que no pueden ocupar otras cajas

La caja también puede tener otros elementos
que se ignoran de cara a la maquetación:

- un contorno (`outline`) que hace de segundo borde por fuera
- una sombra (`box-shadow`) que replica de la forma de la caja desplazada y difuminada

<div style="float: right; border: solid; margin: 5pt;">
<div style="
	margin: 15pt;
	background: grey;
	color: white;
	padding: 10pt;
	border: 5pt dashed blue;
	outline: 5pt dotted red;
	box-shadow: 5pt 5pt 1pt green;
">Content</div>
</div>

En este ejemplo, vemos todos estos elementos:
la caja (gris) que incluye contenido, relleno y borde (en azul).
Fuera de la caja, el contorno (rojo) y la sombra (verde) que queda por detrás.
El margen es transparente y mantiene al resto de elementos a 20px de distancia
del contenido en gris.
Esto incluye el borde negro del contenedor que nos da una idea del alcance del margen.

<style>
@keyframes movingoutlineshadow {
  0%   { outline-width: 5pt; box-shadow: green 5pt 5pt 4pt }
  20%  { outline-width: 5pt; box-shadow: green 5pt 5pt 4pt }
  40%  { outline-width: 25pt; box-shadow: green 5pt 5pt 4pt }
  60%  { outline-width: 5pt; box-shadow: green 5pt 5pt 4pt }
  80%  { outline-width: 5pt; box-shadow: green 25pt 25pt 25pt 10pt }
  100% { outline-width: 5pt; box-shadow: green 5pt 5pt 4pt }
}
</style>
<div style="float: right; border: solid; margin: 5pt;">
<div style="
	animation: movingoutlineshadow 6s infinite;
	margin: 15pt;
	background: grey;
	color: white;
	padding: 10pt;
	border: 5pt dashed blue;
	outline: 5pt dotted red;
	box-shadow: 20pt 20pt 4pt green;
">Content</div>
</div>

Este otro ejemplo muestra que,
si expandimos la sombra o el contorno más allá del margen,
estos empiezan a solaparse con los elementos contíguos,
pero no afecta en nada a la disposición de la caja ni de su entorno,
que es la misma que en el anteriór ejemplo.


## Orientaciones física y lógica

Al indicar las propiedades de una caja
podremos asignar distintos valores para cada
uno de los cuatro puntos cardinales.

Las cuatro **orientaciones físicas (o de papel)** son `top`, `left`, `bottom` y `right`.

Cuando planteamos un diseño multiidioma hay que tener presente
hay idiomas que se escriben de derecha a izquierda (como el árabe y el hebreo)
e incluso algunos que se escriben verticalmente (como muchos asiáticos).

Muchas de las decisiones de diseño no dependen tanto de las orientaciones físicas
sinó de cual es el flujo de lectura.

Por eso, en esos casos, conviene usar las **direcciones lógicas (o de flujo de lectura)**
que se mapean a una o otra orientación física dependiendo del **modo de escritura** del idioma.
Esas direcciones son: `inline-start`, `inline-end`, `block-start`, `block-end`.

Colocamos las letras de `inline-start` a `inline-end` formando una linea o columna.
Cuando esta se completa vamos creando más en dirección de `block-start` a `block-end`.

| dirección logica | física en latino | fisica en árabe | física tategaki |
|---|---|---|---|
| `inline-start`   | `left` | `right` | `top`
| `inline-end`   | `right` | `left` | `bottom`
| `block-start`   | `top` | `top` | `right`
| `block-end`   | `bottom` | `bottom` | `left`
| `block` | `vertical`    | `vertical` | `horizontal`
| `inline` | `horizontal`    | `horizontal` | `vertical`

Cuando mencionemos `propiedad-{direction}`,
`{direction}` será cualquiera de estas direcciónes físicas y lógicas.

Algunas propiedades son atajos para dar valor a varias direcciones.
Dependiendo del número de valores, se repartiran de la siguiente manera:

- 4 valores: top right bottom left (sentido horario desde las 12)
- 3 valores: top right/left bottom (las horizontales juntas)
- 2 valores: top/bottom right/left (tambien las verticales, queda: vertical y horizontal)
- 1 valor: el mismo valor para las cuatro direcciones

Como extension de lo anterior siempre que especifiquemos cosas vertical y horizontal,
siempre primero vertical y despues horizontal.
Por ejemplo, para indicar una esquina, usaremos `bottom-left` y no <strike>`left-bottom`</strike>.

Vemos un ejemplo con la propiedad `padding` y el resto son equivalentes.

## Disposición interna y externa

Cada elemento tiene un modo de despliegue interno y otro modo interno.
Ambos estan controlados por su atributo `display`.

La disposición interna es la que define como se dispondran los hijos dentro suyo.
Por defecto, se disponen en modo `flow`, pero existen otros: `flex`, `grid`, `table`...

El modo de despliegue externo determina como el elemento se comporta dentro
de otro elemento contenedor y hay dos modos:

- **Block:**
	- La caja empezara en una línea (o columna) nueva.
	- Se respetara los atributos `width` y `height`.
	- Los margenes, bordes y padding, expulsan otros elementos.
	- La caja se expandira en la dirección inline todo lo posible.

- **Inline:**
	- La caja se mantendrá en la línea empezada.
	- Las propiedades `width` y `height` se ignoran.
	- Margenes, bordes, padding... se dibujan pero solo expulsan otros elementos en horizontal, no en vertical
	- La caja se divide en varias líneas. (Cada linea que ocupe el elemento tendra borde)

Ambas se controlan con la propiedad `display`.
En CSS moderno deberiamos usar dos valores: uno para el modo interno y otro para el externo.
Pero, por legado, los aspectos interno y externos no estan bien separados.
Y hay palabras que usadas solas establecen los dos modos:

- Cuando definimos `display` como `block` o `inline`,
estamos poniendo el interno implicitamente a `flow`.
- Cuando definimos `display` como `flex` o `grid`
estamos definiendo el externo como `block`.
- Los valores `inline-flex` y `inline-grid` establecen `inline` y `grid` o `flex`

## Tamaño (`size`)

Por defecto el tamaño de la caja lo determina el navegador según el layout.

- En el layout `flow`,
una caja `block` se expandirá 100% en dirección horizontal (`inline`)
y, verticalmente, se ajustará a lo que ocupe el contenido.

A partir de ahí, podemos explicitar o restringir con algunas propiedades.

- Las propiedades `width` y `height` pueden explicitar ese tamaño.
- Las propiedades `max/min-width/height` limitan tanto
el valor calculado por el navegador como el que explicitemos con `width` o `height`.
- La propiedad `aspect-ratio` fija una relación entre `width` y `height`,
al menos que las dos estén explícitadas o les afecte una limitación.
- Si queremos usar direcciones de flujo,
usaremos las propiedades `[max/min-]block/inline-size`.

Los valores que pueden tomar los atributos de tamaño son:

- `auto`: Valor por defecto. Lo que diga el navegador.
- Una longitud con unidades (o una formula usando `max`, `min`, `clamp`, `calc`...)
- Los porcentajes son relativos al tamaño del contenedor en la dirección
	- Si el tamaño del contenedor depende del contenido, es como si lo dejamos a `auto`.
	- Por ejemplo, en `flow`, si no explicitamos la altura del contenedor.
- `min-content`: El mínimo que pide el contenido. Por ejemplo, la palabra más larga de un parrafo.
- `max-content`: El máximo que pide el contenido. Por ejemplo, lo que ocupa todo el parrafo expandido en una línea.
- `fit-content(value)`: cogera el valor, limitado por `min/max-content`
- `fit-content`: lo que diga el navegador, limitado por max/min-content (`fit-content(auto)`)

### Box sizing hasta el borde

El tamaño que fijamos con estas propiedades se refiere por defecto
a lo que ocupará el contenido, excluyendo padding y borde.
A menudo eso dificulta los calculos para el layout,
por eso a menudo se define `box-sizing: border-box`
que hace que se cuenten borde y padding para el tamaño.

Si definimos el `box-sizing` de forma global,
se rompen los componentes definidos de la forma tradicional.

La solución es definirlo globalmente así:

```css
html {
  box-sizing: border-box;
}
*, *:before, *:after {
  box-sizing: inherit;
}
```

Y para el componente antiguo, definir:

```css
.my_old_component {
  box-sizing: content-box;
}
```

## Relleno (`padding`)

El padding es un relleno o cojín entre el contenido y el borde de la caja.
La metáfora sería el relleno que se pone en un paquete para que
el contenido no dé golpes.

Se puede especificar un relleno diferente en cada una de las cuatro direcciones.

Formas de especificarlo:

```css
.midiv {
	/* direcciones especificas, el resto acaba dando valores a estas */
	padding-top: 3px;
	padding-right: 3px;
	padding-bottom: 3px;
	padding-left: 3px;

	/* atajos */
	padding: 2px; /* el mismo valor en las 4 direcciones */
	padding: 1px 2px 3px 4px; /* top left bottom right, clock-wise order */
	padding: 100px 30px;  /* top/bottom left/right */
	padding: 100px 30px 1px;  /* top left/right bottom */

	/* direcciones lógicas específicas */
	padding-inline-start: 1rem; /* inicio en dirección de linea (left para latino) */
	padding-inline-end: 1rem; /* final en dirección de linea (right para latino) */
	padding-block-start: 1rem; /* inicio en direción de bloque (top para latino) */
	padding-block-end: 1rem; /* fin en direción de bloque (bottom para latino) */

	/* atajos direcciones lógicas */
	padding-block: 2rem; /* a la vez direcciones de bloque (up y bottom para latino) */
	padding-inline: 40px; /* a la vez direcciones de linea (left y right para latino) */
	/* experimental */
	padding: logical 2px; /* el mismo en las 4 direcciones, no cal */
	padding: logical 1px 2px 3px 4px; /* block-start line-end block-end line-start, clock-wise order if latin */
	padding: logical 100px 30px;  /* block inline */
	padding: logical 100px 30px 1px;  /* block-start inline block-end */
}
```

::: warning "Error típico"
	_Usar porcentajes para hacer el padding vertical proporcional a la altura del contenedor_

	Cuando especificamos un padding vertical (block) con un porcentage,
	no se toma el alto del contenedor como referencia,
	sinó su ancho (inline).

	<div style="
		width: 100px;
		height: 200px;
		background: grey;
		float: right; margin-inline: 1rem; padding:2px;
	">
	<div style="background: lightgrey; padding: 20% 20%;">XXXXX</div>
	</div>

	En el siguiente ejemplo,
	el padding de la caja interna está fijado al 20% en todas las direcciones.
	Se observa que resulta el mismo padding horizontal y vertical,
	aunque la caja contenedora sea el doble de alta que de ancha.
	Se está tomando el 20% del ancho en todas las direcciones.
	```html
	<div style="
		width: 100px;
		height: 200px;
		background: #f77;
		float: right; margin-inline: 1rem; padding:2px;
	">
		<div style="background: #7f7; padding: 20% 20%;">XXXXX</div>
	</div>
	```

## Borde (`border`)

El borde es una línea que decora el extremo de la caja marcando su límite.
Está fuera del padding pero sigue siendo parte de la caja de cara al maquetado.

También por ser parte de la caja,
se le aplica el fondo (background) de la caja,
aunque, a menudo, el mismo borde lo tape.

La línea de borde tiene 3 atributos: ancho `width`, estilo `style` y color `color`.

El estilo por defecto es `none`.
Eso quiere decir que si no cambiamos ese valor, no se añadira ningún borde,
aunque cambiemos los otros atributos.

El color por defecto es la propiedad `color` del elemento.

Y la anchura, que puede ser una longitud positiva o una de las palabras `thin`, `medium`, `thick`,
tiene como valor por defecto `medium`.
Cabe decir que no está especificado a que longitud corresponde `medium`,
así que si quieres resultados coherentes entre navegadores, siempre
asignale un valor con unidades.

Los estilos posibles son:

<div style="color: #aae; float: right; clear: both; margin: 15pt; flex-flow: column wrap; display: flex; justify-content: space-between; gap: 5pt">
<div style="padding: 5pt; border-style: solid;  border-width: 5pt">Solid</div>
<div style="padding: 5pt; border-style: dotted; border-width: 5pt">Dotted</div>
<div style="padding: 5pt; border-style: dashed; border-width: 5pt">Dashed</div>
<div style="padding: 5pt; border-style: double; border-width: 5pt">Double</div>
</div>

- Invisibles:
	- `none`: Sin borde (por defecto).
	- `hidden`: Sin borde. Pero con prioridad collapsando en tablas.
- Planas:
	- `solid`: Una linea plana
	- `dotted`: Puntos
	- `dashed`: Rayas
	- `double`: Dos lineas paralelas

<div style="color: #aae; float: right; clear: both; margin: 15pt; flex-flow: column wrap; display: flex; justify-content: space-between; gap: 5pt">
<div style="padding: 5pt; border-style: ridge; border-width: 5pt">Ridge</div>
<div style="padding: 5pt; border-style: groove; border-width: 5pt">Groove</div>
<div style="padding: 5pt; border-style: inset; border-width: 5pt">Inset</div>
<div style="padding: 5pt; border-style: outset; border-width: 5pt">Outset</div>
</div>

- Sombreadas: Usa un tono más oscuro del color base para generar un efecto sombreado 3D noventero.
	- `ridge`: Simula un marco sobresaliente  `/\______/\`
	- `groove`: Simula un surco alrededor del contenido `\/--------\/`
	- `inset`: Simula que el contenido està hundido `\______/`
	- `outset`: Simula que el contenido sobresale `/--------\`
	- Los colores que no sean negros, usa una version del color oscurecido.
	- Al menos en Firefox, el negro se comporta diferente, usando tonos de gris.

Para especificar los atributos `width`, `style`, `color` en cada dirección:
`border{-direction}{-attribute}`.
Las direcciones son las mismas que para el padding:
`top`, `right`, `bottom`, `left`, las multicultis `inline/block[-start/end]`.

Los atajos `border{-attribute}` permiten fijar el atributo en las cuatro direcciones a la vez.
Se pueden usar 4, 3, 2 o 1 valores igual que con el padding:

- 4: con las agujas del reloj empezando a las 12
- 3: el left toma el valor del right
- 2: block inline
- 1: para todas las direcciones

Los atajos `border{-direction}` permiten fijar los tres atributos a la vez en una direccion.

El atajo `border` permite especificar los 3 atributos en las 4 direcciones a la vez,
pero no permite especificar distintos valores para cada dirección como permiten `padding` o `border{-attribute}`.

::: warning "Error típico"
	<div style="float: right; width: 200pt">
		<div style="padding: 15pt; border-style: dotted; border-color: red; border-left: solid">Content</div>
	</div>

	_Usar propiedades especificas de dirección para setear solo un atributo_

	`border-color: red; border-left: solid;`

	Si no damos uno de los valores a una propiedad que se espera valores
	para los tres atributos, cogera los valores por defecto.
	Es lo que pasa en la segunda declaración,
	que sobrescribe el rojo con el color del elemento (negro).
	Si solo ponemos el color o el grosor, seria más catastrófico,
	porque estaria cogiendo el estilo por defecto que es `none`.

	Solución en este caso, explicitar los otros valores o usar `border-left-style`

::: warning "Error típico"
	_Usar porcentajes para el grosor del borde_

	CSS no soporta porcentajes en los bordes.
	Una declaración que incluya porcentaje se ignorará.

	Como los bordes se suelen declarar en atajos
	con varias propiedades es más complicado
	detectar que el problema está en el porcentaje.



### Border image

Las imágenes de borde permiten establecer un estilo de borde personalizado
a partir de una imagen.

TODO

```css

```

TODO: Setting `border{-direction}` property sets `border-image` to none


## Margen (`margin`)

El margen es una distancia mínima de exclusión que se establece
para un bloque en cada dirección desde su borde
hasta la caja adjacente en esa dirección
o, en su defecto,
hasta el límite del espacio disponible para colocar los elementos.

- Es transparente, no se le aplica el background.
	- Al contrario del borde y el padding, que si se les aplica el background.
- Los margenes expresados en porcentajes, tanto verticales como horizontales,
  son relativos a la anchura (¡horizontal!) del bloque contenedor.
- Los margenes verticales de cajas adyacentes a menudo se solapan **colapsandose**.
	- De los dos, se toma el mas grande para separar.
	- Da igual que sea de otro nivel, si hay no hay contenido en medio
	- El margen no expande el contenedor

Formas de especificarlo:

```css
.midiv {
	margin: 2px; /* el mismo margen en las 4 direcciones */
	margin: 1px 2px 3px 4px; /* top left bottom right, clock-wise order */
	margin: 100px 30px;  /* vertical horizontal */
	margin: 100px 30px 1px;  /* top horizontal bottom */
	margin-top: 3px;
	margin-right: 3px;
	margin-bottom: 3px;
	margin-left: 3px;
}
```

<div style="float: right; clear: both; margin: 5pt;">
<div style="
	margin: 15pt;
	background: grey;
	color: white;
	padding: 10pt;
	outline: 2pt dashed red;
	outline-offset: 15pt;
">Content</div>
<div style="
	margin: 15pt;
	background: grey;
	color: white;
	padding: 10pt;
	outline: 2pt dotted green;
	outline-offset: 15pt;
">Content</div>
</div>

Los márgenes de dos cajas adjacentes en la dirección de bloque **se colapsan**.
El resultado es que de dos cajas adjacentes, de sus margenes, se toma el mayor.

::: warning "Error típico"

	_Esperar que la distancia entre dos cajas sea la suma de los márgenes_

	Dentro de un contexto de flujo normal los margenes se colapsan.
	Los elementos de flex o grid o table estan aislados y no collapsan márgenes.

<div style="float: right; margin: 5pt;">
<div style="
	margin: 15pt;
	background: grey;
	color: white;
	padding: 0;
	outline: 2pt dashed red;
	outline-offset: 15pt;
">Content
<div style="
	margin: 15pt;
	background: darkgrey;
	color: white;
	padding: 10pt;
	outline: 2pt dotted green;
	outline-offset: 15pt;
">Content</div>
</div></div>

También se collapsan los márgenes en la dirección de bloque (vertical)
de elementos anidados.

Un colapso que no se produce si entre los margenes
hay un padding, un borde o contenido.
En el ejemplo, se colapsa el margen inferior
pero el superior no porque hay contenido de por medio.

### Margen `auto`

<div style="float: right; margin: 5pt; background: lightgrey; width: 120pt; font-size: 70%">
<div style="background: grey; color: white; padding: 10pt; width: fit-content; margin: 3pt;  margin-left: auto">margin-left: auto</div>
<div style="background: grey; color: white; padding: 10pt; width: fit-content; margin: 3pt;  margin-right: auto">margin-right: auto</div>
<div style="background: grey; color: white; padding: 10pt; width: fit-content; margin: 3pt;  margin-inline: auto">margin-inline: auto</div>
</div>

Los márgenes horizontales (inline) con valor `auto` se reparten
el espacio disponible.
Esto puede servir para centrar elementos, distribuirlos
con separacion uniforme o proporcional, o justificarlos a un lado.
Para que haya espacio disponible,
la caja ha de tener un `width` no `auto` y menor que el disponible.







## Esquinas redondeadas (`border-radius`)

<div style="float:right">
<div style="background: grey; margin: 15pt; padding: 15pt; border-radius: 15pt">
Circular
</div>
<div style="background: grey; margin: 15pt; padding: 15pt; border-radius: 30%">
Percent
</div>
<div style="background: grey; margin: 15pt; padding: 15pt; border-radius: 20pt / 10pt">
Elliptical
</div>
<div style="background: grey; margin: 15pt; padding: 15pt; border-radius: 90% 20%">
Rampant
</div>
</div>

Border radius permite hacer redondeadas las esquinas de la caja.

- Las 4 esquinas se enumeran empezando por la `top-left` en sentido de las manecillas del reloj
- Cada esquina tiene dos radios, uno horizontal (inline) y otro vertical (block).
  2 direcciones x 4 esquinas = 8 valores a calcular
- Propiedades específicas:
	- `border-{top|bottom}-{left|right}-radius: h-radius [v-radius]`
	- Si no se especifica radio vertical, se supone igual que el horizontal
- Propiedad atajo:
	- `border-radius: tlh [trh [brh [blh]]] [ / tlv [trv [brv [blv]]]]`
	- La barra separa los horizontales (h) de los verticales (v)
	- si no hay barra, se toman los valores horizontales también para los verticales
	- si falta bottom-left, se coge el valor de top-right
	- si falta bottom-right, se coge el valor de top-left
	- si falta top-right, todos tiene el valor de top-left
- Los porcentajes se refieren al tamaño de la caja en su dirección
	- Si se da el mismo porcentaje para horizontal y vertical, las distancias derivadas pueden no ser iguales
- Si los tamaños de los radios calculados en uno de los lados de la caja supera su tamaño,
  todos los radios, aunque no estén implicados en ese exceso, se ajustan proporcionalmente.

```css
border-radius: 10pt 20pt; /* top-left/bottom-right a 10pt, bottom-left/top-right a 20pt */
border-radius: 10pt 20pt 30pt; /* top-left a 10pt, bottom-left/top-right a 20pt, bottom-right a 30pt */
border-radius: 10pt / 20pt; /* radios horizontales a 10pt, verticales a 20pt */
```

::: warning "Error típico"
	<div style="float:right">
	<div style="background: grey; margin: 15pt; border-radius: 90% 20%">
	Exceding border
	</div>
	</div>

	_No mantener un padding mínimo como el máximo border radius_

	El padding es la distancia entre el contenido y el borde,
	pero el borde sin redondear.
	Cuando redondeamos el borde, si no añadimos padding suficiente,
	puede que el contenido se vea fuera de la caja en las esquinas.



## Contornos (`outline`)

<div style="float: right; border: solid; margin: 5pt;">
<div style="
	margin: 15pt;
	background: grey;
	color: white;
	padding: 10pt;
	border-top-left-radius: 20pt;
	border: 10pt dashed blue;
	outline: 5pt dotted red;
	box-shadow: 5pt 5pt 1pt green;
">Content</div>
</div>

El **contorno** es una segunda línea resiguiendo por fuera el borde.
Es el mismo elemento que usan los navegadores para **indicar el foco del teclado**.
**¡Ojo! ¡Procura no interferir con esta funcionalidad de accesibilidad del navegador!**

A diferencia del borde, la caja no se amplia para abarcarlo:
no tiene background y su presencia o grosor no afecta a la maquetación.

Tiene los mismos atributos de línea que border: `style`, `color` y `width`.
Se pueden setear por separado con `outline-{attribute}` o a la vez con el atajo `outline`.
A diferencia de border, no se puede establecer valores diferentes para cada direccion.
No tiene `radius` pero se adapta al `border-radius` de `border` como se ve en los ejemplos.

<style>
@keyframes moveoutline {
	0% { outline-offset: 0 }
	10% { outline-offset: 0 }
	40% { outline-offset: 20pt }
	50% { outline-offset: 20pt }
	60% { outline-offset: -8pt }
	65% { outline-offset: -8pt }
	100% { outline-offset: -40pt }
}
</style>
<div style="float: right; border: solid; margin: 5pt;">
<div style="
	animation: moveoutline infinite 8s alternate;
	margin: 15pt;
	background: grey;
	color: white;
	padding: 10pt;
	border-top-left-radius: 10pt;
	border: 10pt dashed blue;
	outline: 5pt dashed red;
	box-shadow: 5pt 5pt 1pt green;
">Content</div>
</div>

Un atributo más, `outline-offset`, define la separación del borde al outline
Se puede indicar un offset negativo para ponerlo dentro de la caja
Si el offset negativo supera las dimensiones de la caja, el outline desaparece

::: warning Accesibilidad
	Los navegadores usan el outline para indicar foco en los elementos que reciben eventos del teclado.
	Si una regla css quita incondicionalmente el outline (`none` o `0`),
	por ejemplo porque es más específica que la que usa el navegador para el focus,
	los usuarios no verán dicha indicación y afectará a la accesibilidad.


## Sombra (`box-shadow`)

<style>
@keyframes rotateshadow {
	0%   { box-shadow: rgb(0 0 0 / .5) 0pt 0pt }
	10%  { box-shadow: rgb(0 0 0 / .5) 5pt 5pt }
	20%  { box-shadow: rgb(0 0 0 / .5) 5pt 0pt }
	30%  { box-shadow: rgb(0 0 0 / .5) 5pt -5pt }
	40%  { box-shadow: rgb(0 0 0 / .5) 0pt -5pt }
	50%  { box-shadow: rgb(0 0 0 / .5) -5pt -5pt }
	60%  { box-shadow: rgb(0 0 0 / .5) -5pt 0pt }
	70%  { box-shadow: rgb(0 0 0 / .5) -5pt 5pt }
	80%  { box-shadow: rgb(0 0 0 / .5) 0pt 5pt }
	90%  { box-shadow: rgb(0 0 0 / .5) 5pt 5pt }
	100% { box-shadow: rgb(0 0 0 / .5) 0pt 0pt }
}
@keyframes blurshadow {
	0%   { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 0pt }
	100%  { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 7pt }
}
@keyframes colorshadow {
	0%   { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 2pt }
	25%  { box-shadow: rgb(0 150 0 / .5) 5pt 5pt 2pt }
	50%  { box-shadow: rgb(150 0 0 / .5) 5pt 5pt 2pt }
	75%  { box-shadow: rgb(0 0 150 / .5) 5pt 5pt 2pt }
	100% { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 2pt }
}
@keyframes spreadshadow {
	0%   { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 2pt 0pt }
	25%  { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 2pt 8pt }
	50%  { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 2pt 0pt }
	75%  { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 2pt -2pt }
	100% { box-shadow: rgb(0 0 0 / .5) 5pt 5pt 2pt 0pt }
}
.shadow-example {
	color: black;
	background: lightblue;
	border: solid 2pt #0aa;
	margin: 15pt;
	padding: 5pt 10pt;
	border-bottom-left-radius: 15px;
}
</style>
<div style="float: right; width: 100pt; margin: 0 20pt; border: solid black; background: white">
<div class="shadow-example" style="animation: rotateshadow 5s linear infinite;">Offset</div>
<div class="shadow-example" style="animation: blurshadow 3s linear alternate infinite;">Blur</div>
<div class="shadow-example" style="animation: spreadshadow 5s infinite;">Spread</div>
<div class="shadow-example" style="animation: colorshadow 5s infinite;">Color</div>
<div class="shadow-example" style="box-shadow: inset rgb(0 0 0 / .5) 3pt 3pt 2pt 0pt;">Inset</div>
<div class="shadow-example" style="
	box-shadow:
		inset rgb(0 0 0 / .5) 3pt 3pt 2pt 0pt,
		rgb(0 0 0 / .5) 3pt 3pt 2pt 0pt,
		rgb(250 0 0 / .5) 0pt 0pt 8pt 2pt,
		inset rgb(0 0 250 / .5) 0pt 0pt 3pt 2pt;
">Multiple</div>
</div>

`box-shadow` genera un efecto sombra de la caja, replicando el volumen de la caja detrás de ella.
Tambien se usa para otros efectos como resplandores y relieves.
Lo especificamos con:
```css
box-shadow: [inset] [color] offset-v offset-h [blur [spread]]
```

- El desplazamiento de la sombra (_offset_) es clave para simular de donde viene la luz o de que angulo miramos el objeto
- El radio de difuminado (_blur_) añade realismo a la sombra emulando una fuente luminosa no puntual.
- La expansion (_spread_) extiende la sombra una longitud en todas las direcciones simulando una luz próxima.
  Encoge si es negativo.
- Si añadimos la palabra clave `inset` la sombra será interior, emulando que la caja esta por detras del papel en vez de por encima
	- Ojo: La sombra `inset` va por dentro del borde, el border quedará al nivel del papel.
- Una caja puede tener varias sombras, podemos concatenarlas con comas
	- Ojo: Cada sombra va debajo de la anterior.

Sombras realistas:

- A más amplitud angular de la fuente de luz, mayor difuminado
- A más distancia de la caja a la sombra, mayor difuminado
- A menor distancia de la luz a la caja, mayor expansión

Otros efectos con `box-shadow`:

<div style="float: right; width: 100pt; margin: 0 20pt; border: solid black; background: #222">
<div class="shadow-example" style="
	box-shadow: rgb(0 255 255 ) 0pt 0pt 4pt 3pt;
	border: none;
	background: darkcyan;
	color: white;
">Glow</div>
<div class="shadow-example" style="
	box-shadow: inset rgb(0 50 50 / .5) 0pt 0pt 3pt 3pt;
	border-radius: 10pt;
	border:0;
	background: cyan;
">Emboss</div>
<div class="shadow-example" style="
	background: transparent;
	box-shadow:
		inset rgb(100 100 100 / .5) 0pt 0pt 10pt 2pt,
		rgb(0 0 0 / .5) 2pt 2pt 3pt 0pt
	;
	border-radius: 0;
	border: rgb(0 0 100 / .5) solid 0pt;
	color: white;
">Glass</div>
<div class="shadow-example" style="
	--blurder-color: #aaf;
	background: transparent;
	border: var(--blurder-color) solid 2pt;
	box-shadow:
		var(--blurder-color) 0pt 0pt 4pt,
		inset var(--blurder-color) 0pt 0pt 4pt;
	color: white;
">Blurder</div>
<div class="shadow-example" style="
	--blurder-color: #aaf;
	border: none;
	border-radius: 0;
	box-shadow:
		rgb(255 255 255 / .5) 0pt 0pt 5pt 1pt, /* refulgor limitado*/
		inset #fff7 0pt 0pt 2pt 1pt, /* borde brillante */
		inset #fff7 0pt 2pt 5pt 1pt, /* brillo superior */ 
		inset #a8fa 0pt 10pt 10pt -5pt, /* reflejos de color */
		inset #40fa 0pt -10pt 10pt -5pt,
		inset #0f0a 0pt -5pt 10pt -5pt
		;
	background: #aaa;
">Metal</div>
<div class="shadow-example" style="
	--paper-color: #fff;
	border: none;
	border-radius: 0;
	box-shadow:
		#0007 1pt 1pt 3pt,
		var(--paper-color) 2pt 2pt 0pt,
		#0007 3pt 3pt 3pt,
		var(--paper-color) 4pt 4pt 0pt,
		#0007 5pt 5pt 3pt,
		var(--paper-color) 6pt 6pt 0pt,
		#0007 7pt 7pt 3pt;
		;
	background: var(--paper-color);
">Pile</div>
</div>

- **Glow:**
	Sin offset, con blur, un poco de spread y un color saturado tipo neon.
	En fondos claros funciona pero con colores chillones.
- **Emboss:**
	Da relieve a la caja. Sombra inset sin offset, color saturado.
	Aclarar el background para que parezca iluminado.
	Con esquinas cuadradas le quita realismo al volumen.
- **Glass:**
	Simula un material semi-transparente.
	Dos sombras. Una inset clara semi-transparente, sin offset y muy difuminada, simula difracción.
	Otra outset oscura sin offset más concentrada, da grosor.
	Background transparente, si el contenedor tiene un fondo no plano queda muy resultón usando `backdrop-filter: blur(5px);`
- **Blurder:**
	Aplicar sombras inset y outset sin offset, con background transparente hace que el borde se difumine. Con colores brillantes en fondo oscuro, brille.
- **Metal:**
	En los bordes de los metales se juntan muchas normales,
	y es probable que alguna coincida con una fuente de luz.
	Por eso un glow debil.
	Tambien tienen reflejos distorsionados de color del entorno.
	Se podria hacer con degradados pero con sombras inset en el borde se distorsiona y queda más realista.
- **Pile:**
	Alternado sombras finas que hacen de sombras,
	con sombras tambien finas pero blancas que hacen de papel. Ahora si, profit:
<span style="
	--greens: #4a4;
	color: darkgreen;
	display: inline-block;
	border: none;
	border-radius: 0;
	width: 2.5rem;
	text-align: center;
	box-shadow:
		#0007 1px 1px 3pt,
		var(--greens) 2px 2px 0pt,
		#0007 3px 3px 3pt,
		var(--greens) 4px 4px 0pt,
		#0007 5px 5px 3pt,
		var(--greens) 6px 6px 0pt,
		#0007 7px 7px 3pt
		;
	background: var(--greens);
">[ ($) ]</span>


## Fondo (`background`)

El fondo es el lienzo donde se coloca el contenido.
CSS permite rellenarlo con varias capas que igual que las sombras podremos añadir con comas
y igual que las sombras las ultimas van poniendose debajo.

TODO










