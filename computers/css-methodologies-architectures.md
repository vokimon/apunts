# CSS: Metodologías y arquitecturas

A medida que los proyectos avanzan es común encontrarse con problemas de mantenibilidad.
Cada vez resulta más complicado hacer cambios.
Es importante establecer ciertos criterios para mantener la entropia acotada.

Uno de los problemas más comunes del css es que es complejo controlar
la especificidad de los selectores.
Si los selectores son demasiado específicos es difícil especializar.
Las reglas a aplican 

Ciertas malas practicas al definir selectores
afectan a su especificidad
y que hacen que las reglas interaccionen entre ellas de forma poco predecible o flexible.
Dificulta la mantenibilidad.

Unos primeros criterios:

- Evitar `!important` no se puede sobreescribir y enmascaran problemas de metodologia.
- Evitar `#id` en los selectores
    - Tienen demasiada especifidad.
    - Dejarlos para js. Usar solo clases para CSS.
- Usar clases con nombres intelegibles
    - Minimizar las abreviaciones
    - Si se hacen que sean parte de la cultura de equipo
    - Si son autogenerados que haya una parte no generada que ayude a localizar el origen de la norma cuando depuramos
- Evitar nested selectors
    - Hay algunas metodologias que lo usan de forma limitada
    - Acopla el CSS con la estructura real del HTML y eso no suele ser bueno a la larga

A parte de estos criterios, podemos aplicar:

- Convenciones: Como identificamos las palabras de un identificador (`snake_case`, `camellCase`, `PascalCase`/`UpperCamellCase`, `kebab-case`)
- Metodologias: Como nombramos las clases
- Arquitecturas: Como organizamos el código

DGG: (Todo es un nivell de abstraccion por debajo a como va en programación)

Objetivos de metodologias:

- Comprensible (los nombres tienen significado claro)
- Predecible (efecto de aplicar una clase)
- Reutilizable (no replicar codigo)
- Escalable (funciona para proyectos grandes)
- Modular (cambios en un componente no afecta a otros)

Criterios de organizacion de las metodologias:

- Estructurales: tipo de elemento al que se le aplica
- Funcionales: que attributos afecta

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

Ejemplo:

```html
<div class='menu'>
  <div class='menu__item'>...</div>
  <div class='menu__item menu__item--active'>...</div>
</div>
```

Fuerzas:

- :-) sencillo y facil
- :-( html muy verboso


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

## CubeCSS

https://cube.fyi/

CUBE: Composition Utility Block Exception

- Global (not in the anacronym):
    - Set the reset and the basics for the standard elements
    - Embraces css progresive enhancement and keeps minimal css
- Composition: The skeleton of the page
    - How elements of a container are layout
      - Reusable, flexible layouts
      - Parametrizable with css-variables
          - se pueden personalizar para componentes concretos
    - No deben incluir visuales o decorativas como: colores, fuentes, sombras...
    - No pixel-perfect (visualbasic) sino adaptable (responsive, qt)
- Utilities: piece of funtional rules (bgcolor-primary, flow...)
    - Una sola regla o un conciso grupo de reglas relacionadas
    - Basarse en design tokens (--variables o mixins) para tener una sola fuente de verdad
    - Combinar utilities en una clase tiene mas pinta de bloque
    - Design tokens: utilities which are parts of the design system (colors, spacing...)
        - From some definitions generate (sass) a set of utility classes
        - Now css vars and calc do this
- Block: Just like in Bem but
    - unlike bem, structural selector are ok, shorter classes
    - unlike bem, we can do class combinations
        - most of the work is done on global, composition and utility classes, so high specificity is ok
- Exception: Modifier in BEM, but it uses `data-*` attributes for it, which is cool.

CUBE Methodology suggest to group classes in html by each category
either with [ ] or separating them with |.
`[ main-block ] [ additional blocks ] [ other utilities]`
In order to state clearly which role each class plays.
Such separators are ignored by most browsers.




Pensada para usar las Logical Properties.

Usa atributos `data-*` para el state.

- :-( Las | y los corchetes no son naturales al HTML




# Arquitecturas

https://www.youtube.com/watch?v=tUldrlfIGb4

- Metodologia: Como nombrar las clases
    - BEM, Suit CSS
- Arquitectura: Como organizar ficheros y carpetas
    - OOCSS, ITCSS, ACSS (Atomic Design), SMACSS, BEMIT


## OOCCS

Metodologia BEM + carpetas o archivos separadas asi:

- `styles`: importa el resto
- `_base`: reset css
- `_layout`: mixins, grid, flex, wrappers
- `_modules`: objetos concretos
- `_other`: modificadores
- `_shame`: importants y otras cosas que nos averguenzan (donde comenzar un refactor)

Fuerzas:

- :-) Facil si ya se parte de BEM
- :-) Estructura sencilla
- :-( Clases muy largas




## ITCSS

Inverted Triangle architecture for CSS, Harry Roberts @csswizardry

Convention to organize CSS for a project focusing in maintainability.
Takes profit of css preprocessors like sass, less, postcss, stylus...

Rules are hierarchicalized in folders: from 

- Settings: Variables and preprocessor methods
- Tools: Mixins i funciones
- Generics: resets, global theming
- Elements: styling for standard html elements
- Objects: 
- Components:
- Utilities: Non related to a component

Triangulo invertido:

- Contra mas arriba en la jerarquía, a más elementos afecta.
- Contra más abajo en la jerarquia, más especificidad en los selectores.

Especificidad:

- Settings/Tools: No afecta a elementos
- Generics/Elements: Especificidad de magnitud 1: elementos html standard
- Objects: Una clase: magnitud 2 
- Components: Dos o tres clases: magnitud 2 pero mayor que objects
- Utilities: Llevan important, nivel 4

## Atomic Design CSS

Aproximación bottom up pensada en la reutilización.

- Ions: Valores en un json (colores, tamaños...) (Tambien Tokens o Design Tokens)
- Atoms: Low level widgets
- Molecules: Combination of widgets (cards, dialogs, drowdowns, navigations...)
- Organisms: Combination of molecules: Sidebar, product list... (Si envia o recibe datos, Quark)
- Plantillas: Generalized pages, concentrates in the overall layout
- Paginas: Concrete pages
- Utilities: Including browser hacks, overrides...

- Pensada para equipos con UX - Frontend, integrada en Figma

Proponen una nomenclatura muy mierder con backslashes

## SMACSS

- Base: Reset i generales
    - Selectors are single standard elements
- Layout: Estructura de la pagina
    - Partes de la pagina con ID
    - No visuales, solo distribución
    - Prefijo `l-` (layout)
- Modules: Elementos reutilizables
    - Elementos modulares del diseño
    - Nombre tal cual
- State: Estado de un modulo
    - El nombre del modulo separado con --
- Theme: Colores y estilos
    - Usamos variables

Fuerzas:

- :-) Organizacion simple de clases y carpetas
- :-( ids son lentos





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
- [vanilla-extract](https://vanilla-extract.style)

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



## vanilla-extract

- CSS-in-JS genera css puro.
- Elementos dinàmicos los extrae como variables
- css modules




























