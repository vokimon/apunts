# Animaciones

## Transiciones

Las transiciones son la forma más sencilla de generar animaciones.
Las transiciones se activan cuando cambia el valor de una propiedad de un elemento
y hacen que dicho cambio no se haga de golpe, sinó de forma progresiva.

Dichos cambios se producen, por ejemplo, cuando cambia el estado (:hover, :disabled, :active...)
o cuando cambian las clases que se aplican al elemento.

La transición se define en el estado de llegada.
Si queremos que se haga al entrar y salir del estado hay que poner transiciones en los dos entradas.

### Propiedades de la transición

- `transition-properties`: Las propiedades que se cambiaran separadas por espacios.
	- También podemos usar comas para separar grupos de propiedades que se animan de forma diferente.
	  (Ver 'Multiples transiciones')
- `transition-delay`: Cuanto tarda la transición en empezar
	- Default: 0s
	- Duraciones negativas no empiezan antes, pero empiezan con el timeline a medias como si hubieran empezado antes.
- `transition-duration`: El tiempo que tarda en alcanzar el valor final.


### Multiples transiciones

Cada elemento puede tener más de una transición.

- En cada una de las propiedades se separa cada transición con comas
- La propiedad que manda en el número de transiciones que hay es `transition-property`.
- El resto de propiedades relacionadas,
	- si hay de más se ignoran
	- si hay de menos se repiten los valores en bucle



## Keyframes

## Animaciones de scroll

En las animaciónes clásicas, el progreso en la animación (timeline) lo determina el tiempo.
Se define un inicio y una duración, y, las propiedades se modifican, segun el tiempo avance en ese intérvalo.

Sin embargo, en las animaciones de scroll el timeline no lo define el tiempo, sinó el desplazamiento de un scroll.

::: note Recuerda
    No solo el scroll de la pagina (`:root`), sino el scroll de cualquier elemento que pueda generar un overflow.

Diferenciamos entre el elemento que genera el timeline
y el elemento al que aplicamos la animación,
que podria estar o no dentro el scroll.

### Timelines `scroll` y `view`

Tambien se definen dos tipos de timeline de scroll:

- Desplazamiento (`scroll`):
	- El progreso lo determina la posición de un scroll
	- El sujeto es el elemento que genera el overflow (scroller)
	- 0% cuando está al inicio
	- 100% cuando esta al final

- Visibilidad (`view`):
	- El progreso lo determina la visibilidad parcial de un elemento en el scroller
	- El sujeto es cualquier elemento dentro del que genera el overflow
	- 0% cuando no es visible
	- 100% cuando se ve completamente

Cómo definimos los timelines?

En el objeto que genera el timeline:

- `view-timeline: --my-timeline inline`
- `scroll-timeline: --my-other-timeline y`

Son atajos que juntan las propiedades con sufijos `-name` y `-axis` (y `inset` para view).

- `*-name`: especifica una variable para referenciarla en las animaciones que la usen. (Por defecto, `none` para anonimas)
- `*-axis`: define que eje del scroll (x, y, block, inline) default: `block`
- `*-inset`: (solo para view) reduce (o amplia, si negativo) la zona del viewport en la que se produce la animación
		- Dos valores start y end
		- Si no se indica end es igual que start
		- Si no se indica ninguno, `auto`
		- Si son negativos la animación empieza o acaba fuera del view port.

Ahora, si queremos usar uno de estos timelines en una animación,
hay que especificar la propiedad `animation-timeline` indicando una de esas variables.

El `animation-timeline` por defecto es `auto`, que quiere decir que el timeline es el tiempo de documento, es decir, las animaciones clásicas.
És útil sobretodo para combinar animaciones con diferentes timelines de tiempo y de scroll/view,
que se indican separadas con comas como las otras propiedades de animacion.

TODO: none = auto??

### TODO: Animation Range

TODO: cover, fill...

### Timelines anónimos con las funciones `scroll()` y `view()`

Algunas fuentes de timeline se pueden indicar sin darles nombre,
con las funciones `view` o `scroll`.

- `scroll(...)`:
	- Escoge un timeline scroll
	- Tiene dos parametros: scroller y axis
	- scroller
		- nearest: el mas cercano de los ancestro que tenga scroll en el eje
		- root: el documento
		- self: el elemento animado
	- axis:
		- Ejes físicos: `x` y `y`
		- Ejes lógicos: `inline` y `block`
	- Si no se indica cualquiera de los dos se coge su defecto (nearest block)
		- `scroll()` means `scroll(nearest block)`
		- `scroll(root)` means `scrall(root block)`
		- `scroll(y)` means `scroll(nearest y)` 
	- Se especifican en cualquier orden (son disjuntos)

- `view(...)`
	- No permite escoger
		- ni elemento cuya visibilidad controla la animación, que será self
		- ni el scroller, que será nearest
	- Tiene dos parametros inset y axis
	- axis como el scroll: x, y, inline, block; por defecto `block`

### Propiedad timeline-scope

Por defecto los timelines solo se pueden usar en animaciones de elementos descendientes.
La propiedad `timeline-scope` tiene como valor el nombre de un timeline en un
elemento hijo, augmentando el alcance (scope) a 

```
Document
	Scope
		DirectChild
			Scroller
		Animated
	
```	

En el ejemplo anterior Scroller define un timeline.
Para poder afectar a Animated, el elemento scope tiene que definir `timeline-scope`
al nombre del timeline de Scroller.

### Atrasando o adelantando el timeline view (`inset`)

La propiedad `view-timeline-inset`
A veces queremos empezar o acabar la animacion `view` un poco después o un poco antes de cuando se empieza a ver o ya se ve completamente.


view-timeline-inset: xdir ydir // positive inwards, negative outwards


## View transitions

Las view transitions permite vincular elementos en paginas o layouts diferentes y animar la transición de uno a otro cuando se cambia de pagina o de estado.

La propiedad `view-transition` es para un identificador (en este caso no es necesario los dobles --).

Si en el cambio de pagina o cambio de doom existen antes y despues elementos con el mismo identificador,
se pruduce una animación de transición entre uno y el otro.







