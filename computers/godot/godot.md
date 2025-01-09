# Godot 4 (Game Engine)

## Tutorials

::: linkcard https://www.youtube.com/watch?v=nAh_Kx5Zh5Q
	The ultimate introduction to Godot 4

	Develops a 2D game showing most of the Godot features.

::: linkcard https://www.youtube.com/watch?v=9LaB6wbZepg&list=PLJ690cxlZTgL4i3sjTPRQTyrJ5TTkYJ2_&index=0
	Playlist GDScript from scratch. From very scratch, even programming concepts,
	but explains some of the differences

## Interesting videos

- [Interesting plugin SmartShape2D and workflow](https://www.youtube.com/watch?v=r-pd2yuNPvA)
- [Character creation Blender + Godot](https://www.youtube.com/watch?v=dd6G2S6MQ6U)
- [Character Riging Blender + Godot](https://www.youtube.com/watch?v=VasHZZyPpYU)
- [3D character movement](https://www.youtube.com/watch?v=UpF7wm0186Q)
- [GDQuest: Smooth 3D Character Movement with drone camera](https://www.youtube.com/watch?v=JlgZtOFMdfc)
- [Depth based outline with gdshaders that work in compatible mode](https://www.youtube.com/watch?v=-SXJvpbFJ7M)
- [Le x Lu: Channel on 3d games effects with godot](https://www.youtube.com/@Le_x_Lu)
- [Realist environment parametrization (cielo, sol, sombras, niebla. Impresionante)](https://www.youtube.com/watch?v=PmiMUuFvxzg)
- [Animation tree (blending animations together)](https://www.youtube.com/watch?v=n872lbC-_BU)

## Extracted topics

- [Concepts](concepts.md)
- [Tiling](tiling.md)
- [Physics](physics.md)
- [UI](ui.md)
- [Shaders](shaders.md)
- [Particles](particles.md)
- [Addons](addons.md)


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

- Globalize Plugins: (deprecated by Global Project) Install plugins to all projects
- Godot Global Project: Successoror the former
- DRY
	- Basic FPS player: Dont reinvent the wheel
	- Phantom camera: Camara con targets, movimientos con easing, evita obstaculos... (2D y 3D)
	- Scene Manager: Transiciones entre escenas
	- Delta Rollback: Saves game
	- BulletUpHell: gestiona proyectiles masivos
- Asset editors/generators
	- Cyclops: Editor de escenarios 3D al estilo del de Quake
	- Dialogic: Creador de un sistema de dialogos.
	- CGS Toolbox: Modelado CGS visual
	- Smartshape 2D: Definir volumenes en vez de tile a tile, formas no cuadriculadas...
	- [Goshapes](https://github.com/daleblackwood/goshapes): Seria el equivalente de Smartshape para 3D. Defines formas que se auto texturan o rellenan con otros assets.
	- Gaia: Procedural generation
	- Hoodie: Procedural geometries
	- Anima: Makes complex animations simpler. Many presets.
	- TreeGenerator: Proceduraly generated trees (dev version)
	- Volumetrics: Fog, particles...
	- VPainter: Vertex painter inside the editor
	- Godot LOD: Adapts level of detail with distance, a node which contains several meshes to use
- Smart Agents:
	- RL Agents: Entrenador de IA's para bots.
	- LimboAI
- Dev tools
	- GDUnit3: Unit testing
	- ScripIDE: IDe mejor
	- Signal visualizer: Muestra las connexiones de signals como graph editable, tambe fa log
	- Runtime Debug tools: Free cameras, wireframe mode, runtime object selector...
	- Litle Camera preview: muestra lo que ve la camara en modo edicion
	- Block Coding: Similar a un Scratch para Godot
	- Tracy Profiler: Graphical profiler
	- EmbedGame: Permite Ver el juego ejecutandose en el IDE
	- Orchestrator: Visual modular programing
	- Godot SQLite: integracion de bases de datos.
	- Beehave: Behaviour definition logic as node trees (actions, conditions, compositors, decorators...). https://www.youtube.com/watch?v=n0gVEA1dyPQ
- Fisicas
	- Jolt Physics: Motor de fisica 3D mas potente y optimizado que el de serie
	- Box 23: Motor de física 2d
	- Waterways: Para generar y simular rios y aguas corrientes en 3D.
	- OceanWaves: Simulates ocean waves
	- DistanceJoin2D: Rigid join to keep two object at a distance without elasticity
	- SmashTheMesh: rompe objetos 3d
	- Concave Mesh slicer: Permite partir objectos con un plano
	- Polygon Fracture: Rompe objetos 2D
	- Shaker: Emula sacudidas y temblores en los objetos 3d
	- SoftBody2D: Emula cuerpos blandos (deforma, flexiona, parte...) tambien en 2D
	- GPUTrail: Hace lineas cinéticas de colorainas, para 
- Others:
	- Mixing Desk: Context aware music and sound effects
	- Godot Virtual Jostick: Joystick emulator for touch screens (mobile)


## Asset repositories

- [GDQuest 3D Animated Characters](https://github.com/gdquest-demos/godot-4-3D-Characters)
- [GDQuest FPS arms](https://github.com/gdquest-demos/godot-4-FPS-arms)
- [GDQuest Shader Library](https://github.com/gdquest-demos/godot-shaders])
- [GDQuest 2D Visual Effects](https://github.com/gdquest-demos/godot-visual-effects)
- https://syntystore.com/ by [Synty Studios](https://www.syntystudios.com/)
	- Propietario, de pago
	- Low poly assets for realtime
	- Single payment for "small studio"
- https://www.fab.com  (Old Sketchfab)
	- Colaborativo (usuarios suben modelos y ponen precio o no)
- https://www.shadertoy.com/
	- Compartición de shaders (gsgl)
	- https://docs.godotengine.org/en/stable/tutorials/shaders/converting_glsl_to_godot_shaders.html
- https://webgl-shaders.com/
- https://kenney.nl/assets Kenney Assets
	- 3D, 2D and isometric assets, audio, cursors, ui...
	- Free, optional donations

## Resource Catalog

### Mallas

Meshes define 3D shapes as polygons define 2D shapes.

- PointMesh: Single visible point




### Texturas

Abstracting the concept of texture enables many cool features.
They can be obtained/generated in many ways
and they are used extensively in the framework as source of data.

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



