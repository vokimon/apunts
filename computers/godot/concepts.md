# Godot Introduction (for Pythoners)

This is a compilation of the concepts I needed to organize
in my mind to start developing in Godot.
It could be as useful to you as you share background with me:
mostly OOP and Python.

So what follows are the organized notes i took while
watching, first, this tutorial, and, then, the documentation
and some other complementary videos i will quote.

::: linkcard https://www.youtube.com/watch?v=nAh_Kx5Zh5Q
	The ultimate introduction to Godot 4

## The node tree

- Node: Any element in the game is a Node in a tree.
	- Meshes, skeletons, 2D/3D transforms, sprites, timers...
- Scene: Tree of composed nodes with a single root
	- Whatever you display in godot has to be a scene
	- You can also nest scenes inside others to compose complex scenes
		- Why: reuse and encapsulation
	- Useful operations:
		- Import a scene inside another
		- Extract a subtree as independent scene
	- Scenes are stored as .tscn files
		- Text files. Format based on .ini
		- git friendly as long as you commit frequently, many changes together won't make sense. hard to merge.
- Node Type/Class: Each node has a type which defines its behavior and and the set of properties it has.
- Properties: Named values whose values can be set differently for each node.
	- Set of properties: Defined for the class (name and type)
	- Values for the properties different for every instance of the class
	- Example: A Node2D will have properties for translation/rotation... while a sprite3d will have the image resource as property
- Inheritance: A type of node can inherit from other type
	- Properties are inherited
	- Default properties values can be set differently
	- They can extend with new properties
	- You can add/modify childs
	- Example: A Sprite2D inherites Node2D so you can also rotate/scale/translate it.
- Node composition
	- Modifications on the parent (scaling, rotating, positioning, skew, groups...) affect their children
	- Siblings order has effects on the drawing order
	- Clarification: Component design pattern. You could add a Node property, it won't be a children by itself.
	- Clarification: Don't mess Composition hierarchy != Inheritance hierarchy
- Root node types:
	- Node2D: 2D scene to organize objects in a 2D canvas
	- CanvasItem (UI): Control node (a Node2D it self) but organizes controls in layouts
	- Node3D: 3D scene to organice object in a 3D world
- Some useful node types:
	- Node2D: A 2D point bearing 2D transformations to its children
	- Sprite2D: An 2D image (also a Node2d by inheritance)
- A node can be bound to a script
	- The script redefines the default behaviour of the node
	- When you create a node in the tree normally, you create it of a type, for instance, Sprite2D
	- Adding an script creates an (annonymous) subclass which extends the behaviour of the original one (a subclass of Sprite2D)

## Languages in Godot

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
	- [Language tutorial](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/index.html)
	- [Language reference](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html)
	- Unlike Python, no Global Thread Lock!! You have real Multithreading!
	- Like Python: Ref counted object instead Garbage Collection
	- Instead quack typing, uses **gradual typing**: Some variables are statically typed others dynamically typed
- [Many others languages](https://github.com/Vivraan/godot-lang-support) comunity driven
	- [godot-python](https://github.com/touilleMan/godot-python)
		- Currently (2023-01) rewritting it for Godot 4
		- Unmature: Even in Godot 3, limitations and flaws
- So, the recommended path for pythoners is to use GDScript
- False friends: Whenever you jump across two "similar" languanges you start fast but end getting stuck in your falses expentances
	- ie. Javascript coming from C about var scoping, casting...

## GDScript (vs Python)

- Every script defines a class
	- Most tutorials i saw avoid explaining this up front
		- they consider classes are an advanced topic for non-programmers
		- you have them from scratch, so know they are there
		- if not, all becomes weird, until you are told, and...
		- you come from Python, so, come on
	- Java nicety of everything is a class, without Java boilerplate, see
- Any function, variable, constant... defined at the top level of the script will be class members (methods and properties)
	- Unlike Python you don't need to specify `class MyClass:` and put all members indented inside
	- Indeed if you do, you will be defining what in Python would be an inner class (see below)
- Classes are by default unnamed, they are refered by their script path
	- `const MyClass = preload("./path/to/myscript.gd")`
		- `preload` is not that far from `import` clauses in other languages (javascript)
	- You could explicitly name them adding this clause at the top: `class_name MyClass`
		- Then the symbol is globally accessible
		- But there are no namespaces so explicit names crowds the global scope
		- They will also compete for names with Autoload instances (singletons available globally, instances, not classes)
- Inheritance:
	- Add the line `extends OtherClass` to specify the base class in the hierarchy
		- This is done from the editor, you can change the default superclass from the dialog
	- Usually the superclass is a standard Node type or resource type
	- You can use filepath for unnamed `extends "res://path/to/superclass"`
	- Again, dont mess Tree/scene hierarchy (composition) vs. class hierarchy (inheritance)
	- By default, `extends RefCounted`, not `Object` like in Python.
	- Multiple inheritance not allowed
		- This is a good thing, [use composition instead](https://en.wikipedia.org/wiki/Composition_over_inheritance)
- Variables (var) and constants (const)
	- Unlike Python you have to declare variables
	- Top level are class instance attributes, inside a function they are locals
	- `var name: type = initialvalue` <- Static type variable
	- `var name` <- Uninitialized vars point to `null` (Python `None`)
	- `var name = initialvalue` <- Dynamic type variable
	- `var name := value` - Static type variable, but type implied by the value type
	- `const name: type = value` <- Constant
	- Unlike Python, type binding is enforced in compilation and run time
	- Dynamic type just means typed as [Variant](https://docs.godotengine.org/en/stable/classes/class_variant.html) 
	- Any instance prepended with `@export` will be exposed as editable property in the editor
	- Other `@export_XXX` directives allow finner control on how the IDE will present them
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
	- `self` is used in some cases, see bellow, but it is not passed as method parameter
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
- Instanciating:
	- `var myinstance: MyClass = MyClass.new(params)`
	- `var myinstance := MyClass.new(params)` ?? Is this working?

- Overrides
	- Godot overridable ([hollywood](https://en.wikipedia.org/wiki/Inversion_of_control)) functions have a prefixed `_`
	- TOSOLVE: Is this a godot only thing or a GDScript thing
	- Call same function from parent with `super(params)`
	- Unlike Python, super() is not the receiver object but the overriden function itself
	- Call other function from parent when overriden with `super.otherfunction(params)`
- Dynamic type checking:
	- `myvar is MyClass` checks is instance (same class or subclass)
	- warning: `typeof(x)`, just says it is a `TYPE_OBJECT`, not the class
- Basic datatypes: int, float, bool, String, dict, Array, Array[T], Null
	- note that list and tuple -> Array
	- Custom Types: Vector2, Vector3, Color, Angle...
		- Use them: integrates better in the editor, useful methods...
- Arrays:
	- Typed array Array[T]
		`var typed_array : Array[string] = ["uno", "dos"]`
	- Untyped arrays (Equivalent to `Array[Variant]`)
		`var untyped_array : Array = ["uno", "dos"]`
	- Packed arrays: PackedXXXArray (String, Int32/64, Float32/64, Byte, Vector2/3/4) 
		`var packet_array := PacketStringArray(["uno", "dos"])`
- Dictionaries
	- `dict` like in python
	- Cannot use keyword arguments to initialize
	- Cannot use comprehension lists to initialize
	- iterate through keys, no `items()` method
	- Arrays can be typed `Array[int]`
	- Dictionary cannot, always `dict[Variant, Variant]` (python definition, as 4.3 still not valid to type it in gdscript)
	- Avoid quoted keys by using `=` instead of `:`
	- With `:` unquoted are references to variables
	- When key is string known in compile time (not a number, not a var), can be accessed with `.key`
- Getting other nodes from the tree:
	- `get_node("../scene/path")`
		- Warning: just an example, accessing parent's children couples with the context which tampers reuse
	- `$../scene/path` (equivalent shortcut)
	- `%UniqueNodeName` (You have to activate that for the node, context menu and search a %)
	- `get_parent()` or `$".."`
	- `add_sibbling(newSib)`
	- `add_child(newKid)`
	- Drag-and-dropping elements from the tree will generate $ or % references

- builtin methods, starting with `_`
	- `_init`: Constructor
	- `_ready`: run when node added to a tree
	- `_process(delta)`: run every tick, delta is floating point seconds since last tick
	- ...

## Godot editor integration:

- Editable properties
	- By default, properties (top level `var`) are not available in the editor to edit
	- Prepend the declaration with `@export`
	- Types helps to better edit the object
	- If no type specified, Variant will be used (user has to select select one of the many available types)
	- Normally you don't want that but often (dictionaries) you have no option to type inner types
	- `@export_*` variations to specify how to edit the attribute
- Organize properties
	- `@export_category('My Category')` Banner in property editor (like the ones for each super class)
	- `@export_group('My Group')/@export_subgroup("Subgroup")` Collapsable group of properties
- Class icon: `@icon("res://path/to/myclass.svg")`
	- Helps to identify better the nodes in the tree, and in the node type selector
	- By default, takes superclass icon
- `@onready`: Prefixed to a var to delay its initialization from `_init` to `_ready`
- `@rpc`: Prefixed to a func enables it for remote call (multiplayer)
- `@static_unload`: to a script deinstantiate its variables as soon as all reference are removed, instantiates again if a new reference appear.
- `@tool`: to a script to make it run by the editor
- Documentation `##` will generate documentation.
	- Above @export is shown in the hover of the property
	- Uses bbcode to format
	- 

## Formatting


## Enums

They work very different as named or unnamed!!

- Unnamed:
	- `enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}`
	- Equivalent to define constants
		- `const UNIT_NEUTRAL = 0; const UNIT_ENEMY = 1; ...`
	- Accessed `UNIT_ENEMY` or from outside `MyClass.UNIT_ENEMY`
- Named:
	- `enum Named {THING_1, THING_2, ANOTHER_THING = -1}`
	- Equivalent to define a constant dictionary:
		- `const State = {THING_1 = 0, ...}`
		- `Named.keys()` returns a dictionary name -> value
		- `Named.values()` returns just the values
	- Accessed `Named.THING_1` or from outside `MyClass.Named.THING_1`

Named enums allow more introspection, still print will show the value not the label.

## Encapsulating attributes

- Centralizes attribute changes and accessing
- While keeping syntax nice for class users (attribute like)

```gdscript
var my_mar := 100:
	set(value):
		do whatever with value
	get:
		return the value
var other_var setget mysetter, mygetter # both are existing class methods
var another_var setget mysetter # mysetter is an existing class method
```

- Pitfall: they won't be used from class code!!
	- They require the dot notations to activate `my_attribute = 100` won't trigger accessor
	- You must use `self.my_attribute = 100` for that
	- This enables the class access to the inner representation so it can be used for encapsulation
- Pitfall: do not call from the setter methods that set the value,
	just the setter itself can directly set the var.
	If other method does, it will call the setter again
	resulting in an infinite loop.

## Other less used advanced language features

- Singletons/Autoload:
	- Instance objects that are loaded outside of the scene and are available by a global name
	- Defined in the project properties
	- Useful to share attributes and methods globally whichever the main scene is
- Inner classes
	- Defined like in Python but using `extends` instead of parenthesis
	- `class MyInnerClass extends InnerSuperClass:`
	- Referring from other classes if unnamed: `extends "./script.gd".MyInnerClass`
- Class behaviour
	- Static vars
		- `static var next_id := 0`
		- Shared value among instances
		- Accessed with dot from instance or class
		- Accessed as is from methods and static methods
		- `@static_unload` is required for the variable to be unreferenced and destroyed
	- Static method
		- Callable without instances, but through class dot or instance dot or the class without dots
		- Sees static (class) variables but do not se regular (instance) variables
		- `static func mymethod(params):...`
	- Static constructor
		- Called when the class is loaded after static var initialization
		- `static func _static_init(): ...`
- StingName:
	- Prehashed string, faster as internally represented by the hash itself
	- Literal: `&"example"` equivalent to `StringName("example")`
	- It casts String so you do not usually need
	- Has all String methods but turns into String, inefficient
- (`match`)[https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html#match]
	- Mostly like new python `match` with some diferences:
	- Does not match Objects yet, just combinations of Arrays, Dicts, and basics
	- Captures (when you asign a part of the matched to a new variable)
		have to be prepended with `var`
		`[var x, var y, _]:`
	- `_` is used as place holder like python
	- Rest is matched by `...` but can not be captured (in python `*` or `**` and a var name can be specified to capture)
	- Guard appends `when <condition>` to the pattern (Python uses `if`)
	- multipatterns with ',' instead of python's `|`
	- Classes not supported

## Resources

Resources are objects that can be used as value for node attributes
but they are not themselves nodes.
Resources have to be serializable.
Typical resources are Textures, Materials, Meshes, Shaders, and indeed Scenes...

Resources can be serialized in a file.
In that case `load(resourcepath)` obtains it.
By default, they are stored along the scene,
unless you specify them to be in a separate file.
In this case, usual extension is `.tres`.


## File system

- Use unix slashes, case sensitive.
	- If original development is done in windows, may cause problems
	- Convention: always use lower case for files (naming and refering)
- `res://' root for project resources.
	- Whenever the `project.godot` is.
	- `/` alias for `res://`
	- This enables packaging, resources could be not in the system filesystem but in a tmp or memory.
	- Read only in runtime (not developing)
- `user://'
	- Writable location for user files in the system
	- In Linux: /home/myuser/.local/share/godot/myproject
	- In Windows: %APPDATA%/myproject

## Debugging

- We can use `print` function
- `prints()` automatically separates parameters with spaces (like python print)
- `printt()` like prints but uses tabs to separate
- `print_stack()` prints the stack trace
- `print_debug()` Shows the file and line
- `print_rich()` uses bbcode to add ansi: `[b] [color=red] [/color] [/b]`
- `push_error/warning()`: enables a stacktrace besides the error message
- When in run, the running scene tree is availabe as 'Remote' tab in the scenen tree docker.
	- You can fix it as the default shown in project settings.
- KWin "Always on top" option is good to keep the game in front and still being able to manipulate and inspect the editor interface.
- `OS.is_debug_build():` to conditionally activate debug tools




### Lifecycle

- `_init` called from root to leaves order within the tree
- `_ready` called from leaves to root within the tree (your children should be available)

Recursive hollywood calls:

- parent first: `_init`, `_process`, `_draw`...
- child first: `_ready` (when we run `_ready`, children already are ready)
- inverse (of parent first): `_input`, `_exit_tree`


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


## Importing from blender

You can import blend files directly but Godot will require Blender installed to export gltf.
Gltf/glb is the recomended export format.

It includes Mesh (vertex, edges, faces, normals, colors...), Materials Rigging, Animations

Import Tab: Defines many options on how to import the selected asset

Interesting ones:

- Root Scale

"Advanced" Button: Shows more details on how the scene is composed
and allows to visualize the import changes while changing the same options,
and some options to be changed per part.
Also how to import the materials to each part or whether to assing your own.

Gltf are imported as read only scenes.
But we might want to alter them.
There are different strategies for that:

- Inherit:
    - How: Open the scene, choose "New inherited"
    - Allows:
        - Modifying properties of existing nodes (materials, position...)
        - Adding scripts to the existing elements
        - Accessing the elements separatelly by node name
        - Adding elements to the scene
    - But you cannot alter the original hierarchy elements which are marked in yellow
    - Warn: changes to the element properties might be lost if on import the hierarchy changes
- Nest:
    - How:
        - Creating a empty scene and dragging the gltf
    - Stable to reimports
    - We cannot access to the inners unless:
        - Right click the imported element and chose "Make Editable children"
        - With editable children, they are no more read only and you can even modify the hierarchy
        - Don't think on reimport once you make them editable
        - Consider splitting in multiple gltf
- Local:
    - How:
        - Create a wraper scene
        - Drag the gltf into it
        - Right click and "Make local"
    - We can alter the scende freely, even split the members as scenes
    - All the data is incorporated into the scenes making them larger

Animations: gltf might contain animations,
either linked to their model and rig,
or separated as reusable Animation Library.
This is useful for retargeting animation
as such in mixamo website.


https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/node_type_customization.html

Import suffixes in blender objects alter how godot import them

    - `-noimp` exclude node from import
    - `-col` autogenerates a collider using the same mesh (Concave, acurate but slow)
    - `-convcol` autogenerate the convex hull as collision (
    - `-colonly` import as a colision mesh, not as visual mesh
    - `-convcolonly` import as a colision mesh but the convex hull
    - `-occ` Defines an occlusion mesh with the same geometry
    - `-occonly` Defines the object as occlusion mesh
    - `-navmesh` Defines the object as navmesh (works like the only above, not creating the mesh)
    - `-rigid` Imported as RigidBody3D instead of Node3d.
    - `-loop` in animations auto loop them





















