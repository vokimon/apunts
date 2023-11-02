# Geometric algebra

https://www.youtube.com/watch?v=60z_hpEAtD8
https://www.youtube.com/watch?v=0bOiy0HVMqA (Addendum)
https://www.youtube.com/watch?v=2hBWCCAiCzQ&list=PLVuwZXwFua-0Ks3rRS4tIkswgUmDLqqRy (From zero to Geo)

Close but different concepts:

- Clifford Algebra: is the mathematical abstraction, not applied to physics
- Algebraic geometry: Algebraic description of geometries. Not to be confused with.

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
	- Add components of axis representation


Trivector: Oriented volume

- Magnitude
- Orientation? In 3D inside and outside.
	- a k-vector in a k-space just can have those two orientations
	- ie. vector in a 1D can be positive or negative, 2-vector in 2D can be facing up or down

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


## Operations

::: youtube https://www.youtube.com/watch?v=2AKt6adG_OI

Object Generalization

- k-vector
	- k-dimensional subspace
	- Magnitude
	- Orientation
- k grade multivector: sum of j-vectors of dimensions j up to k

Operation Generalization

### Grade projection operator

- `<A>_k`
- The k-vector part of A
- Example `<3e0 + 5e12 + 4e01 + e012>_2 = 5e12 + 4e01`

### Geometric product

- Geometric vision
	- in VGA the geometric product of 2 vectors
		- parallel, is product of their lengths, negative if different directions
		- perpendicular, the bivector span of the two vectors
		- Thus contracts parallel, joins perpendicular
		- oblique vectors, we can decompose the second vector in a perpendicular and a parallel
			- uv = u(v|| + vT) = uv|| + uvT
	- Generalization:
		- given a basis e1,...,en
		- basis are perpendicular so the product of two different of them gives the bivector of the span, which anticonmutes
			- eiej = -ejei
		- when multiplying with it self, is paralel so the result is a scalar
			- in VGA the scalar is 1 but in others might be 0, 1, or -1 for each basis.
			- Indeed which basis squares to what caracterizes the geometric algebra we are using
		- algebraically:
			- distribute the multiplication keeping the order of the basis
			- swap the basis order by swapping the sign of the term (each pair swapped a sign change)
			- apply squares to scalar mapping
				- 0: remove term
				- 1: remove dupped basis
				- -1: remove dupped basis inverting the term sign
		- transformations:
			- auv = rotate `a` the angle between `u` and `v`
				- vua = rotate `a` the angle between 
 



- Products:
	- **Geometric product:**
		- of two vectors:
			- Paral·lel: Scalar from multiplication both magnitudes with negative sign if they are opposite directions
			- Perpendicular: bivector span of two vectors
			- Contracts parallels, joins perpendiculars
			- Neither parallel neigher perpendicular: split one of them into a parallel and 
	- **Outer product:**
		- A^B
		- Span: the smallest subspace containing the inputs
		- If linear dependent 0 else the span subspace
		- Algebraically, like geometric product but considering all basis square to zero
		- j-vector ^ k-vector = (j+k)-vector
		- Aj ^ Bj = <AjBj>k+j (outer product is equivalent of to the k+j grade projection of the geometric product)
	- **Regressive product:**
		- AvB = (Ai ^ Bi)/i
		- the largest subspace contained in both subspaces
		-  
	- **Inner product:**
- Involutions:
	- **Reverse:** Invert the order of the basis of each kvector
	- **Grade involution:** Invert the sign of odd k-vector components 
- Other
	- **Dual:** Orthogonal complement
		- Ai (pero no funciona cuando alguna base se cuadra en 0)
	- **Grade Projection:** Take the k-vector part of a multivector
	- **Magnitude:**


- **Grade projection:** `<A>_k` k-vector part of a multivectora (without k subscript, means 0)
- **Grade k multivector:** A multivector that just have a k-vector component


### Reverse

Given a product of multivectors, the product in the reverse order.

`(uvw)† = (wvu)`

Useful becaue of rotation. `R u R†`

Because it is linear, we can apply the reverse to its components and extract factor.
So you can obtain the reverse of a multivector by applying the reverse to their kbasis,
which corresponds to a sign change or not depending on the number of basis.

`(e1..n)† = en (e1..n-1)† = (e1..n-1)† en (-1)^(n-1)`

Every 2k swaps the sign


- k=0: + ie. (a)† =  a
- k=1: + ie. (a e1)† = a(e1)† = a e1
- k=2: - ie. (a e12)† = a(e12)† = ae21 = -a e1 e2
- k=3: - ie. (a e123)† = a(e123)† = a(e321) = -ae231 = +ae213 = - ae123

### Grade involution

`u*` 


Linear and multiplicative

`(A+B)* = A* + B*`

`(aA)* = a A*`


`(AB)* = A* B*`


### Magnitude squared

`|A|^2 = <A† A>`

- Scalar part of the multiplication with its reverse is the square of the magnitude
- Squared root is not appliable to some squares which are negative
- Scalar product with itself does not compute, use the inverse
- Some vectors squared are multidimensional, just take the zero



## Projective Geometric Algebra

https://www.youtube.com/watch?v=0i3ocLhbxJ4

### In 2D euclidean space

- We use a 3D space e0 representing infinity
	- Basis e0, e1, e2
	- ei ej = - ej ei,  i!=j (anticonmute)
	- e0 · e0 = 0   this is different
	- e1 · e1 = 1
	- e2 · e2 = 1
- Vectors represent lines:
	- `ax + by + 1 = 0` is represented as `c e0 +  a e1 + b e2`
	- `e1` and `e2` are the horizontal and vertical lines passing by origin
	- `e0` is a line at infinity  ????
	- Scalar multiplication of the vector represents the same line
	- Normalized by seting 1 the e0 coefficient unless it is zero
- Linear combination of two lines
	- A linear combination of two lines is a line passing by their intersection more or less parallel to one or the other depending on the ratio of their coefficients
	- A plain addition is the bisectrix
	- Adding a e0 component is translating the line keeping the slope
- Inner product:
	- a·b = |a||b|cos theta
	- e0 component gets removed
		|a|² = a a
		= (ae1 + be2 + ce0) (ae1 + be2 + ce0) = 
		= ae1ae1 + ae1be2 + ae1ce0 +be2ae1 + be2be2 + be2ce0 + ce0ae1 + ce0be2 + ce0ce0 =
		= aa + ae1be2 + ae1ce0 +be2ae1 + bb + be2ce0 + ce0ae1 + ce0be2 =
		= aa + ae1be2 + ae1ce0 -ae1be2 + bb + be2ce0 - ae1ce0 - be2ce0 =
		= aa + bb
	- Parallel if `|a·b| = |a||b|`
	- Perpendicular if `a·b = 0
	- TODO: demostrar que las paralelas son la misma añadiendo un `alpha e0`
- Bivectors represent points: e12 + Xe01 + Ye20
	- A bivectors represents the subspace created by the linear combination of two vectors
	- A bivector of two lines are the set of lines passing by the intersection
	- Indeed they can be sumarized by the intersection, the point
	- `p = e12 + x e20 + y e01` normalizando e12 a 1
	- points with no e12 component are points in infinity at the given direction
- Outer product of two vectors. Meet `A^B` Intersection of two lines
	- TODO: derivation
	- The meet of two parallel lines is the point at the infinity on the direction at the lines
- Regresive product of two points: Join. `AvB`
	- The intersection subspace of the two points
	- That is the line that joins the two points
	- TODO: derive the formula
- Inner product:
	- Two points, not that interesting -a3b3
	- aB (line·point): The perpendicular line passing by the point
- Projection `(A·B)B` Projection of A into B
	- Project a point A into a line B: Intersect the perpendicular line with the line (a·B)a
	- Project a line to a point: (a·B) Perperdicular passing by B, to the line Perpendicular to a passing by B
- Geometric product:
	- Reflection: uau refleja a respecto a u
	- Rotation: vuauv rota a el angulo entre u y v
	- Translation: vuauv (u i v paralelas) traslada a el doble de la distancia entre u i v
	- Same for points: TODO: Develop from a point as a intersection of two lines

## Extension to 3d

Objects:

- Planes
- Lines
- Points

Meets:

- 2 planes -> line
- plane + line -> point
- 3 planes -> point

Joins:

- 2 points -> line
- 3 points -> plane
- point + line -> plane

Projections:

- Plane <-> Point <-> Line <-> Plane

Basis:

- In 3D geometry we use 4D geometrical algebra
- Vectors are planes:
	- ae1 + be2 + ce3 + de0  <-> ax + by + cz + d = 0
- Bivectors are the span of two vectors (planes), the set of planes share the intersecting line -> lines
	- a e01 + b e02 + c e03 + x e12 + y e13 + z e23
- Trivectors are the span of three vectors (plane), they share the point -> points
	- e123 + x e032 + y e013 + + z e021

Operations

- Meet: A^B whichever the objects
- Join: AvB whichever the objects
- Inner Product: 
	- General: object perpendicular to the higher dimensional object passing by the lower dimensional object
	- plane · line: Perpendicular plane passing by the line
	- plane · point: Perpendicular line to the plane passing by the point
	- line · point: Perpendicular plane to the line passinb by the point
- Projection: (A·B)·B


























