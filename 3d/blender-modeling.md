# Curso Blender

Introducción: https://www.youtube.com/watch?v=2f5RaH5UCmo&list=PLRfbgTMylROJvWR5IbrF6ZMSTKJ4ToJRV
Modelado: https://www.youtube.com/playlist?list=PLRfbgTMylROKqXDVVCHobVyM-rVNUFH80
Modificadores: https://www.youtube.com/playlist?list=PLRfbgTMylROKYYtPTxfqvTuTcQx8Bjzp\_
Ejemplos de Modelado Low-Poly: https://www.youtube.com/playlist?list=PLRfbgTMylROIE0G62Mi-PerWehj_AdEwi
Iluminación: https://www.youtube.com/playlist?list=PLRfbgTMylROLeFQ52aIvtWtPovVKUhedV
Materiales: https://youtu.be/jZQ8CE8MYgw

## Preguntas

* Lattice deformation y el centro del objeto.

## Abreviaciones

* Sh (Mayusculas)
* Cn (Control)
* Alt (Alt)
* RB/MB/LB Right/Middle/Left Mouse Button

## Glossario

* Objeto: Sujeto de transformaciones 3D.
* Object Origin/Center: Punto de referencia de las transfromaciones y de las coordenadas locales del objeto.
* Colleccion: Elemento organizativo que incluye otros objetos.
* Parent/Child: Un objeto es hijo de otro si hereda todas las transformaciones del padre
* Pivot point: Punto de referencia de la interficie con diversos usos 
  * Situar los objetos nuevos
  * Punto fijo de trasformaciones afines (escalado, rotación...)
* Vertice (vertex): punto en el espacio que forma parte de una geometría
* Arista/Segmento (edge): segmento que une dos vértices como parte de una geometría
* Cara/Poligono (face): Area delimitada por segmentos
* Malla (mesh): Un objeto definido por un conjunto de caras, aristas y vertices que definen una superficie compleja.
* Quad: Cara delimitada por cuatro segmentos.
* Tri: Cara delimitada por tres segmentos.
* N-gon: Cara delimitada por mas de 4 segmentos.
* Polo: Vertice en el que convergen 3, 5 o mas vertices. Si convergen 1, 2, o 4, no es polo.
* Concave face: Cara definida por vertices no coplanares
* Crease: Sharpenes of an edge/vertex
* Face Loop: Sequencia de quads adyacentes por segmentos opuestos 
  * Se para cuando un vertice no tiene 4 segmentos.
* Edge Loop: Sequencia de segmentos adyacentes
* Edge Ring: Sequencia de segmentos que conectan dos edgeloops adjacentes
* Empty: objeto sin geometria pero al que afectan las transformaciones
* Topology: Disposicion de los Vertex-Edges-Faces para dar forma a una malla.
* Manyfold: Superficie cerrada sin intersecciones con ella misma.
* Primitiva: Objeto básico que se usa para modelar objetos mas complejos.
* Curve: Object defined as a line interpolated between several control vertices 
  * Poly(line): Puntos connectados por lineas rectas
  * Path: Pasa por los puntos de forma suave
  * Bézier: Nodos por donde pasa con control points para controlar las derivadas
  * Nurbs: Non uniform rational basis spline: solo pasan por el primer y ultimo punto, el resto controlan la curbatura, conteniendola
* Control vertice:
* Curve segment: the interpolated object between two concurrent control points
* Cyclic curve: having the last control point connected to the first one
* Active object: Last selected object (even if later unselected). Single object ops and ops that take a distinctive object in a group.
* Selected objects:

## Navegación

MB -> Orbitar (rotar alrededor del centro de la vista)
Also numpad arrows
Sh+MB -> Panning (changes the orbit center
Cn+MB -> Zoom
Also Numpad +-
Also mouse wheeL
Alt+MB drag -> Isometric axis view closer in drag direction
Alt+MB click -> Center pan on click

Numpad 5 -> Toggle Isometric - Perspective
Numpad 7-1-3: View from axis X Y Z
Numpad 9: View from the other side (z up unless actually z)
Numpad .: Adapt view to selected objects
Numpad 0: Camera view
Home: View all
Numpad /: Isolate object (para editarlo sin ruido de los otros objetos)

Para mayor control se aconseja manipular los objetos en vistas
ortogonales alineadas a cada eje.

## Selection

T: para ver el panel de herramientas
Por defecto esta en la herramienta de seleccion modo cuadro.

W cicla modo seleccion:

* Click o cuadro (Recomendado por defecto)
* Circulo (con radio configurable)
* Selector por lazo
* Seleccion y mueve (en segun que contextos mas rapido, pero error prone)

Modificadores de seleccion:

* Por defecto, substituye la seleccion anterior
* Shift: add or remove (toggle)
* Control: Shortest path ???

Seleccion vs Activo

El activo es el ultimo seleccionado, outline amarillo,
a diferencia de los otros seleccionados que aparecen en naranja.

Al lado del icono de seleccion aparece el activo
Vemos la ultima seleccion al lado del icono y en la lista de objetos.

Lista de objetos

El nombre sale en el color del outline. Fondo azul.

Selecciones inteligentes:

* Alt-click: selecciona un loop
* Cnt-Alt-click: selecciona un ring
* ShCn-Numpad+: Repite seleccion con intercalado
* CN-J join selected objects (el activo mantiene el punto origen)
* Sh-R Repetir la ultima operación

## Object mode

Sh+A -> add an object

Cursor: Es un punto de referencia que se usa para varias cosas.
De entrada como punto de inserción de los nuevos objetos.
Por defecto esta en el origen.

* Sh-RB Set Cursor (podemos arrastrar) 
  * Si mientras arrastramos presionamos Cn (no antes) hara snap
* CnSh-R posiciona el cursor en el medio de la geometria seleccionada

## Transformaciones

* **G**rab
* **R**otate
* **S**cale

Se entra en modo transformación,
se acaba aceptandola on return o LB o abortandola con ESC o RB.
Entre medias podemos hacer diferentes cosas.

* Mover el raton para controlar la transformación
* por defecto se limita al plano perpendicular de la vista
* Pulsar x y o z para limitar la transforamción a ese eje
* Pulsar X Y o Z para limitar la transformacion al plano perpendicular al eje
* Si repetimos xyzXYZ se referiran a las coordenadas locales en vez de las globales
* Indicar numericamente el valor de la transformación 
  * Numero de grados
* Arrastrando con MB, limita al eje mas cercano
* Arrastrando con Sh-MB, limita al plano mas cercano
* Sh en modo precision
* Cn invierte el modo snap (si esta habilitado, lo deshabilita y alreves)
* Si pulsamos B podemos escoger el elemento de snap.

En la parte superior hay un toolbar con modificadores de las transformaciones.

* Ejes de referencia: Global, local, normales...
* Pivote para la transformacion: Centro del objeto, origen, cursor, el elemento activo 
  * El elemento activo es interesante para una selección múltiple que se transforme de forma solidaria, si no cada uno rotara sobre si mismo
* Modo snap. Que puede estar activo o no por defecto 
  * Recomendado desactivarlo y activarlo con Cn cuando se requiera.
  * Desplegable para escoger que se usa como snap (vertice, arista, plano,
* Sh D: duplicar, a continuacion podemos aplicar transformaciones (por defecto empieza en Grab)
* Sh R: repetir operacion (por ejemplo si duplicamos con transformacion, volvera a transforma para hacer arrays y demas)

## Visualización

en la esquina superior derecha esta el toolbar de visualizacion

* Que tipo de objetos ver y poder interacturar
* Que gizmos (elementos de control) ver
* Que overlays ver (ejes, rejilla...)
* Como renderizar los objetos (wireframe, sombreado, goroud...)

## Proceso de producción

* Layout: Encuadre de los elementos de la escena 
  * Se puede hacer con primitivas simples

# Edit mode

* Tab o Sh-R intercambia entre object mode y edit mode
* Edit mode es para modificar la geometria que tiene tres niveles de objetos
* 1 vertices 2 segmentos 3 caras (seleccionamos con 1, 2 y 3)
* RB Menu del nivel seleccionado (vertex, edge, face) 
  * Tambien Cn-V, Cn-E, C-F)
* l (linked) selecciona toda la geometria enlazada a la selección
* Transformaciones (GSR) se aplican de forma similar. 
  * Diferencias?
* Alt-S - scale along normals
* GG - los mueve dentro del objeto superior 
  * Si esta activado el automerge, cuando arrastras a otro vertice/arista los fusiona
  * Options Transform en el toolbar arriba a la derecha
  * Explicitamente M (merge) en edit mode
* Dentro de una G de vertice, C permite extender el segmento, no solo acortarlo como GG.
* Escala es juntar o separar, mejor que trasladar uno a uno
* Cn J: Join, junta punts seleccionats amb un vertex
* Alt-click: Select loop
* Alt-Z: See through (tambien para seleccionar ocultos)

Compte: Se propaga en coordenadas de vertice: suele ser bueno aplicar antes transformaciones
Cn-A en modo objeto aplica transformaciones a los vertices, reseteando las transformaciones de objeto.

## Edicion proporcional

* O (o en el toolbar) - Intercambia modo Transformacion proporcional 
  * Las transformaciones afectan fuera de la seleccion a la geometria conectada
  * genera cambios mas orgánicos
  * Podemos definir area de afectación
  * PgUp PgDn o en el toolbar o con wheel

## Subdivide

* Cn-R Subdivide 
  * Tienen que ser quads y no tener "cosas raras"
  * Primero indicamos el eje, aproximando el cursor al segmento que queremos partir
  * Una vez visualice el eje: 
    * AvPag/RePag: numero de segmentos
    * Tambien podemos escribir el numero de segmentos con numeros
    * (LB/return para confirmar, RB/ESC para cancelar)
  * Despues entramos en el modo de transformacion de las divisiones por defecto una translación siguiendo el eje cortado 
    * Podemos aplicar R y S
    * ESC/RB para dejarlo por defecto en el medio
    * Click para confirmar
  * Hasta que selecionemos otra cosa tendremos el Panel de Accion abierto para alterar los parametros anteriores y otros

## Cut

* Last resource when subdivide is not the option 
  * Mas control, pero menos regular, puede derivar en mayas menos manipulables
* K - Cut 
  * C cut through, la linia atraviesa el otro lado (recomendado)
  * Arrastrar: Freehand
  * click: pivot para cortar con linia
  * click on point: set the point as pivot
  * Sh middle point cut
  * Cn ignore snap
  * RB-ESC undo last step
  * Podemos hacer panning con las combinaciones de (Cn-Sh-Alt)MB

## Extrusion

Extruir es extender una geometria en una dirección.
Hay muchas variaciones de como hacerlo.

Alt-E: Menu extrusiones disponibles para las primitivas seleccionadas

* E Extrude Face/Vertex/Edge
* Extrude along normals no same direction as E does
* Extrude individually, break connections
* Extrude manifold, fusiona y divide con lo que genera 
  * Super util cuando extruimos para dentro y se generan planos bordeando la extrusion
* Extrude repeat, crece en segmentos, podemos añadir un step

Ojo: si extruimos y cancelamos, lo que cancelamos es la transformación.
La geometria queda duplicada, y eso genera ruido para otras operaciones.
Para deshacer la extrusion de forma efectiva, Cn-Z.
Si no nos hemos dado cuenta, M Merge by distance. Abajo deberia decir que ha eliminado geometria.

Ojo: Muy sensible a la escala, normalmente querremos aplicar escala (Cn-A)
antes de aplicar un bevel.

## Inset

Se aplica a faces (Se puede aplicar a segmentos cerrados?)

I - Crea nodes en l'area interior a una distancia controlable con el raton
\- Consejo: aleja el raton antes de pulsar I para tener espacio de control
\- I - Individual (inset per face en vez de todo)
\- O - Outset: el espacio lo crea fuera
\- Cnt - Con el raton profundiza o
\- ESC/RB - Cancel
\- Return/LB - Acepta y
\- Queda seleccionado con las opciones de accion
\- Edge Rail: si hay una arista de un inset anterior, la sigue, ideal si queremos hacer insets concentricos
\- Offset even: Activado calcula distancia a las aristas en vez de a los vertices, que suele ser mas natural. (Deduzco por lo que hace. Se ve cuando incluyes varias faces)

## Bevel

Dos tipos diferentes de bevel

* CnSh-B Vertex Bevel
* Cn-B Segment Bevel
* Aun podemos pasar de uno a otro con V

Mecanica

* Cuando empieza controlamos la extension con la distancia al centro de la pantalla 
  * A area (default)
  * P profile, concavidad/convexidad
  * S segments, subdivisiones
* Con la rueda o PgUp/PgDn controlamos el numero de segmentos
* Al confirmar con RB o Return podemos aun alterar los parametros en el panel de operacion abajo izquierda (puede estar colapsado)

Truco: De vertice a redonda. Vertex Bevel dependiendo del perfil, genera estrellas, redondas, rombos

Truco: Si aplicamos un Edge Bevel a todo el loop, mantendremos la topologia.
Y al revés si no lo hacemos en todo el loop o si lo hacemos de vertice la rompemos.

## Unir geometrias

* Cn-X disolver (eliminar geometria pero sin generar vacio)
* JF Fill cavity
* J Join vertex (en orden de selección)
* (Face Menu) Poke face: crea un vertice en el medio y lo enlaza con los vertices de la face

## Symmetrize

Menu Mesh/Symmetrize:

Compara las geometrias seleccionadas a uno y otro lado de un eje,
y hace que la una sea igual que la otra. pe. +X -> -X.
Lo no seleccionado lo mantiene.
Quiere decir que segun lo que tengamos seleccionado
en uno o otro lado, podemos, no intencionadamente, perder geometrias o duplicarlas.

## Conectar (o penetrar) geometrias

Menu Edge / Bridge Edge Loops

Seleccionados dos grupos de aristas inconexos entre ellos,
genera geometria para conectar uno con otro.
J une dos vertices de la misma geometria.

## Organizando los modelos

M mueve a la coleccion existente o nueva
Aparecen en el panel con la estructura de la escena a la derecha.

* Cn-P: Establece relacion padre (activo) y hijo (selecionados no activos) 
  * Los hijos heredan las transformaciones 3D del padre, las suyas locales
  * Cuando establecemos la relacion, podemos mantener o no las transformaciones absolutas 
    * Si las mantenemos, se traduciran a transformaciones respecto al padre
    * Si no, las locales se aplicarán encima del padre.
    * Ojo si hay transformaciones no aplicadas.

## Otros Objetos

### Curvas

Una curva es un objeto creado a partir de una secuencia
de puntos que se conectan por segmentos usando diferentes
tipos de interpolación.

* Radius: A cada punto podemos darle un grosor
* Weight: TODO
* Tilt:
* Hook:

Alt-S Cambia el radio del punto seleccionado
El radio de todos los puntos se controla
desde las propiedades.

* E Extrude point and move
* F Fill connect disconnected points
* x borrar
* Cn-T Node Tilt
* Alt-T Clear Node Till
* V Toggle Node type
* Sh-N

Herramienta de dibujar

* Cursor en le plano perpendicular que pasa por el cursor
* Surface, plano encima de la superficie que encuentra. 
  * Util para cables y raices

### Redes 3D (Lattice)

Una red 3D es una matriz de puntos con 8 vecinos cada uno.

### Latices

## Geometry modifiers

Los modificadores per

**Generate/Mirror:** Genera geometria simétrica a origen de coordenadas.

* Alternativa al simetrize, pero en vez de puntual lo aplica continuamente.
* La geometria espejo no existe realmente hasta que no aplicamos el modificadores con lo cual se genera la geometria y se pierde el modificador.
* Hay que marcar la opcion de cliping para que no cruzar el plano de reflexion.

**Generate/Solidify:** Da grosor a una superficie creando una superficie paralela y cerrandola si quedase abierta.

* Offset hacia donde crece la cara: -1 interno, 0 igual, +1 externo

**Generate/Array:** Repite una geometria.

* Alternativa al Sh-R
* Offset para cada eje 
  * Relative: Factor relativo del tamaño del objeto
  * Constant: independiente de la medida del objeto en parametros
  * Object: Especificamos un objeto la transformacion del cual se aplica repetidamente 
    * Se suele usar con un objeto Empty
    * Permite hacer rotaciones y escalados

**Generate/Screw:** Genera un objeto por revolución de otro

* Eje
* Steps de revolucion
* Angulos de inicio y final
* Desplazamiento por vuelta para hacer espirales

**Deform/Curve:**

**Deform/Lattice:** Deformacion respecto a un laticce regular.

## Materiales

Propiedades

Transmisivos

Activar transmisivo

Ponerle un grosor

Cn L / Link Materials (Pasar un material del objeto activo a los seleccionados)

## Organización y limpieza

Cosas que tenemos que limpiar:

* Eliminar geometrias duplicadas o superfluas
* Aplicar modificadores de geometria
* Convertir Curvas -> A malla
* Coherencia en las normales
* Agrupar sub-objetos en objetos
* Aplicar la escala y rotación
* Origen de los objetos en el punto de aplicación
* Nombrar los assets

CnJ Unir objetos

Transformar curvas

Consejo: Mantener un objeto duplicado de trabajo y otro convertido en mesh para usar

Cn . Move el punto de origen

### Normales:

Ver Normales: Toolbar overlays / Face Orientation

Sh-N recalcula normales automaticamente

TODO: Invertir una concreta

F2: renombrar objeto

Object/Asset/Mark as asset

## Iluminación

### Environment

https://www.youtube.com/watch?v=IXeOQLvbvhI&list=PLRfbgTMylROLeFQ52aIvtWtPovVKUhedV&index=3

El environment es clave para dar naturalidad a la iluminación.

* Tono para la luz difusa
* Fondo para los reflejos

Pestaña de propiedades World.
Tambien lo podemos editar como un material modular en el Shader Editor (o Pestaña layout Shader)
En el Shader Editor en vez de Object seleccionamos World para ver el material.

El shader de world tiene dos salidas: Surface y Volumen

Por defecto Volumen desconectado y Surface esta conectado a un Background.
Podemos poner el background a un color plano y ya tenemos efecto.
Strength hace que el color tenga mas efecto en el modelo.

Podemos conectar el color a otro modulo por ejemplo un environment texture.
Las Environment texture son imagenes que se mapean a coordenadas polares (.exr).
Muchos exr en dominio publico en https://polyhaven.com

Como otros shaders se evaluan para cada punto, en este caso de la esfera.
Ese punto viene dado por un vector que es el input de 'vector' de "Environment Texture".
Podemos transformar el exr (rotar, desplazar, escalar...)
aplicando un Mapping al vector que entonces lo tenemos que tomar de "TextureCoordinates:Generated".

Podemos modular el color de la textura interponiendo un Hue/Saturation/Value y cambiandole el Hue.
Podemos augmentar el contraste para darle dramatismo mas a los reflejos.

## Luces puntuales

Se pueden añadir luces omni añadiendolas como objeto.
Son luces que decrecen con la distancia.
Tienen un color y un radio de emision (cuan grande es la fuente).
El radio afecta a los bordes de las sombras que se veran mas difuminados si es grande,
y a los objetos que estan dentro del radio que se visualizaran sin sombra.

## Luces solares (direccionales)

DUDA: Porque no me hacen efecto?

## Motor de renderizado

Propiedades de "Render" icono Camara.
Motor de renderizado EEVEE (Real-time)

Mil formas de hacer y mejorar outlines en Blender: https://www.youtube.com/watch?v=cnQu1kMs49s

## Asset library

Menu Object/Asset

Cuando arrastramos un asset a una escena busca una superficie donde soportarlo adaptando la orientacion si la superficie no es plana.

Modificador Boleanos

Especificamos otro objeto que recorta. Si modificamos el objeto, se modifica el recorte.

Normalmente no queremos ver los recortadores. DUDA: Como?

Si hay mas de un recortador hay que crear un modificador con el nuevo objeto.

Seleccionar random

Substituir objeto Link Object data: Substituye un objeto por

## Camara

La camara se añade como objeto

CnAlt Numpad 0 Pon la camara en la vista

Numpad 0 Va a la vista de camara (o el icono de la camara debajo de los ejes)

El candado debajo de los ejes permite arrastrar la camara con la vista.

El icono de la camara.

## Iluminación

Los materiales emisivos afectan a los otros objetos.

Pestaña propiedados World

Si creamos uno, creara un gris homogeneo. Shading.

Podemos dar un hdi (polyhaven.com).

Activar Propiedades Render / Raytracing

Fast GI Aproximation:

TODO: Como activar sobras por oclusion??

En el modo Shading

Si no queremos que se vea el hdr solo que de color, Render Film Transparent

Añadir un TextureCoords y un Vector Mapping para manipular el mapeo polar.

Alt arrastrar lo desconecta.

Mix Color: Combina dos fuentes de color

Plano invisible: Bloquea luz pero no aparece. Opciones de objeto: visibility / camera.

Point lights: Para puntos de luz (bombillas, velas...)

* Radio: zona  de emision

Consejo: si hay un grupo de luces, no es necesario una luz por fuente, hacer una fuente con radio amplio.

### Gloom

Workspace Compositing

Glare type Bloom

## Atmosfera: Niebla/Polvo

* Creamos un objeto que defina el volumen
* Quitarle el surface
* Añadirle volumen
* Bajamos density
* Hay que activar el aspecto 'volumen' en la luz
* En "render" hay opciones de calidad (rsolucion) pra volumen
* La niebla tiene color, por defecto neutro

Shaders:

Density:

Emision: luz interna de la 'niebla'

Coordenadas:

* generated: respecto a las dimensiones del objeto
* uv: el mapeo que hagas
* normal, camera, object, window, reflection?

## Renderizado

\- hdri

# Modelado personaje

## Herramientas: Subdivision Surface

Subdivision surface: modifier que altera una geometria subdividiendo y suavizando

Como modificacor en Generator/SubdivisionSurface pero tambien con Cn1, Cn2, Cn3...Cn5

Hay un nivel diferente para render y para viewport (diseño)

Catmul clark es el algoritmo, simple no deforma

Queda todo muy suavizado, podemos hacer loops extra para marcar mas las formas con Subdivide, Inset o Extrude.

Modos de visualizacion:

* On cage: proyecta la geometria real a la interpolada
* Los otros son para ver el interpolado en Edit, object o render.

Control click derecho en modo edicion con plano seleccionado

Marcar segmentos como creasing haces que sea una arista fuerte.

* Equivalente a la

## Carga de referencias

Imagen de referencia sirve para

Sh-A / Image / Reference o Mesh plane

Reference: mas brillante

Mesh plane: podemos recortarlo alterando la geometria

* Centrar el origen en los pies
* Escalar la imagen al tamaño real

Grid field (para cerrar puntas)

Inset con symmetry si es en el centro para que junte los dos lados 'B' o boundary en el panel de tool.

## Cuerpo

## Manos

* Cubo
* Escalamos a la palma
* Dividimos en tres: molla, pulgar, tarso
* Dividimos los 4 dedos
* Ajustamos el tamaño de cada dedo
* Con edicion proporcional deformamos la salida de los dedos para que esten avanzados el medio i anular. Tambien hara que las normales diverjan
* Extruimos los dedos por separado
* Reducimos las esquinas de los quads de los extremos en la muñeca
* Extruimos la muñeca de los cuads del medio
* Extruimos el pulgar, movemos a y y escalamos
* Damos mas geometria para las falanges (loop cut en 3 segmentos
* Añadimos dos loop cuts en los tarsos
* Ajustamos la geometria
* Cn-1 para aplicar subsurface
* En las uniones de los dedos quedara un polo de 6 puntos que conviene corregir 
  * para corregirlo hacemos un bevel de los segmentos que separan y la primera continuacion por ambos lados
  * Dividimos el bevel por el medio
  * Del bevel quedara una por cada lado, gg para fusionarla al anterior vertice, y borrar el segmento de enmedio
  * Esta bien si solo hay vertices con 4, 3 o 5
* Para que la muñeca coincida con los 8 vertices del cuerpo añadir un loop cut transversal
* Relax de la muñeca para juntarlo con el cuerpo
* Copiarlo al cuerpo

## Ropa

* Sh-D Duplicar
* P para separar en otro objeto
* Alt-S para inflar o reducir
* Modelamos o ajustamos 
  * Cuellos y mangas
* Solidify al acabar (si hiciera falta

## Rostro

Si modelamos la cara  con geometria:

* Ojos 
  * Normalmente en los ojos y las cabidades tenemos un inset que los envuelve.
  * Dejar un quadentre los ojos y el centro. Al juntarse los dos insets de los ojos deja un vertice de 6, mala topologia
  * DUDA: Como repartir los loops?
  * Profundicar la cuenca
  * Mover el cursor al centro del parpado
  * insertar una uvsfere, rotarla para que el polo quede en el centro
  * Suavizar
  * Modifier Mirror pero tomando la cabeza como punto de referencia
* Nariz 
  * como esta en el eje, hacemos un inset con boundary activado (B mientras lo arrastramos)
  * Extrude para darle volumen, mover los vertices para darle la caracteristica
* Boca 
  * Seleccionamos dos linias horizontales de quads
  * inset con boundary
  * borrar el interior de la boca
  * 
  * marcar los labios con un loop extra
  * cerrar la cavidad de la boca por dentro
* Dientes y lengua 
  * Tomamos un loop de abajo de la boca y lo extruimpos
* Orejas 
  * construirlas afuera con geometria similar en el punto de inserción
* Cabello 
  * Corto: Seleccionar la zona, duplicar i inflate o extrude along the normals
  * Largo liso: partir de un plano subdividir, modelar y solidify
  * No pasa nada si entra en el cuerpo

Con el mouse encima del modificador, en modo objeto, Cnt-A lo aplica

Para recortar visualmente, en modo objeto, Alt b para hacer un corte visual y cnt-alt-b par adeshacerlo

* Cabello largo con mechones: 
  * Añadir curva tipo path
  * Escalar , pero **en modo edicion** para evitar problemas, de 4 metos
  * Rotar para orientarlo en z (el primer mechon para trabajarlo bien)
  * Curva tipo path porque es mas facil de manipular y tenemos que manipular muchos
  * Añadimos una curba tipo circulo para la sección (no mesh/Circle)
  * Escalamos tambien en modo edicion pero la dejamos en el plano xy podemos rotar en modo objeto pero en modo edicion tiene que seguir en xy locales. puede ir bien rotarlo en objeto para editar a la vez el perfil y la longitudinal.
  * En la primera curva  ponemos la segunda como seccion: Geometry/Bebel/Object
  * Ajustamos la segunda para ajustar el perfil del mechon
  * Controlamos el grosor del mechon con el radio de los nodos del path longitudinal con Alt-S
  * A partir de ahi deformamos el mechon y copiamos y pegamos
  * Consejo: mechones gruesos de bulto para la forma basta y mechones mas finos de detalle
  * Consejo: combinar diferentes secciones
  * Consejo: Mechones que ya tengan el aspecto de varios para simplificar
  * Cnt-T Twist (giro del perfil respecto a la curva

# Materiales procedurales

Extension: NodeWrangler para manejar mejor los grafos

* Cn-Sh-click sobre un nodo envia el nodo a la salida de color. Se usa para debugar nodos intermedios.
* Para añadir una textura, seleccionar el PrincipleBDF y Cnt-T. Crea una textura el mapeo afin y la inyección de coordenadas.
* Cnt-Arrastra RB para cortar conexiones

Texture Coordinate:

* UV: Coordenadas de textura editables
* Generated:  Ajusta la imagen a las dimensiones del objeto
* Object: Se mapea la textura a coordenadas de objeto, un metro de espacio de objeto a partir del punto de origen del objeto. (Ojo si aplicamos transformaciones, cambiaran)
* ...

No tener nada conectado a un vector equivale a Generated

Con el nodewrangler si cortamos un cable con shift y arrastrar creamos un nodo vacio para hacer connexiones

* Mapping: Transformaciones afines
* ColorRamp: degradados de color
* Mix: balancea entre os coloreas A y B segun un Factor (A y B pueden ser texturas o otra fuente de color) 
  * Metodo de composicion: Mix, multiply...
  * Adopta el nombre del metodo pero lo buscamos como Mix
* Math: (Add, multiply,...) Cambia de nombre a la op pero lo buscamos como Math
* SeparateXYZ
* Gabor (mirarlo en casa)
* Gradient Texture: Permite hacer radiales, esferical, conical...
* Texturas procedurales: Voronoi, FractalNoise, Wave, Checker, Gradien  (Spherical, radial, linear)
* TextureImage: 
  * Projection: 
    * Flat: x,y a 0..1 de la imagen y repite en z
    * Cube: escoge el eje que se usa para proyectar dependiendo de la orientacion de la cara
    * Sphere, Tube: Desde esos objetos usando la z como control
  * How to extend beyond 0..1: Repeat, Extend, Repeat...

### Cuero

Objetivo, micro proturberancias reflectivas.
De base un material de color marron poco rugoso (para generar reflexion),
y aplicaremos a la altura ruido voronoi suave.

* BSDF con color marron oscuro(ie #6D2C00FF), rougness a 0.25
* A la normal, Bump con strength 0.075
* Al height del Bump (no a la normal), color ramp 
  * Gradient: Blanco a negro -> Negro a Blanco (invertir puntos)
  * interpolacion Linear -> Ease
* Al Fac del Bump, un Math power, con base 2.5
* A la Base de Exponent, el Distance de Voronoi Texture 
  * Voronoi calcula la distancia a una serie de puntos colocados al azar
  * Feature: Smoothed F1 
    * si f1 es la ditancia al punto generador mas cercano, el smoothed es la suma ponderada a los puntos mas cercanos
  * Scale: 5 -> 250 para que sean pequños
  * Random: 1 -> .8 (No tiene mucho efecto)
* Vector de Voronoi a Object coordinates

### Tejido

* Object Coords -> Magic Texture 
  * Genera un patron reticular cuya R se parece a un tejido cruzado
  * Scale: 100
* Magic.color -> Factor de Ramp 
  * Bajar el blanco para crear una meseta blanca al final
  * Crear un gris y subirlo para que tenga mas grises intermedios
* Ramp.Result -> Mix.Factor 
  * A: Color de base
  * B: Color contratejido
  * TODO: en el ejemplo no seteados
* Mix.Result -> Mix/Overlay.A
* Noise 
  * Generara un poco de variacion en el patron
  * Scale 1 -> 10
  * Detail: 2 -> 5
  * Roughtness: .5 -> 1
* Noise.Color -> Mix/Overlay.B 
  * Factor .25
* Mix/Overlay.Result -> Surface
* Ramp.Result -> Bump.Height 
  * Strength 1.0 -> 0.075
* Ramp.Normal -> Normal

### Madera🚨

Coordenadas Objeto -> estiradas en una dimension -> NoiseTexture scale 0.5 -> Noise Texture scale 5.0 -> Color ramp para contraste -> Color ramp para colores de vetas -> Surface color

Si queremos la parte de anillos de la madera: Wave con distorsion y ajustando Detail

### Metal 🤘

### Baking procedural materials

Crear una imagen de textura a partir de un material procedural. Para optimizar

A partir de las uv de un objeto. Creamos un nodo TextureImage y una imagen nueva.

En Render/Bake, seleccionar

### Rigging

Add Armature: Crea un hueso

(Para humanoides, mas practico usar un addon que te los crea ya)

En el modo edicion editamos los cabos. Con extrude creamos

Control tab para entrar en el modo pose.

En modo Objeto, seleccionamos el skiin  y el bone como activo: Cnt-P  Armature with automatic weights

Pesos: influencia que tiene cada objeto en  cada elemento de la geometria

Modo Weight paint permite ver y editar los pesos, una vez vinculado

Lo hace via vertex groups. el vinculo con el hueso se hace via nombre del grupo, si renombramos lo rompemos.

Desconect bone: sigue estando vinculado pero no

Los huesos fluyen en y, usar doble xx yy zz para rotar en los ejes locales.

Para los dedos rotar en z con individual origins.

Simetria: Poner nombre a los huesos con left o right en el nombre. Seleccionar los que necesitan simetrico y seleccionar simetrize.

Objetos auxiliares, hacemos tambien parent a pero sin pesos y en modo pose.

Vincular a un solo hueso:

* En modo objeto, seleccionar el objeto y la armadura, la ultima como activa
* Entrar en modo pose
* Seleccionar el hueso
* Ctr-P / Bone

#### Animando la ropa

Ropa, hay mas distancia entre el hueso y la ropa que al cuerpo. Eso hace que los pesos automaticos no apliquen la misma intensidad.

Seleccionamos ropa y esqueleto: empty loops. Asigna los grupos pero no asigna peso.

Modificador data transfer.  Como source el cuerpo, marcamos vertex data y dentro, vertex group, Nearest vertex. A veces al cambiar la pose canvia el nearest y genera artefactos. Queremos aplicar el modificador en la rest pose para que se quede fijo.

Aquellas partes que no se mueven solidarias podemos pintarles los pesos para borrarlas.

Para editar los pesos: seleccionamos los huesos y el activo es el skin. Con alt-click cambiamos de hueso.

Se puede seleccionar geometria en modo edicion ir a modo weight y activar mascara (donde?)

alt p ctr p

TODO: Inverse kinematics
TODO: Constraints

### Creando acciones

Las acciones permiten abstraer animaciones a un más alto nivel: correr, disparar, saltar, agacharse, mirar...
Son muy utiles para juegos, normalmente van asociadas a los estados del personaje.
Pero tambien para animación ya que permiten abstraerlas y solo ir al detalle para hacer micro ajustes.
Además existen librerias que ya contienen acciones animadas hechas.

* Selecciona el tab Animation.
* En el panel inferior cambiar Dope Sheet -> Action Editor
* Clica en New y pon un nombre a la accion 
  * "default" sera la pose que se vea cuando cargas el asset en Godot
  * si acaba en "loop" Godot lo interpretara como una animación en bucle
* Clica en el Shield para que la animacion no se borre aunque no este usada
* Desde el panel en modo Pose selecciona todos los huesos (o al menos los relevantes para la pose)
* Presiona 'i' para insertar las modificaciones en el keyframe
* Atajos 
  * Click en los puntos selecciona (todos) los valores del keyframe
  * Sh-chilc añade a la seleccion
  * Wheel -> zoom
  * MB drag -> pan
  * Space play
  * Left-Right move frame
  * Sh-Left rebobina
  * Sh-Rigth ff
  * Cnt-Ini Setea el loop de reproduccion
  * Cnt-Fin Setea el fin del loop de reproduccion
  * G mueve el key frame en el tiempo

https://github.com/dynamic-X-LAB/DynamicPose

## Texture painting

freestylized.com

* Partimos de geometrias simples: 
  * Cubos escalados, aplicar escala y hacer bebel minimo en las aristas.
  * Lo mismo con cilindros
* Mas adelante podriamos aplicar detalles, estilizar, subdividir... ahora mantenerlo simple, muchos detalles los haremos con la textura
* Marcar cortes de la geometria para estirarlo 
  * Seleccionar vertices
  * Marcarlo como seam: U (UV) / Mark seams
  * Queda marcado en rojo (en modo solido)
  * Seleccionamos todo
  * U / Unwrapp / angle based
  * Ojo con las opciones de unwrap: 
    * margin: sensible a la resolucion de la imagen para que haya pixeles de separacion (unidades 1 = ancho/alto)
  * F Cambia tamaño pluma (movemos raton y click para selecccionar
  * Sh-F Camba strength
  * Pipeta Cnt-Sh-X (Si ademas haces click lo añades a la paleta)
  * Crear una textura nueva 
    * Camino node: añadimos un Texture image y asignamos imagen nueva
    * Camino uv editor:

Almacenaje externo de texturas

Consejo: una carpeta con texturas al nivel del archivo blender, indicar los encaminamientos relativos

Encaminamientos relativos permiten relocalizar el proyecto

File/external data / Make path relative

Solo pinta en el objeto activo

Altq para cambiar de pieza mientras estamos en texture-painting

Panel de herramienta en la derecha replicado arriba en el toolbar y en el desplegable tool del panel.

## Extension Univ

* Quadrify: convertir los cuads en rectangulos
* Si la textura es tileable podemos hacer que los uv salgan de la textura.
* Componentes de texturas 
  * Ambient oclusion
  * Displacement map (Hay que activarlo en el render)
  * Normal (GL, y DirectX)
  * Roughness
  * Metalic
  * Albedo/Base Color
* CnSh-T Seleccionamos todos los mapas y los mapea a el principal
* AltS invierte los puertos de entrada (mixer)
* UV / Pack island: reposiciona las pieles en la textura
* Stack: poner objetos similares encima unos de otros para aprovechar la misma textura.

### Texturas complejas

* Com aplicar Ambient occlusion correctamente: https://www.youtube.com/watch?v=AguPCHZuF88

### Técnicas

* Mascaras: usar una textura  como "factor" para mezclar otras dos con un "Mix" 
  * La idea es reaprovechar la textura original para otros objetos
* Proyecciond de plano shrinkwrap envuelve una maya sobre otro objeto aplicando el material 
  * Crear un plano
  * Hacer las subdivisiones (se necesita una malla detallada)
  * Aplicar una textura con alpha
  * Modificador shrinkwrap en el objeto
  * Aplicar offset para que quede por encima
* Vertex painting 
  * Usar colores para marcar la geometria y usarlo para separar materiales

### Plantas (texturas con alpha)

* Son planos con una textura con alphas
* Usar un formato de fichero que soporte alphas (png, webp...)
* Usar un programa de dibujo a parte
* eliminar el fondo o desactivarlo para tenerlo como referencia visual
* en la capa superior, seleccionar la forma de la planta
* crear el canal como alpha..
* Truco, poner un fondo de color un poco mas oscuro que el color base del borde para suavizarlo
* En blender conectar el alpha de la textura a el puerto alpha del bsdf
* Nos tenemos que asegurar que el backface culling esta desactivado
* Truco: dividir el plano y separar (V) las hojas y montar una planta mas 3d deformando y transformando las hojas 
  * Si movemos los nodos se deformara la Para mover los nodos con GG para no modificar las V's
* Truco, repetir el mismo plano a diferentes escalas y rotado

### Vertex painting

Tecnica usada por ejemplo para caracterizar terrenos, se añaden atributos adicionales a los vertices que se usan en los shaders para tomar decisiones, por canal rgb. Lo obtenemos con el modulo Color Attribute. Se pueden pintar los vertices en el modo Vertex Painting de forma similar a como pintabamos el weight.

Grupos: abstraer una serie de nodos como un solo nodo.

custom Attribute, podemos pintar el attributo

Tipo shader, lleva todo los atributos de salida (albedo, metalic heigth...)

Mix shader: Para mezclar

Creando attributos de color:

* Attribute: Data / Color Attributes -> +
* Cambiar el nombre para hacer referencia
* Modo Vertex Paint
* Para ver los colores ir al modo solido y ver Modo: Attribute 
  * Util para debug y para hacer pick de color

### Agrupar nodos

Cnt-J mete en una caja para organizar visualmente pero no encapsula.
Encapsular permite abstraer ocultando un monton de modulos como si fueran uno solo.
Ademas el modulo nuevo estara disponible cuando haces sh-A.

Para crear un grupo:

* Seleccionar lo que queremos meter en un grupo y Cnt-G
* Ponerle un nombre con F2
* Entrar y salir del grupo con la tecla tab. (Analogo a Object-Edit modelando)
* Cnt-Alt-G desagrupa
* Puertos externos 
  * Dentro del grupo hay dos nodos nuevos: Group input y Group output
  * Todas las conexiones con modulos que quedaran, apareceran como puertos de esos modulos.
  * Ambos tienen un puerto vacio para exportar nuevos puertos externos
  * Añadimos nuevos modules arrastrando una connexión al puerto vacio.
  * En propiedades podemos cambiar nombre, tipo, valor por defecto...
  * Desde fuera se ve como un parametro (los inputs)

### Agua estilizada

Muy artificial

* Metalic 1
* rougnes bajo
* textura de ruido en las normales: ruido -> normal map -> normal
* escala

### Escultura

* Shift y control para que sea para dentro y fuera
* grab tiramos de un punto
* elastic grab: igual pero tira de la pieza

### Tronco

Con curvas para construir el tronco

### Particulas para hojas

* Creamos la particula
  * plano aprox medio metro, aplicar escala
  * shading nuevo material para el plano,
    * cargamos la imagen (con ojas superpuestas negras)  control t
    * lo conenctamos en el apha como alpha
    * Le damos un color plano de momento
    * Podriamos poner el color de una textura pintada para hojas de diferentes colores
  * Le damos un poco de forma dandole un poco de curbatura al plano para que no sea tan plano
* Para la copa del arbol
  * cubo esferizado con subdivision surface
  * le cortamos la parte de abajo
  * seleccionamos la copa
  * Aseguramos que la escala aplicada
  * Añadimos Mod Geometry Nodes
  * "dp" distribute points on faces: genera puntos en las caras de la geometria de entrada
    * Controlar la densidad
  * iop instance on points: crea objetos en el punto
  * arrastamos instance, oi (object info)
    * podemos coger con la pipeta la particula
  * Alinear la particula con la normal sobre la que se a
    * conectar la rotacion de points on faces, a  rotation de instance on points
  * Darle rotacion aleatoria
    * Rotation instance entre instance on points y la salid
    * Añadimos un random value  y lo ponemos en rotations
    * Gira pero poco porque esta en radianes
    * seleccionar los max i insertamos tau (2pi)
* Exponer controles
  * Igual que con los grupos de shaders
    * conectar los puertos con el node de entrada para que se vea como control en cada objeto y poder cambiar parametros de forma diferente en las instancias.
    * A la N para abrir podemos editar los nombres y los tipos de los puertos
      * Nombre, tipo, valor por defecto...
      * Util si queremos propagar por ejemplo un float a los tres componentes
* Para transferir las texturas Cn-L Transfer Modifiers
* Colection info, nos pasa todos los objetos que estan en una coleccion
* 

## Assets library

## TODO

* Pintar curva para colgante
* Mandibula

## Cosas a mirarme

* Agrupar modulos shaders para reuso
* Parametrizar modulos shaders
* Definir Acciones
* Como animar la capa al tiempo que el personaje en una acción

## Animando

### Pasos de la animación

* Shoot reference: Partir siempre de un video de referencia, si cal, de nosotros mismos.
* Golden poses: Poses que hacen la historia entendible, las que cuentan la historia, las saldrian en viñetas de un comic para entender lo que pasa. Dedicar tiempo a que estas poses esten bien. 
  * Anticipation: aquellos movimientos que se hacen para acumular energia. Se suelen incluir como golden poses.
* Blocking: Sin que el ordenador interpole añadir nuevos keyframes intermedios para que el movimiento parezca completo 
  * Leading: aquellas partes inician el movimiento o se mueven primero: la mirada o un cambio de contrapeso 
    * Los introduciremos en las intermedias mas cercanas a la pose origen
  * Dragging: aquellas partes que siguen el movimiento con retraso, arrastradas 
    * Los introduciremos en las intermecias mas cercana a la pose final
  * Overshoot: aquellas partes que se pasan de tirada 
    * Las añadiremos pasada la pose final, para que no quede frenada de golpe
* Splining: Generar la interpolacion con el ordenador. Esta interpolacion no suele ser buena de entrada.
* Smoothing: Improve the computer interpolation to feel more natural. Usually change timing and interpolation functions, adding follow ups, anticipations...
* Adding life: Usually exagerating some movements, or adding expressions, errors...

### Anticipation

El personaje o objeto acomula energia antes de la acción se ejecute.
Normalmente con un movimiento opuesto al deseado para generar una reacción.

* Doblar las piernas o atrasar los brazos antes de un salto

### Follow through and overlap

Inercia de las partes no rigidas del objeto:

* Cuando la acción principal empieza se resisten a moverse
* Cuando la accion principal acaba siguen moviendose

Se puede exagerar para emfatizar el movimiento.

## References

Hay que usarlas: Obtenerlas, estudiarlas y aplicarlas.
De memoria nos perdemos sutilezas que hacen la animación mucho mas creible.

### Not Early Splining

Keep adding keyframes until the action

### Ejercicios standard de Animacion

* Ball bounce in place
* Ball bounce across the screen
* Ball falling off of the shelf
* Pendulum
* Hand slaping a table
* Animating objects made of different materials and weights
* Character weight shift
* Walk cycle
* Run cycle
* Head turn

Timing
Spacing
Squash and stretch
Overshot

### Non robotic movement

* Using arcs for movements, not linear
* Cada parte del cuerpo entra en movimiento en diferentes momentos, primero cargamos peso con el hombro y la cintura y despues movemos la pierna
* Movimientos no simetricos: Normalmente un lado lidera y el otro sigue en tiempo y posicion, al saltar, al caer, al equilibrar...

## Tutorials

* Generative Stylized Grass 
  * Taiwan Sunflower: Hair + Geometry nodes + Plane + Wind 
    * Part 1: https://www.youtube.com/watch?v=F7_btP0Vhzo
    * Part 2: https://www.youtube.com/watch?v=Uh-kkZBQEO0
  * Retro Shaper: Geometry nodes + Vector groups 
    * https://www.youtube.com/watch?v=Im1qPlaYBaw
  * Simon 3D: Grass reacting to objects. using hair, vector groups, dynamic paint modifier on weight 
    * https://www.youtube.com/watch?v=YTu1ntau43I
  * Trungduyng (demo incluida) vertex color, object scattering/geometry nodes 
    * https://www.youtube.com/watch?v=M4kMri55rdE
    * Tutorial and files: https://trungduyng.gumroad.com/l/animegrassblender
  * baeac: geometry nodes, wind, clear and bend grass arround objects, color control 
    * https://www.youtube.com/watch?v=MZskE3qd3g8
  * TooEazyCG: billboarding grass (rotation follows camera) 
    * https://www.youtube.com/watch?v=hx8m9w4YyNo
* Realistic Grass 
  * MorganVincent: Realistic Grass 
    * https://www.youtube.com/watch?v=BEW3NguW3Nw
  * Ryan King: Realistic Grass 
    * Part1: https://www.youtube.com/watch?v=bG1GsK_g7oc
    * Part2: https://www.youtube.com/watch?v=WBhchj-WoQg
* Generative Stylized trees 
  * Trungduyng: Copa de arboles estilizada 
    * https://www.youtube.com/watch?v=52sTppv7Y-E
  * LilPuf: 
    * https://www.youtube.com/watch?v=byUj5cdx5wE
* Stylized water 
  * crzyzhaa: Water Cascade 
    * https://www.youtube.com/watch?v=25kwDu3OPmM
* Stylized sky 
  * Kristof Dedene: Anime style clouds and starry nightsky 
    * https://www.youtube.com/watch?v=m4aOZm6auxQ
* Geometry nodes
  * Joey Carlino
    * Getting started: https://www.youtube.com/watch?v=szTYXk0t09A
    * Instances: https://www.youtube.com/watch?v=JvbppmT0ILY
   
## Geometry nodes



   
