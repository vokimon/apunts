# Godot 4 (Game Engine)

::: link https://www.youtube.com/watch?v=nAh_Kx5Zh5Q
	The ultimate introduction to Godot 4 

::: link https://www.youtube.com/watch?v=9LaB6wbZepg&list=PLJ690cxlZTgL4i3sjTPRQTyrJ5TTkYJ2_&index=0
	Playlist GDScript from scratch. From very scratch, even programming concepts,
	but explains some of the differences

## The node tree

- Game: Is composed by a tree of nodes.
- Node: Any element of the game is a Node in a tree. Shape, skeleton, 2D/3DNodes, Sprites, Timer...
- Properties: Nodes have named values which depend of the node type
- Inheritance: Type of nodes are subtypes of other types
	- Properties can be inherited
	- Default properties values can be set differently
	- They can extend with new properties
	- You can add childs
- Tree structure (Composition hierarchy != Inheritance hierarchy):
	- Modifications on the parent (scaling, rotating, positioning, skew, groups...) affect their children
	- Siblings order affects to the drawing order
- Scene: Root node that organizes other nodes and display them
	- Current scene is the scene currently displayed
	- Scenes are also reusable groups of nodes
	- You can convert a subtree of nodes into its own scene
	- You can insert a scene inside another scene
	- Scenes are stored as .tscn files
- Root node types:
	- Node2D: 2D scene to organize object in a 2D canvas
	- UI: Control node (a Node2D it self) but organizes controls in layouts
	- Node3D: 3D scene to organice object in a 3D world
- Some useful node types:
	- Node2D: A 2D point bearing 2D transformations to its children
	- Sprite2D: An 2D image (also a Node2d)

## Scripting (GDScript)

- Scripts are bound to nodes
- Scripts can be done in several languages
	- C, C++, GDScript (similar to python)
	- `.gd` files, same name than node (but turn node's `PascalCase` into script's `snake_case`)
- GDScript is similar to Python (yupi) but it has many differences (oops)
- Every script defines a class
	- Functions, variables, constants... defined at the top level of the script will be class members (methods and properties)
	- Unnamed class by default
		- Refer a class: by a string with the script path `"res://path/to/myclass.gd"`
		- The path can be also relative `"../utils/hex.gd"` `"./subitem.gd"`
		- In other scripts: `var MyClass = preload("res://path/to/myclass")`
		- Or you can load on demand: `var MyClass = load("res://path/to/myclass")`, but its recommended to use ExtensionLoader
	- Named class, if specified:
		- The line `class_name Myclass` to the script (top line, usually for clarity)
		- The name will be available globally to other scripts
		- Class names cannot be namespaced so be conservative on what you name as a class (damn Resource)
	- Inheritance:
		- Add the line `extends OtherClass` to specify the base class in the hierarchy
		- Usually the superclass is a standard Node type or resource type
		- You can use filepath for unnamed `extends "res://path/to/superclass"`
		- Do not mess tree hierarchy (composition), with class hierarchy (inheritance)
		- Multiple inheritance not allowed!! Party!!
	- Variables (var) and constants (const)
		- `var name: type = initialvalue` <- Static type variable
		- `var name` <- Uninitialized vars point to `null` (Python `None`)
		- `var name = initialvalue` <- Dynamic type variable
		- `var name := value` - Static type variable, but type implied by the value type
		- `const name: type = value` <- Constant
		- Unlike Python, type binding is enforced in compilation and run time
		- Dubt: Dynamic typing is just defaulting Static typing with Variant type??
		- Editable member: 
		- Properties (top level variables) decorated by `@export` will be available to the editor (also seralized)
	- Functions, just like python but `def` -> `func`, indented blocks...
		- Parameters and return value can be dynamically or statically binded.
		- Returning a type binded value: `func f() -> int: `
		- Type binding parameter: `f(param: int)`
		- Optional parameters with default: `f(param = 100):`
		- Combining both:  `func f(param: int = 100):`
		- Or implied: `func f(param := 100):`
		- You cannot use Python keyword parameter binding in calls :-(
	- Godot editor integration:
		- Editable properties
			- By default, properties (top level `var`) are not available in the editor to edit
			- Prepend the declaration with `@export`
			- Types helps to better edit the object
			- If no type specified, Variant will be used (user can select any type among available for the editor)
			- Normally you don't want that but often (dictionaries) you have no option to type inner types
		- Class icon: `@icon("res://path/to/myclass.svg")`
			- Helps to identify better the nodes in the tree, and in the node type selector
			- By default, takes superclass icon
	- Inner classes
		- Defined like in Python but using `extends` instead of parenthesis
		- `class MyInnerClass extends InnerSuperClass:`

- Basic datatypes: int, float, bool, String, dict, Array, Array[T], Null
	- note that list and tuple -> Array
	- Custom Types: Vector2, Vector3, Color, Angle...
	- accessing members:
		- inherited and own members can be accessed as local variables
			- but you can explicitly use `self.` (ie. when scoped out)
			- when overriden you can use parent class member with `super.`
	- By default unnamed, referenced by filename to others
	- You can name them with 
		
	- `extends MyParentNode` defines inherintance
	- builtin methods, starting with `_`
		- `_ready`: run when node added to a tree
		- `_process(delta)`: run every tick, delta is floating point seconds since last tick
	- Referenced as `res://path/from/root/mynode.`
- Getting other nodes from the tree:
	- `get_node("../scene/path")`
	- `$../scene/path`
	- `%UniqueNodeName` (You have to activate that for the node)
	- `get_parent()` or `$".."`
	- `add_sibbling(newSib)`
	- `add_child(newKid)`
- Debugging
	- We can use `print` function
- Intanciating a class
	- 

## Scripts

GD Scripts work like classes.

- Variables `var` and constants `const` are attributes of the class
- Functions `func` are methods of the class
- Adding a script is subclassing the type you selected for the node
- You specify the base class at the top with `extends BaseClass`
- Any `var`, you prefix with `@export` will be shown on the inspector and can be modified from outside.
- You can also declare a `signal` you can emit at the class root, just name it `signal mysignalHappened`
- Members (inherited or not)  are accessible without `this.` but you can explicitly use `this.member` if the name is shadowed by a local variable.
- Chldren nodes can be accessed by prepending `$` to their name
- Node types and types can be accessed by name (`Vector2D`, `Input`, `CollisionObject2D`...), no import required (also means, names must be unique)
- Built-in methods starts with `_`

### Typed variables

If not specified, variables are untyped.
You can enforce a type for a variable like:

Unlike Python, type declaration are enforced if defined.
In compile time and in run-time.

Values can be casted to a type with the `myvalue as MyType` expresion

TODO: Implications on conversions, reinterpretations...?
Object of class can be casted as the subclass

TODO: checked in runtime?


## Collisions

Collisions are segmented by physics layers
so that each layer can be checked for collisions separatelly.

`CollisionObject2D` base class has those attributes:

- Layer: The layers where the object can be detected by others
- Mask: The layers that the object will scan for collisions with others
- Priority: The order in which the object will be notified. Useful to avoid race conditions.

`RigidSolid2D`, besides physics of rigid solids, also defines signals like:

- `body_entered/exited(body: Node)`


## Tilesets

Tilesets are tile based maps 

Atlas: Definicion de los elementos individuales que hay en una imagen multi sprite.







## Input and actions

- Action: Interaction event that can be bound to device actions (mouse, joystick, keyboard...)
	- Actions are semantic: 'fire', 'left'...
		- Godot defines a convenient set of default actions
		- Game designers can define their own actions and default bindings
		- Althought actions may specify their default bindings, users can configure them
	- `if Input.action_pressed('myaction'): ...`
	- Direction actions can conveniently use `Input.get_vector('left', 'right', 'up', 'down')` to add it to the position

## Signals

- Signal are events that may trigger function execution on other objects
- They are a low coupling call mechanism
	- Mainly to decouple emitter and receiver
	- Warning, too many low coupling might lead to hard to trace code
	- If you know the receiver do not use signals
- Ex. Timer nodes have a signal `timeout` you can bind to a method of your node when it expires.
- In the editor, slots are marked with a green icon

## Physics

- Area2D: Can be checked on whether another body enters (changes position, orientation...)
	- Signal: `on_area2d_entered`
	- Signal: `on_area2d_entered`
- CollitionBody3D:
	- Defines a list of CollitionPolygon or PolygonShape to check collisions
	- StaticBody2D: A moveable body that other bodies collides with (static)
	- RigidBody2D: Moving body that moves according phisics (projectils...)
	- CharacterBody2D: Moves controlled by code (players, enemies...)
		- attribute velocity (Vector2D)
		- `move_and_slide()` Updates position accordint to velocity avoiding getting into static body areas by slipping on the border
		- `move_and_collide()` 

## Shaders

[Original Geometry]  -> Vertext Shaders -> [Modified Geometry] -> Rasterization ->  [Fragments] -> Fragment Shader -> [Final output]


- Fragments are not called Pixels because they have lots of more information:
	- Color
	- Screen location
	- UV coordinates
	- Normals
	- Light information
	- ....

In Godot, we can use either a shader node editor (`VisualShader`) or shader code (`Shader`).

Create a resource, choose either `Shader` or `VisualShader`, drag the file as material of the target object.

For VisualShader, a node editor will open with an output node.
Input nodes have to be added by hand.
Change the shader type (vertex, fragment...) with the dropdown selector.

## Coroutines: await, yield

```gdscript
func myregularfunciton():
	print("before")
	mycorutine()
	print("after")

func mycorutine():
	print("entering")
	await get_tree().create_timer(1.0).timeout # timeout is a signal
	print("exiting")
# Outputs before-entering-after-exiting
```
`await` returns to the caller, the corutine is remumed once the signal is emited

La funcion `yield()` (sin parametros) en cambio permite al llamador de la corutina
controlar cuando continua ejecutandose.

```gdscript
func myregularfunciton():
	print("before")
	y = mycorutine()
	print("after", )
	y.resume("value for yield")

func mycorutine():
	print("entering")
	value = yield()
	print("received", value)

# Outputs before-entering-after-exiting
```






## PackedScene

https://gamedevacademy.org/packedscene-in-godot-complete-guide/

A PackedScene is a tree of nodes stored as a file with extension `.tscn`
(for "text-based scene", you can also use binaries) 

```gdscript
var subscene_pack = load("res://scenes/my_subscene.tscn") # could be any path in the project
var subscene = subscene_pack.instance()
subscene.attribute = "value # Changing original attributes if needed
get_node("/root/Main").add_child(enemy_instance)
```

For scenes that are loaded often in the game is better to use `preload`
Why? How?

Doubt: for later instances is duplicate() faster than instantiate()?


## Node catalog

### 2D Nodes

https://www.youtube.com/watch?v=22VYNOtrcgM

- Node2D: Base of every 2D Node
	- Inherits CanvasItem and thus, Node
	- rotation, position, scale, skew
- Camera2D: Specify which part of the world is viewed
	- Inherits Node2D
	- Offset, Anchor, Limits
	- Smoothing, Drag: Easy view changes
- (Animated)Sprite2D: Render 2D texture to the screen
	- Supports sheeting (images with many sprites)
	- Animated adds sequences of sprites you can switch between
- CollisionObject2D: Base for all objects with collisions
	- Layer, Mask, Prioriry
- PhisicsBody2D: Base for all objects affected by physics
	- Inherit CollisionObject2D
- CollisionShape: 
	- Inherit CollitionBody3D
- StaticBody2D:
	- OBject that can not be moved but collides with other objects
- AnimatableBody2D:
- RigidBody2D: Moves but does not have initiative
- CharacterBody2D: Controled by player
- Joint2D: Base for joining 2 objects together
	- DampedSpringJoint2D: Elastic joint
	- GrooveJoint2D: Move in a direction like a rail (length, initial offset)
	- PinJoint2D: Join with point
- Area2D: Can be use to collision or to set specific physics
- AudioListener2D: sets the listener location for the audio
- AudioStreamPlayer2D: Source of sound
- GPUParticle2D: Emits cheap objects affected by phisics (particles)
	- Properties to configure how they move and are affected by gravity
- TileMap: Tiles
- CanvasModulate: 2D shadows color removed by light
- Light2D: Base for all Lights
	- color, energy, blendmode
	- PointLight2D: texture, 
	- DirectionalLight2D: sun like light
	- LightOcluder2D: Shape that ocludes light
- Line2D: Polyline with vectorial properties
- Marker2D: Debug helper 
- MeshInstance2D: Render a 3D mesh in a 2D scene
- MultiMeshInstance2D: Optimally (GPU) rendered replicated objects
- Navigation Nodes: Used to resolve automated movement and path finding
	- NavigationRegion2D: Defines the allowed navigation
	- NavigationLink2D: 
	- NavigationObstacle2d: Defines a forbiden region
- ParallaxBackground: root of a set of ParallaxLayer
	- Needs either a Camera2D or setting the scrolloffset of each layer by hand
- ParallaxLayer: Background image that moves slower than the camera to gave a 3D feeling
- Path2D: Defines a point path to be follow by other node
- PathFollow2D: A node that change position according to a Path2D controlling the progressRatio
- Polygon2D: Draws filled polygon
- RayCast2D: Computes collision points in a direction from a point
- ShapeCast2D: Computes collisions on shapes projected over a direcction
- RemoteTransform2D: Applies its own transform to a different node not in the hierarchy
- Skeleton2D, PhysicalBone2D, Bone2D: Used to build hierchical animations
- visibility
	- VisibleOnScreenModifier2D: Sends signals when item changes it visibility
	- VisibleOnScreenEnabler2D: Enables itself (and children) when visible
- CanvasGroup: renders children once
- BackbufferCopy: Copy a region as texture for the shaders to use it

### 3D nodes



- Node3D: Positionable, scalable, rotable object
- Marker3D: Helper to visualize a node postion and orientation
- VisualInstance3D: Base for all nodes that can be seen, add layering and bounding boxes
- GeometryInstance3D: Base for all nodes with material properties: lightning, shadowing...
- MeshInstance3D: Godot bultin or loaded mesh files
- MultiMeshInstance3D: Optimally repeated geometry
- Label3d: Text in 3D, can be or not camera facing
- Decal: Projects a texture into a geometry
- Sprite3D/AnimatedSprite3D: Plane with a texture applied
- WorldEnvironment: Sets the lightning of the world
- FogVolumen: Sets a volumen of fog
- GPUParticles3d: Genera partículas
- GPUParticlesAttractor3D: Attracts or repulses particles
- GPUParticlesCollision3D: Collides particles  
- Light3D: Base for lights strength, color, project shadow...
	- OmniLight3D: omnidirectional light
	- SpotLight3D: focused light
	- DirectionalLight3D: celestial light, just direction
- CSGShape3D: Base for shapes that can do boolean operations
- SoftBody3D: Emulates physics of textiles, inherits MeshInstance3D, adds attachment points, colliders to affect on...
- CollisionObject3D: layers what object can collide, childs can be:
	- CollisionShape3D: Thickened Shape
	- CollitionPolygon3D: Thickened Polygon
	- PhysicsBody3D: Base. Holds any dimensional and rotational locking
		- StaticBody3D: material, velocity, spin, but static because it is unaffected by others collisions (walls, floor...)
			- AnimatableBody3D: it can push or pull other object but unaffected by others
		- RigidBody3D: Mass, inertia, bouncing...
	- CharacterBody3D: User controlled
- Area3D: Collision detection and change physical properties within
- Camera3D:
- VehicleNode3D/VehicleWheel3d: Emulates vehicle physics
- Joint3D: Base to join 2 objects, you add it as a sibbling and configure it with the objects
	- HingeJoint3D: rotation around an axis (bisagra) limits, lubricació...
	- ConeTwistJoint3D: Rotula limitada a cierto cono
	- SliderJoint3D: piston like movement
	- PinJoint3D: single point of contact
	- Generic6DOFJoint3D: Full generalization for complex joints. Angular/Linear limits/springs/motors for xyz
- Skeleton3D: Normally imported from blender (skeletons and skeletons animations)
- BoneAttachment3D: To bind extra elements to a bone
- RootBoneAnimation3D: surface that acts as root (floor) for the animation




	
	










### UI Nodes

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



