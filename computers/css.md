## Units

Absolute lengths:

- cm: centimeters
- mm: milimeters 0.1cm
- Q: quarter milimeters 0.025cm
- in: inches 2.54cm
- px: pixels 1/96in 1/243.8cm (cannonical unit)
  - Not a device pixel! At the time of the standard, monitors where 96 DPI in 1024x798
  - Distance to the screen also counts.
    - Reference pixel, defined by the angle at arm length distance 71cmi s .26mm
    - Thus, closer screens (mobiles) have smaller px and further screens (tv's, projectors) have wider px
  - in screens also the distance to the screen counts, so it is the angle compared to that size at the arm distance
- pt: points 1/72in 1/182.88cm 1.333px
  - often used for absolute font sizes
- pc: picas 1/6in 16px 4.2mm
- lh: line height, altura de linia del elemento (ideal para alturas donde quepan n lineas)
- rlh: root line height, altura de linea del elemento raiz

Rules of thumb for sizes:

https://www.youtube.com/watch?v=N5wpD9Ov_To

Font sizes: use rem. To adapt the settings of the user

Width

- percentance with max-min with as limit, in px/rem
- ch per controlar el nombre aproximat de characters

Height

- let it flow min-height and relative to the viewport

Padding or margin: rem or em

- rem para distancias consistentes
- em para adaptarse a la fuente del elemento

px for small gaps, shadows...

media queries: em for consistency among browsers


Font relatives:

- ch: advance measure of a '0' zero of the current typeface. The advance measure of the font is the spacing with the next letter (text orientation is taken into account)
- ex: height of an 'x' of the current typeface (or the parent if it is used to change font-size).  Used to compute interline spacings and margins
- em: width of an 'm' of the current typeface  (or the parent if it is used to change font-size)
  - being m the wider letter, ensures that at least those letters will be in
  - matches the font size (a 10pt font size, 1em is 3.5mm)
- rem: root em, em of the root element, not the current or the parent (Takes into account user's and system preferences)

Parent relative lengths:

- %: percent relative to the parent's size
- fr: fraction of leftover space

Viewport relative lengths:

- vw: percent relative to the view port width
- vh: percent relative to the view port height
- vi: percent relative to the view port line axis (horizontal for most, but vertical for some asian scripts)
- vb: percent relative to the view port block axis (vertical for most, but horizontal for some asian scripts)
- vmin: percent relative to the view port min axis (height or width)
- vmax: percent relative to the view port max axis (height or width)

Angles:

- turn: full turn
- deg: degrees 360 per turn (canonical unit)
- grad: gradians 400 per turn
- rad: radians 2pi per turn

Rotations are clockwise

When stating a direction 0 is north and 90deg is right/east

Time

- s: seconds
- ms: miliseconds

Frequency

- Hz: 1/s
- kHz: 1000/s


Resolution:

The size of a real pixel (dot) in the device

dpi: dots per inch
dpcm: dots per cm
dppx: dots per pixel unit


## new functions

- `calc(expression)`
- `min(value, value, value...)`
- `max(value, value, value...)`
- `clamp(min, value, max)`
- `attr(name units, fallback)` takes the value from named xml attribute of the target (no comma between attribute name and the units
- `url(url)`
- `rgb(r,g,b)`
- `rgba(r,g,b,a)`
- `hsl(hue, saturation, lightness)`
  - hue 0/360 red, 120 green, 240 blue.
  - saturation 100% is the full color, 0% a shade of gray
  - lightness: 100% white, 50% normal, 0% black
- `hsla(hue, saturation, lightness, alpha)`

## new colors

- currentColor: Inherited color
- transparent: rgba(0,0,0,0)


## new features

aspect-ratio: 16 / 9;
size: 50vw   // sets both height and width
list-style-type: 
import styles from './file.css';



CSS frameworks:

- Normalization: Stablish a common ground for default styles
- Polyfill (implementing new features in old browsers)
- Automated vendor prefixing
- Component Isolation (no class name clash, misspelling...)
- Dynamic properties
- Variables
- Rule selection (just if you use the component)


# Methodologies


## BEM (Block, Element, Modifier)

https://en.bem.info/methodology/css/

Evita ciertos problemas en la definicion de estilos
cuando queremos reusar componentes,
mover componentes de sitio,
o redefinir su comportamiento.

Tal y como esta definido CSS, se aplican segun especificidad.
Eso hace que los selectores anidados o los basados en id, o los que tienen muchas clases,
sean muy dificiles de sobreescribir.
Tambien hace que sean muy sensibles al contexto DOM en el que se usan.
Para evitarlo, proscribe el uso de id's y de selectores padre hijo.

Un **Bloque** es una parte de una interfaz que se puede reusar o mover como unidad.
Los bloques pueden
contener otros bloques,
usarse repetidamente en un proyecto o
reusarse como elemento aislado en otro proyecto.

**Elementos** son partes del bloque que no tienen sentido fuera de el.
Por ejemplo, cada una de las pestañas de una barra de pestañas.

Los **Modificadores** cambian como se ve o comporta un bloque o elemento.
Esos modificadores pueden cambiar en tiempo de ejecución.

Un nodo DOM puede ser a la vez varias entidades (bloque o elemento) BEM.
Por ejemplo un `menu__item` (elemento dentro de `menu`) puede ser a la vez un bloque `link`.

Nomenclatura: `block-name__elem-name_mod-name_mod-val`

Ejemplo: `main-menu__item_status_background-color_red`

- El `-` separa palabras
- El `__` separa el bloque del elemento (si es un elemento)
- El `_` separa el modificador (si es un modificador) y su valor (si lo tuviera)

Si se sigue la metodologia se puede redefinir los estilos facilmente
y no deberian de existir conflictos.

- Los selectores son casi siempre una sola clase para no augmentar su especificidad y poderse redefinir facilmente:
  - no usa ids
  - no usa tags
  - no usa clases combinadas,
  - solo en unos pocos casos se usan clases anidadas
- Usa clases que identifican
  - bloques `button`,
  - elementos de esos bloques `button__icon`, `button__ripple` o
  - modificadores `buton_enabled`, `button_cool_theme`.
- La excepción para usar clases anidadas son:
  - cuando se depende de los modificadores del padre (el modificador como contexto)
  - cuando se depende de el tema de la aplicación (el tema como contexto)
  - No para indicar jerarquia (el nombre ya lo documenta)
- La excepción para usar clases combinadas
  - cuando los modificadores tienen efectos juntos (enabled y theme)
- Cada selector se ocupa de un aspecto.


## Suit CSS

Usa una nomenclatura analoga a BEM pero diferente:

`namespace-ComponentName-descendantName--modifierName`

`u-utilityName`

Para las variables `--ComponentName[-descendant|--modifier][-onState]-(cssProperty|variableName)`

Para las variables del tema simplemente camelCase y en theme.css

Utilities: basada en los conceptos de atom

Components: basada en los conceptos de BEM

Principios:

- Classes and variables are scoped to the component
- All related css in a single file named as the component, or a directory.
- Components should not set their width, margin and positioning.
  - Make it inline or full-width (100%) and let the ancestors fit in
- Documentation:
  - Intended presentation
  - Modifiers and states
  - Reason for specific, opaque property values
  - Known limitations

## Tailwind



# Resources

- [Defensive programming](https://defensivecss.dev/tips)
  Soluciones a cosas raras que suelen pasar con los estilos.




























