# Design principles

https://www.refactoringui.com/


## Empezando de cero

Empieza por la funcionalidad no por la aplicación.

- Una aplicacion es un conjunto de funcionalidades
- Hay una parte del layout común a todas las funcionalidades: Barras, navegacion, dashers, títulos...
- Puede ser prematuro decidir la interfaz común antes de tener diseñadas las funcionalidades
- Incluso, esos elementos comunes pueden no incluirse en alguna o todas las funcionalidades (login, zen mode...)

Empieza sin detalles

- Iconos, shades, typefaces... son detalles que mejoran el diseño pero no claves para empezarlo
- Baja fidelidad: los entornos de diseño computerizados suelen ser de alta fidelidad -> Usa esbozos
- Aguanta el color: Trabajando en gris ayuda a focalizar en usar espaciado, contraste... para establecer la jerarquia de elementos

No invertas demasiado

- Baja fidelidad te permite moverte rapido
- Provar muchas ideas y descartar sin dolor

No sobre-diseñes

- Evita los castillos en el aire: 
En abstracto cuesta tener presente cada interacción o cada caso extremo.
- Alterna diseño y implementación en ciclos
	- Diseña solo la siguiente funcionalidad que se va a añadir al producto
	- Contruye el producto real lo más rápido posible para no carga la imaginación 
- No incluyas en los diseños elementos futuribles, solo los que se puedan hacer ya
	- Nice to have -> Design it later

Dedide una personalidad

- Hay que decidir de inicio que queremos expresar con el diseño.
	- Seriedad, dinamismo, desenfado, lujo, futurismo...
- Así tomamos decisiones conscientes que lo lleven a ese punto.
- Fuente, Color, incluso detalles como el border radius, pueden dar personalidad
- El contenido y el diseño han de acompañarse el tono

Limita las opciones

- El exceso de opciones genera parálisis de diseño
	- Colores, tamaños y grosor de la fuente, tamaño de los iconos, espaciados...
	- Tener opciones limitadas agiliza el proceso.
	- También hace más coherente el conjunto
- Define sistemas (conjuntos de valores validos para un paràmetro) por adelantado
- Tener opciones perceptiblemente diferentes ayuda a descartar
- Sistematiza lo que puedas
	- **Tintas de la paleta:** Usar de 2 a 5 colores principales
		- Asignarles funciones
		- Más facil de intercambiar las funciones
	- **Tonalidades de la paleta:**
		- Para cada tinta, máximo 8 y 10 tonos entre el casi blanco y el casi negro
		- En los cambios 
	- Tamaños de letra
	- Tamaños de iconos: 12px, 16px, 24px, 32px
	- Font size: Saltos perceptibles a simple vista
	- Font weight: 200 es un salto perceptible
	- Line height
	- Margin
	- Padding
	- Width
	- Height
	- Box shadows
	- Border radius
	- Border width
	- Opacity


## Jerarquías

Cuando todo en el interfaz demanda atención, se percive ruidoso.

Cuando intencionadamente se enfatiza de forma desigual los elementos és más fácil entrar al contenido.


Tamaño pero no solo

- Si solo usamos el tamaño de letra tendremos contenido principal muy grande y secundario muy pequeño.
- Tambien se puede usar el grosor, la intensidad del color, el especiado entre letras...

No usar grises en fondos de color

- Reduce el contraste
- Transparencia tampoco se aconseja
- Usar otro color de la misma gama con suficiente contraste

Destaca degradando

- Cuando no tienes espacio para destacar lo importante, considera degradar lo no tan importante

Etiquetas como último recurso

- Inercia presentar la información tabular _label: value_
- Dificulta la jerarquización de la información
- A menudo el formato del valor ya dice que es (telefonos, nombre, precio...)
- Se puede mezclar la etiqueta y el valor: _habitaciones: 3_ vs _3 habitaciones_
- Si las pones, son secundarias, el valor es lo importante
- Tienen importancia cuando los valores son similares (ie tamaños) y tenemos que destacar cual es cual (alto, ancho...)

Jerarquia de documento vs Jerarquia visual

- El markup es jerarquico h1, h2, h3, igual lo importante no es el titulo (contexto)
- No necesariamente hay que destacarlos visualmente en la misma jerarquia

Equilibrar grosor y contraste


- Cuando no es bueno modificar la jerarquia alterando uno se puede compensar con el otro
- Ejemplo: los iconos parecen bold y no se le puede quitar -> reducir con contraste
- Ejemplo: augmentar el contraste a elementos finos (hr) se ven duros -> añadir grosor y reducir contraste

Jerarquizar botones

- Poner el estilado jerarquico (primary, secondary...) delante del semantico (danger, info, warning...)
- Acciones primarias destacadas: solidas, contraste alto
- Acciones secundarias claras no prominentes: lower contrast o outlines
- Acciones terciarias descubribles pero ignorables: Como links
- Acciones destructivas: El estilo rojo llamativo solo cuando son la accion primaria

## Maquetado

Dar más espacio del necesario para que el diseño pueda 'respirar'

- No empezar comprimido, y dar espacio hasta que se vea bien.
- Mejor es dar espacio de sobras y acercar lo que tenga más sentido junto
- Los densos tienen sentido como excepción. Ex. dashboards que tengan que presentar mucha información

Establecer un sistema de espaciado

- Agiliza las decisiones y consigue cierta consistencia
- Pasos no lineales: para tamaños grandes las diferencias pequeñas no son tan distingibles
- Definirlo respecto a un valor de referencia (16px)

No es necesario llenar la página

- Si nos adaptamos al ancho los elementos pueden quedar demasiado dispersos
- Mobil primero: Diseñar interfaces estrechos en canvas estrechos para que las restriciones sean reales, despues expandir y adaptar lo que haga falta
- Si al expandir no se ve equilibrado, doblar en columnas
- No forzarlo: Ni rellenar todo el espacio con cosas, meter todas las cosas

Las grids en columnas estan sobrevaloradas

- Los grids se basan en porcentajes y hay cosas que mejor con tamaño fijo (imagenes, iconos, sidebars...)
- Si hay un tamaño ideal para un elemento, no tiene sentido comprimirlo proporcionalmente, si aun queda espacio.
- Mejor un max-width con el tamaño óptimo y dejar que se comprima en estrechos

Escalado proporcional? no siempre buena idea

- Escalado al dispositivo:
	- En dispositivos pequeños, el contraste entre tamaños de fuente se ve más equilibrado si 
	- En 'sm', respecto 'lg', las letras se ven más equilibradas con menos contraste de tamaño entre niveles
	- Significa que, al reducir el dispositivo, las fuentes grandes se empequeñeceran más rápido que las pequeñas, no proporcionalmente
- Escalado de elementos respecto al escalado (variante) de un componente
	- No siempre un escalado uniforme tiene sentido.

Evitar espaciado ambiguo

- No usar espaciado igual para separar cosas que no tienen la misma distancia conceptual


## Typografia

Usa buenas fuentes

- Opción segura: usa las fuente del sistema: `-apple-system, Segoe UI, Roboto, Noto Sans, Ubuntu, Cantarell, Helvetica Neue`
- Evita fuentes con menos de 5 grosores
- Optimiza Legibilidad para la letra principal: altura de x alta y amplio espaciado entre letras
- Confia en la mayoria / Copia a los que saben / Desarrolla intuicion (Vamos, no clue)

Limita la longitud de las línias

- Entre 45 and 75 carácteres

Alineado vertical

- Cuando se mezclan tamaños de fuentes, para alinearlas verticalmente `baseline`


El espaciado interlineal no es proporcional al tamaño de la fuente

- Importancia: Facilitar la lectura al cambiar de linia
- Recomendado 1.5 de la altura de la fuente
- Sin embargo, en las fuentes grandes. esa proporcion no se ve tan bien, 1 es correcto
- Conviene que sea inversamente proporcional al tamaño de la fuente

Enlaces de colores? no es necesario

- Dentro de un bloque de texto que no es link, resaltar el link es bueno
- Cuando todo el elemento es interactivo, hay que hacerlo mas sutil o en interactivo

Alineado para legibilidad

- No centrar textos largos
- Textos largos alineados a inline-start
- Alinear números a la derecha para alinear dígitos del mismo peso 
- Solo justifica para dar un aspecto formal o de impreso
- Si justificas textos, hipheniza para evitar saltos gordos entre palabras

Espaciado de letras

- 0 que es la distancia de referencia puesta por del autor de la fuente
- Para titulos con letras grandes suele ser mejor reducir el estàdard
- Para los textos en mayúsculas conviene augmentarla


## Color

HSL es mas práctico que RGB

- Los cambios en los componentes HSL son más plasticos

Limitar los tintes, pero usando varios tonos

Grises

- Normalmente son necesarios mas tonos de grises que del resto de colores
- Se usan para la mayoria de los fondos, las sombras y bordes
- El negro absoluto suele quedar bastante poco natural

Color Primario

- Es el que da identidad a la aplicación
- También necesita muchos tonos
- En temas claros, tonos mas claros en el fondos, oscuros para textos y en los oscuros, al reves.

Color de Acentuado

- Ha de ser un color llamativo que no se confunda con los semánticos


Colores semánticos

- Rojo para acciones destructivas
- Amarillo/Naranla para mensajes de advertencia
- Verde para cosas positivas

Definiendo los tonos

- Definir un numero de tonos de antemano
- Escoger el color principal para el tinte
	- Truco: Normalmente escoger un tono que funcione bien como fondo de boton
- Escoger los tonos extremos, claro y oscuro
- Rellenar el resto de niveles de forma que sean distinguibles

Saturación percibida y luminosidad

- El mismo valor de saturación no corresponde con la misma saturación percibida si variamos la luminosidad
- Luminosidades bajas y altas necesitan subir la saturación para que parezca la misma

Brillo percibido y tinte

- Para el mismo valor de brillo:
	- Los tintes cerca del amarillo tienen más brillo percibido
	- Los tintes cerca del azul tienen menos brillo percibido
- Brillo percibido: sqrt( 0.299 r² + 0.587 g² + 0.114 b²) / 255
- Los tintes primarios additivos son minimos locales: `b<r<g`
- Los tintes primarios substractivos son máximos locales: `m<c<y`

Usando el tinte para cambiar el brillo

- Si movemos brillo a los estremos se desatura
- Si lo movemos hacia los tintes cercanos que se perciben mas brillantes o oscuros conseguimos un efecto mas natural
- Limitar el canvio a 20ª o 30ª para mantener el cambio

Usando grises con temperatura

- Los grises neutros tienen saturacion 0, se ven igual independiente del tinte
- Si subimos un poco la saturación (12%) tendremos grises templados o frios segun el hue.


## Depth

Dar relieve emulando una fuente de iluminación

- Si supones que la fuente de luz esta arriba
- Los elementos que sobresalen tiene luz arriba y sombra abajo
- Los elementos que se hunden tienen sombra arriba y luz abajo

Usar el grosor de la sombra para emular elevación sobre el fondo

- Contra más relieve, más destaca
- Sombras ligeras para botones y elementos fijos del interfaz
- Sombras medianas para popups y menus
- Sombras profundas para dialogos 

Un sistema de sombras, tiene las ventajas de los otros sistemas

- Ventajas de los otros sistemas: Coherencia, agilidad de desarrollo...
- Definirlo como colores: extremos aceptables y rellenas en pasos perceptibles

Interacción

- Hundir los botones cuando los clickas
- Levantar los elementos cuando haces drag an drop

Sombras en dos partes

- Una amplia y ligera, considerable vertical offset, mucho radio de difusión
- Otra estrecha y oscura, con menos difusion que simula la sombra que esta debajo
- Cuando se eleva las sombras tambien seran mas sutiles

Diseños 2D con profundidad

- Colores claros sobre fondo claro sobresalen
- Colores oscuros sobre fondo oscuro se hunden

Sombras solidas

- Con sombras sin difuminar o con bordes


Solapamiento

- Sobreponer encima de una transicion entre dos fondos
- Sacar el hijo fuera del padre tambien da profundidad
- Si los elementos se confunden, por ejemplo porque son imagenes añadir un borde sutil


## Images


Usa fotos de calidad

- Pueden arruinar un buen diseño
- Fotografo profesional
- Buenas imagenes de stock

Contraste de las imagenes de fondo

- Problema: diversos colores sin un contraste uniforme
- Añadir un overlay semitransparente, blanco o negro con transparencia para augmentar el contraste con el texto
- Modificar el contraste de la imagen (con editor de fotos o con effects)
- Colorizar la imagen (Bajar el contraste, desaturar par quitar el color, multiplicar por un color solido
- Añadir sombra al texto

Intención en el escalado

- No augmentar, pixela
- SVG aunque se pueden escalar, se piensan para ciertos tamañon
- No reducir screenshots, difumina textos
	- No escalar si se puede
	- Reducir la ventana pantalleada
	- Recortar al aspecto significativo
- No escalar iconos

Ojo con el material subido por usuarios

- Controla el aspect ratio y tamaño
- Usa `background-size: cover` (o `fit`)
- El fondo puede coincidir con el color de la foto generando poco contraste
	- usar un inset shadow con transparencia, un border puede ser muy duro

## Retoques finales

Carga los por defecto

- Cambiar los bullets por iconos
- En listas añadir un icono como avatar para indicar que cosa es que estas listando
- Embellecer las citas con unas commillas grandes y de color suave
- Custom checkboxes y radio buttons para poder estilar-los acordes al diseño

Añade color con bordes en color acentuado

- Solo uno de los bordes del elemento
- Da un toque de color sutil y lo mete en el tema

Decora los fondos

- Un color de background diferente al blanco/negro por defecto
- Marcar secciones con fondos diferentes
- Un fondo con gradiente sutil para darle el toque
- Un patron repetido a un lado para ser sutil y alejado del contenido para asegurar legibilidad
- Incluir un grafico puntual y simple en un extremo (cuadrado, circulo...)

Piensa en el estado vacío

- Normalemente diseñamos la pantalla con datos
- Que hacemos cuando no los hay
- Cuando el usuario tiene que añadir el contenido, este estado es prioritario: hay que llamar a la acción
- Si hay mucho ruido del resto de la aplicación, hay que hacer que esa primera acción destaque

No satures con demasiados bordes

- Puede recargar demasiado el diseño
- Usa sombras
- Usa diferentes colores de fondo
- Usa el espaciado para agrupar/separar

Salte de lo típico

- Lo que sale de un menu no tiene porque ser un menu, puede ser un interfaz mas rico
- Las tablas no tienen porque tener un campo por columna como en un excel, podemos combinar columnas, poner secundarios
- Tampoco los campos de una tabla tienen porque ser texto, pueden incluir imagenes, iconos, color
- Radiobuttons: en vez del circulo con el texto, podemos usar cajas seleccionables con una descripcion

En general, las restricciones acceleran el diseño,
y nos dan tiempo para despues pensar como saltarlas y ser originales.









## 








# lalal





Gestalt psicology school

- Contrast
- Repetition
- Alignment
- Proximity


## Contrast

Use contract to highlight the hierarchy among the content

Use size, weight, face or color.

By using color using lighnest is hsl domain.

## Repetition

Usar elementos similares en diferentes sitios.

No centrar texto largo y multilinia, es complicado de leer.
Si se hace que las linias no sean de longitudes muy diferentes.

## Proximity

Placing pieces together makes them an unity

## Typography

Serif: luxury, rusty, newspaper, books

Sans: 

Size:
Considerar un grid, pe. Usar sizes multiples de 8px

Weight: mantener saltos de 200 para que haya contraste entre ellos

Color: Valores extremos white/black, estresan el ojo, reducir el light
Darle un poco de hue a un blanco/negro tambien le dan emocion.







