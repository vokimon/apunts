# Blender: Temple

## Blocking

### Caja contenedora

## Ajuste de camara

Queremos un contrapicado para que se vea majestuoso en la escena:

* Focal lens 14m es lo normal 21mm da mas perspectiva de contrapicado para grandes estructuras
* Tambien hay que ajustar en la camara el "clip end" para que quepa toda la escena
* Passepartout a negro tope para bloquear lo que no se ve de la escena

### Vista Referencia

Para mantener la refenencia de la camara, aunque nos movamos para modelar, es bueno mantener una vista de camara en pequeño

* Clickar en tab del layout y duplicar
* 

Despues

### Escaleras

* Con un cubo rotado ya valdria para el blocking
* Para hacer la rampa bevel con un solo nivel y hace una rampa
* Podemos añadir los escalones ajustando el profile del bevel: 
  * Profile/Custom/Escalator
  * TODO: Jugar con las opciones para ajustar el numero y la proporcion de los escalones
  * Type: Offset es 45º pero despues podemos escalar para cambiar pendiente
  * Type offset percent, permite dibujar darle el aspecto a las escaleras y que sea la
  * Numero de segmentos. Cuando lo cambias no se aplica. Darle al

### Recursos

* \[EMC3d - Game Art\]([EMC3D - Game Art - YouTube](https://www.youtube.com/@EMC3D)) 
  * Trim sheets
* Assets y texturas 
  * Polyhaven
  * Fab
  * Ambient CG
  * gscatter.com (vegetacion realista)
  * quixel
  * kitbash23.com  (da problemas con el displacement) Hay arquitectonicos
  * blenderkit 
    * Tiene un addon para browsear desde blender, pero hay que registrarse para bajarselos.
  * Artstation
  * Fxelements

### Detalle esculpido en suelo y paredes de la roca

* Apliccar subdivide varias veces (Cn R)
* Sculpt con herramienta blob 
  * Click añade volumen
  * Cnt Lo quita
  * Shift suaviza

File/External Data /Automatically Pack Resources  Para que las texturas esten dentro del blend

Truco: Cnt-Shift y arastrastrar con el boton derecho un nodo a otro ya conectado, y hace la mezcla

Para el displacement Material/Surface/Displacement/Displacement and bump

Para las rocas cambiar el metodo de proyeccion flat->Box en los nodos.  A veces hay que jugar con el blending para que no se noten las esquinas el salto de la textura.

Truco: para cambiar el mismo valor en todos los nodos seleccionados Alt cuando lo aplicas

### Agua

* Version Cycles 
  * Partimos de cubo para usar su volumen 
    * Crear una base con textura y objetos que crucen a profundidad para ver el efecto
  * Principled volume 
    * Density determina como se difumina con la profundidad .25 - .5
    * Color:
    * 
  * Para la superficie mezclaremos los shaders 
    * Glass Shader Para los brillos 
      * IOR 1.33 de agua
      * Rougntes y color por defecto pero podemos cambiar el color para darle un matiz
    * Transparent (no translucent) para que deje pasar al volumen
    * Para el factor del miser al IsShadorRight
    * Noise en texturas de objeto conectado
* Version EEVEE 
  * En vez de usar el shadow ray mezclar con un factor que pone el glass por encima
  * En el  nodo material Output cambiar All -> Eevee o Cycles

### Ruinas

installar cellFracture

* Seleccionar objeto a partir
* Object/Quick Effects/Cell Fracture
* Ajustar el numero de piezas
* Separamos las piezas de la original que se conserva (consejo: moverlas piezas en una coleccion para tenerlas controlados
* Añadir un plano 
  * Object/Rigid body/Passive
* A los trozos Rigid body en active
* Play
* Cuando acabe nos ponemos en el punto del timeline y aplicamos: Object/Rigid bocy/Apply
* Para quitar:  Object/Rigid Body/Remove
* Esto genera un efecto fisicas al que podemos acceder desde panel derecho tab physics 
  * Podemos usar un colisionador activar  "Animate"
* Material de fractura

### Distribute assets

* Con GN: 
  * Para el objeto a distribuir
  * Object info y tomamos el objeto sobre el que distribuir 
    * Cualquier cosa que hagamos en el original se aplicara en el
  * Distribute point on faces 
    * Poison Distance mantiene la distancia dentro del random, con el random a pelo
  * Instances on points
  * Object Info con el objeto a distribuir y lo conectamos al instance de instance on points
  * Random Scale and Rotation
  * Para controlar donde distribuir con weigth painting 
    * Hay que aplicar los subdivisions para tener suficiente geometria
    * Cambiamos el nombre del vertex group en data
    * en el geometry node creamos un input que conectamos en el density
* Con el plugin 
  * Tenemos varios sistemas de distribucion
  * A cada uno le aplicamos efectos: Weigth map, distance...

### Romper el tiling

* Poner color de voronoi en el location de las coords
* Combinar texturas con texture painting
* Insertar decalls, elementos que hacen variable 
  * Planos con texturas con transparencia que aportan variabilidad
  * En estos es importante el componente Opacity
  * En Object/Visibility/Shadow -> No
  * Podemos modificar hsv o saturation para hacer que el color corresponda
  * Considerar el modificador de shrink-wrap para adaptar el decall al target

### Fuego

* physics/Fluid/Fire
* Texturas animadas 
  * Se importa igual que las multitexturas
  * Ciclic / autorefresh / frames
  * Si no viene con alpha, mix shader con un transparent
  * En Materials Settings / Render Method  Dither -> Blended
  * Para que mire siempre a la camara: 
    * Constraints Track to, escogemos la camara y los ejes
    * Añadimos un driver (controlar un parametro con otro parametro) 
      * Cn-D en el parametro