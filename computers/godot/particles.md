# Godot: Particles

Particles are multiple similar objects that are generated and controlled in the same way.
Being similar objects, we can parallelize its control usually with the GPU.
They are quite useful to generate a large variety of effects
which would be quite expensive implemented as regular meshes:
Rain, smoke, fire, flares, leaves, droplets, snow...

## Particle nodes (GPU vs CPU, 2D vs 3D)

In Godot, we use emitter nodes that setup and control the particles.
Such nodes, as 3D/2D Node, establishes the center of emission.
We can use 4 different particle emitter nodes.

The GPU accelerated ones are:

- GPUParticles2D
- GPUParticles3D

Some platforms, those based on GLES2,
do not support GPU accelerated particles,
since particles were introduced in GLES3.
To support those platforms we can still use the CPU version
of the previous nodes:

- CPUParticles2D
- CPUParticles (yes, has no 3D in the name)

::: warning TODO
	Find what platforms are GLES2

Particles are generated with a fixed interval,
and have a given lifetime.
During it lifetime they are controlled by a set of parameters
which usually includes some random variability to give them organicity.

In GPU versions, creation and behaviour are controlled by a shader (called "process material").
Godot provides a generic shader (ParticleProcessMaterial) with many parameters we can control.
We could add our own shader (ShaderMaterial) to add a custom behaviour.
Like Mesh materials, you can create a godot standard material,
adjust the parameters and use it as starting point for you own shader,
by using the 'Convert to ShaderMaterial' option in the 'process material' field menu.

CPU versions are slow CPU implementation of the generic shader and share many parameters.
Sadly the properties are not located in the same place.
In CPU particles the material parameters are top level,
while in GPU those parameters are inside the ParticleProcessMaterial resource.

## Minimal setup

For GPU based Particles you should add, at least the ProcessMaterial property.
Choose a ParticleProcessMaterial, which is similar to what the CPU based has.

For 3D particles you should chose a mesh.
For GPUParticle3D, go to "Draw Passes/Pass 1" and choose a PointMesh.
For CPUParticles, go to "Drawing Mesh" and choose PointMesh.
2D particles already have a default drawing that also draws points.

## Emision and lifetime

The emision is controlled mainly by 3 parameters:

- Lifetime: is the time each particle will be visible
- Amount: is the amount of particles to handle. Changing this restarts the particles.
- Amount rate [0..1]: Changes the amount of particles visible without restarting.

The emision rate will adapt so that particles are emitted in a constant pace,
so that afer the last particle is emitted the first one dies and can be reemitted.

	emision interval = lifetime / (amount * amount rate)

Those main parameters can be altered by those other ones:

- Emitting: controls the emission, set to false to stop emitting.
- One Shot: If true, particles won't be reemitted after its lifecycle is ended.
	- After the last particle is emitted, Emitting attribute is set tu false.
	- Retrigger can be controlled by setting Emitting attribute to true again.
- Preprocess (s): time to advance the simulation.
	- This is useful for example if you want to skip the initial transient where not all the particles are emitted.
- Explosiveness [0..1]: Concentrates particle emision in a burst.
	- 0 will spread the creation of particles evenly (default)
	- 0.5 will create all the particles in half of the life time.
	- 1 will emit all the particles at once
	- Indeed the parameter controls the ratio of the lifetime of the first particle when all the particles have been alredy emitted.
		emision interval = (lifetime - lifetime * explosiveness) / (amount * amount rate)
- Randomness [0..1]: randomly makes the lifecycle of some 
	- TODO: How this affects particles (they die early? is emission delayed/advanced? )
	- TODO: What 1 means?

## Spawn

Spawn parameters control the initial state of the particle when its lifecycle starts (spawned/respawned).

The initial position is defined within a given shape:

- Point (default)
- Sphere (any point of its volume)
- Sphere Surface (not inside the sphere)
- Box
- Ring

Special shapes Points and DirectedPoints enable to control initial parameters (position, velocity, color) ampling textures.

The initial velocity is determined by:

- Direction (vector, unit): the central direction
- Spread: angle particles will diverge from the central direction (180 degrees means all directions)
- Initial velocity: scalar range for the velocity
- Flattness: ??? (for 3D)
- Inherit velocity: velocity factor particle inherits from emitter node
- Velocity Pivot: center for radial and orbital movements

## Processing

Because shaders cannot access cpu, we have to define the behaviour beforehand.
For most parameters,
the default shader provides `xxx_max` and `xxx_min` attributes that will be used as bounds to randomize the initial value.
They could also provide a curve (bpf or 1d texture).
In this case, the curve will control the parameter evolution along the lifecycle between `xxx_max` and `xxx_min`.

- Alpha: (0-1 factor) multipler for alpha (curve) (not randomized?)
- Color: Base color (Color) (multiplies) all colors multiply the texture or white.
- Color Initial Ramp: Initial variability by sampling (multiplies) (GradientTexture1D)
- Color Ramp: Variation along lifecycle (multiplies) (GradientTexture1D)
- Hue Variation: (factor) shift on the hue of Color 1.0 is full hue rotation (min, max, curve)

- Scale: (factor)  (min, max, curve) (CuverTexture or CurveXYZ to scale differently each axis)
- Anim Offset: (0-1 factor) the starting point for the animation (min, max, curve)
- Anim Speed: (factor) 1.0 means correspondence of the lifecycle with the animation loop (min, max, curve)


- Angle: Rotation arround the center of the texture (degrees) (min, max, curve)
- Angular Velocity: turn around its center (degrees/second) (min, max, curve)
- Initial Velocity: (m/s scalar) (min, max)
	- Combined with direction and spread to get a vector
	- Added to inherited velocity from parent
- Radial velocity: Velocity component away from the pivot (negative towards) (min, max, curve) (not damped with curve)
- Orbit Velocity: (rotations per second) Perpendicular to the radial velocity (min, max, curve) (not damped with curve)
- Linear Accel: In the direciton (min, max, curve)
- Radial Accel: Repels from the pivot (min, max, curve)
- Directional velocity	
- Tangential acceleration: In the orbital velocity direction
- Damping: (m/s²) velocity reduction per second (min, max, curve)
- Gravity: (vector m/s²)
- Inherit Velocity Ratio: (factor) how much or the emitter node velocity is inherited by the particle. 1
- Particle Flags
	- Align y: Align y with velocity (make the particle point to where it is headed)
	- Disable z: for 2d particles
	- Rotate y: ???


Guess:

- Most of those parameters conflict
- Accelerations may add, no problem
- Velocity curves are perpendicular components, no problem.
- But if acceleration and velocity curves are both set...

**Local coords** tells if, once emitted the particle physics apply in local or world coordinates.
Default is false. This is natural when the particle dettaches from its emitter (ie. sparkle).
If true, a emitted particle will move solidary to its parent, natural when there is some link to the emitter (ie. orbiter).


- TODO: 3D Drawing
- TODO: Turbulence
- TODO: Subemitters
- TODO: Texture based emision
- TODO: Animation





GPUParticlesCollisionBox3D: Defines a collision box for the particles that is handled by the GPU.
You can control what happens with particles when they collide with such colliders:
Ignore, disappear or do physics.





