# Navegación en el mástil

## Método "Gusano"

Este método es una simplificación del método
explicado aquí:

https://www.youtube.com/watch?v=rQf6i8KIwJU

**Objetivo:**
poder puntear una escala diatónica
con cualquier raiz y modo,
en cualquier punto del mastil de la guitarra.

::: note Nota
	Una escala diatónica es una rotación
	y/o transposición de la escala de Do Mayor.
	Más en [Musica: Armonía](music-harmony.md)

### Construcción

Queremos construir una escala diatónica
tocando 3 notas en cada cuerda.
Tal y como están definidas las escalas diatónicas,
tres notas contíguas, solo pueden tener
tres patrones posibles en la distancia tonal entre ellas.
Eso nos da tres patrones de fingering que llamaremos X Y Z:

|Nombre| Intervalos    | Dedos | Tríos en C Mayor |
|------|---------------|-------|----|
|  X   | tono-tono     | 1-2-4 | **C**DE, **F**GA o **G**AB |
|  Y   | semitono-tono | 12-4  | **E**FG o **B**CD |
|  Z   | tono-semitono | 1-34  | **D**CE o **A**BC |

- El guión en el fingering significa un traste que saltamos.
- Los números: 1 Indice, 2 medio, 3 anular, 4 meñique.
- No nos dice nada de en que cuerda o que traste poner cada patron

Si agrupamos las notas de diferentes octavas
en grupos de 3, obtendremos 7 tríos diferentes,
cada uno empezando en una nota diferente.
Después de la tercera octava, se repetirá la sequencia.

Ejemplo en C mayor: **CDE|FGA|B**CD|EFG|AB**C|DEF|GAB**|CDE

Si ordenamos la sequencia de tríos,
vemos que los patrones X, los Y y los Z
están, casualmente, adjacentes a sus similares.
Los numeramos en orden ascendente:

|Nombre| Grave | Media | Aguda | C Major |
|--|--|--|--|--|
|X1 | **V** | VI | VII | **G**AB
|X2 | **I** | II | III | **C**DE
|X3 | **IV** | V | VI | **F**GA
|Y1 | **VII** | I | II | **B**CD
|Y2 | **III** | IV| V | **E**FG
|Z1 | **VI** | VII | I | **A**BC
|Z2 | **II** | III | IV | **D**EF

Convenientemente, coincide que 5 semitonos (una 4a perfecta) es la distancia tonal...

- Entre las cuerdas contiguas de la guitarra (en afinación estandard EADGBE), con una excepción.
- Entre las notas graves de los trios, con una excepción

Asi que la mayoría de las veces pondremos **la primera 
nota de los patrones alineadas en el mismo traste**.

Las dos excepciones están muy localizadas:

- **Subiremos un traste cuando pasemos de X3 a Y1**
	- El intervalo de IV a VII (Fa a Si) no son 5 semitonos (4a perfecta) sinó 6 (4a augmentada).
	- Es el único intervalo de 4a entre blancas, que tiene 3 negras entre medias.
- **Subiremos un traste, los patrones en las dos cuerdas más agudas (1a y 2a).**
	- La distancia tonal entre las cuerdas 2a (B) y la 3a (G) cuerda es de 4 semitonos en vez de 5.
- Ambos desplazamientos se suman si coinciden en una cuerda

En el siguiente esquema, se puede observar
la sequencia de patrones,
los intervalos de 5 semitonos
y el semitono que sobra entre X3 y Y1:

	   X2    X3     Y1    Y2   Z1     Z2    X1    X2'
	|C_D_E|F_G_A|_|BC_D_|EF_G_|A_BC_|D_EF_|G_A_B|C_D_E|
	|1-2-4|1-2-4|-|12-4-|12-4-|1-34-|1-34-|1-2-4|1-2-4|


### Progresión ascendente

- Podemos empezar la figura en cualquier traste y en cualquier cuerda
- La nota en la que empecemos será la tónica de la escala.
- El patrón por el que empecemos determinará el modo de la escala
- Aplicar los sucesivos patrones con la nota grave de uno debajo de la del otro
- Si pasamos de la 3a a la 2a cuerda, avanzar un traste
- Si pasamos de X3 a Y1 avanzar otro traste más

El Fingering, sin tener en cuenta el cambio de 3a a 2a cuerda, quedaría:

	X1 V     1-2-4
	X2 I     1-2-4    
	X3 IV    1-2-4
	Y1 VII   -12-4 (fret grave avanza)
	Y2 III   -12-4
	Z1 VI    -1-34
	Z2 II    -1-34
	X1 V     -1-2-4 (bucle)

### Mnemotécnica

::: figure guitar-worm-patterns.svg
	Los trastes que usamos en los patrones X Y Z
	avanzan como un gusano.
	En progresión descendiente ZYX es simétrico,
	se empieza comprimiendo el intervalo agudo.

- El patron X se repite 3 veces, los otros, Y-Z, solo 2.
- X es el ancho. Para recordar cual es Y o Z, aplicar el gusano (ver abajo)
- La escala mayor, o modo I, empieza con el X2.
- Cada patron contiguo salta el modo en 3 grados, porque salta 3 notas. ie. I+3 = IV
- Cuando el modo sea mayor que 5, es más rapido restarle 4. ie. `V+3-7 = V-4 = I`
- Los patrones se comprimen como un gusano para avanzar:

		X: 1-2-4
		Y:  12-4
		Z:  1-34
		X:  1-2-4
		Y:   12-4
		Z:   1-34
		X:   1-2-4


### Progresión descendente

- La escala ahora empieza con el dedo agudo, por lo que el dedo agudo será la tónica
- Por ello, el modo que corresponde a cada patron sube 2 grados (o resta 5) (lo que era el I ahora es III)
	- La escala mayor I, empieza en en Z1
- Puede ser más práctico alinear los patrones con el dedo agudo
	- Lo retrocedemos traste, cuando pasamos de 2a a 3a cuerda
	- Lo retrocedemos otro traste, cuando pasamos de X1 -> Z2 (Es donde ahora pasamos de VII a IV)
- O puede que te sea más sencillo saber el gusano funciona en dirección opuesta

Los grados correspondientes a cada patrón serían:

	Z1 I      1-34
	Y2 V      12-4
	Y1 II     12-4
	X3 VI    1-2-4
	X2 III   1-2-4    
	X1 VII   1-2-4
	Z2 IV    1-34  (fret agudo salta)
	Z1 I     1-34  (bucle)

Recuerda que a la alineación
hay que añadir el salto de 2a a 3a.

### Progresiones en mastil

- Los patrones se repiten arriba y abajo en el mástil
- Para saltar de un patrón a otro, nos saltamos un traste
	- Excepción: si el patrón de ida o de llegada es X2 que es el traste immediato
	- Equivalente: Entre patrones X no saltamos un traste
	- ¿Por qué? El patron X2 es I-II-II (C-D-E en C Mayor) es el que no tiene negras a los lados
- Sirve para dibujar pero a veces es un salto demasiado grande, se suelen usar otras estrategias
- En octavas:
	- Sea ascendente o descendente, después de dos cuerdas y dos notas, estamos en la siguiente octava
	- El segundo dedo marcará el traste de la tónica
	- Movemos el dedo de alineado (el grave o agudo, segun la progresión) a ese traste
	- Volvemos al patrón inicial, si hemos empezado con Y2, otra vez Y2
	- Nos da espacio para hacer 3 octavas completas en las 6 cuerdas
	- La secuencia es repetitiva y fácil
- Solapado en segunda:
	- Saltamos al segundo dedo, descontamos dos patrones en la progresión que llevabamos
	- El mismo principio que en el salto en octavas pero, sin tener que esperar a la tónica
	- Echamos dos patrones para arriba, ie En ascendente Z1 -> Y1
- Solapado en tercera:
	- Saltamos al tercer dedo, descontamos tres patrones en la progresión que llebabamos


### Ejercicios

Para estos ejercicios es importante,
interiorizar en que patron estamos en cada momento:
X1, X2...
Tambien que apliquemos el fingering correcto a cada patrón.

- Escalas ascendentes en cada uno de los modos, con tres notas por cuerda, empezando siempre en el do bajo (8o traste, 6a cuerda)
- Escalas descendentes en cada uno de los modos, con tres notas por cuerda, empezando siempre en el do alto (8o traste, 1a cuerda)
- Para cada modo, aplicar los patrones sucesivos ascendentes y descendentes en una cuerda para sacar una octava de la escala.
- Escala ascendente y descendente cambiando de caja cada octava usando la tonica de puente
- Escala ascendente y descendente haciendo desplazamiento en una nota media que no sea octava (salto -2 o +5 en la secuencia de patrones)
- Escala ascendente y descendente haciendo desplazamiento en una tercera nota (salto -3 o +4 en la secuencia de patrones)
- Escoge un modo al azar, una raiz al azar que puede estar en una cuerda del centro, recorre la escala y despues improvisa sobre ella

## CAGED

CAGED es un sistema que permite tocar un acorde con
cualquier nota raiz en 5 puntos distintos a lo largo del mastil
usando solo 5 patrones de acordes al aire bien conocidos:
C, A, G, E, D pero añadiendo cejilla.

Tambien se puede usar el patron de acorde para puntear en escala, hacer arpegio...
O modificar la forma para que sea el acorde menor, septima...

¿Que diferencias para punteo hay con el método del gusano?
En el método del gusano tocamos notas en escala.
En el método CAGED tocamos notas en el acorde.

Hay que aprender:

- La secuencia: C-A-G-E-D (en ingles, _caged_, enjaulado)
- La forma del acorde con cejilla que corresponde a cada uno de los 5 acordes
- Como empalmar una forma con la siguiente:
	- La cejilla de la siguiente va donde los dedos mas avanzados del acorde anterior.
	- Excepción: D -> C, La segunda cuerda
- Tambien es importante saber las notas de las cuerdas mas graves para poder transponer a la raiz que nos interesa

Para arpegios, las celdas CAGED, son celdas como las escalas explicadas arriba,
conpatrones X, Y y Z

 
::: figure appliedguitartheory.com-caged-major.webp lightbox
	Major and pentatonic.
	Extraido de [Applied Guitar Theory - CAGED System](https://appliedguitartheory.com/lessons/caged-guitar-theory-system/)
::: figure appliedguitartheory.com-caged-minor.webp lightbox
	Minor diatonic and pentatonic chords and arpeggios
	Extraido de [Applied Guitar Theory - Minor CAGED System](https://appliedguitartheory.com/lessons/minor-caged-system/)


::: figure caged-scales.jpg



### Forma E: Raiz en la 6a (y 1a) cuerda

| Frets | Fingering | Intervals | Name |
|-------|-----------|-----------|------|
| 0-2-2-1-0-0 | 1-3-4-2-1-1 | R-p5-R-3M-p5-R | Major
| 0-2-2-0-0-0 | 1-3-4-1-1-1 | R-p5-R-3m-p5-R | Minor
| 0-2-1-1-0-0 | 1-4-2-3-1-1 | R-7M-R-3M-p5-R | Major 7th
| 0-2-0-1-0-0 | 1-3-1-2-1-1 | R-7m-R-3M-p5-R | Dominant 7th
| 0-2-0-0-0-0 | 1-3-1-1-1-1 | R-7m-R-3m-p5-R | Minor 7th
| 0-2-2-2-0-0 | 1-2-3-4-1-1 | R-p5-R-p4-p5-R | Sus4

### Forma A: Raiz en la 5a cuerda

| Frets | Fingering | Intervals | Name |
|-------|-----------|-----------|------|
| 0-0-2-2-2-0 | 1-1-2-3-4-1 | p5-R-p5-R-3M-p5 | Major
| 0-0-2-2-1-0 | 1-1-3-4-2-1 | p5-R-p5-R-3m-p5 | Minor
| 0-0-2-1-2-0 | 1-1-3-2-4-1 | p5-R-p5-7M-3M-p5 | Major 7th
| 0-0-2-0-2-0 | 1-1-3-1-4-1 | p5-R-p5-7m-3M-p5 | Dominant 7th
| 0-0-2-0-1-0 | 1-1-3-1-2-1 | p5-R-p5-7m-3m-p5 | Minor 7th
| 0-0-2-2-3-0 | 1-1-2-3-4-1 | p5-R-p5-R-2M-p5 | Sus2
| 0-0-2-2-0-0 | 1-1-3-4-2-1 | p5-R-p5-R-p4-p5 | Sus4

(suena mejor si la primer cuerda no suena, para que no domine el p5)

### Forma D: Raiz en la 4a cuerda

| Frets | Fingering | Intervals | Name |
|-------|-----------|-----------|------|
| x-0-0-2-3-2 | x-1-1-2-4-3 | x-p5-R-p5-R-3M | Major
| x-0-0-2-3-1 | x-1-1-3-4-2 | x-p5-R-p5-R-3m | Minor
| x-0-0-2-2-2 | x-1-1-2-3-4 | x-p5-R-p5-7M-3M | Major 7h
| x-0-0-2-1-2 | x-1-1-3-2-4 | x-p5-R-p5-7m-3M | Dominant 7h
| x-0-0-2-1-1 | x-1-1-4-2-3 | x-p5-R-p5-7m-3m | Minor 7h
| x-0-0-2-3-0 | x-1-1-3-4-1 | x-p5-R-p5-R-2M | Sus2
| x-0-0-2-3-3 | x-1-1-2-3-4 | x-p5-R-p5-R-p4 | Sus4

En esta forma, el fingering no lo he tomado de ningun manual,
es el que hago yo y puede no ser el más indicado.

### Forma G: Raiz en la 3a cuerda

| Frets | Fingering | Intervals | Name |
|-------|-----------|-----------|------|
| 3-2-0-0-0-3 | 3-2-1-1-1-4 | R-3M-p5-R-3M-R | Major
| 3-1-0-0-3-3 | 3-2-1-1-4-4 | R-3m-p5-R-p5-R | Minor
| 3-2-0-0-0-2 | 3-2-1-1-1-4 | R-3M-p5-R-3M-7M | Major 7th
| 3-2-0-0-0-1 | 3-2-1-1-1-4 | R-3M-p5-R-3M-7m | Dominant 7th
| 3-1-0-0-x-1 | 3-2-1-1-4-4 | R-3m-p5-R-xx-7m | Minor 7th

G Minor 7th muteamos la 2a cuerda con el mismo dedo que freteamos la 1a
para evitar que suene la 3M.


### Forma C

Como la afinación estandard es E-A-D-G-B-E el acorde C no tiene ninguna raiz al aire.
Los otros acordes CAGED tienen una tonica en la cejilla y otra en el traste mas avanzado.

No he encontrado versiones basadas en la forma mayor para el menor

| Frets | Fingering | Intervals | Name |
|-------|-----------|-----------|------|
| 0-3-2-0-1-0 | 1-4-3-1-2-1 | 3M-R-3M-p5-R-3M | Major
| x-3-1-0-1-x | x-4-3-1-1-1 | 3M-R-3M-p5-R-3M | Minor (intocable con cejilla)
| 3-3-1-0-x-x | 3-4-2-1-x-x | p5-R-3m-p5-x-x | Minor
| 0-3-2-0-0-0 | 1-3-2-1-1-1 | 3M-R-3M-p5-7M-3M | Major 7th

El empalme entre D y C es la segunda cuerda, no el traste.

### Mnemotecnicas para construirlos

Las formas E A y D, comparten estructura harmonica:

- Fijate que los intervalos de los E, A y D mayores tienen estructura: R-p5-R-3M
- E, A y D son diferentes porque la afinacion relativa de las cuerdas se rompe entre la 2 y tercera cuerda.
	- En A, avanzamos un taste el dedo de abajo
	- En D, avanzamos un traste los dos dedos de abajo
- R está duplicada en la cejilla y en en el dedo avanzado del medio
- p5 es la cuerda mas grave con dedo avanzado
- 3M es la cuerda mas aguda con dedo avanzado
- Para hacer un acorde menor (Minor o Minor 7th) retiraremos un traste la cuerda 3M, el dedo avanzado inferior, para que sea 3m
- Para hacer los acordes 7th retiraremos la R duplicada en el dedo avanzado de en medio
	- Un traste para tener el 7M (Major 7th)
	- Dos trastes para tener el 7m (Minor 7th y Dominant 7th)
- En las transiciones de una forma a la otra, pasamos la R más avanzada a la cejilla
	- Excepcion D->C en que 


transition | bar shift | bridge string |
-----|---|---|
C -> A | 3 | 5a |
A -> G | 2 | 3a |
G -> E | 3 | 1a |
E -> D | 2 | 4a |
D -> C | 2 | 2a |


## Cajas Pentatónicas

Función

- Las escalas pentatónicas son útiles como marco para hacer punteados.
- Las notas de la escala están en intervalos de 2 y 3 semitonos.
- Como son subconjuntos de varios modos diatónicos, cuadran bastante bien con armonías diatónicas
- Las cajas son zonas en las que tocar 2 notas de la pentatónica en cada cuerda
- Las cajas estan encabalgadas, la segunda nota de una es la primera de la siguiente



Útiles para hacer punteos.
Definen zonas del mástil donde tocar con dos notas por cuerda.
Las posiciones de las dos notas de cada zona están
aproximadamente colocadas haciendo dos columnas,
y las zonas estan encabalgadas de forma que 
la segunda columna de una zona se convierte
en la primera columna de la siguiente.
Bastaria pu


Cada zona comparte una fila con la anterior.
El patron se repite cada 5 zonas que coincide con una octava en el mastil.

	 Em     G  Asus Bmblues Dscot
	0 - - 3 - 5 - 7 - - 10 - 12
	0 - - 3 - 5 - - 8 - 10 - 12
	0 - 2 - 4 - - 7 - 9 -  - 12
	0 - 2 - - 5 - 7 - 9 -  - 12
	0 - 2 - - 5 - 7 - - 10 - 12
	0 - - 3 - 5 - 7 - - 10 - 12





Muy parecida a como funciona el método del gusano pero
con dos notas por cuerda.
Definimos varias zonas en el mastil donde tocarlas.
Nos sirven de marco para hacer punteos.

En el caso de las pentatónicas, cada posicion toma
el segundo dedo de la posicion anterior y 


