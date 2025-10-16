# CSS frameworks

- Normalization: Stablish a common ground for default styles
- Polyfill (implementing new features in old browsers)
- Automated vendor prefixing
- Component Isolation (no class name clash, misspelling...)
- Dynamic properties
- Variables
- Rule selection (just if you use the component)

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


## Precompiladores

Expanden el lenguage CSS dándole funcionalidades superiores
sobretodo en cuanto a expresividad y no repetición.
También para suplir problemas de compatibilidad.
Se implementan como precompiladores que
acaban generando css o a veces tambien javascript.

- [Stylus](https://stylus-lang.com)
- [Less](https://lesscss.org)
- [Sass](https://sass-lang.com)

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


