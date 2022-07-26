# CSS Grid

## In a nutshell

- Enables setting page layouts with minimal css code.
- Establishes a grid with vertical and horizontal guidelines.
- You can define areas (squares defined by those lines) where each children will be placed.
- The placement of the lines can be fixed, relative, flexible or adaptable to the content.
- Obsoletes css frameworks like bootstrap grid. They are more powerfull.
- Supported by all major browsers since 2017 (when Edge got into)

## Grids vs Flexbox

Although many people was using Flexbox to build grids,
Flexbox still is relevant as it has its own niche.
Which are the differences?

- Grids are two dimensional, while Flexbox work in one dimension at a time.
- Grids sets the frame and the children try to fit,
while in flexbox sets the children and the layout adapt.

## Glossary

- Grid: Framework of horizontal and vertical lines to organize the layout of children elements
- Track: Space between to parallel contiguous lines
- Column: Vertical track
- Row: Horizontal track
- Area: Square delimited by two vertical and two horizontal lines of the grid
- Gap: space between inner tracks

A grid layout sets a set of vertical and horizontal lines (like inkscape guides) delimitating tracks.
Horizontal tracks are rows.
Vertical tracks are columns.
Each track can be either fixed size (percent, px, vh...) or flexible (fr) taking the proportional fraction of the remaining size.

Items are positioned referencing start and end separation lines.
Lines are indexed but can be also be named.

By default items take the next grid cell available

Explicit positioning can be set by specifying the vertical 


```css

grid-template-columns: 20rem 1fr 1f
grid-template-rows: 4rem repeat(3, 1fr 2fr)

grid-auto-columns/rows: size size Successive rows and columns get this with

grid-template-rows/columns: subgrid // use parent grid

align-items: on the parent for the children
align-self: on the children within the parent
	start, end, stretch
gap: size [size]
column-gap: size
row-gap: size

// Explicit grid placing
grid-column/row-start: linestart
grid-column/row-end: lineend // absolute
grid-column/row-end: span nlines // relative
grid-column/row: <cells> [[span] <cells>] // negative columns start counting from end
grid-area: rowlinestart columnlinestart rowlineend columnlineend

// The cells get occupied and the implicit placed elements jump those

// You can name lines between tracks

grid-template-columns: [main-start] 20rem [content-start] 1fr [content-end] 1f [main-end]
// then in the childs
grid-column: content-start / content-end
// if you named the lines with and start and end suffixes
grid-area: content


grid-auto-rows: size // creates rows as needed of the provided size

grid-template-areas: 'area1 area2 area3' 'area4 . area3'
// each quoted is a row.
// dot (or multiple dots without spaces) is a place holder
```

Blocks absolutely positioned into a relative pos grid container are positioned
relative to the grid container and not put on the flow.

If you name a line `xxxx-start` or `xxxx-end` it will implicitly
define an area named `xxxx` and the other way arround:
If you name an area `xxxx` you will implicitly define
lines `xxxx-start` and `xxxx-end` foreach direction.

- You can specify two ids for the line like `[id1 id2]`
- If you use a line name multiple times (ie. using repeat) you can specify which one
by adding a number after it 'content-col 2`.
- Likewise you can span just counting instances of a name `span content-col 2`

Example: setting up bootstrap 12 columns model

```css
/* This single selector sets it up */
.grid {
	display: grid;
	gap: 10px;
	grid-template-columns: repeat(12, [col-start] 1fr);
}

/* And for example, the tipical header-sides-footer structure */
.footer,
.header {
	grid-column: col-start / span 12;
}
.side-1 {
	grid-column: col-start / span 2;
	grid-row: 2;
}
.content {
	grid-column: col-start 2 / span 8;
	grid-row: 2;
}
.side-2 {
	grid-column: col-start 10 / span 2;
	grid-row: 2;
}
```

`grid-auto-rows/columns` determines the size of implicitly created columns.
You can specify several values and they will be asigned in loop.

Beside absolute (rem, px...) realative (%,vh,vw...) and flex sizes,
there are some cool sizes we can use.

`auto`: (The default value)
As minimum, the maximum minimal size of the track.
As maximum, max-content.

`min/max-content` Adapts to the smaller/bigger content requirement in the track



