# 3D animation pipeline

https://dreamfarmstudios.com/blog/3d-animation-pipeline/

## Phases

- Pre-production

	- [Inception]: Idea generation
	- [Story creation]: Developing the core elements of the story
	- [Script writting]: Written version of what happens in the screen
	- [Storyboard]: Static visual and often schetchy 2D representation of the scenes described on the script
	- [Animatic]: Animated version of the storyboard
	- [Design]: Develop the visual aspects of characters and scenarios

- Production

	- [Layout]: How 3D elements dispose in the scene
	- [Modeling]: Geometric surfaces of the objects
	- [Texturing]: Provide colors and surface properties to the objects
	- [Rigging]: Provide a bone structure for the animators to move the characters
	- [Animation]: Define the movements along the scene
	- [VFX]: Add any automated animation (hair/fur, fluids, dust, physics simulation...)
	- [Lighting]: Place the lights
	- [Rendering]: Produce video for the scenes.

- Postproduction

	- [Composition]: Sequence and mixing images, including chroma effects
	- [2D VFX]: Some effects are cheaper in 2D
		- Adds: Sparks, rain/snow, lens flares, smoke, dust, pixie dust
		- Rotoscoping: trace and remove an object 
		- Camera shakes or distorsions
	- [Color Correction]: Make colors standup and be consistent along the production
	- [Mastering]: Generating the final files in a proper format



[Inception]: https://dreamfarmstudios.com/blog/ideas-for-3d-animation/
[Story creation]: https://dreamfarmstudios.com/blog/story-for-3d-animation/
[Script writting]: https://dreamfarmstudios.com/blog/script-writing-for-3d-animation/
[Storyboard]: https://dreamfarmstudios.com/blog/3d-animation-storyboard/
[Animatic]: https://dreamfarmstudios.com/blog/animatic-in-a-nutshell-the-storyboard-made-animated/
[Design]: https://dreamfarmstudios.com/blog/shape-language-in-character-design/
[Color design]: https://dreamfarmstudios.com/blog/color-theory-for-character-design/

[Layout]: https://dreamfarmstudios.com/blog/what-is-a-3d-animation-layout-and-why-does-it-matter/
[Modeling]: https://dreamfarmstudios.com/blog/a-quick-guide-to-3d-modeling/
[Texturing]: https://dreamfarmstudios.com/blog/getting-to-know-3d-texturing-in-animation-production/
[Rigging]: TODO, no article
[Animation]: https://www.animationmentor.com/blog/the-ultimate-guide-to-animation-for-beginners/
[VFX]: https://dreamfarmstudios.com/blog/what-you-might-not-know-about-the-vfx-component-of-the-3d-animation-pipeline/
[Lighting]: https://dreamfarmstudios.com/blog/the-ultimate-guide-to-lighting-fundamentals-for-3d/
[Rendering]: https://dreamfarmstudios.com/blog/the-final-step-in-3d-animation-production-3d-rendering/

[Composition]: https://dreamfarmstudios.com/blog/compositing-in-animation-what-it-is-and-how-its-done/
[2D VFX]: https://dreamfarmstudios.com/blog/how-2d-vfx-helps-make-perfect-3d-animations/
[Color Correction]: https://dreamfarmstudios.com/blog/a-quick-look-at-color-correction-in-3d-animation-production/


## Preproduction: Story creation


In story creation phase, core elements of the story are developed, such as:

- Burning core: 
	- Why we must tell this story? (No answer? back to idea)
- Character development
	- Name, description, desires, habits, traits, personal details, goals and ambitions
	- Archetypes: sidekick, villain, shape-shifter, challenger, tricster...
- World description
	- How the world will work
	- Even physics: which real world rules apply and which not
	- Story context
- Engaging conflict:
	- Motivates the view
	- Characters struggle against other persons, nature, system, themselves...
- Storyline
	- Network of cause effects that lead the argument
	- Not necessarily a line, but do not make it overly complicated
- Narrative arc
	- How the elements of the storyline are presented to
		- catch attention at the beggining
		- keep tension to maintaing audience engaged
		- resolve at the end
- Character arc
	- How the character evolves along the story
	- A typical arc: Background - Challenge/Struggle - Growth/Adaptation - Realization

## Production: Layout

- Design the cameras and the framing of the scenes (scene composition)
- Based on the animatic or the story board, collaborating with the director
- Uses simples geometries and environments instead of actual models
- Rought animations as starting point
- Serves as guide for the rest of the pipeline
- Cheap: several versions maybe provided to choose
- It enhances as the production incorporates elements: models, textures, animations, voice, music...

## Production: Modeling

Every object in the scene has to be modeled.
That is define a 3D surface/volume that represents it.

Within the pipeline:

- Takes as inputs the outputs of the design stage: drawings, sketches and scupltures
- Feasibility of the models: technically viable (level of detail...)
- Feedback from later Animation and Rigging phases because of deformities when the model is animated


Techiques

- Box modeling:
	- Starting with cubes reensembling the body parts and then refining using other techniques
- Subdivision modeling:
	- Build a general form, then subdivide and add more detail to the subdivision
	- Hierarchical geometries that can be used to ignore details on low res (real-time, sketch, far views...)
- NURBS modeling
	- Basic shapes are easily parametrizable but limited
	- NURBS are curved surfaces we can manipulate using control points
	- Manipulating surfaces with control points to produce complex but natural curves
- Boolean 
	- Combining basic geometric objects by joining, intersecting, removing... their volumes
- Sculpting
	- Emulates clay modeling with tools like carving, adding, extending, polishing...
	- Quite intuitive for non-technical artists
	- Generates a high resolution model, that needs to be turned into low res (retopology)
- 3D Scanning
	- Many technologies: Laser scans, IR coding, IA...
	- Usually models need some clean up
- IA generation: - Latests advances of IA already enables:
	- Recovering 3D geometries from video shots or even photographs
		- [Nerf](https://github.com/awesome-NeRF/awesome-NeRF)
		- [Human body scan](https://arxiv.org/abs/1803.04758)
	- Generating 3D geometries from a text description
		- [Dream3D](https://arxiv.org/pdf/2212.14704.pdf) ([src](https://github.com/bluequartzsoftware/DREAM3DSuperbuild))
	- Generating animations from video
		- [Skeleton free pose transfer](https://arxiv.org/abs/2208.00790)
		- https://www.deepmotion.com/animate-3d
		- https://radicalmotion.com/


## Production: Texturing

Texturing is providing **material** properties to the model.

It is called texturing because the main technique (but not the only one)
is to apply textures.
But also shaders takes part of this process.

Textures is a cheap mechanism to provide level of detail to a simple model.
They consist of images that are mapped to the model surface like a vynil,
providing fine grained values for a set or properties, originally color
but nowadays extended to many others, see bellow.

Shaders is another technique used in combination with textures
to recreate materials and styles.
Shaders can also generate the properties provided by the textures
generatively.

Nowadays the material of a model is conformed by
properties given to the object, the textures
applied to it and the shaders added to the object.

- Geometry properties:
	- Bump map:
		- Represents height
		- Used to simulate high detail surface geometries.
		- Computes the normals used to apply lighting.
		- Does not modify geometry, just fakes it.
		- May have artifacts on normal calculation
	- Normal map:
		- Same function as Bump maps
		- Contains the normals, skipping computation and making them predictable
		- Still fakes the geometry
	- Displacement map:
		- Alters the actual geometry providing real detail.
		- More expensive than normals
		- When? When the emulated geometry would cause occlussions:
			- Prominent features
			- Aligned polygons
			- Close surfaces
	- Height math: A displacement map when used, not for details but for big features like muntains and valeys
- Optical Properties
	- Metallic/Roughness workflow
		- Base color: (RGB) Represents RGB color, provides a basecolor to work with on the other layers
		- Metalic map: How metalic (reflective) the material is
		- Roughness map: How much light is scattered emulating
	- Specular/Glossiness workflow
		- Albedo map: Non metalic base color (black if metallic)
		- Specular map: Metalic color multiplied by the specular reflection coefficient
		- Glossiness map: Gray scale how much light is reflected as gloss (inverse of Roughness)
- Optical properties:
	- Opacity map: How ocludes
	- Refraction map: 
	- Emissive map: self emitted light
	- Ambient occlusion: Exposure to ambient light
	- Refraction: 
	- Anisotropy map: Direction of the rougness, implies different diffusion patterns depending on the direction
		- Brushed metals, fabric, shinny hairs

Texturing production Process:

- Unwrapping: define how the surface of the model maps to a square where the texture.
	- UVMap: Map each model vertex to a texture pixel position (coordinates u,v)
	- They look like you deskined the character
- Painting: Set the values for the texture
	- In uvspace, or directly on the model.
- Shading: Applying shaders to a model
	- Shaders may provide an extra twist to the material.





