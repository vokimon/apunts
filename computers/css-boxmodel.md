# El modelo de caja

## Elementos

El modelo de caja, es la base para la maquetación (layout).

Considera cada elemento una caja que tiene que albergar 4 niveles de espaciado:

- un contenido con un ancho y un alto
- un relleno (`padding`) dentro de la caja que no puede usar el contenido
- un borde (`border`) alrededor del padding que delimita la caja
- un margen (`margin`) alrededor del borde que no pueden invadir los bordes de otros bloques

La caja también puede tener otros elementos
que se ignoran de cara al layout:

- un contorno (`outline`) que hace de segundo borde por fuera
- una sombra (`box-shadow`) que replica de la forma de la caja desplazada y difuminada

<div style="float: right; display: flex; border: solid; margin: 5pt;">
<div style="
	margin: 15pt;
	background: grey;
	color: white;
	padding: 10pt;
	border: 10pt dashed blue;
	outline: 10pt dotted red;
	box-shadow: 5pt 5pt 1pt green;
">Content</div>
</div>

En este ejemplo, vemos
la caja (gris) que incluye contenido, relleno y borde (en azul).
Fuera de la caja, el contorno (rojo) y la sombra (verde) que queda por detrás.
El margen no se pinta, mantiene al resto de elementos a 20px de distancia
del contenido en gris incluido el borde del contenedor que es el que esta pintado de negro.
Si el margen no superara el ancho del contorno o de la sombra,
quedarian solapados por los elementos contiguos.

<div style="float: right; display: flex; border: solid; margin: 5pt;">
<div style="
	margin: 15pt;
	background: grey;
	color: white;
	padding: 10pt;
	border: 10pt dashed blue;
	outline: 25pt dotted red;
	box-shadow: 20pt 20pt 4pt green;
">Content</div>
</div>

En el siguiente ejemplo,
hemos augmentado el contorno y la sombra de la caja,
sin que haya efectos en el posicionamiento de la caja gris.
Borde y sombra, al superar el margen, se solapan con el resto de elementos.


## Orientaciones físicas y lógicas

Las cuatro orientaciones físicas son `top`, `left`, `bottom` y `right`.

En muchos casos, en qué dirección establecer un parámetro depende del modo de lectura.
En el sistema de escritura latino
escribimos las palabras _en líneas_ de izquierda a derecha
y añadimos las líneas de arriba abajo.
Esto no siempre es así.
Las escrituras semíticas (árabe, hebreo...) escriben de derecha a izquierda,
y algunas asiàticas de arriba a abajo o incluso de abajo a arriba.
Es lo que se llama el modo de lectura.

Si queremos especificar las direcciones según el modo de lectura tenemos las direcciones _lógicas_ (o _multiculti_ que les llamo yo):

| dirección logica | física en latino | fisica en semítico | física en oriental |
| `block-start`   | `top` | `top` | `left`

- `block-start`, en latino, `top`
- `block-end`, en latino, `bottom`
- `inline-start`, en latino, `left`
- `inline-end`, en latino, `right`

Cuando implicitamente tengamos que especificar parametros en orden para las cuatro direcciones
iran en orden de las manecillas del reloj empezando a las 12: `top` `left` `bottom` `right`.
Con tres valores, van a `top`, `left-right` y `bottom`.
Con dos valores, van a `top-bottom` y `left-right`.

Si queremos que se asignen a las _direcciones lógicas_ correspondientes, hay que preceder los parametros por `logical`.


## Relleno (`padding`)

El padding es un relleno o cojín entre el contenido y el borde de la caja.
La metáfora sería el relleno que se pone en un paquete para que
el contenido no dé golpes.

Se puede especificar un relleno diferente en cada una de las cuatro direcciones.

Formas de especificarlo:

```css
.midiv {
	/* direcciones especificas */
	padding-top: 3px;
	padding-right: 3px;
	padding-bottom: 3px;
	padding-left: 3px;

	/* atajos */
	padding: 2px; /* el mismo en las 4 direcciones */
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

	Cuando especificamos un padding vertical (block en multiculti) con un porcentage,
	no se toma el alto del contenedor como referencia,
	sinó su ancho (inline en multiculti).

	<div style="
		width: 100px;
		height: 200px;
		background: #f77;
		float: right; margin-inline: 1rem; padding:2px;
	">
	<div style="background: #7f7; padding: 20% 20%;">XXXXX</div>
	</div>

	En el siguiente ejemplo,
	el padding de la caja interna está fijado al 20% en todas las direcciones.
	Se observa que resulta el mismo padding horizontal y vertical,
	aunque la caja contenedora sea el doble de alta que de ancha.
	Se está tomando el 20% del ancho en todas las direcciones.
	```html
	<div style="
		background: #f77;
		width: 100px;
		height: 200px;
		float: right; margin-inline: 1rem; padding:2px;
	">
		<div style="background: #7f7; padding: 20% 20%;">XXXXX</div>
	</div>
	```

## Borde (`border`)

El borde es una línea que decora el extremo de la caja marcando su límite.
Está fuera del padding pero sigue siendo parte de la caja de cara al maquetado.

También por ser parte de la caja,
se le aplica el fondo (background) del elemento,
aunque muchas veces no es visible.

La línea de borde tiene 3 atributos: ancho `width`, estilo `style` y color `color`.

El color por defecto es el `color` del elemento.

La anchura puede ser una longitud o una de las palabras `thin`, `medium`, `thick`.
La anchura por defecto es `medium` pero no esta especificada a cuanto corresponde,
así que cada navegador usa la suya como `medium`.
Para que sea consistente se recomienda siempre explicitar una anchura con unidades.

El estilo es importante porque por defecto es `none` y si no lo cambiamos no se verá.

Los estilos posibles son:

- Invisibles:
	- `none`: Sin borde (por defecto).
	- `hidden`: Sin borde. Pero tiene prioridad cuando colapsa con otro.
- Planas:
	- `solid`: Una linea plana
	- `double`: Dos lineas paralelas
	- `dotted`: Puntos
	- `dashed`: Rayas
- Sombreadas: Se crean oscureciendo o aclarando el color para generar efecto sombreado
	- `ridge`: Simula un marco sobre saliente  `/\______/\`
	- `groove`: Simula un surco alrededor del contenido `\/--------\/`
	- `inset`: Simula que el contenido està hundido `\______/`
	- `outset`: Simula que el contenido sobresale `/--------\`
	- Los colores que no sean negros, usa una version del color oscurecido.
	- Al menos en Firefox, el negro se comporta diferente, usando tonos de gris.

<div style="color: #77f; display: flex; justify-content: space-between; gap: 5pt">
<div style="border-style: none; border-width: 5pt">None</div>
<div style="border-style: solid; border-width: 2.5pt">Solid</div>
<div style="border-style: dotted; border-width: 5pt">Dotted</div>
<div style="border-style: dashed; border-width: 5pt">Dashed</div>
<div style="border-style: double; border-width: 5pt">Double</div>
<div style="border-style: ridge; border-width: 5pt">Ridge</div>
<div style="border-style: groove; border-width: 5pt">Groove</div>
<div style="border-style: inset; border-width: 5pt">Inset</div>
<div style="border-style: outset; border-width: 5pt">Outset</div>
</div>


La línea del borde tiene 3 atributos (`width`, `style`, `color`)
que se aplican en las cuatro direcciones con: `border{-direction}{-attribute}`.
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

### Collapsing borders

Si dos bordes no tienen margen entre ellos podemos decir que los fusione.
Esto es útil en las tablas donde a menudo solo queremos un borde entre celdas.

Para activar el colapso de los bordes `border-colapse: colapse`.
Cual es la politica para colapsar bordes:

- Tomaran preferencia los bordes del padre.
- Después los de los hijos por orden de definición.
- Si un borde es `none` cede la preferencia al otro borde.
- Si un borde es `hidden` adquiere la preferencia.

<div style="border: solid green; border-collapse: collapse;">
<div style="border: solid yellow; border-collapse: collapse;"></div>
<div style="border: solid blue; border-collapse: collapse;"</div>>
</div>

### Border radius

TODO

### Border image

TODO

Setting `border{-direction}` property sets `border-image` to none


## Margen (`margin`)

El margen es una distancia mínima de exclusión que se establece para un bloque en cada dirección
desde el borde de la caja al borde de la caja adjacente en esa dirección.

- Es transparente, no se le aplica el background.
	- Al contrario del borde y el padding, que si se les aplica el background.
- Los margenes de cajas adyacentes se solapan **colapsandose**.
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

<div style="background: green">
	<div style="background: blue; margin: 0;">content</div>
	<div style="background: red; margin: 10px 10px 20px 10px; border: solid 1pt black">content</div>
	<div style="background: red; margin: 90px 10px; border: solid 1pt black">content</div>
	<div style="background: blue; margin: 0;">
		hola que tal esto es un texto largo
		hola que tal esto es un texto largo
		hola que tal esto es un texto largo
		hola que tal esto es un texto largo
		content</div>
</div>

Los márgenes de dos bloques adjacentes **se colapsan**.
Es decir, de los dos se toma el mayor.

Cuando ponemos al lado dos márgenes, se colapsan en el más grande.

## Contornos (`outline`)

Otras cosas que añaden capas pero no pertenecen al box model y, por tanto,
**no se tienen en cuenta para calcular el maquetado**:

- Outline:
	- Es un borde extra que se añade normalmente cuando el elemento esta en foco
	- Tiene la misma sintaxis que `border` pero sin poder especificar por direcciones
	- Pintado en rojo en el ejemplo.
	- El borde en azul, esta dentro de la caja. El outline en rojo no se tiene en cuenta para el maquetado.
- Box shadow: 
	- El box shadow replica el volumen de la caja con un cierto offset, color y difusión.
	- Tampoco se tiene en cuenta para calcular el 
	- En purpura en el ejemplo, con un offset de 5pt en cada direccion y una difusion de un punto.

La propiedad `outline-offset` permite definir una distancia de separación
entre el border y el contorno.


## Margin

The margin 

- Margenes entre bloques adyacentes (del nivel que sea) no se suman sino que colapsan al más grande.
- Excepciones:
  - Si hay algo entre medias que tambien puede ser un borde o un padding
  - Si hemos creado un contexto de flujo diferente (flex, grid, position...)

Other

- `width: auto` takes the available space without overflowing
- `margin: auto` takes the availabel space
- `width: max-content;` expands to the max content expans, but does not shrink
- `width: min-content;` sets to the mininum width the content could shrink without over flowing content. (The longer word in a paragraph)
- `width: fit-content;` expands between max and min content according to the available size





