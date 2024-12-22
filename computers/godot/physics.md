# Godot Physics

## Levels of complexity

Below ND means either 2D or 3D.
Godot intent is 2D and 3D apis to be analogous,
so you don't have to learn two different API's.

- **NodeND**
	- Defines relative **afine transformations** relative to its parent
	- **CollisionObjectND** (NodeND, Abstract)
		- Collides with other objects
			- Defines **collision shapes** (CollisionShape) that sets its volume/area
			- The object lives in a **collision layer**
			- The object will collide with objects living in collision layers specified in its **collision mask**.
		- **AreaND** (CollisionObjectND)
			- Defines zones for other objects to be or not.
				- Collisions trigger signals and can be programmatically tested.
				- But it does not generate physical collisions.
				- Can change default physics parameters in its zone.
					- gravity, wind, liniear/angulardamp...
				- Can change audio parameters: reverb, audio bus...
		- **PhysicsBodyND** (CollisionObjectND, Abstract)
			- Objects affected by physics.
			- Logic to move and test whether the movement causes a collision.
			- **StaticBodyND** (PhysicsBodyND)
				- Inmobile object but other object collides with it (pasive).
				- Code can move it, not triggering any collision
				- External forces do not affects it.
				- **AnimatableBodyND** (StaticBodyND)
					- External forces do not affect it
					- Move by code affects other objects.
			- **RigidBodyND** (PhysicsBodyND)
				- Affected by external forces (elastic collissions, impulses, forces)
				- Has mass/inertia, `linear/angular_velocity/dump/`
				- freeze(static): not affected by forces, its movement by code, do not generate collisions
				- freeze(kinematic): like the previous one but it does trigger collisions
				- sleep: stopped saving cpu waiting to receive a collision, or an impulse/force
				- **VehicleBody3D** (RigidBodyND)
					- Simulates a Car
			- **PhysicalBoneND**
				- TODO
			- **CharacterBodyND**
				- User controlled
				- Not affected by external forces
				- Affects collided objects
				- Versus the AnimatableBodyND, it considers walking, floors, walls

::: warning
	CollisionObject != CollisionBody != CollisionShape



## CollisionBody2D/3D (Volume)

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


## Collisions

Collisions are segmented by physics layers
so that each layer can be checked for collisions separatelly.

`CollisionObject2D` base class has those attributes:

- Layer: The layers where the object can be detected by others
- Mask: The layers that the object will scan for collisions with others
- Priority: The order in which the object will be notified. Useful to avoid race conditions.

`RigidSolid2D`, besides physics of rigid solids, also defines signals like:

- `body_entered/exited(body: Node)`


## RigidBody2D/3D (Dynamics)

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

## Joints

Joint2D/3D constrains the relative movement of two objects

- DampedSpringJoint2D/3D: Elasticly
- GrooveJoint2D / SliderJoint3D: Allows movement along an axis (groove = surco, slider = desplazamiento)
- PinJoint2D/3D: Allows any rotation around a fixed point (pin = chincheta)
- HingeJoint3D: Allows rotations around an axis (hinge = visagra)
- ConeTwistJoint3D: Allows rotations limited to a an angle (Ball joint/Rotula mecanica) (que no "la rotula" de la pierna, mas bien como la cadera o el hombro)
- Generic6DOFJoint3D: The most general articulation you can limit any of the 6 degrees of freedom (rotation and motion on the three axis)


