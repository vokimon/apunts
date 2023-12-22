# CSS: Animaciones


## Accessibilidad primero

### No molestar

Primero de todo, las animaciones pueden ser molestas para algunos usuarios.
Los navegadores tienen una opción para indicar a la página que el usuario
prefiere reducir los elementos en movimiento.

Desde css podemos adaptar las animaciones para que sean menos violentas
especializandolas dentro de un media query:

```css
@media (prefers-reduced-motion: reduce) {
  /* styles to apply if a user's device settings are set to reduced motion */
}
```

Para probar como se ve con dicha opcion Mozilla ha hecho una
[compilación de como activarla en diferentes platformas](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion#user_preferences)

### Pausa-Para-Oculta

Si hay alguna animación que:

- Comienza automáticamente
- Dura más de 5s
- Se presenta en paralelo a otro contenido

Hay que proporcionar algún método para que el usuario la pause, pare o oculte.

### Tres flashes o menos

Los elementos que parpadean son peligrosos para las personas con epilepsia.

[Hay estudios que establecen el umbral seguro.](https://www.w3.org/TR/2008/REC-WCAG20-20081211/#general-thresholddef)

Es seguro si:

- No hay cosas que parpadeen mas de 3 veces por segundo.
	- Flash general: Alternar luminancias
	- Flash rojo: Alternar entre rojo saturado y otro color
- O el fulcrum que engloba los parpadeos no supera los 10 grados

### Animación como forma de suavizar o naturalizar los cambios

Como lo molesto es el parpadeo, las animaciones justamente pueden ser útiles para hacer más naturales los cambios en las transiciones.

### Objetivos en el diseño

Como pueden ser molestas es importante aplicar animaciones allí donde aporten algo:

- Continuidad: Cuando un elemento aparece, desaparece o cambia, hacerlo de una forma gradual para que la pagina no de saltos
- Feedback: Comunicar al usuario que la pagina responde a lo que hace (hover, clicked, drag...)
- Atención: Hay un elemento (uno, si, no dos) que queremos que capte la atención del usuario
- Esperas: En las esperas, indica que la aplicación no se ha colgado sinó que está esperando datos.
- Emoción: Refuerzan el mensaje y conectan con el usuario
- Marca: Las animaciones son parte de la marca

Respecto a las animaciones de espera:

- Tipos:
	- Animación de carga: ofrecen algo interesante que mirar mientras se carga (por un ratín)
	- Animación de progreso: Da cuenta de cuanto tiempo queda
	- Esqueletos de carga (skeleton loaders): Muestran la maquetación aproximada de como serán los elementos que esta cargando.
- Criterios:
	- Por bonica que sea, si es corta, mejor
	- Esperar duele, hagamosla interesante
	- Es parte de la marca
	- Explicar a qué esperamos
	- Si se conoce aprox, decir cuanto queda

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
	- Default: `all`
	- También podemos usar comas para separar grupos de propiedades que se animan de forma diferente.
	  (Ver 'Multiples transiciones')
- `transition-duration`: El tiempo que tarda en alcanzar el valor final.
	- Default: 0s
- `transition-delay`: Cuanto tarda la transición en empezar
	- Default: 0s
	- Duraciones negativas no empiezan antes, pero empiezan con el timeline a medias como si hubieran empezado antes.
- `transition-timing-function`: la funcion que dicta como interpolar los valores entre el inicial y final.
	- Default: `easy`
- `transition`: Atajo para las anteriores. Si solo hay un tiempo es el duration.

Default to: `all 0s 0s easy`


### Funciones de interpolación

Hay tres funciones de interpolación:

- linear(v1, v2...)
	- Incremento uniforme en los valores entre puntos de control
	- Normalmente, el primer valor sera 0 y el ultimo 1
	- Divide temporalmente el intervalo en tantos pasos como valores
		- `linear(0, .4, 1)` (al 50% del progreso valdra .4)
	- Si no nos va bien esa división, también podemos añadir al valor un porcentaje
		- `linear(0, .5 40% 1)` mueve el punto que llegara al .5 a cuando llege el 40% del progreso
	- Hace interpolación linial entre los pasos de un valor a otro

- `steps(nsteps, jumpmode)`:
	- hace la transición en nsteps saltos abruptos
	- el jumpmode indica si hay o no salto al principio o al final
		- jump-start/start: 5 -> 0%, 20%, 40%, 60%, 80% (no 100)
		- jump-end/end: 5 -> 20%, 40%, 60%, 80%, 100% (no 0)
		- jump-none: 4 -> 20%, 40%, 60%, 80% (neither 0 or 100)
		- jump-both: 6 -> 0%, 20%, 40%, 60%, 80%, 100%

- cubic-bezier(v1, t1, v2, t2)
	- Los puntos iniciales de la curva son siempre (0,0) y (1,1)
	- Lo que controlamos son las aristas de control (v1,t1) y (v2,t2)
	- Según las aristas la funcion puede salirse del intervalo (0,1)

Tambien hay algunos alias con nombre para funciones típicas.

- linear:
	- velocidad uniforme
	- cubic-bezier(0.0, 0.0, 1.0, 1.0)
	- linear(0, 1)
- ease:
	- aceleracion suave al inicio y al final
	- cubic-bezier(0.25, 0.1, 0.25, 1.0)
	- a diferencia de ease-in-out, se esta mas tiempo en torno a los valores inicio y final
- ease-in
	- lento al principio, rapido al final
	- cubic-bezier(0.42,0,1,1)
- ease-out
	- rapido al principio, suave al final
	- cubic-bezier(0,0,0.58,1)
- ease-in-out
	- suave al principio y al final (un poco mas lento que ease)
	- cubic-bezier(0.42,0,0.58,1)
- step-start:
	- Un salto brusco al inicio de la transicion
	- step(1, start)
- step-end:
	- Un salto brusco al final de la transicion
	- step(1, end)

### Multiples transiciones

Cada elemento puede tener más de una transición.

- En cada una de las propiedades `transition-*` puede definir transiciones independientes separandolas por comas
- La propiedad `transition-property` es la que determina en el número de transiciones independientes
- El resto de propiedades relacionadas,
	- si hay de más se ignoran
	- si hay de menos se repiten los valores en bucle


## Animaciones basadas en fotogramas clave (`keyframes`)

Las animaciones basadas en fotogramas clave dan más flexibilidad
que las animaciones de transición pero son un poco más complejas de definir.

TODO: verificar que es asi

El timeline viene definido por el tiempo desde que se aplica el selector
que contiene la animación.


### Fotogramas clave (`keyframes`)

```css
@keyframes colorchange {
  0% {
    background: yellow;
  }
  100% {
    background: blue;
  }
}
```

### Atributos

- `animation-name`: Nombre de la definición keyframes 
- `animation-duration`: Obligatoria, sino por defecto es 0s y no hay animación.
- `animation-delay`: igual que en la transicion (usando el shortcut, el segundo tiempo que indiquemos)
- `animation-timing-funcion`: igual que en transiciones (default: ease)
- `animation-iteration-count`: un numero (float!) o infinite (default 1)
- `animation-fill-mode`: 
	- `none` (default) Fuera del intervalo la animación no afecta a los atributos
	- `forwards` Las propiedades se quedan con el último valor de la animación
	- `backwards` A la que aplica la animación y durante el delay, las propiedades adoptan el primer valor de la animación
	- `both`: aplica backwards y forwards
- `animación-direction`: en que dirección progresan las distintas iteraciones
	- `normal` -> -> (default)
	- `reverse` <- <-
	- `alternate` -> <-
	- `alternate-reverse` <- ->
- `animation-play-state`: 
	- `running` (default)
	- `paused`


### Multiples animaciones independientes

Un keyframe puede controlar varias propiedades.
Pero si queremos controlar propiedades con parametros de animación distintos,
podemos separar los parametros de las animaciones independientes con comas.

Cuando varias animaciones o transiciones setean una misma propiedad,
el atributo `animation-composition` especifica como mezclarlas.

- `replace`: (default) Sobreescribe 
- `add`: concatena el valor 

Esto es especialmente útil con attributos como `transform` que se especifica con llamadas a diferentes funciones (translate, rotate...).
Por ejemplo si partimos de un `transform: rotate(10) translateX(3)` y la animación aplica `rotate(20)`

- `replace`: substituira todas las funciones existentes: `rotate(20)`
- `add`: añadira las tranformaciones a las existentes `rotate(10) translateX(3) rotate(20)`
- `combine`: añadira a las funciones existentes que coincidan: `rotate(30) translateX(3)`



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

- `*-name`: especifica un nombre (sintaxis de variable css) para referenciarla en las animaciones que la usen. (Por defecto, `none` para anonimas)
	- Se especifica para el elemento subject
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

### Animation Range

`animation-range{-start/-end}`: Define el intervalo considerado como inicio y final de tránsito.

Intervalos del scroll considerando el movimiento de un Subject (S) por un Puerto de scroll (P).
Convención: en la dirección de scroll, 
P0 y S0 son sus bordes de inicio,
P1 y S1 son sus bordes de final.

https://scroll-driven-animations.style/tools/view-timeline/ranges/

- `entry-crossing`: Mientras que el subject cruza la entrada del puerto
	- 0% `S0=P1` empieza a entrar todo el puerto
	- 100% `S1=P1` ha entrado todo en el puerto
- `exit-crossing`: Mientras que el subject cruza la salida del puerto
	- 0% `S0=P0` empieza a salir del puerto
	- 100% `S1=P0` acaba de salir del puerto
- `entry`: Como entry crosing pero 
	- 0% `S0=P1` empieza a entrar en el puerto
	- 100% `(S<P) S1=P1` ha entrado todo en el puerto
	- 100% `(S>P) S0=P0` empieza a desaparecer
- `exit`: Como exit crossing pero si es grande se espera a que haya entrado todo.
	- 0% `(S<P) S0=P0` empieza a salir del puerto
	- 0% `(S>P) S1=P1` ha entrado todo el puerto
	- 100% `S1=P0` acaba de salir del puerto
- `contain`: Mientras que se vea entero, si no cabe, mientras cubra todo el puerto.
	- 0% `S<P S1=P1`
	- 100% `S<P S0=P0`
	- 0% `S>P S0=P0`
	- 100% `S>P S1=P1`
- `cover`: Durante el tiempo que se ve algo del componente
	- 0% `S0=P1` Empieza a entrar
	- 100% `S1=P0` Acaba de salir

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
	- Lo que controla la animacion es el tránsito de un elemento (subject) por la parte visible (scroll port) de un elemento contenedor con scroll
	- No permite escoger
		- ni elemento cuya visibilidad controla la animación (subject), que será self
		- ni el scroller, que será nearest y defile lo que es el view port
	- Tiene dos parametros inset y axis
	- view-timeline-inset: son dos distancias (`-start` y `-end`) positivas (o negativas) que reducen (o amplian) el scroll port
		 - el scroll port es la zona que se consider por la que tiene que pasar o verse el subject
	- `view-timeline-axis` como el scroll: x, y, inline, block; por defecto `block`
		- Firefox: `horizontal`, `vertical`, hay que especificarlo a parte mientras no se actualiza para no invalidar la regla en otros navegadores



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







