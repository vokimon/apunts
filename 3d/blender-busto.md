# Esculpido de personajes

## Estrategias de modelado multiresolucion

Las mallas se deforman a medida que vamos modelando y quedan estiradas o sobrepuestas.

### Remesh

* Ir recalculando la malla Cn-R
* Menu arriba derecha "Remesh" (resolucion de voxel...)
* Podemos fijar el tamaño del voxel de.
* A mano 
  * crear una cavidad en el irs
  * poner una esfera con el material transmisivo para la cornea

## Retopologia

Estrategia: Simplificar la geometria,  para pasar de M a K pero haciendo baking de las normales permiten recuperar los detalles.

Definir la estructura de la topologia simplificada:

* Dentro de sculpting, Herramienta pincel verde (vetex painting) 
  * Pintamos de un color cada loop que queramos forzar
  * Se fuerzan loops para facilitar la animacion
  * Para recuperar colores Sh-X (la pipeta normal coge el color render, con este coges el original)
  * X intercambia colores fondo y plano
  * Cn usa el color de fondo
* Partes o loops principales (tipico para animacion de la cara: 
  * cavidad ocular
  * parpado
  * Mascara rodeando los dos ojos juntos
  * Tabique de la nariz entre los ojos
  * Labios
  * Alrededor de boca
  * Nariz y boca (hocico)
  * Contorno de la cara
  * Loop entorno a la oreja
  * Cuello. base del cuello...
* Creamos un plano y lo colapsamos en un solo vertice 
  * Edicion de vertice, X, Collapse edges and faces
  * Snap a face o face project, o face nearest
  * Movemos el vertice del plano a un punto del loop que queremos añadir
  * Cn-Click derecho para ir añadiendo puntos
  * Asegurarse de que en la convergencia de tres o mas zonas hay un vertice
  * Tambien intentar que coincidan con los angulos de la cara
  * cerramos seleccionando los dos y F
  * Teniendo el primer quad, F repetida lo va haciendo sin seleccionar
  * Subdividir en varios loops
  * Aplicar Shrinkwrap modifier para adaptar el plano a la geo original
  * Procedemos con el siguiente loop
  * Aplicar Mirror con la opcion para que fusione los dos costado
  * Si no queremos low poly: Aplicar un subdivision con un nivel y un segundo shrinkwrap para que el suavizado del subdivision se adapte otra vez a la malla original
  * 

## UV unwrap

Seams:

* Cara
* Fosas y interior de boca, ojos
* Cuello
* Craneo partido en dos o no

### Backing relieve en jarron

* Extruir la forma en low poly
* Bevel en las aristas para suavizar
* Subdivision y aplicar
* En overlays activar estadisticas
* Sculpt y remesh a 0.005m
* En el mirror esta la opcion de simetria radial
* Dibujar el relieve
* En el low poly marcar los seams
* Copiar el low poly, moverlo a la posicion del que tiene el relieve
* Modifier shrinkwrap en el low poly 
  * Above surface
  * offset .02 (asegurarse que queda por fuera)
  * Si hay alguna superficie que quede, se puede adaptar el low poly
* Creamos un material para el low poly
* Hacemos una textura y la desconectamos
* Ponemos nombre al fichero de textura
* Activar el automatically pack external resources (menu file)
* En el panel del image editor, Image/Pack para que ya quede gravada
* Render, cambiar engine a cycles
* Seleccionar los dos, que quede el lowpoly activo
* Cuando hacemos el baking no puede estar conectada la textura! 
  * Si no da un error de dependencia circular
* Render / Bake 
  * Bake Type: Normal
  * Extrusion: permite añadir un offset si la esculpida, queda por fuera (sale amarillo en el mapa
* Seleccionar el nodo textura para que guarde ahi el baking y darle al bake
* Copiamos el low poly para ver el resultado y dejamos para rehacer el baking si fuera necesario
* En la copia, Conectamos con un normalMap a normal

## Lo mismo con multires

* Creamos el low poly
* Modificador multires
* 3 nivels o mas con Cn-3
* Esculpimos igual
* Cuando acabamos ponemos el viewport level a cero (servira de referencia, dejaremos de ver el bump)
* El bake igual pero 
  * No hace falta usar un segundo objeto
  * activando "Render/Bake/Bake from multires"

## Hair-cards

Parecido al sistemas de curbas pero con una textura con alpha.

Sets de hair card, hebras de pelo pintadas

* Alpha, ambien oclusion marcando los inferiories, normal
* Height para el bump
* root: degradado de principio a fin que se puede usar para efectos
* id: sirve para pintar de colores distintos

Uso:

* Add curve path
* Escalar en modo edicion, no objeto
* crear un path corto Convexo
* Seleccionar path largo
* Object/geometry Bevel Ojbect y seleccionamos la curva corta
* Cargar el material con las texturas del hair-card 
  * Cargar a mano las que no coja
  * Conectar las manuales a las coordenadas de textura
  * Poner los que no son colores como Non-Color
* En una textura hay varios mechones 
  * Para adaptar la textura del mechon que nos interesa
  * de todas a la vez hacerlo con el Mapping
  * Rotar en z 90,
  * Escalar y mover para ajustar al mechon
* Ambient oclusion A Color B -> mix multiply
* Podemos mezclarlo modo screen con un color base para cambiar el tono del pelo
* Alpha mix multiply con Root (Alpha en A, Root en B) 
  * Si el root es un degradado total, igual queremos meterle una rampa antes para que solo sea en la raiz

### Hair

* Duplicar la superficie que ira cubierta de pelo
* Con el casquete seleccionado, add /curve/ empty hair
* Modo sclupt 
  * Colocamos piezas guia
  * Primer pincel: Groomingy las peinamos
  * generalmente moduficamos todo
  * podemos seleccionar concretas con la herramienta de seleccion
  * herramienta de grow y shirnk para hacer crecer o reducir el pelo
* Cuando tenemos las guias puestas añadimos densidad 
  * En la bilblioteca de interpolador de hair curves (miles)
  * Es un modificador
  * Si el ordenador rasca, puedes reducir el factor "view amount"
* Hair cut profile: 
  * Permite cambiar el pico del pelo
* Habra que aplicar un materia.l, principle Hair BSD, que esta adaptado a ello
* Opciones para cabello rizado

http://www.makehumancommunity.org/content/user_contributed_assets.html

Hair  Tools

Si no tienes el low poly del cuero cabelludo esfera que cubra, Snap face nearest, automatico, G,z,return

Seleccionamos el cuero, F3, add empty hair

Seleccionamos el empty que se ha creado como hijo

Herramientas en sculpt mode

* Comb: peina
* Grow/Shink:
* Pinch para gomas
* Puff: para crepar
* Pull tips para  estirar de las puntas
* Slide: mueve la raiz del mechon
* 

En el modo edicion podemos editar los nodos

Para controlar donde crecen y la densidad crear un weigth paint para cada zona

Density mask de Interpolate

Hay que escribir el nombre del grupo

Modifiers:

* Curl: rizar
* Clump, Agrupar en mechones. Por  distancia, por hebra guia....

## Materiales

Anisotropia 0.8

## Rigify

Instalar Rigify

* Add Armature /Rigify / Human
* En Data / viewport Display / In Front
* Escalamos y aplicamos
* En modo edicion ajustamos las piezas 
  * En este caso borramos los rigings de la cara incluido uno que esta dentro de la armadura de la cabeza que hay que hacer AltX para verlo
  * Marcamos simetria X
  * Pivot point active element
  * A veces va bien snap volumen, va al centro de la forma
  * Se rota normalmente en X, las articulaciones van hacia Y.
  * Para cambiar la rotacion AltS para hacer rol (tambien en el panel de numbers)
  * Enderezar huesos: 
    * Seleccionar con l todo el dedo/brazo
    * escalar en no-Y (xz) a 0
  * Truco: alt-B nos permite hace recuadro y trabajar con parte del model, altB para restaurarlo
  * H hide Alt H unhide
  * Si separamos dos nodos, volvemos a juntarlos seleccionando los dos y s0
* Una vez ajustado añadimos el rig 
  * Seleccionamos el metarig
  * Datos de el metarig
  * Rigify / Generate Rig
  * Generara un hijo del cuerpo llamado rig
  * podemos ocultar el metarig, que solo usaremos en caso de tener que hacer ajustes
* Definamos las zonas de influencias 
  * Seleccionamos primero el cuerpo y despues el rig
  * Cn-P -> Armature Deform with Automatic Weights
* Seleccionamos el rig
* Entramos en pose mode 
  * Para el pie la base roja para posicionar y otra en el talon que permite move
  * Las flechas del femur rotan la rodilla
  * Dedos escalar para encoger, para cerrar el puño rotar en x local (xx)
* Para recuperar Pose/clear Transform
* Refinado: 
  * Volver al metarig, editar
  * Regenerar rig
  * Regenerar los pesos
* Para los elementos adjuntos 
  * Ojos, set parent to bone,