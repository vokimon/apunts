# Navegación en el mástil

## Método tripletas

Este método es una simplificación del método
explicado aquí:

https://www.youtube.com/watch?v=rQf6i8KIwJU

**Objetivo:**
poder puntear una escala diatónica
con cualquier raiz y modo,
en cualquier punto del mastil.

### Construcción

Queremos construir una escala diatónica
tocando 3 notas en cada cuerda.
Las escalas diatónicas,
tienen intervalos de tono y semitono,
donde los intervalos de semitono están
separados como mínimo por 2 intérvalos de tono.
Eso nos deja solo 3 posibles configuraciones de fingering
que llamaremos X Y Z:

|Nombre| Intervalos    | Dedos | Tripletas en C Mayor |
|------|---------------|-------|----|
|  X   | tono-tono     | 1-2-4 | **C**DE, **F**GA o **G**AB |
|  Y   | semitono-tono | 12-4  | **E**FG o **B**CD |
|  Z   | tono-semitono | 1-34  | **D**CE o **A**BC |

El guion significa un traste que saltamos. 1 Indice, 2 medio, 3 anular, 4 meñique.

En la escala hay 7 notas que se repiten en octavas.
Si saltamos o agrupamos las notas de 3 en 3,
obtenemos 7 tripletas diferentes que se repiten cada 3 octavas.
El motivo matemático de que esto pase es que los números 7 y 3 no comparten factores comunes.

Ejemplo en C mayor: **CDE|FGA|B**CD|EFG|AB**C|DEF|GAB**|CDE

Así obtenemos paquetes de 3 notas se suceden en orden y de forma cíclica.
Numerándolos para distinguir Xs, Ys y Zs:

|Nombre| Tonica | C Major |
|-|-|-|
|X1 | V | **G**AB
|X2 | I | **C**DE
|X3 | IV | **F**GA
|Y1 | VII | **B**CD
|Y2 | III | **E**FG
|Z1 | VI | **A**BC
|Z2 | II | **D**EF

Convenientemente:

- La mayoría de saltos
entre la primera nota de un grupo y la del siguiente
es una cuarta perfecta, es decir, 5 semitonos.
- La mayoría de cuerdas
de la guitarra, en afinación estandard EADBE,
están afinadas a distancia tonal de 5 semitonos entre ellas.
- Asi que la mayoría de las veces podemos alinear
la primera nota de un patrón encima de la
primera del siguiente.

Con dos excepciones muy localizadas:

- El intervalo entre F y B (IV a VII) es una 4a augmentada, es decir 6 semitonos en vez de 5.
	- F->B es el unico salto de 4a en naturales con 3 negras entre medio.
	- Por eso, **moveremos los patrones un traste agudo, a partir de la transicion de X3 -> Y1**
- La distancia tonal entre la 2a y la 3a cuerda es de 4 semitonos en vez de 5.
	- Por eso, **moveremos los patrones un traste agudo en las dos cuerdas más agudas (1a y 2a).**
- Los dos desplazamientos se combinan

Podemos observar la sequencia de patrones,
los intervalos de 5 semitonos
y el semitono que sobra entre X3 y Y1:

	   X2    X3     Y1    Y2   Z1     Z2    X1    X2'
	|C_D_E|F_G_A|_|BC_D_|EF_G_|A_BC_|D_EF_|G_A_B|C_D_E|
	|1-2-4|1-2-4|-|12-4-|12-4-|1-24-|1-24-|1-2-4|1-2-4|


### Escalas diatónicas ascendentes

- Establece 3 patrones de fretting posibles para cada cuerda, incluyendo el fingering
	- X: 1-2-4
	- Y: 12-4
	- Z: 1-34
- Los patrones se dan cíclicamente **XXXYYZZ**XXXYYZZ de cuerda grave a aguda
	- Numeramos las repeticiones: X1 X2 X3 Y1 Y2 Z1 Z2 X1 X2
	- Hay 7 patrones y 6 cuerdas. Sí, uno siempre queda fuera
- Los patrones se alinean verticalmente a la nota mas grave, excepto:
	- Cuando saltamos de la 3a y 2a cuerda, avanzamos un traste
	- Cuando salimos de los patrones X, avanzamos un traste
	- Cuando se producen las dos condiciones se avanzan dos trastes
- Podemos empezar la figura en cualquier traste y en cualquier nota
- La nota en la que empecemos define la tónica
- El patron por el que empecemos define el modo diatónico de la escala

		X1 V     1-2-4
		X2 I     1-2-4    
		X3 IV    1-2-4
		Y1 VII    12-4 (fret grave avanza)
		Y2 III    12-4
		Z1 VI     1-34
		Z2 II     1-34
		X1 V      1-2-4 (bucle)

### Mnemotécnica

- Los patrones Y y Z se repiten dos veces, X se repite 3
- El X2 es la escala mayor I
- Los modos saltan sumando 3 grados, que es el numero de notas que sube cada patron: I IV VII III VI II V I
- Cuando el modo sea mayor que 5, es más rapido restarle 4 ( `x+3-7 = x-4`)
- Los patrones se comprimen como un gusano para avanzar:

		: 1-2-4
		:  12-4
		:  1-34
		:  1-2-4
		:   12-4
		:   1-34
		:   1-2-4

### Justificación

- ¿Por qué los patrones ciclan?
- ¿Por qué cada patrón empieza en un modo diferente?
- ¿Por qué están en ese orden?
- ¿Por qué los dedos van ahi?
- ¿Por qué están mayormente alineados en las cuerdas?
- ¿Por qué desalineamos un traste las cuerdas 1a y 2a?
- ¿Por qué desalineamos otro traste de X3 a Y1?

La escala tiene 7 notas que se repiten en octavas
Si las agrupamos de 3 en 3,
como los números 3 y 7 no tienen factores comunes,
volveremos a la misma nota en 7 saltos sin repetir ninguna.
El bucle serían 3 octavas y 21 notas:

**CDE|FGA|B**CD|EFG|AB**C|DEF|GAB**|CDE

Si en vez de en grados de escala lo miramos en semitonos,
vemos que todas las tripletas estan a 5 semitonos (una 4a perfecta)
a excepción de la IV (X3) (Fa en Mayor) y la VII (Y1) (Si en Mayor)
que tienen un intervalo de 6 semitonos (4a augmentada).
De hecho en el teclado del piano puedes ver que
Fa y Si son las unicas notas a intervalo de 4a,
que entre ellas tienen 3 teclas negras.

La afinación estandard de la guitarra establece entre
las cuerdas una distancia de 5 semitonos.
La excepción son la 3a y la 2a cuerdas que estan
a una distancia tonal de 6 semitonos.
Por eso, cualquier patrón que establezcamos,
estará un traste más agudo en la 2a y 1a cuerda.


El patron de fingering y el orden de los patrones
los puedes deducir del siguiente cuadro.
También se ve como, entre X3 y Y1,
sobra un semitono de los grupos de 5.

Por otro lado, las cuerdas de la guitarra en afinación estandard,
estan a una distancia tonal de 5 semitonos,
a excepcion de la 3a y la 2a que estan a una distancia tonal
de 4 semitonos.
Por eso, la mayoria de patrones están alineados,
pero en el salto de la 3a a la 2a se avanza un traste.
La 1a mantiene este avance.


### Progresión descendente

- La escala ahora empieza con el dedo agudo, por lo que el dedo agudo será la tónica
- Por ello, el modo que corresponde a cada patron sube 2 grados (o resta 5)
	- La escala mayor I, está en Z1
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
	- Por qué: El patron X2 es I-II-II (C-D-E en C Mayor) es el que no tiene negras
- Sirve para dibujar pero a veces es un salto demasiado grande, se suelen usar otras estrategias
- En octavas:
	- Sea ascendente o descendente, después de dos cuerdas y dos notas, estamos en la siguiente octava
	- El segundo dedo marcará el traste de la tónica
	- Movemos el dedo de alineado (el grave o agudo, segun la progresión) a ese traste
	- Volvemos al patrón inicial
	- Nos da espacio para hacer 3 octavas completas en las 6 cuerdas
	- La secuencia es repetitiva y fácil
- Solapado en segunda:
	- Saltamos al segundo dedo, descontamos dos patrones en la progresión que llevabamos
	- El mismo principio que en el salto en octavas pero, sin tener que esperar a la tónica
	- Echamos dos patrones para arriba, ie En ascendente Z1 -> Y1
- Solapado en tercera:
	- Saltamos al tercer dedo, descontamos tres patrones en la progresión que llebabamos

## CAGED

CAGED es un sistema que permite tocar un acorde con
cualquier nota raiz en 5 puntos distintos a lo largo del mastil
usando solo 5 patrones de acordes al aire bien conocidos:
C, A, G, E, D pero añadiendo cejilla.

Tambien se puede usar el patron de acorde para puntear en escala, hacer arpegio...
O modificar la forma para que sea el acorde menor, septima...

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


