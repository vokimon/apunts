# Godot 4 (Game Engine)

::: link https://www.youtube.com/watch?v=nAh_Kx5Zh5Q
	The ultimate introduction to Godot 4
	
	Develops 

::: link https://www.youtube.com/watch?v=9LaB6wbZepg&list=PLJ690cxlZTgL4i3sjTPRQTyrJ5TTkYJ2_&index=0
	Playlist GDScript from scratch. From very scratch, even programming concepts,
	but explains some of the differences

## Interesting videos

- Interesting plugin SmartShape2D and usage: https://www.youtube.com/watch?v=r-pd2yuNPvA
- Character creation Blender + Godot: https://www.youtube.com/watch?v=dd6G2S6MQ6U
- Depth based outline with gdshaders that work in compatible mode: https://www.youtube.com/watch?v=-SXJvpbFJ7M

## Extracted topics

- [Tiling](tiling.md)

## The node tree

- Node: Any element of the game is a Node in a tree. Shape, skeleton, 2D/3DNodes, Sprites, Timer...
- Node Type: Each node has a type which defines its behavior and and the set of properties it has.
- Properties: Named values whose values can be set differently for each node.
- Inheritance: A type of node can inherit from other type
	- Properties are inherited
	- Default properties values can be set differently
	- They can extend with new properties
	- You can add/modify childs
- Node composition (Composition hierarchy != Inheritance hierarchy):
	- Modifications on the parent (scaling, rotating, positioning, skew, groups...) affect their children
	- Siblings order has effects on the drawing order
- Scene: Tree of composed nodes with a single root
	- Whatever you display in godot has to be a scene
	- You can also nest scenes inside others to compose complex scenes
		- Make a set of nodes a scene for reuse and encapsulation
	- Useful operations:
		- Import a scene inside another
		- Extract a subtree as independent scene
	- Scenes are stored as .tscn files
- Root node types:
	- Node2D: 2D scene to organize objects in a 2D canvas
	- UI: Control node (a Node2D it self) but organizes controls in layouts
	- Node3D: 3D scene to organice object in a 3D world
- Some useful node types:
	- Node2D: A 2D point bearing 2D transformations to its children
	- Sprite2D: An 2D image (also a Node2d)
- A node can be bound to a script
	- Normally you bound to a type (which has its own behaviour)
	- When you bind a script you are defining a new type by extending the asigned one

## Scripting (GDScript) for Pythoners

### Languages in Godot

- Scripts in Godot may be written in several languages
	- Godot provides a C interface for any language to interact with
- Indeed you can use that interface to write extensions directly in C++ or C
	- [C](https://docs.godotengine.org/en/3.5/tutorials/scripting/gdnative/gdnative_c_example.html)
	  [C++](https://docs.godotengine.org/en/3.5/tutorials/scripting/gdnative/gdnative_cpp_example.html)
	  But there is no Editor integration AFAIK so they are used mostly to write native extensions later integrated into a project
- Officially suported languages: GDScript (own) and C#
- C#
	- Welcome path to developers coming from widely used game engines like Unity and Unreal
	- Also because M$ donates to the port
	- Problems with Garbage Collector
- GDScript is similar to Python (yahoo) but it has many differences (oops)
	- Unlike Python, no Global Thread Lock!! You have real Multithreading!
	- Like Python: Ref counted object instead Garbage Collection
	- Instead quack typing, uses **gradual typing**: Some variables are statically typed others dynamically typed
- [Many others](https://github.com/Vivraan/godot-lang-support) comunity driven
	- [godot-python](https://github.com/touilleMan/godot-python)
		- Currently (2023-01) rewritting it for Godot 4
		- Unmature: Even in Godot 3, limitations and flaws
- So, the recommended path for pythoners is to use GDScript
- False friends: Whenever you jump across two "similar" languanges you start fast but end getting stuck in your falses expentances
	- ie. Javascript coming from C about var scoping, casting...

### GDScript (vs Python)

- Every script defines a class
	- Most tutorials i saw avoid explaining this up front
		- they consider classes are an advanced topic for non-programmers
		- you have them in the first page, so you have to deal with them
		- you come from Python, so, come on
- Any function, variable, constant... defined at the top level of the script will be class members (methods and properties)
	- Unlike Python you don't need to specify `class MyClass:` and have all members indented inside
	- Indeed if you do, you will be defining what in Python is an inner class (see below)
- Classes are by default unnamed, they are refered by their script path
	- `const MyClass = preload("./path/to/myscript.gd")`
	- You could explicitly name them adding this clause: `class_name MyClass`
	- Then the symbol is globally accessible
	- But there are no namespaces so explicit names crowds the global scope
	- TOCHECK: Why autoload modules? Has the modules be loaded by any other to be available? -> They make an instance not a class globally available
	- Still, `preload` is not that far from import clauses in other languages (javascript)
- Inheritance:
	- Add the line `extends OtherClass` to specify the base class in the hierarchy
		- This is done from the editor, you can change the default superclass from the dialog
	- Usually the superclass is a standard Node type or resource type
	- You can use filepath for unnamed `extends "res://path/to/superclass"`
	- Tree/scene hierarchy (composition) vs. class hierarchy (inheritance)
	- By default, `extends RefCounted`, not `Object` like in Python.
	- Multiple inheritance not allowed!! Party!! Use composition!
- Variables (var) and constants (const)
	- Unlike Python you have to declare variables
	- Top level are class attributes, inside a function they are locals
	- `var name: type = initialvalue` <- Static type variable
	- `var name` <- Uninitialized vars point to `null` (Python `None`)
	- `var name = initialvalue` <- Dynamic type variable
	- `var name := value` - Static type variable, but type implied by the value type
	- `const name: type = value` <- Constant
	- Unlike Python, type binding is enforced in compilation and run time
	- Dubt: Dynamic typing is just defaulting Static typing with Variant type??
- Functions, just like python but `def` -> `func`, indented blocks...
	- Parameters and return value can be dynamically or statically binded.
	- Returning a type binded value: `func f() -> int: `
	- Type binding parameter: `f(param: int)`
	- Optional parameters with default: `f(param = 100):`
	- Combining both:  `func f(param: int = 100):`
	- Or implied: `func f(param := 100):`
	- You cannot use Python keyword parameter binding in calls :-(
	- A method can refer attributes and other methods (own or inherited) 
	- Methods can use attribute or other methods directly (no need to prepend `self.`)
- Refering script classes:
	- Script classes are unamed by default
		- Referred by the path to the script:
			- Absolute: `"res://path/to/myclass.gd"`
			- Relative `"../utils/hex.gd"` or `"./subitem.gd"`
		- In other scripts: `const MyClass = preload("res://path/to/my_class.gd")`
		- On demand: `var MyClass = ResourceLoader.load('./my_class.gd')`
			- When you want to control in memory resources
			- Global `load` function but this does not work as expected: `var MyClass = load("res://path/to/myclass")` Use `ResourceLoader`. Why?
	- Named class, if specified:
		- The line `class_name Myclass` to the script (top line, usually for clarity)
		- The name will be available globally to other scripts
		- Use it carefully, it polutes the global scope (no namespaces in GDScript)
	
- Godot editor integration:
	- Editable properties
		- By default, properties (top level `var`) are not available in the editor to edit
		- Prepend the declaration with `@export`
		- Types helps to better edit the object
		- If no type specified, Variant will be used (user can select any type among available for the editor)
		- Normally you don't want that but often (dictionaries) you have no option to type inner types
		- `@export_*` variations to specify how to edit the attribute
	- Class icon: `@icon("res://path/to/myclass.svg")`
		- Helps to identify better the nodes in the tree, and in the node type selector
		- By default, takes superclass icon
	- `@onready`: Prefixed to a var to delay its initialization from `_init` to `_ready`
	- `@rpc`: Prefixed to a func enables it for remote call (multiplayer)
	- `@static_unload`: to a script deinstantiate its variables as soon as all reference are removed, instantiates again if a new reference appear.
	- `@tool`: to a script to make it run by the editor
- Instanciating:
	- `var myinstance: MyClass = MyClass.new(params)`
	- `var myinstance := MyClass.new(params)` ?? Is this working?
- Overrides
	- Godot overridable functions have a prefixed `_`
	- TOSOLVE: Is this a godot only thing or a GDScript thing
	- Call same function from parent with `super(params)`
	- Unlike Python, super() is not the receiver object but the overriden function itself
	- Call other function from parent when overriden with `super.otherfunction(params)`
- Inner classes
	- Defined like in Python but using `extends` instead of parenthesis
	- `class MyInnerClass extends InnerSuperClass:`
	- Referring from other classes if unnamed: `extends "./script.gd".MyInnerClass`
- Dynamic type checking:
	- `myvar is MyClass` checks is instance (same class or subclass)
	- warning: `typeof(x)`, just says it is a `TYPE_OBJECT`, not the class
- Basic datatypes: int, float, bool, String, dict, Array, Array[T], Null
	- note that list and tuple -> Array
	- Custom Types: Vector2, Vector3, Color, Angle...
- accessing members:
	- inherited and own members can be accessed as local variables
		- but you can explicitly use `self.` (ie. when scoped out)
		- when overriden you can use parent class member with `super.`
	- builtin methods, starting with `_`
		- `_init`: Constructor
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

### Lifecycle

- `_init` called from root to leaves order within the tree
- `_ready` called from leaves to root within the tree (your children should be available)

Recursive hollywood calls:

- parent first: `_init`, `_process`, `_draw`...
- child first: `_ready` (when we run `_ready`, children already are ready)
- inverse (of parent first): `_input`, `_exit_tree`


### Encapsulating attributes

- define accessors to be used when accessing attributes
- keeps syntax nice for class users

```gdscript
var my_mar := 100:
	set(value):
		do whatever with value
	get:
		return the value
var other_var setget mysetter, mygetter # both are functions in class
var other_var setget mysetter # both are functions in class
```
- Pitfall: they won't be used from class code!!
	- They require the dot notations to activate `my_attribute = 100` won't trigger accessor
	- You must use `self.my_attribute = 100` for that
	- This enables the class access to the inner representation so it can be used for encapsulation

## Scripts

GD Scripts work like classes.

- Variables `var` and constants `const` are attributes of the class
- Functions `func` are methods of the class
- Adding a script is subclassing the type you selected for the node
- You specify the base class at the top with `extends BaseClass`
- Any `var`, you prefix with `@export` will be shown on the inspector and can be modified from outside.
- You can also declare a `signal` you can emit at the class root, just name it `signal mysignalHappened`
- Members (inherited or not)  are accessible without `self.` but you can explicitly use `self.member` if the name is shadowed by a local variable.
- Children nodes can be accessed by prepending `$` to their name
- Node types and types can be accessed by name (`Vector2D`, `Input`, `CollisionObject2D`...), no import required (also means, names must be unique)
- Also scripts with `classname MyClass` directive will be available by name
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
	- RigidBody2D: Moving body that moves according physics (projectils...)
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

Note: `yield` is Godot 3.x. Deprecated in Godot 4.x

Doubt: how to map yield functionality to await?

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

Instantiating PackedScene returns the root node.

Pitfall: When you add a script to the root node of a scene, you are creating a class.
When instanciating that class with `new()` the node will be created but the children in the scene won't.
How to encapsulate a bunch of nodes in an abstract class?

- Creating the children programmatically
- ??? 

Doubt: for later instances is duplicate() faster than instantiate()?


## Texturas

- Texture2D
	- GradientTexture2D: Values are obtained from a gradient
	- GradientTexture1D: Like 2D one but only provides variation in one coordinate
	- NoiseTexture2D: Values are obtained from a noise generator (See Noise)
	- ImageTexture: Values are taken from an Image
	- MeshTexture: Still an image but aplies to meshes?? https://gamedevacademy.org/meshtexture-in-godot-complete-guide/
	- PortableCompressedTexture2D
	- CompressedTexture2D: loaded from a ctex file
	- CanvasTexture: Physical properties (difuse, specular, normal...) for 2D objects (CanvasItem) with Light2D (Use Materials for 3D)
		- Should be a Material2D since it has several Textures inside
		- `difusse_texture`, `normal_texture`, `specular_texture`. Specular and Diffuse have color. 
	- ViewPortTexture: Sets a ViewPort as the source of dynamic data for the texture
	- CameraTexture: Maps image from a camera (not godot camera, but a physical camera device)
	- CurveTexture: Curve stored as a 1D sequence of data (A sampled 1D function)
	- CurveTextureXYZ: Like CurveTexture but uses each channel for a different curve
	- AtlasTexture: Texture cuted from another Texture2D (its atlas) by defining a region and a margin.
		- Reusing the same atlas for different textures optimizes video memory
	- AnimatedTexture: Deprecated
- TextureLayered: N layers of textures of the same size
	- CubeMap: Environment mapping for reflections each layer for a side of an covering cube. See ReflectionProbe
	- CubeMapArray: CubeMaps packed in a single texture for faster GPU upload and caching
	- Texture2DArray: Array of independent textures of same size and mipmap for GPU upload and caching efficiency
- Texture3D: Line N layers but enables interpolation between layers
	- CompressedTexture3D, ImageTexture3D, NoiseTexture3D, PlaceholderTexture3D, Texture3DRD
- GLFTTexture: Texture from standard file format (represents the object, not the texture you may use) (usually written glFT) for physics based shading
- PlaceholderTextureXXX: No textures (Error or no need in a client server environ)

## Physics

### CollisionBody2D/3D (Volume)

Defines a volume as being ocuppied by the object.

Holds Shape3D (Resources) as children that will determine its volume for collisions.

- Shape holders:
- Shapes:

Collision detection is splitted on layers. One object can define:

- Collision Layers: Layers where other objects can find this object
- Collision Mask: Layers the objects looks for collisions with other objects

Having a volume:

- They can receive input events from cameras (`_input(camera, event, normal, shape_idx)`).
- They receive `mouse_enter/exit()`
- They emit homonimal signals without the `_`


### RigidBody2D/3D (Dynamics)

https://www.youtube.com/watch?v=XSFkAzXQSWE

A RigidBody3D is not controled by the kinetics but by the dynamics.
Kinetics describe an scene by setting the initial position and orientations,
and giving a set of velocities and angular velociites, computes the new positions and orientations.
Dynamics considers forces (including gravity) and torques
and given initial position, orientation, velocities and angular velocites
derives the evolution.

Because the physics engine computes them,
setting `position`, `rotation`, `global_position`, `liniar_velocity` and `angular_velocity`
has only sense for the initial conditions.
**Beyond that any write we do will be overriden by the physics engine.**

The controlling parameters are:

- mass (kg)
- gravity (factor to the project one in m/s²)
- inertia (Vector3(kg)) how hard it is to make it spin in each direction (if zero computed from mass and shape)
- `constant_force`
- `constant_torque`
- `linear_velocity` (Vector3(m/s))
- `linear_damp` (units) object -> Area3D -> project, if zero
- `linear_damp_mode` Combine (add the value to the others), Replace set to that.
- `angular_velocity` (Vector3(m/s))
- `angular_damp` (units) object -> Area3D -> project, if zero
- `angular_damp_mode` Combine (add the value to the others), Replace set to that.

But those are computed values.
To affect the body we should call:

- Major drivers: attributes `constant_force` (liniar) and `constant_torque` (angular)
	- `force` are proportional to the volume (radious size) of the object. `F = m.a = ð * r^3 * a`
	- `torque` are proportional to the fourth power of the size. `ŧ = r F = ð * r^4 * a`, perpendicular to the plane of rotation, right hand rule
- Physics engine uses:
	- `constant_force/torque` to update velocities (linear/angular) (with damp and gravity)
	- velocities to update position/rotation
	- also collisions have effect
- You can set them directly or alter them with `add_constant_central_force(V3)` and `add_constant_torque(V3)`.
- Also `add_constant_force(force: V3, pos: V3)` may generate both for force and torque if not applied to the center of mass.
	- Why? Forces not applied to the center of mass (not central) generate torque
	- Be aware of the messing names:
		- `constant_force` updated by `add_constant_central_force` while `add_constant_force`, updates both `constant_force` and `constant_torque`
- For one time impacts, use the impulse versions. Impulse is the integral over time of force.
	- `apply_impulse(inpulse: V3, pos: V3)` torque + force
	- `apply_torque_impulse(inpulse: V3)` just torque
	- `apply_central_impulse(inpulse: V3)` just force
	- The effects will be applied instantly to the velocities, won't modify `constant_X` to be applied on next physics frames.
- When to use `apply_torque`, `apply_central_force` and `apply_force`?
	- When you want to have fine tunning of the forces applied every physics frame and implementing `_integrate_forces`
	- They alter velocities the equivalent of applying those forces during a physics frame
	- This is too small, and if you do it in `_process` inconsistent and 

**Freezing:**
A rigid solid can be frozen.
Depending on the `freeze_mode`, during the freeze, the rigid body behaves like a static or a kinematic.

**Sleeping:**
Whenever a rigid is not moving, if `can_sleep` is set to true (the default),
the `sleeping` flag is set and it is exclude from physics engine
until a collision or a programatic `apply_force`/`apply_impulse`

- Doubt: Effect of parent transformation in mass/inertia.
- Doubt: How damp affects to the forces, velocities...


## Debugging

- `push_error/warning()`: enables a stacktrace besides the error message
- When in run, the running scene tree is availabe as 'Remote' tab in the scenen tree docker.
	- You can fix it as the default shown in project settings.
- "Always on top" option is good to keey the game in front and still being able to manipulate and inspect the editor interface.




## Node catalog

### General purpose

- AnimationPlayer: Stores a set of animation definitions you can play by name. Animations can define a time line for properties, function calls...
- AnimationTree:
	- https://www.youtube.com/watch?v=KAZX4qfD06E
	- Requires a sibbling AnimationPlayer which is related by property
	- Animation root is the root of the tree. Usually


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
- GPUParticle2D: Emits cheap objects affected by physics (particles)
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



### 3D escenes

Even though you can use any dimensions you want and fine tune,
the physics engine is tuned to use SI Units,
mostly Meter, Kilogram, Second, Radians and derived units.
So, its better if you use the model scaled to that in world units.



	










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

## Snippets

Reacting to window resizes: `get_tree().get_root().size_changed.connect(on_resize)`
Better? would takes the viewport, not the window viewport:  `get_viewport().size_changed.connect(on_resize)`


## Model formats

- glTF
	- Mantenido por Khronos
	- Directorio del ecosistema: https://github.com/KhronosGroup/glTF#gltf-tools
	- Contenido json (Text Format)
		- .bin:
			- Geometry:Vertices, Indices...
			- Animation: Keyframes
			- Skins: Inverse bind matrices
		- .glsl: Shaders
		- .png/.jpg/...: Textures
- FBX 
	- Comun para escenarios y modelos con esqueletos y animacions
	- Las texturas van en ficheros locales
	- En Godot 2 se usaba la herramienta FBX2glTF
	- En Godot>3.2 hay importacion nativa

- DAE Digital Asset Exchange .dae
	- Propiedad AutoDesk, soporte de Khronos
	- COLLADA (COLLAborative Design Activity) XML schema
	- https://en.wikipedia.org/wiki/COLLADA


## Extensiones recomendadas

- Globalize Plugins: Install plugins to all projects
- DRY
	- Basic FPS player: Dont reinvent the wheel
	- Phantom camera: Camara con targets, movimientos con easing, evita obstaculos... (2D y 3D)
	- Scene Manager: Transiciones entre escenas
	- Delta Rollback: Saves game
	- BulletUpHell: gestiona proyectiles masivos
- Asset editors/generators
	- Cyclops: Editor de escenarios 3D al estilo del de Quake
	- Dialogic: Creador de un sistema de dialogos. Logica
	- CGS Toolbox: Modelado CGS visual
	- Smartshape 2D: Definir volumenes en vez de tile a tile, formas no cuadriculadas...
	- Gaia: Procedural generation
	- Hoodie: Procedural geometries
- Smart Agents:
	- RL Agents: Entrenador de IA's para bots.
	- LimboAI
- Dev tools
	- ScripIDE: IDe mejor
	- Signal visualizer: Muestra las connexiones de signals como graph editable, tambe fa log
	- Runtime Debug tools: Free cameras, wireframe mode, runtime object selector...
	- Litle Camera preview: muestra lo que ve la camara en modo edicion
	- Block Coding: Similar a un Scratch para Godot
	- Tracy Profiler: Graphical profiler
	- EmbedGame: Permite Ver el juego ejecutandose en el IDE
	- Orchestrator: Visual modular programing
- Fisicas
	- Jolt Physics: Motor de fisica 3D mas potente y optimizado que el de serie
	- Box 23: Motor de física 2d
	- Water way: Para generar y simular rios y aguas corrientes en 3D.
	- OceanWaves: Simulates ocean waves
	- DistanceJoin2D: Rigid join to keep two object at a distance without elasticity
	- SmashTheMesh: rompe objetos 3d
	- Shaker: Emula sacudidas y temblores en los objetos 3d
	- SoftBody2D: Emula cuerpos blandos (deforma, flexiona, parte...) tambien en 2D
	- Concave Mesh slicer: Permite partir objectos con un plano

## Asset repositories

- https://syntystore.com/ by [Synty Studios](https://www.syntystudios.com/)
	- Propietario, de pago
	- Low poly assets for realtime
	- Single payment for "small studio"
- https://www.fab.com  (Old Sketchfab)
	- Colaborativo (usuarios suben modelos y ponen precio o no)













