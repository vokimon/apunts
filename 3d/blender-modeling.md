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
    Also mouse wheeL
Alt+MB drag -> Isometric axis view closer in drag direction
Alt+MB click -> Center pan on click

Numpad 5 -> Toggle Isometric - Perspective
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
- Shift: add or remove (toggle)
- Control: Shortest path ???

Seleccion vs Activo

El activo es el ultimo seleccionado, outline amarillo,
a diferencia de los otros seleccionados que aparecen en naranja.

Al lado del icono de seleccion aparece el activo
Vemos la ultima seleccion al lado del icono y en la lista de objetos.

Lista de objetos

El nombre sale en el color del outline. Fondo azul.

## Object mode

Sh+A -> add an object

Cursor: Es un punto de referencia que se usa para varias cosas.
De entrada como punto de inserción de los nuevos objetos.
Por defecto esta en el origen.

- Sh-RB Set Cursor

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

- Tab o Sh-R intercambia entre object mode y edit mode
- Edit mode es para modificar la geometria que tiene tres niveles de objetos
- 1 vertices 2 segmentos 3 caras (seleccionamos con 1, 2 y 3)
- RB Menu del nivel seleccionado (vertex, edge, face)
    - Tambien Cn-V, Cn-E, C-F)
- l (linked) selecciona toda la geometria enlazada a la selección
- Transformaciones (GSR) se aplican de forma similar.
    - Diferencias?
- Alt-S - scale along normals
- GG - los mueve dentro del objeto superior
    - Si esta activado el automerge, cuando arrastras a otro vertice/arista los fusiona
    - Options Transform en el toolbar arriba a la derecha
    - Explicitamente M (merge) en edit mode
- Escala es juntar o separar, mejor que trasladar uno a uno
- Cn J: Join, junta punts seleccionats amb un vertex
- Alt-click: Select loop
- Alt-Z: See through (tambien para seleccionar ocultos)

Compte: Se propaga en coordenadas de vertice: suele ser bueno aplicar antes transformaciones
    Cn-A en modo objeto aplica transformaciones a los vertices, reseteando las transformaciones de objeto.


## Edicion proporcional

- O (o en el toolbar) - Intercambia modo Transformacion proporcional
    - Las transformaciones afectan fuera de la seleccion a la geometria conectada
    - genera cambios mas orgánicos
    - Podemos definir area de afectación
    - PgUp PgDn o en el toolbar o con wheel

## Subdivide

- Cn-R Subdivide
    - Tienen que ser quads y no tener "cosas raras"
    - Primero indicamos el eje, aproximando al segmento que queremos partir
        - AvPag/RePag: numero de segmentos
        - (LB/return para confirmar, RB/ESC para cancelar)
    - Despues entramos en el modo de transformacion de las divisiones por defecto una translación siguiendo el eje cortado
        - Podemos aplicar R y S
        - ESC/RB para dejarlo por defecto
    - Click para confirmar, si hacemos RB, dividira en el centro
    - Aun asi despues podemos controlar desde el panel de tool options los parametros

## Cut

- Last resource when subdivide is not the option
    - Mas control, pero menos regular, puede derivar en mayas menos manipulables
- K - Cut
    - C cut through, la linia atraviesa el otro lado (recomendado)
    - Arrastrar: Freehand
    - click: pivot para cortar con linia
    - click on point: set the point as pivot
    - Sh middle point cut
    - Cn ignore snap
    - RB-ESC undo last step
    - Podemos hacer panning con las combinaciones de (Cn-Sh-Alt)MB

## Extrusion

Alt-E: Menu extrusió

- E Extrude Face/Vertex/Edge
    - 
- Extrude along normals no same direction as E does
- Extrude individually, break connections
- Extrude manifold, fusiona y divide con lo que genera
- Extrude repeat, crece en segmentos, podemos añadir un step


## Inset

I - Crea nodes en l'area interior

## Bevel

Dos tipos diferentes de bevel

- CnSh-B Vertex Bevel
- Cn-B Segment Bevel
- Aun podemos pasar de uno a otro con V

Mecanica

- Cuando empieza controlamos la extension con la distancia al centro de la pantalla
    - A area (default)
    - P profile, concavidad/convexidad
    - S segments, subdivisiones
- Con la rueda o PgUp/PgDn controlamos el numero de segmentos
- Al confirmar con RB o Return podemos aun alterar los parametros en el panel de operacion abajo izquierda (puede estar colapsado)

Truco: De vertice a redonda. Vertex Bevel dependiendo del perfil, genera estrellas, redondas, rombos

Truco: Si aplicamos un Edge Bevel a todo el loop, mantendremos la topologia.
Y al revés si no lo hacemos en todo el loop o si lo hacemos de vertice la rompemos.

## Unir geometrias

- F Fill cavity
- J Join vertex
- (Face Menu) Poke face: crea un vertice en el medio y lo enlaza con los vertices de la face







