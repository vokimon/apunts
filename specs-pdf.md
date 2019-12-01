
Los elementos básicos de un pdf son los _objetos_.
Los hay de distintos tipos:

- array
- boolean
- dictionary
- integer
- name
- null
- real
- stream
- string

La _estructura de fichero_ es la que determina como
los objetos se almacenan en el fichero.
Disposicion, compresion, cifrado...
Donde almacenarlos, donde irlos a buscar y como
actualizarlos.

La _estructura de documento_ determina como los objetos
construyen el documento formando paginas, fuentes...

El _content stream_ contiene los objetos con los
datos que van en esa estructura.

## Lexico

Los elementos estructurales estan limitados a ASCII,
pero las strings y los streams pueden contener cualquier byte.

White spaces: Son todos equivalentes fuera de comentarios, strings y streams. Separan tokens.

- 0x00 \0 null
- 0x09 \t tab
- 0x0A \n line fed
- 0x0C \f form feed
- 0x0D \r carriage return
- 0x20 ' ' space

Aunque sintacticamente son equivalentes, a veces se requiere que un elemento empiece en nueva linia.

Son marcadores EOL `\r`, `\n`, asi como la sequencia `\r\n` que se considera uno solo.

Delimitadores: `[ ] { } ( ) < > / %`

El `%` se usa para comentarios hasta el siguiente EOL.
El comentario es equivalente a un espacio.

Hay dos comentarios especiales:

- `%PDF-n.m`: magic que encabeza el fichero e indica la version
- `%%EOF`: que indica el final del fichero

Se llama _regular characters_ a los que no son ni espacios ni delimitadores.


## Objetos

### Booleanos

Palabras clave `true` y `false`

### Null object

Palabra clave `null`

Tambien una indireccion fallida es `null`


### Numericos

- Enteros: 4 +3 -4
- Reales: -.034 

Donde se puede usar un real se puede usar un entero.
Se habla de numeros cuando son reales,
se especifica enteros cuando solo pueden ser enteros.

Algunos writers no conformes escriben numeros con formato exponencial (`3.2E-123`) o con radix no decimal (`16#FFEA`)

### Strings

- Literales: Entre `(parentesis)`
	- Si contiene parentesis balanceados, ningun problema
	- Cuando no estan balanceados podemos escaparlos con `\(` o `\)`
	- Otras sequencias de escape con `\`: `\n \r \t \b \f \\ \777`
	- Toda barra seguida de algo que no sea eso se ignora
	- Un EOL precedido de `\` se ignora
	- Cualquier EOL en un string se interpreta como `\n`
	- Los octales pueden ser `\004`, `\04` o `\4`
	- Ojo: `\0004` ya seria el '\0` seguido de un `4`
- Hexadecimales: `<FA4C>`
	- Si un byte no esta completo se llena por ceros a la derecha
	- Puede incluir espacios (incluidos EOL)

### Nombres

- Serie de caracteres, cuales quiera, que identifican algo de forma única.
- Puede ser cualquier tipo de caracter
- A la hora de representarlos en el fichero:
	- los precedemos de `/`
	- los separadores, espacios en blanco y el signo `#` los representamos con su hex precedidos de `#`
	- el resto de caracteres los podemos representar literalmente o tambien con `#hh`
- Aunque no limita a ello, cuando el nombre se tenga que representar se supone UTF8

### Arrays

- Arrays entre corchetes `[ ]`
- Dentro otros objetos separados por espacios
- Se pueden anidar

### Dicts

- Dicts entre dobles angulos `<< >>`
- Dentro parejas clave-valor
- Las claves han de ser todas nombres
- Un valor `null`, es como si su clave no existiera
- El orden de las claves ignorado
- Las claves han de ser unicas en el diccionario
- Un diccionario puede tener otros diccionarios (y arrays y ...)
- Ojo: los hex strings usan solo un angle bracket
- A menudo se usan las claves `Type` y `Subtype` (o su abreviatura  `S`) para indicar el tipo de objeto.


### Streams

Representan datos binarios grandes.
Los strings y los names pueden estar limitados en longitud.
Los streams no.

Se compone de:

- Un diccionario:
	- `Length`: Requerido. Numero de bytes del stream.
	- `Filter`: nombre del filtro o array de nombres de filtros que se aplicaran en orden al contenido
	- `DecodeParams`: diccionario o array de diccionarios con los parametros a aplicar a cada filtro.
		- Cada uno de los diccionarios puede ser un Null si no hay parametros
	- `F`: Indica un fichero o ficheros de los que obtener el stream
		- Substituye al contenido entre `stream` y `endstream`
		- No quita que si hay bytes entre `stream` y `endstream` especifiquemos el tamaño.
	- `FLength`, `FFilter`, `FDecodeParams`: lo propio para el `F`.
	- `DL`: Hint para el decoded length
- Un tag `stream` posiblemente seguido de un eol ignorado
- Los bytes
- Un tag `endstream` posiblemente precedido de un EOL ignorado


### Objetos indirectos

- Un objeto se puede etiquetar y despues referenciar posteriormente.
- Se identifica unicamente por dos números:
	- numero de objeto: un numero arbitrario (>0)
	- numero de generacion: indica secuencia de actualización del fichero
- Se etiqueta
	```
	12 0 obj
		(My texto)
	endobj
	```
- Se referencia con los numeros y una R:
	```
	12 0 R
	```
- Una referencia a un objeto inexistente no es un error, si no que es null

### Filtros

## Estructuras de datos comunes

### Strings

Tiene subtipos:

- string type
	- text string
		- PDFDocEncoding: Latin1
		- UTF16-BE con markador de encoding al inicio
			- puede tener marcadores de lenguage en medio
	- ascii string
	- byte string
		- no tiene por que ser texto (pero puede)
- text stream: un stream que descodificado es un string type

- Date: `(D:YYYYMMDDHHmmSSOHH'mm)` pe. `D:199812231952-08'00`
- Rectangle: `[ xleft ybottom xright ytop ]`
- Name Tree: Arbol de búsqueda
	- Las claves son strings y no names
	- Valores son referencias indirectas
	- Las claves aparecen lexicamente ordenadas
	- Cada nodo tiene:
		- `Kids`: array de claves valores que son RI a subnodos
		- `Names`: array de claves valores que son RI a objetos
		- `Limits`: en los nodos no root la primera y ultima clave contenida en los hijos
- Number Tree: Como el name tree pero con claves numéricas
	- En vez de `Names` tienes `Nums`
- Functions: Funciones NxN (n variables, n salidas)
	- Numericas
	- Multivariables, Multivalor (R^n -> R^n)
	- Sin efectos laterales
	- Domain (input interval) y Range (output interval, optional)
	- Type0: Sampled (puntos) se interpolan los puntos intermedios
	- No existe Type 1??
	- Type2: Exponential interpolation (monomio + cte)
		- C0: valor para x=0
		- C1: valor para x=1
		- N: grado del exponente
	- Type3: Stitching (junta varias funciones)
	- Type4: Postscript (adjunta un stream con codigo postscript)

- File specification strings:
	- Es un string, entre parentesis, escaping
	- Usa forward slashes para separar componentes
	- Puede ser absoluta o relativa dependiendo si hay barra inicial
	- El origen de los relativos es el contenedor del fichero (puede ser una URL o el file system)
	- Puede usar el `..`
	- Se puede escapar la barra si forma parte del nombre con doble contrabarra (una para escapar la segunda, la segunda para interpretar el nombre)
- File specification dict:
	- Type: FileSpec
	- Permite cosas avanzadas:
		- especificar url's (`FS`: `URL`)
		- especificar un nombre diferente dependiendo del sistema
		- ficheros embedido
		- referir ficheros relacionados



## Estructura de fichero

Objetivo:

- Acceso aleatorio eficiente
- Actualización incremental


Elementos:

- Header: identifica la version de especificación PDF
- Body: Objetos propios del documento
- Cross reference table: objetos indirectos
- Trailer: Contiene punteros la XRef y a ciertos objetos
- Objetos añadidos en actualizaciones posteriores

### Header

- Debe empezar por `%PDFn.m` donde n.m es la version de la especificacion (1.0 a 1.7 actualmente)
- La version efectiva no es esa, esta en el trailer, para poderse incrementar con actualizaciones
- Añadir un comentario con 4 bytes > 128 para que se detecte como binario el fichero


### File Body

- Secuencia de indirect objects (y de streams con indirect objects) que forman el documento

### XRef Table

- cross reference section
	- `xref` eol
	- subsections:
		- subsection header:
			- first object number
			- count
			- eol
		- referencias
			- 10 digitos byte offset en el ¿stream decodificado?
			- 1 espacio
			- 5 digitos generationa
			- 1 espacio
			- `n`
			- \r\n  o `_\n` o `_\r`
		- referencias libres
			- 10 digitos object number del siguiente libre
			- 1 espacio
			- 5 digitos generationa
			- 1 espacio
			- `n`
			- \r\n  o `_\n` o `_\r`

### File Trailer

- `trailer`
- dict
- `startxref
- byte offset of last xref section
- eol
- `%%EOF`

El diccionario tiene lo siguinte:

- `Size`: Numero de objetos
- `Prev`: 
- `Root`: El diccionario de catalogo del documento (Requerido, indireccionable)
- `Encrypt`: Diccionario de cifrado del documento (Requerido si hay encriptación)
- `Info`: Diccionario de informacion (Opcional, indireccionable)
- `ID`: Array de dos strings de bytes que identifican el documento (Requerido si hay cifrado)
- `Next`: 

### Actualizaciones

Se puede actualizar un fichero de forma aditiva manteniendo la versión anterior.
Se añade detras del `%%EOF`:

- Otro Body con los objetos
- Una XRef section referenciando todos los objetos (mantenidos, borrados, actualizados...)
- Trailer actualizado apuntando a la ultima xref

Se puede hacer n veces.



### Object Streams

Un stream que almacena una secuencia de objetos indirectos.
Permite almacenar los objetos con los metodos de compresion de un stream.

No se puede meter en un stream object:

- Streams objects
- Objetos de generacion distinta a la zero
- El diccionario de cifrado
- Un objeto que represente el Length de del diccionario de otro object stream

- Igual que los otros streams es un objeto que empieza con el diccionario, seguido de `stream`, el contenido, y `endstream`

El diccionario de un Object Stream añade los siguientes campos al de un Stream convencional:

- `Type`: ha de ser `ObjStm`
- `N`: Número de objetos
- `Offset`: El offset en los datos decodificados del primer objeto
- `Extends`: (opcional), indica la referencia a otro ObjStm del cual este es continuacion

El contenido sin codificar es:
- una linia con una sequencia de pares de numeros
	- Cada par correspondiendo a
		- el numero de objeto
		- su offset relativo al primero.
	- El primer offset sera siempre 0
	- La generacion hemos dicho que siempre 0 implicitamente
- Le sigue una secuencia de objetos sin los tags `obj` y `endobj`.


### Cross reference stream

- Representacion mas compacta
- Posibilidad de añadir tipos de objetos futuros
- Tambien son stream objects, con su diccionario y su seccion de stream data
- El diccionario contiene estos campos adicionales
	- `Type`: `XRef`
	- `Size`: numero de objetos mas uno.
		- Puede contener menos
		- Ninguna reescritura puede contener mas
		- Puede ser igual que el numero de objetos total indicado en el trailer
	- `Index`: (Defecto `[0 Size]`) un para de numeros por cada subsseccion
		- El primer número indica el primer object number de cada subseccion
		- El segundo indica el numero de objetos de la subsseccion
	- `Prev`: indica el anterior xref stream (TODO: en mixtos con xrefs no stream no me queda claro)
	- `W`: array of 3 integers with the size in bytes of the fields
		- Un tamaño cero implica que no se indica y se usa el valor por defecto
- Siguen los datos que, decodificados tienen la siguiente estructura
	- Entradas de objetos libres
		- Tipo (0) (equivalente al  `f`)
		- Object number del siguiente objeto libre
		- Generacion que toca si este object number se vuelve a usar
	- Entradas a objetos en uso sin comprimir
		- Tipo (1) (equivalente al `n`)
		- Byte offset dentro del fichero
		- Generacion del objeto (default 0)
	- Entradas a objetos en uso comprimidos
		- Tipo (2)
		- El object number del stream que lo contiene
		- El indice del objeto en el object stream

### XRefs compatibles hacia atras

TODO: No me lo he leido


### Cifrado

TODO: Saltado


# Estructura de documento

Un documento es una jerarquia de objetos partiendo del Document Catalog.

- Document Catalog
	- Page Tree
		- Page
			- Content
			- Thumbnail
			- Annotations
		- Page
			- ...
	- Outline hierarchy
		- Outline entry
		- Outline entry
		- ...
	- Article Thread
		- Thread
			- Bead
			- Bead...
		- Thread...
	- Named destinations
	- Interactive Form

## Document Catalog

Referenciado en el Trailer por la clave `Root`


Dictionary:

- `Type`: `Catalog`
- `Version`: (Optional)
- `Extensions`: (Optional) Diccionario de extensiones
- `Pages`: Referencia indirecta o no al Page Tree
- `PageLabels`: A Number Tree with page indices -> page label dictionaries
- `Names`: Name dict.
- `Dests`: Named destinations dict. Nombres con destino.
- `ViewerPreferences`: Viewer preferences diccionary. Sugerencias de presentación.
- `PageLayout`: Como presentar las paginas de entrada:
	- SinglePage (default), OneColumn, TwoColumnsLeft (odd pages on the left), TwoColumnsRight, TwoPageLeft, TwoPageRight
- `PageMode`: Que cosas presentar a parte del contenido
	- UseNone (nada, default), UseOutlines, UseThumbs, Fullscreen, UseOc (content group??), UseAttachments
- `Outlines`: Diccionario representando el esquema del documento
- `Threads`: Diccionario connectando los hilos de lectura
- `OpenAction`: como abrir puede ser:
	- Un array de destinations
	- Un action dict
- `AA`: diccionario con acciones adicionales a ejecutar cuando se disparan eventos concretos
- `URI`: diccionario con acciones relacionadas con la activacion de URI a nivel de todo el documento
- `AcroForm`: El formulario del documento
- `Metadata`: dict con Metadatos del documento
- `StructTreeRoot` Document Tree root Structure dict
- `MarkInfo`: 
- Lang: 
- SpiderInfo: Diccionario con la lista de comandos para hacer la captura web para generar el documento
- OutputIntents: Especifica que perfiles de color usar para cada uso (impresora, pantalla...)
- PieceInfo: Datos privados ignorables por los visores que no los entiendan asociados con una pagina o xform
- OCProperties: Contenido opcional ???
- Perms: Acciones a las que tiene acceso un usuario no propietario
- Legal: Atestados de sobre el contenido firmado
- Requirements: Lista las features que usa el documento
- Collection: Diccionario para mejorar el renderizado de los attatchments
- NeedsRendering: Cuando hay XFA Forms, dice que el documento necesita rerenderizado cuando se abra
- ...


### PageTree

PageTree -> [PageNode] -> Page

Los campos que se definen arriba se heredan de los padres
si no se especifican en los hijos.

Que tiene una page?

- Varios rectangulos progresivos: si no se especifican uno, por defecto coge el valor del externo
	- Usualment se deja mínimo 3-5mm entre cada uno
	- MediaBox: Rectangulo del medio (papel)
	- CropBox: Rectangulo donde en el papel ira todo. Es el que se imprime y visualiza, incluye marcas de recorte e impresion. por defecto el MediaBox
	- BleedBox: Espacio de recorte en produccion contiene fondo que hay que cortar , por defecto el CropBox
	- TrimBox: Espacio de recorte para acabado (recortado), por defecto Bleed, si no se ha definido 
	- ArtBox: Rectangulo dentro del TrimBox con contenido (no incluiría los margenes), por defecto TrimBbox
- Contents:



























































