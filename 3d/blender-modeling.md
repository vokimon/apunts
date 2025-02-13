# Modelado con Blender

Abreviaciones

- Sh (Mayusculas)
- Cn (Control)
- Alt (Alt)
- RB/MB/LB Right/Middle/Left Mouse Button


## Navegación

MB -> Orbitar (rotar alrededor del centro de la vista)
    Also numpad arrows
Sh+MB -> Panning (changes the orbit center
Cn+MB -> Zoom
    Also Numpad +-
    Also mouse wheel

Numpad 5 -> Togle Isometric - Perspective
Numpad 7-1-3: View from axis X Y Z
Numpad 9: View from the other side (z up unless actually z)
Numpad .: Adapt view to selected objects
Numpad 0: Camera view
Home: View all

Para mayor control se aconseja manipular los objetos en vistas
ortogonales aliniadas a cada eje.

## Selection

T: para ver el panel de herramientas
Por defecto esta en la herramienta de seleccion modo cuadro.

W cicla modo seleccion:

- Click o cuadro (Recomendado por defecto)
- Circulo (con radio configurable)
- Selector por lazo
- Seleccion y mueve (en segun que contextos mas rapido, pero error prone)

Modificadores de seleccion:

- Por defecto, substituye la seleccion anterior
- Control: Toggle selection keeps previous
- Shift: 

Seleccion vs Activo

El activo es el ultimo seleccionado, outline amarillo,
a diferencia de los otros seleccionados que aparecen en naranja.

Al lado del icono de seleccion aparece el activo
Vemos la ultima seleccion al lado del icono y en la lista de objetos.

Lista de objetos

El nombre sale en el color del outline. Fondo azul.

## Adding object

Sh+A -> add an object

Cursor: Es un punto de referencia que se usa para varias cosas.
De entrada como punto de inserción de los nuevos objetos.
Por defecto esta en el origen.



## Transformaciones 

- **G**rab
- **R**otate
- **S**cale

Se entra en modo transformación,
se acaba aceptandola on return o LB o abortandola con ESC o RB.
Entre medias podemos hacer diferentes cosas.

- Mover el raton para controlar la transformación
- por defecto se limita al plano perpendicular de la vista
- Pulsar x y o z para limitar la transforamción a ese eje
- Pulsar X Y o Z para limitar la transformacion al plano perpendicular al eje
- Si repetimos xyzXYZ se referiran a las coordenadas locales en vez de las globales
- Indicar numericamente el valor de la transformación
    - Numero de grados
- Arrastrando con MB, limita al eje mas cercano
- Arrastrando con Sh-MB, limita al plano mas cercano
- Sh en modo precision
- Cn invierte el modo snap (si esta habilitado, lo deshabilita y alreves)
- Si pulsamos B podemos escoger el elemento de snap.

En la parte superior hay un toolbar con modificadores de las transformaciones.

- Ejes de referencia: Global, local, normales...
- Pivote para la transformacion: Centro del objeto, origen, cursor, el elemento activo
    - El elemento activo es interesante para una selección múltiple que se transforme de forma solidaria, si no cada uno rotara sobre si mismo
- Modo snap. Que puede estar activo o no por defecto
    - Recomendado desactivarlo y activarlo con Cn cuando se requiera.
    - Desplegable para escoger que se usa como snap (vertice, arista, plano, 

- Sh D: duplicar, a continuacion podemos aplicar transformaciones (por defecto empieza en Grab)
- Sh R: repetir operacion (por ejemplo si duplicamos con transformacion, volvera a transforma para hacer arrays y demas)
- Cn J: Join, junta punts seleccionats amb un vertex

## Visualización

en la esquina superior derecha esta el toolbar de visualizacion

- Que tipo de objetos ver y poder interacturar
- Que gizmos (elementos de control) ver
- Que overlays ver (ejes, rejilla...)
- Como renderizar los objetos (wireframe, sombreado, goroud...)


## Proceso de producción

- Layout: Encuadre de los elementos de la escena
    - Se puede hacer con primitivas simples


# Edit mode

- Tab switches object and edit mode (also Sh-R?)
- Transformations are similar 
- Alt-S - scale along normals













