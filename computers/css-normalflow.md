# Flujo normal (normal flow)

La disposición (_layout_) es la forma de repartir los elementos en el espacio disponible.

La disposición por defecto es el _flujo normal_ (_normal flow_).
Está pensada para repartir elementos de texto.

## Modo de lectura

La forma de repartir el texto depende del idioma.
Según el idioma, hay una dirección principal de lectura, la **dirección de línea**.
En escritura latina, disponemos las letras de izquierda a derecha en líneas.
Según llenamos las líneas vamos añadiendo más de arriba a abajo,
la **dirección de bloque**.

Se hace esta abstracción porque el caso latino no es el general.
Por ejemplo, en idiomas semíticos (árabe, hebreo),
escriben de derecha a izquierda, y, en idiomas asiáticos,
es comun escribir de arriba a abajo o incluso de abajo a arriba
y añaden las lineas en horizontal a veces a derecha, a veces a izquierda.

## Inline y block

Hay dos tipos de elementos a repartir:

<div style="border: solid; float: right; width: 30%; padding: 3pt">
<h5>Example of flow layout</h5>
<span style="background: #faa; border: solid 2pt #f66">
inline1 inline1 inline1 inline1 
</span>
<span style="background: #aaf; border: solid 2pt #66f">
inline2 inline2 inline2 inline2
</span>
<div style="background: #afa; border: solid 2pt #4f4">
block block block
block block block
</div>
<span style="background: #ff7; border: solid 2pt #cc4">
inline3 inline3 inline3 inline3
</span>
<div style="background: #aff; border: solid 2pt #3ff; width: 50%">
half width block
</div>
<span style="background: #faf; border: solid 2pt #f4f">
inline4 inline4 inline4 inline4
</span>
</div>

- Elementos en linea (_inline_):
	- Siguen con la línea empezada.
	- Cuando se agota la línea pasan a la siguiente.
	- No consumen la línea si no lo necesitan
	- Comportamiento por defecto de `span`, `b`, `i`, `a`, `img`...
	- Explícito con: `display: inline`
- Elementos bloque (_block_)
	- Rompen la linea (empiezan siempre en la siguiente línea)
	- Consumen todo el espacio de línea, aunque no lo ocupen, 
	  así, el siguiente elemento irá en la siguiente línea.
	- Comportamiento por defecto de `div`, `p`, `table`, `ul`...
	- Explícito con: `display: block`

Algunos detalles:

- Los inline parten su caja en las líneas que ocupa, los block en cambio, tienen una caja que engloba todas las líneas
- Los inline ignoran los márgenes en dirección de bloque (verticales) pues se guían por los parametros de texto (`line-heigth`...) 
- Los block colapsan sus margenes en la dirección de bloque, en vez de sumarse, queda el mayor de los dos

## Propiedad `display`

La propiedad `display` indica dos aspectos del elemento:

- (inner) Como contenedor: con qué modelo se reparten el espacio los elementos hijos
	- `flow`, `flow-root` `flex`, `grid`, `table`...
- (outer) Como contenido: cómo participa en la composición de su elemento padre
	- `block`, `inline`, `run-in`, `table-row`...

Por herencia histórica, los valores para display no son así de ortogonales.

- `block` y `inline`, implican disposición `flow` que es la por defecto.
- `flex` y `grid` implican `block`
- `inline-flex` y `inline-grid` implican `inline` y el layout interno `flex` o `grid`.

El flujo normal es `flow`.


## Position

Position 


El valor por defecto del atributo `position`, `static`,
significa que los elementos contenidos se van a posicionar usando el llamado _flujo normal_ o _normal flow_.
Como es el normal, se comporta como esperarías, pero es importante saber qué esperar.

- Se ignoran las propiedades de posicionamiento explícito: `top`, `left`, `right`, `bottom`.
- No se considera el elemento como referencia de posicionamiento explícito para sus hijos (más sobre esto abajo)
- Los hijos se posicionan siguiendo el flujo de lectura,
  teniendo en cuenta lo que se ha colocado antes.


Por ejemplo, aunque `display: flex` y `display: grid`,
determinan un layout de los elementos internos diferentes al flujo normal,
el elemento que tiene tales propiedades, se considerarà block en su contenedor.
Al mismo tiempo, `display: inline-grid` y `display: inline-flex`,
son los valores equivalentes que hacen

## Floats



