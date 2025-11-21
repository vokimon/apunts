# CSS Recursos i Novetats

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

## Novetats 2025

### Declarative popovers

https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using

Html declaration:

- In the popover add `popover` attribute with an `id`
- In the target add `popovertarget="myid"` this will make the popover visible on target (Button)
- `popovertargetaction` default `toggle` can also be `hide` or `show`

CSS styling:

Si a l'html tenimem el target es el popover, normalment l'estil
posicionarà el popover respecte a una ancla (anchor).

- Com que `popover` no es pas un element sinó un atribut,
els podem seleccionar `[popover]`.
- Pero com alguns estils són específics per quan estan oberts (sobretot `display`)
també fem servir la pseudo class `:popover-open`

https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_anchor_positioning

Com posicionar-lo respecte l'element que dispara (anchor)?

Podem relacionar el popup i el seu anchor amb 
definint al css de l'anchor `anchor-name: --my-anchor` a l'anchor i
al css del popup `position-anchor: --my-anchor`.
En el cas dels popovers, aquesta relació s'estableix automàticament
amb l'element que el dispara.






`anchor(top)` retorna la posicio de 

- `anchor-name: 

`@position-try`
`position-area`
`position-fallbacks`





## Novetats 2024

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

## Novetats 2023

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

## Novetats 2022

### new functions

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

### new colors

- currentColor: Inherited color, useful to expand to pseudo selectors or modify it
- transparent: rgba(0,0,0,0)


