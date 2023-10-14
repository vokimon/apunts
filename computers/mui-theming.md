# MUI Theming

https://www.youtube.com/watch?v=SUEkAOuQZTQ

## Components

- `components`: specific values for components, keys are component classes
	- More info https://mui.com/material-ui/customization/theme-components/
	- Children are Components names
	- `defaultProps`: sets default component props in API
	- `styleOverrides`: slots names with react css
		- can be a function receiving the component state, state.variant, state.color, state.orientation
		- the function receives a second parameter theme to acces the final theme values
	- `variants`: create new variants {props, style}, if the component matches props (variant, color, size...), apply style
- `breakpoints`: Defines the viewport sizes 
	- keys: ordered list of the names of the breakpoints (xs, sm, md, lg, xl)
	- values: map key->int for the starting width for each breakpoint
	- functions to calculate 
- `palette`:
	- standard colors: primary, secondary, error, warning, success, info
		- customized by providing color objects (main, light, dark, contrastText) called tokens
		- non-specified will be computed from main using palette.getContrastText(partialColorObject)
			- palette.tonalOffset is used to compute `light` and `dark` tokens
				- 
			- light and dark are shifted using palette.tonalOffset, can be an factor or a 
			- contrastText is computed depending on the palette.contrastThreshold
				- 4.5 is the recommended value for accessibility
	- custom colors can be defined but tokens are not calculated automatically
		- either define all tokens explicitly
		- or use palette.augmentColor({color: {tokens}, name: colorname})
	- non standard colors with specified tokens
		- common.white
		- common.black
		- grey[number]
		- grey.Anumber
		- text
			- primary
			- secondary
			- disabled
		- background
			- default
			- paper
		- divider
		- action: active, hover, selected, disabled, disabledBackground, focus
		- action: hoverOpacity, selectedOpacity, disabledOpacity, focusOpacity, activatedOpacity
		
	- common? text? background?
	- Each role has keys: main, light, dark, contrastText. Missing ones are computed from main if specified.
	- mode: light, dark sets the whole website light or dark
		- By defaults changes the palette for some components:
			- Typography: primary, secondary, text.disabled
			- Button: action.active, action.hover, action.selected, action.disabled, action.disabledBackground
			- Background: background.default, background.paper
			- Divider: divider
	- tonalOffset: contrast factor to generate dark and light variations.
		- Each variation can have its value by providing an object
	- contrastThreshold: the higher the more likely a background is considered light, and contrastText will be black
	- by providing new keys you can create new colors to use as color= attribute
	- getContrastText(color, color): returns the contrast ratio between two colors
	- augmentColor({color: {main...}, name: 'name'}) computes the variation for a custom color
- `typography`
	- 



