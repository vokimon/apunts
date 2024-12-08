# SVG

## ViewPort and ViewBox

- View port: Size in outside units of the image.
	- Controlled with `width` and `height` attributes of the `svg` element.
- View box: the window of the world seen for the view port
	- Controlled with the `viewBox` attribute of the `svg` element.
	- `"anchor-x anchor-y width height"`
	- It can also be set in `symbol`, `marker`, `pattern` and `view`

- `preserveAspectRatio`  `xAncorYAnchor strategy` | `none`
	- `Anchor` can be `Min`, `Max`, `Mid`, default `Mid` for both axis (xMidYMid)
	- `strategy` can be `slice` (css cover) o `meet` (css fit)
	- `none` scales both axis to fit the viewport
- `svg` can be nested, they are sub viewports
	- on nested `svg` we can also set `x` and `y` to position it.
	- also `x`, `y`, `width` and `height` can be animatable.
- `view` tags are alternative view boxes focusable by `#id`
	```svg
	<view id="target" viewBox="100 0 200 200" />
	```



