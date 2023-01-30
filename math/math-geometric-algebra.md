# Geometric algebra

https://www.youtube.com/watch?v=60z_hpEAtD8
https://www.youtube.com/watch?v=0bOiy0HVMqA (Addendum)
https://www.youtube.com/watch?v=2hBWCCAiCzQ&list=PLVuwZXwFua-0Ks3rRS4tIkswgUmDLqqRy (From zero to Geo)

Context:

- Clifford Algebra: is the mathematical abstraction, not applied to phisics
- Algebraic geometry: not to be confused with.

What it can do for us:

- Unifies complex, quaternions, spinors, rotations, spatial field operators...
- Simpler than all those

## Primitives

Let's define a set of primitives. Some of those we already know:

Scalars (sum and product)

Vectors

- Magnitude + direction
- Equivalence: same magnitude and direction
	- Ignore origin
- Scalar multiplication
- Vector addition
- Representation refered to a basis
	- Project the vector to each basis
	- Divide by the size of the basis

Bivectors: Oriented area

- Area + direction
	- A series of connected vectors defining a circulation around an area
	- The magnitude is the area || A ||
	- The direction is the right hand of the enclosing vectors
- Equivalence: same area and orientation
	- Ignore shape and position
- Axis representation:
	- Axis are the orthogonal unit areas coplanar with the planes
	- Components are area projection to those planes
- Addition:
	- Add componentsof axis representation


Trivector: Oriented volume

- Magnitude
- Orientation?

k-vector: extension to k dimension

## Geometric Product

For simplicity lets consider just 1-vectors at first

Inner product:

- `a·b`
- Length of the projection of one vector over the other
- Also `||a|| ||b|| cos(\theta)` where `\theta` is the angle among them.
- Conmutative, distributive, and linearity

Problem: does not keep information about the original vectors.

- Perpendicular vectors give 0, any magnitude info is lost
- vectors having the same angle with the other will give same product
	- in 2D, the symmetric one
	- in 3D is a cone of vectors

Cross product keeps more info but just works in 3D, not higher dimension

Outer product:

- `a^b`
- The 2-vector created as paralellogram of a and b, **starting the bounding vectors at `a`**
- `||a^b|| = ||a|| ||b|| sin(\theta)`
- The orientation is the same that the cross product: perpendicular to operators oriented according to the rigth hand rule)
- Properties: Anticonmutative, Distributibity, Linearity

Problems:

- Outer product between aligned vectors is 0 (indeed auto outoproduct is 0)

Outer product of a bivector and a vector results in a trivector.
Extruding the bivector area along the vector to generate a volume.
Like the outer product of vector along another 'extrudes' an area.

In multidimentional, vector if the second vector can be expresed in terms of the other, the outer product will be zero.
For example multiplying a bivector by a coplanar vector.

TODO: No acabo de ligar la intuicion con como funciona la coplanaridad



Geometric Product: `a b = a·b + a^b`

Combining outer and inner product.
Adding different animals?
No problem, just like complex numbers are the sum of imaginary and real numbers.
A **multivector** is the sum of k-vectors of maybe diverse k.

	uu = u·u + u^u
	uu = ||u||² + 0
	uu = ||u||²
	u² = ||u||²

	u/||u||² u = ||u||²/||u||² = 1, so
	u^{-1} = u / ||u||²

Defined as long as u has non-zero magnitude.

Having inverses, we can divide vectors.

	Because is antisymmetric

	uv = u·v + u^v
	vu = v·u + v^u = u·v - u^v

	adding and substracting both:

	u·v = (uv + vu)/2
	u^v = (uv - vu)/2

## Canonical bases

You can express the bivector bases as outer product of two vector bases.

Supose ei and ej are orthonormal basis for N-dimesional 1-vectors.
Being autonormals:

	ei ei =
		= ei·ei + ei^ei
		= ei^ei + 0  (parellepiped with itself is 0 ||)
		= ei^ei   (projection over itself is 1)
		= 1

	ei ej =           (i!=j)
		= ei·ej + ei^ej
		= 0 -ej^ei
		= -ej ei

Lets keep those two properties in a box.

	ei ei = 1
	ei ej = - ej ei  (i!=j)

In a 2d space, the 1 vector basis would be:

	x y     (would have the caret above).
	
There is only one posible 2-vector base which is:

	xy = x^y

That means that areas can only have one orientation in 2D.
They can be either looking up or looking down.

2D multivectors can be expressed generally with 4 components:

	V = a + bx + cy + dxy


In a 3D space the 1-vector basis would be.

	x y z    (would have the caret above)

2-vector basis are the product of the above.
The orthogonal surfaces perpendicular to each one.

	xy = x^y
	yz = y^z
	zx = z^x

And the 3-vector basis just requires a single base

	xyz = x^y^z

Which is the k-vector that has no orientation in a 3D space, but in ND...

TODO: what the sign implies??

A 3D multivector can be expressed with 8 components:

	V = a + bx + cy + dz + exy + fyz + gzx + hxyz

## Mutiplication mechanics

How to multiply multi vectors?

- Express them in terms of its bases
- Apply the distributive property
- Apply the properties of axis multiplication
- Group by base

Example:

	(ax + by) (cx + dy) =
	= acxx + adxy + bcyx + bdyy    (distribute multiplication)
	= ac + adxy - bcxy + bd        (applying axis multiplication)
	= (ac+bd) + (ad-bc) xy         (group by base)


By multiplying two 2d bivectors we got:

- an scalar which is lenght of the mutual projection among them
- a bivector representing the area of the parallelipiped

Nothing we already didn't have with inner and cross product.
But cross product definition is limited to 2D and 3D vectors
and its definition is overly complicated.
Geometric product definition is just based on simple algebra and
extends to n dimensions and to any kind of multivector (sum of k-vectors).

	(ax + by)(cx + dy)(ex + cy) =
	= ((ac+bd) + (ad-bc) xy) (ex + fy)
	= (ac+bd)ex + (ac+bd)fy + (ad-bc)xyex + (ad-bc)xyfy
	= e(ac+bd)x + f(ac+bd)y + e(ad-bc)xyx + f(ad-bc)xyy
	= e(ac+bd)x + f(ac+bd)y + e(ad-bc)xyx + f(ad-bc)x   [ yy=1 ]
	= e(ac+bd)x + f(ac+bd)y - e(ad-bc)y + f(ad-bc)x   [ xyx=-xxy=-y ]
	= (e(ac+bd)+f(ad-bc))x + (f(ac+bd)-e(ad-bc))y


## 2D Spaces (relation to complex numbers)

A 2-vector in a 2D space has only a single component, the one multiplied by xy.

	(xy)^2 = xyxy = -xxyy = -1 = ... i^2  !!!

Post-multiplying a vector by i:

	(ax + by)i = axxy + byxy = ay - bx   => rotated 90 degrees
	i(ax + bx) = xyax + xyby = -ay + bx  => rotates -90 degrees

Careful!: not the same thing as multiplying by regural imaginary i!!!

Multiplying multivector based complex numbers:

	(a + bi)(c + di) =
		= ac + adxy + bxyc + bxydxy
		= ac + adxy + bcxy - bd
		= (ac-bd) + (ad+bc) xy
		= (ac-bd) + (ad+bc) i

This is rotation + scaling in complex plane

Now post-multiplying a 2-vector by a multi vector based complex number:

	(ax + by)(c + di) =
		= axc + axdxy + byc + bydxy
		= (ac-bd) x + (ad+bc) y

That is rotation + scaling in the 2D space

Rotations

	e^i\theta = cos(\theta) + i sin(\theta)

	v e^i\theta = e^-i\theta v

	Multiplying by the conjugate 

The product of two 2-vectors gives a complex number.

	uv =
		= u.v + u^v
		= ||u|| ||v|| cos\theta + xy ||u|| ||v|| sin\theta
		= ||u|| ||v|| cos\theta + i ||u|| ||v|| sin\theta
		= ||u|| ||v|| e^i \theta

The complex number represents
a rotation of the angle between the vectors,
and an scaling by the producto of the magnitudes.
If the vectors are unitary, just a rotation.

Also we we swap the order of the multiplicaiton

	vu =
		= v.u + v^u
		= u.v - u^v
		= (uv)*

Which is the conjugate (`*`), and the inverse rotation.


Other identities:

	vz =? z* v
	vz =
		= (ax + by) (c + dxy)
		= acx + adxxy + bcy + bdyxy
		= acx + adxxy + bcy - bdxyy (reorder bd  xy applying sign change)
		= acx + ady + bcy - bdx     (extract factor xx and yy)
		= acx + adyxx + bcy - bdxyy (add reversed factors xx and yy)
		= acx - adxyx + bcy - bdxyy (reorder ad factors applying sign change)
		= c(ax+by) - dxy(ax+by)     (grouping xy and independent
		= (c-dxy)(ax+by)
		= z* v

	uvw = (uv) w = (vu)* w = wvu
	xi = xxy = y
	yi = yxy = -x


In summary, in 2D spaces:

- 2-vectors are imaginary numbers, the base xy is equivalent to i
- The scalar and xy components form a complex number
- Multiplying a vector by a complex (scalar+2vector), returns a 1vector (rotated and scaled)
- Multiplying a vector by a 1vector, returns a complex (rotation and scaling that can be applied to a vector)
- Multiplying a complex by a complex, rotates and scales it
- TODO: What does other combinations mean?

## 3D Spaces ()

3D multivector has 8 components:

	V = a + bx + cy + dz + exy + fyz + gzx + hxyz
                \---  v ---/   \----- V -----/

- Here the 3-vector is the pseudo-scalar.
- 2vector are no longer pseudo-scalars
- In 3D space i = xyz
- Ai = iA for any 3D multi vector. For each factor of terms of A
	- If the factor is a scalar you can swap without swapping the sign
	- If the factor is a base, the sign will be swapped twice, once for each of the other bases

Multiply a 1-vector base by i returns its complementari 2-vector

	xi = yz, yi = zx, zi = xy

	xi = xxyz = yz
	yi = yxyz = -xyyz = -xz = zy
	zi = zxyz = -xzyz = --xyzz = xy

Because of that often multivectors are expressed as:

	V = a + bx + cy + dz + exy + fyz + gzx + hxyz
	V = a + v + ui + hi
	where ui = V = exy + fyz + gzx
	-u = Vi = exyxyz + fyzxyz + gzxxyz
	-u = -exxyyz - fxyyzz - gxxyzz
	u = ez + fx + gy
	
Where u is a regular 1-vector not a 2vector.

Relation to cross product in 3d

	iu ^ v = iu x v  (Notice the i, has important implication on the signs)

In phisics pseudo vectors (torque, magnetic field...) are bivectors and pseudo scalars are trivectors.

	(xy)² = (yz)² = (zx)² = xyxzyz = -1
	i² = j² = k² = ijk = -1    <- Quaternions!! scalar + 2vector


Rotations: To rotate a vector v by `\theta` in the plane I (unitary vector)

	e^(I\theta /2) v e^(I\theta/2) = R* v R

	e^(I\theta/2) is a rotor

Phisics spinors are Rotors: R spins half for every 




	




En 2d:

- 0v 1v => 1v
- 1v 1v => 0v + 2v
- 2v 1v => 1v











