# CSS

## Resources

- [Defensive programming](https://defensivecss.dev/tips):
  Soluciones a cosas raras que suelen pasar con los estilos.
- [CSS Tricks](https://css-tricks.com/):
  Artículos buenos sobre como usar CSS para conseguir según que resultados.
- [MDN CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
  Documentación de Mozilla sobre CSS (tutoriales, referencia...)
- [W3Schools CSS](https://www.w3schools.com/css/default.asp):
  Documentación de W3Schools sobre CSS
- [Can I Use](https://caniuse.com/):
  Buscador mantenido por la comunidad para saber qué navegadores soportan una funcionalidad.
- [Layout Generator](https://layout.bradwoods.io/customize)
  Generador de layouts CSS


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

Container query relative lengths:

- cqw: container query width per cent
- cqh: container query height per cent
- cqi: container query inline size (in ltr width, but changes with direction)
- cqb: container query block size (in ltr height, but changes with direction)
- cpmin: container query min of width and height
- cpmax: container query max of width and height

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

### 2023

```css
aspect-ratio: 16 / 9;
size: 50vw   // sets both height and width
list-style-type: 
inset: 3rem; // sets up, right, left, and bottom
isolation: isolate; // creates a new context for z-index (like svg layers)
import styles from './file.css';
div:focus-within  // selector any subelement has focus
filters: 
  blur(size) // gaussian blur
  brightness(factor) // color value multiplier
  grayscale(factor) // 0 unmodified 100% grayscale
  contrast(factor%) // enhances contrast, 0% grey, 100% normal, more adds contrast
  invert(factor) // negative colors linear beteen 0 and 100%
  drop-shadow(x-offset y-offset span color) // unlike box-shadox follows the profile of the content, not the box, no inset nor spread applied
  hue-rotate(angle) // applies a color wheel rotation
  opacity(factor) // 0 full alpha 100% full opacity
  saturate(factor) // 0 unsaturated, 100 normal, beyond saturated
  sepia(factor)
contain: layout/style/paint // TODO: limit
```
### 2024

```css
orphans: n // Number of lonely lines at the end of a page/column/region (fragmentation break)
widows: n // Number of lonely lines at the begining of a page/column/region (fragmentation break)
text-wrap: balance // balances words in each line, for example for titles
color-mix(in <model> longer/shorter param, <color1> [percent], <color2> [percent])
lch/oklch // new color model
rgb(from var(--color) calc((r + g) / 2) calc((r + g) /2) b / .4) // modifies components of a given color


// make rules not to depend that more on specificity or order
@layer reset, elements, layout, components // from general to specific
@layer my-layer {
  rules...
}
// subgrids (until now only in firefox, since sep 2024 also in safary and chrome)
// view transitions: 
:user-invalid // much like :invalid but wait for the user to interact
```

## lala

CSS frameworks:

- Normalization: Stablish a common ground for default styles
- Polyfill (implementing new features in old browsers)
- Automated vendor prefixing
- Component Isolation (no class name clash, misspelling...)
- Dynamic properties
- Variables
- Rule selection (just if you use the component)



## Tailwind

Basado en utility classes.

Pros:

- No hace falta entender CSS, selectores...

Cons:

- Poca legibilidad
- Poco semantico
- No replicable
- Poca mantenibilidad
- Dificil de salir



## Styled Components

## Emotion

## Vanilla CSS


## CSS Modules

CSS files which are scoped locally by default.

Not a standard but a build step for component based frameworks
which consists in generating unique names for classes and animatios used in a component.
This isolates component design.

Css are imported into js files generating hashed classes that can be used in 

Frameworks and libraries enabling css modules:

- [styled-components](https://styled-components.com/)
- [emotion](https://emotion.sh)
- [css-modules](https://github.com/css-modules/css-modules) ([React Integration](https://create-react-app.dev/docs/adding-a-css-modules-stylesheet/))


## Concepts


- **Utility class:** A class created not by semantic (header, card...) but to apply a specific style (red, left-aligned...)
- **Breakpoint:** Different device sizes for which a framework consider for you to change the styles for a responsive design
    - Common sizes:
        - xs (extra small, mobile)
        - sm (small, tablet)
        - md (medium, laptop)
        - lg (large, desktop)
        - xl (extra large, tv)
- **Breakpoint prefixing:** Defining utility classes which are activated just at certain breakpoint (device size).
    - Example: `md-hidden` to activate hidden on medium 
    - Following the mobile first principle, md means from md size and above, you set mobile and then, customize larger sizes with prefixed utility clases.
    - Frameworks enable redefining boundaries and names.






























