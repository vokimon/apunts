Para renderizar animaciones Cn-F12 (F12 era para imagenes fijas)

Para cambiar de camara activa en el icono del 

No queremos que tenga ninguna modificacion aplicada, sino seran relativo

Las camaras miran a la z local y dejan arriba la y local.

Antes de hacer estas mierdas alt-

Crear un empty

Hacer hija la camara del empty

Podemos mover la camara haciendo

* Expresion en funcion de 'frame'
* Podemos usar funciones trigonometricas y demas

### Traveling usando curvas

* Creamos la curva y la camara
* En la camara en constraints añadimos un "folow path", seleccionamos la curva


* Usando asdw como en un juejo
* Usando curvas
* Constrain Tract-To observa el objeto que designemos. Si es un empty lo podemos animar independientemente de los objetos
* Para controlar el tiempo que tarda en recorrer la curba: en los datos de la curva Data/ Path Animation / Frames

Key frames

* posiciono en el la posicion inicial
* en el n location boton derecho y create keyframe
* la posicion animada aparecera en amarillo
* nomoves el tiempo al segundo punto
* movemos el objeto los parametros keyframe cambiados aparecen en naranja

### Traveling manual (modo FPS)

* Crear una camara
* Entrar en la vista de camara y bloquearla
* Sh-Ñ entra en modo navegacion FPS
* Con el raton orientamos, asdw  mueve alante atras straffe
* qe arriba y abajo, shift para acelerar
* Podemso configurar en propiedades  projecto Navigation, podemos cambiar velocidad
* Controles extra debajo en la barra de estado

Para grabar

* Seleccionamos camara
* Activamos el autokey en la barra del 
* play con la barra
* sh-Ñ para entrar en modo walk
* movemos 
* click para salir del modo walk
* barra para parar la grabacion
* salimos del autokey

Conviene limpiar los temblores cogiendo keyframes mas espaciados,, seleccionamos los que queremos, cn-I  para invertir seleccion y X.

Si alguno no nos gusta lo editamos

Podemos ajustar la escala para acelerar o decelerar el movimiento

### Parametros de grabación

* Render Cycles / Volume / Steps: Planos de niebla
* Render EEVEE / Raytracing / Screen Tracing / Thickness 0.2 -> 1.0
* Importante Edicion Preferencias System y configurar la api de aceleracion
* Render Cycles /Light Paths  considerar subir valores para segun que tipos de materiales
* Ouput
  * Resolucion
  * Formato
  * Frame rate
  * Frame range (tambien se cambia en el timeline)
* Environment
  * Mist Path, start stop