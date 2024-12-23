# Godot UI

## Basics

UI in Godot are also composed of nodes.
Most nodes derive from Node -> CanvasItem -> Control

Related videos:

- [Godotneers - Godot UI Basics](https://www.youtube.com/watch?v=1_OFJLyqlXI9)

## Creating a UI scene

TODO: How to combine IU with other 2D and 3D scenes.

## UI Positioning

### Absolute positioning

Transform properties (Control/Layout/Transform)

- Position: Top left corner relative to (top left corner of) the parent
- Size: Where the botom right corner is respect the top left corner
	- In the Editor size and position are controlled by the orange balls.
- Pivot: reference point for transformations Scale and Rotation (absolute so it is hard to center, for example.
	- In the Editor this is a + hair cross.
- Scale: Not size, will affect all the inner elements, will keep the pivot at center
- Rotation: Also will use the pivot as anchor.

::: figure images/godot-ui-markers.png
	The orange square and the round handles represent the control position and size.
	Because the control is toplevel the parent is the viewport represented by a purple box.
	Anchors are the green arrows see below.
	The orange hair cross is the pivot for rotation and scaling.

Problems: Absolute positioning relative to the origin breaks interfaces.

- Different window sizes or devices may left out elements or decenter centered elements.

More convenient models (Anchors, Layouts) abstract absolute positioning,
which still is the base and it is good to know

### Anchors

Anchors are used to place an object relative to the parent area,
not just the origin like in absoute positioning.
They are represented as the four green arrows,
by default pointing to the parent origin.


Top and bottom anchors are specified as a factor (0 to 1) of parent's width,
and left and right anchors as a factor of parent's heigth.
So, 0.5 will be always in the middle which ever the parent size.

The control then is placed at a given offset from those anchors.
Whenever the size of the parent changes,
the control resizes and repositions.

Notice that having all those anchors at parents origin,
the default,
is equivalent to the absolute positioning:
all is specified as offsets from that origin.

For convenience, Godot provides some common presets
for anchoring, available also in the editor as tool.

::: figure images/godot-ui-anchorpresets.png
	Tool to choose anchoring presets.

- 4 corners
- 4 sides centered
- Fully centered
- Vertically expanded left, center, right
- Horizontally expended top, center, bottom
- Fully expanded

The presets are only the combinations of values
0.0, 0.5 and 1.0 for the anchors.

Both anchors and offsets are not constrained to the parent.
Anchors can go beyond 0 and 1.

Placing a single component within its parent with anchor
is palatable.
When you start combining componets, it quickly becomes
chaotic.

Usually we use anchors to place a single component in the window,
and use Containers to organize its children.

### Containers (Layouts)

Containers are controls that organize
the children positioning with certain criteria.
You don't have to calculate positioning.
Direct children of a container cannot transform freely.

Examples:
- Single child: Put many direct childs and will be put one on top of the other
	- PanelContainer: Just provides a background and positions children to cover it all.
	- MarginContainer: just places one children but add margins
- Multi child
	- HBoxContainer/VBoxContainer: stack children vertically or horizontally
	- FlowContainter: Places them like text (wrapping lines)
	- GridContainer: Arranges children in rows and columns
	- SplitContainer: Box but with user controlable splitter

Since the container manages positioning,
children are constrained and cannot be freely positioned or sized.
Still, there are some parameters that provide us
some control:

- Alignment: Within the space given by the container
	- Horizontal alignment: left, center, right, expand
	- Vertical alignment: top, center, bottom, expand
	- Is the tool in the editor
- Minimum size: some controls sets it automatically, if not, it might be zero!! Set it!
- Expand: Whether the widget should ask for more space if available
- Stretch ratio: When several children want to expand,
  the expanded space will have the same proportion
  than this value for each children.
  - children A has 3 and children B has 6,
    so the parent will give double extra space to B


::: figure images/godot-ui-containersizing.png
	Tool for the placements of an object within a container
	Given the space provided by the container where
	the child will positon or expand.

::: figure images/godot-ui-containersize-properties.png


## Theming

Every control class may add themable properties.
This means that those properties can be set globally.
This is quite convenient to achieve a coherent
look and feel and change all of them in a centralized form.

If we tweek those parameters in every component
it would be pretty hard to maintain or change it.

Themes can be set at project level from the settings,
or at any level of the node tree, afecting the children
of the node setting it.

Component adds an special attribute "Theme Overrides"
enabling to make changes local to the component.

This means a property that can be set globally by a theme.
A theme is a set of values for those properties
specified per class.
For example, buttons have this font,
every control has this background...
Yes you can use inheritance for that.

A theme is a resource, you can setthe theme in a node and all children
will be affected.

You can also set the theme globally
in the project settings.

### Theme Overrides

All those properties available for theming
are also available on the widget properties
to override the theme in "Component/Theme Overrides" section.

Notice that
because every class in the hierarchy can add theme attributes,
Those overrides can be spread
on properties for the different subclasses.
They alwa

### Style box

::: figure images/godot-ui-stylebox.png
	A panel with custom style box parameters.

The style box are a set of themable properties
for the base Control so they can be set in every control.
It offers css box like properties:
background, border, padding, margin, shadow...

Stylebox definitions are shareable resources.
You can reuse them.
Indeed if you copy a control, the copy will share the style box.
Changes in one control will change also the other.
If you don't what that to happen, right click on the style box
and select to make it unique.


## UI Nodes Catalog

https://www.youtube.com/watch?v=sPfoZy-cW-E

- ContainerNode: Layout childs
	- AspectRatio: Keeps aspect ratio of child
	- CenterContainer: child centered 
	- MarginContainer: generates a padding arround the child
	- BoxContainter: Stacked in one direction
		- HBoxContainer: horizontal stack
		- VBoxContainer: vertical stack
	- SplitContainer: Like BoxContainter but using an editable splitter to control relative sizes of children
		- VSplitContainer: Vertical
		- HSplitContainer: Horizontal
	- FlowContainter: Displays elements using wrapping text layout
	- GridContainer: Arrange in rows and columns
	- PanelContainer: Adds an styled background
	- ScrollContainer: Allows overflows of the children with an scroll
	- TabContainer: Separates children in tabs
- Displays/Backgrounds
	- Label: Text display
	- RichTextLabel: With styles
	- ColorRect: 
	- TextureRect:
	- VideoStreamPlayer:
	- Separator: Line
		- VSeparator
		- HSeparator
	- Panel: Not container just background
	- -NinePatchRect: textured borders
- Control: Input. You can connect events to react
	- BaseButton:
		- Button: Text button
		- TextureButton: Image button
		- LinkButton: Shown as a link
		- CheckBox: [x]
		- CheckButton: `*-` `-*`
		- MenuButton: opens a 
		- OptionButton: Dropdown selection
		- ColorPickerButton:
	- LineEdit: single line text edit
	- TextEdit: Plain multiline editor
	- CodeEdit: Syntax highligted editor
	- Range: Selecting or displaying a number in a range
		- ProgressBar: Styled progress bar
		- TextureProgressBar: Displays a texture partially to show progress
		- SpinBox: shows a number with arrows to increase or discre
		- (V/H)ScrollBar: Usually use the ScrollContainer
		- (V/H)Slider: Grab a handle to select a number within 
	- ItemList: clickable list of items
	- Tree: Hierachical items
	- MenuBar: Array of MenuButtons
	- TabBar: Top element of the TabContainer
	- ReferenceRect: ???
	- GraphEdit: ???
	- GraphNode: ???
	- TouchScreenButton: ???

Common control attributes:

- Layout
	- ClipContent: Overflowed content clipped by parent or can be seen
	- CustomMinimumSize: Do not 
	- LayoutDirection: for children, Left to right, localization dependant...
	- LayoutMode: Anchor or Coordinates
- Transform: position, size, scale, rotation, pivot point (With anchor are changed automatically)
- Localization:
	- Autotranslate:
	- Localize numerals:
- Tooltip: 
- Focus:
	- Neighbours (sequence and directional)
- Mouse:
	- Pass or stop the event
	- Pass or stop scroll events
	- Cursor Shape:
- Input
	- Shortcut context:
- Theme:
