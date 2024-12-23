# Godot Shaders

A shaders contains code that is executed in the graphics card.
It helps to customize the renderization pipeline.

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



