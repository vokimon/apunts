# Godot 4 (Game Engine)

<https://www.youtube.com/watch?v=nAh_Kx5Zh5Q>

## The node tree

- Game: Is composed by a tree of nodes.
- Node: Any element of the game is a Node in a tree. Shape, skeleton, 2D/3DNodes, Sprites, Timer...
- Properties: Nodes have named values which depend of the node type
- Inheritance: Type of nodes are subtypes of other types
	- Properties can be inherited
	- Default properties values can be set differently
	- They can extend with new properties
	- You can add childs
- Tree structure:
	- Modifications on the parent (scaling, rotating, positioning, skew, groups...) affect their children
	- Siblings order affects to the drawing order
- Scene: Node that organizes other nodes and display them
	- Current scene is the scene currently displayed
	- Scenes are also reusable groups of nodes
	- You can convert a subtree of nodes into its own scene
	- You can insert a scene inside another scene
	- Scenes are stored as .tscn files
- Some useful node types:
	- Node2D: A 2D point bearing 2D transformations to its children
	- Sprite2D: An 2D image (also a Node2d)


## Scripting

- Scripts are bound to nodes.
- Scripts can be done in several languages
	- C, C++, GDScript (similar to python)
	- `.gd` files, same name than node
- Basic datatypes: int, float, bool, String, dict, Array[T]
	- note that list and tuple -> Array
	- Custom Types: Array2, Array3, Color, Angle...
- Variables (var) and constants (const)
	- `var name: type = initialvalue` <- Static type variable
	- `var name = initialvalue` <- Dinamic type variable
	- `const name: type = value` <- Constant
- Functions, just like python but `def` -> `func`, indented blocks...
	- You can type bind parameters like variables
- Classes: Nodes
	- a single file
	- top level functions are methods
	- top level variables are attributes/properties
		- `@export` prefix on a property shows it as editable property
		- properties (own and inherited) can be accessed with or without `self.`
	- `extends MyParentNode` defines inherintance
	- builtin methods, starting with `_`
		- `_ready`: run when node added to a tree
		- `_process(delta)`: run every tick, delta is floating point seconds since last tick
	- Referenced as `res://path/from/root/mynode.`
- Getting other nodes:
	- `get_node("../scene/path")`
	- `$../scene/path`
	- `%UniqueNodeName` (You have to activate that for the node)
	- `get_parent()` or `$".."`
	- `add_sibbling(newSib)`
	- `add_child(newKid)`
- Debugging
	- We can use `print` function

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



## 2D Nodes

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

