# Comic look en blender

## Sombreado

### Difuse

* Emision shader al final para que el color que salga sea el que le damos
* Difuse Shader da la info de shading Si el color es blanco da la iluminacion.
* shader to RGB extrae el color del shader
* Podemos hacer un ramp de ese gris

### Metal

* Glossy BFSF para capturar el reflejo
* Ramping para hacer una mascara del reflejo
* Superpuesto a un difuse

Layer weigth: Da factores que dicen como de tangencial es TODO: ver que es cada salida

* Facing: orientacion a la camara: se puede usar para hacer brillos de banda, poniendo un ramp detras que escoja unos angulos.

Reflection coords

### Cristal

## Line Art

### Método con Solidify

* Duplicar el objeto
* Escalar el duplicado
* Invertir las normales (Sh-N)
* Activar el face culling (TODO: donde)
* Ponerle un material emisivo con el color

Esto mismo se puede hacer con solidify envez de duplicando y escalando.

* Añadimos un material extra al objeto 
  * emisivo, eligimos un color
  * Material/Settings/Backface Culling 
    * Activar para Shadow y Camera
* Añadimos Modifier de Solidify 
  * Activar Normals/Flip
  * Materials
  * Ajustar thickness y offset (Ojo signos negativos, Ambos deben ser iguales y con los negativos pasan cosas)

Problemas:

* Solo contorno, no aristas
* Escala con el objeto
* A veces se cruzan

### Curbas

Para añadir aristas a los contornos

* Sh-D para duplicar
* P para independizarlo
* X Borrar solo las caras  Only faces, dejando el wireframe
* Convert edge to Curve (Modo objeto, menu contexto, Convert To/Curve)
* Le damos un grosor 
  * Geometry/Bevel: depth
* Le aplicamos el material de linea anterior
* Siendo curvas podemos controlar el grosor o partirlo
* Tambien dentro de la curba podemos pintar mas lineas adicionales

Problema:

* No funciona para cosas redondas

Otras tecnicas:

* Pintar las aristas con texture painting

### Grease Pencil

* Add Grease pencil/Empty
* Cambiar el modo a Draft Mode
* Cambiar el stroke placement a Surface (en medio de la barra superior del draw mode)
* Podemos escoger diversos pinceles, se convierte en puntos que podemos editar en Edit mode
* Ojo, si pintamos fuera, el trazo se va al fondo
* Se puede configurar relleno pero no se adapta a la superficie aunque estemos en modo surface
* Hay capas, en los datos y arriba en la barra
* Modo sculpt: 
  * Tint, cambia el vertex color que se superpone al material, para quitarlo pintarlo con cntl
  * Cambiar el grosor, smooth, dar grosor, opacidad, deformar hacer pinching...

Calculo automatico de grease pencil

* Modificador lineart: genera el lineart 
  * para la camara que asocias, y solo para esa
  * Si lo aplicas lo transforma en grease pencil
* En el menu de añadir, hay opciones para crear grease pencils para objetos, escena.... 
  * Genera un grease pencil con modificador que referencia al objeto 
    * Es bastante lento
    * Funcional para renderizar offline animaciones
    * No es valido para videojuejos
  * Opciones para decidir que marcar: contornos, vertices, angulos, sombras...
* Stroke placement 
  * Stroke: Une con los trazos existentes (no funcionaba en 4.3)
  * Surface: proyecta en la superficie visible (ojo si te sales)
  * Cursor: Plano perpendicular  a la vista que pasa por el cursor
  * Origin: lo mismo con origin

### Lineart modifier

* Es un modificador de un greasepencil que referencia aun objeto y por defecto, genera con
* Se añade como objeto cuando tienes seleccionada una mesh 
  * Con la mesh seleccionada, añadir  objeto GreasePencil/ObjectLineArt
  * Se genera segun la camara actual 
    * Para que se genere independientemente de la camara antes en el objeto 
      * Check Object/Viewport Display/InFront
    * En el modifier de LineArt Occlusion Range poner de 0 a infinito
* Podemos escojer que lineas salen
* Una de las opciones es "marked edges" 
  * Object: Sharp edges, controlando el angulo del tool
* 

### Geometria para los bordes

* Seleccionar la geometria que queremos 
  * Select non-manifold: Para selecccionar los segmentos que que son bordes (no forman volumen
* Hacer un duplicado de los segmentos
* Convertir a GreasePencil/Curve
* Añadir el artline modifier
* Seleccionar solo loose
* Una vez que ya hemos aplicado el modificador, Deseleccionar Object /Viewport display/Infront
* Modificadores adicionales (a aplicar al grease pencil) 
  * Simplify
  * Noise: emula la linea irregular (desvio, grosor...) 
    * Randomize: para las animaciones emula trazo manual (cada steps)
* Trazos discontinuos 
  * "Seleccionar random" unos pocos y borrarlos emula linea entre cortada
  * Despues a mano podemos usar el Alt-S con proporcional, con select first/last para hacerlo mas finos cuando desaparecen los puntos
* Para añadir ruido al solidify, añadirle despues un Transform Displace muy leve. Si no hay geometria suficiente, antes poner un subdivision sin suavizado ("simple").
* Si ponemos un lattice al objeto, ponerle el mismo lattice a las lineas a parte.
* Modificador de Thickness es un modificador para cambiar el grosor proporcionalmente
* Skulpt Mode de GP: 
  * Tools 
    * Noise
    * Smooth
    * Strength (opacidad, con control trasparencia)
    * Thickness (con control afina)
    * Grab, Pînch, Pull, Twist

### Troubleshoting

* En render no se ocultan los trazos de detrás. 
  * ViewLayers / Passes / Data -> Activar "Z"