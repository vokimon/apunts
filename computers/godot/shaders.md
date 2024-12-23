# Godot Shaders

## References

- https://thebookofshaders.com/
- https://docs.godotengine.org/en/stable/tutorials/shaders/index.html

## Intro

### Parallel execution

A shaders contains code that is executed in the graphics card (GPU)
in contrast to code that is run in the CPU.
They are useful to customize the renderization pipeline
benefiting of the parallelization capabilities of graphics cards.
For example,
instead of writing a double loop to change the value of every pixel,
we write a function that writes a single pixel and the graphic card
runs it for every pixel in parallel.

There are many places where you can insert those parallel computations.
For example: When processing the geometry (vertex) or when rastering
the final pixels (fragments).

Because all the computations run in parallel every unit cannot access
the results of the others.
Also they cannot keep any internal memory from
one frame to the next (although there are tricks).

### Writing shaders

Most platforms use GLSL language for shaders.
Godot may use it but also provides two alternatives:

- gdshader language: close to GLSL but with convieniences
- visual shader: a visual processing graph


A simplified view of the render pipeline:

	[Original Geometry]
	  Vertex Shaders
	[Modified Geometry]	
	  Rasterization 
	   [Fragments]
	 Fragment Shader
	  [Final output]


**Vertex shaders** modify the geometry of the vertex of the geometry,
while **fragment shaders** define how to draw each pixel.
Not exactly pixels, they are called **fragments** because
they carry much more information than color in the screen.
Fragments are a future pixels and carry all the info
to endup computing that color in the screen:
normals, textures, albedo color, metalicity, light...

You can create several kind of shaders:

- **Spacial shader:**
	- Material of any 3D object
	- Directive: `shader_type spatial;`
	- Entry points: `vertex()`, `fragment()`, `ligth()`
- **CanvasItem shaders:**
	- Material of any 2D/Canvas item
	- Directive: `shader_type canvas_item;`
	- Entry points: `vertex()`, `fragment()`, `ligth()`
- **Particle shaders:**
	- Directive: `shader_type particles`
	- Used to compute the particle properties when they are generated they are computed before the pipeline
	- Entry points: `start()`, `process()`
- **Sky shaders:**s
	- Directive: `shader_type sky;`
	- Entry points: `sky()`
- **Fog shaders** 
	- Directive: `shader_type fog;`
	- Entry points: `fog()`
- **Compute shaders:**
	- glsl
	- Directive: `#[compute]`
- **Compose shader:**
	- glsl

- `vertex()`: runs over all the vertices in the mesh and sets their positions and some other per-vertex variables
- `fragment()` runs for every pixel covered by the mesh (similar parameters than the vertex but interpolated)
- `light()` for every pixel, for every light
- `start()` for every particle at its begining
- `process()` for every particle for each frame
- `fog()` for every 'fogxel' volumetric buffer

Shaders are inserted as materials.
Indeed standard material result in shaders as well.
Indeed you can take a standard material tweek parameters,
convert it into a shader and see how it works.

## Input and outputs

The pipeline provides the shader a set of input data
and gives the option to set a set of output data.
These are accessed as they were global variables.
Many input variables are in fact global,
but most input and all outputs are local
to the processed element: a vertex, a fragment, a particle...

## Uniforms

Uniforms are data that is injected by the CPU into the GPU:

- Floating point parameters
- Colors
- Textures
- ...



## Spatial Shaders

https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html

Spatial Shader for 3D materials




- Fragments are not called Pixels because they have lots of more information:
	- Color
	- Screen location
	- UV coordinates
	- Normals
	- Light information
	- ....

In Godot, we can use either a shader node editor (`VisualShader`) or shader code (`Shader`).

Create a resource, choose either `Shader` or `VisualShader`, drag the file as material of the target object.

::: tip
	By creating a standard material you can modify it and later save it as an equivalent shader.

For VisualShader, a node editor will open with an output node.
Input nodes have to be added by hand.
Change the shader type (vertex, fragment...) with the dropdown selector.

Exponer valores con `uniform`.

```shader
uniform float myparameter = 3
```


## GLSL vs gdShader

- joined programs:
	- GLSL have several programs (vertex, fragment) with a main()
	- gdShader have a single program with several functions vertex() fragment()
- 






