# Flex box

https://css-tricks.com/snippets/css/a-guide-to-flexbox/

El poster ![](https://css-tricks.com/wp-content/uploads/2022/02/css-flexbox-poster.png)

## Concepto

Flexbox es un sistema para organizar la disposición (layout)
de unos elementos hijos en un elemento contenedor,
de forma que los hijos se van ordenando primero en un eje principal
y posiblemente en un eje secundario.



Por ejemplo cuando escribimos, (sistema latino de escritura),
ponemos las letras de derecha a izquierda y cuando
llenamos una linea empezamos una linea abajo.

Lo activamos definiendo el contenedor con `display: flex`
o con `display: flex-inline`

```css
.container {
  display: flex;           /* or flex-inline, see bellow */
}
```

## Controlando los ejes de apilamiento

En un contenedor flexbox puedes definir cual es el eje y la direccion principal
con la propiedad `flex-direction` en el contenedor:

- `row`: writting direction (left to right, for us)
- `row-reverse`: counter writting direction (right to left, for us)
- `column`: block development direction (up down for us)
- `column-reverse`: counter block development direction (down up for us)

Ojo, eso si es script latino ltr. Con otros scripts izquierda y derecha se intercambian.
Lo importante es que row es el sentido de lectura horizontal,
y row-reverse sentido al reves de la lectura.

Que pasa cuando se llena la línia?
Siguen poniendose elementos, hace `overflow`.
Se puede configurar la propiedad del contenedor `flex-wrap` a `wrap`
para que los hijos pasen a la siguiente linea si no caben.

También se pueden juntar `flex-direction` y `flex-wrap` en la propiedad fusionada `flex-flow` (direction, wrap)

Si quieres que los elementos wrappeen en la otra dirección: `wrap-reverse`

## Flexibilidad de los elementos

Por defecto:

- Los elementos toman como base el tamaño en la dirección principal que requiere el contenido del elemento (propiedad `flex-basis` a `auto`)
- Los elementos no se expanden en el eje principal más allá  de lo que pide su contenido si sobrara espacio (propiedad `flex-grow` a 0)
- Si se pueden comprimir si no caben en una linia (propiedad `flex-shrink` del elemento a `1`)
- Los elementos se estiraran en el eje secundario hasta alcanzar la altura del elemento mas alto (propiedad `item-align` a `stretch`)

Como se pueden modificar estas propiedades?


- `flex-grow`: if there is not enough space for the children, this is a number indicating the proportionality to shrink in respect to the other elements
  - Por defecto 0
- `flex-shrink`: if there is empty space to fill, this is a number indicating proportionality to grow in respect to the other elements
  - Por defecto 1
- `flex-basis`: is the size to grow or shrink the element from. By default, it is `auto`, meaning the size (width or height style of the element)
  - `content` adapt to content
  - size, could be relative to the parent.
  - `max-content`: El tamaño del contenido maximo de los hermanos
  - `min-content`: El tamaño del contenido mínimo de los hermanos
  - `fit-content`: Just 

Se pueden juntar los tres en la propiedad `flex`, donde se especifican por orden grow, shrink y basis.

  - 'initial': Equivalent to `0 1 auto`. All the default values. Do not expand, but will shrink.
  - 'auto': Equivalent to `1 1 auto`. Will adapt shrinking or growing as required
  - 'flex': Equivalent to `1 1 auto`
  - number: 

## Ajustando/aliniando los elementos

Por defecto los elementos se agrupan al inicio de la dirección principal (`justify-content` a `start` del contenedor),
y se expanden en la direccion secundaria (`align-items` del contenedor).
Los items se pueden expandir en la dirección secundaria

- cuando el contenedor fija una tamaño mayor
- cuando alguno de los hermanos es mayor

La propiedad `align-items`? Es análogo a lo que hacemos al alineamiento de texto pero en el eje secundario.

- `stretch`: Estira el tamaño en el eje secundario para que llegue a los dos extremes (equivalente a un justify)
- `flex-start` ajusta los elementos al inicio del eje secundario (equivalente a un left)
- `flex-end` ajusta los elementos al final del eje secundario (equivalente a un right)
- `center` deja el mismo espacio a los dos lados del eje secundario (equivalente a un center)
- `baseline` alinia los elementos en su linea base.

La propiedad `justify-content` del contenedor se parece a la `align-items` pero de cara a justificar ahora tiene varias estrategias:

- `space-arround`: Añade espacio alrededor de cada item (En los extremos habra la mitad porque en los intermedios habra dos)
- `space-between`: Añade espacio solo entre los elementos interiores
- `space-evenly`: Añade el mismo espacio entre los elementos y en los extremos
- `flex-start` (default) ajusta los elementos al inicio del eje principal (equivalente a un left)
- `flex-end` ajusta los elementos al final del eje principal (equivalente a un right)
- `center` deja el mismo espacio a los dos lados del eje principal (equivalente a un center)

`justify-items`

`align-content` determina como alinear/justificar las lineas wrapeadas en el eje cruzado.


`place-items` agrupa align-items y justify-items, en ese orden si se dan un valor para cada uno.

Cuando hay wrapping 


Haciendo el símil con el texto:

- `justify-content`: Justificación de los items en la direccion principal dentro de una linea. Seria el text alignment. Si a la derecha a la izquierda, centrado o insertando espacio.
- `align-items`: Alineamiento en la dirección de cruze de los items dentro de su linea. Seria el vertical alignment. Si el elemento no es tan alto, para donde lo tiramos en vertical.
- `align-content`: Alineamiento en la dirección de cruze de lineas wrappeadas.  Si las lineas se justifican arriba, abajo en el centro o insertando espacio.
- `justify-items`: Existe pero se ignora en flexbox. A los items no se les assigna un espacio mas grande del que disponen en la dirección principal como podria ser en una tabla o en un grid.



Las propiedades `column-gap`, `row-gap` y la combinada `gap` (row column),
indican un espacio minimo entre los elementos interiores.
Es un margen, entre los elementos interiores que no afecta al margen de los elementos exteriores.
Es un espacio minimo, asi que si por  `space-between`, `space-evenly` o `space-arround`,
toca mas espacio, se dará más espacio.

## Hijos díscolos

A veces queremos que algún hijo concreto no siga la politica especificada en el padre.

La propiedad `align-self` los hijos,
permite controlar este alineado cruzado para elementos concretos,
para que sea diferente del `align-items` del contenedor.

La propiedad `order` permite sacar el item de la secuencia de declaracion.

