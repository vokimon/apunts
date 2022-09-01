Mathematical object: numbers, permutations, partitions, matrices, sets, functions, relations...

Property:
	A function for a set of objects (of a given type) 
	that renders true or false.
		p: X -> {true, false}

Relation:
	A property assigned tuples of objects.
	Holds true or not for a given tuple of objects.
		r: x1,x2,..,xn -> {true, false}
	Arity: number of objects in the tuple

Set: Object related to other objects by a membership/inclusion relation.
	Inclusion: a relation holded between a set and its members
	Cardinality: number of included objects
		Same if bijection relation can be stablished
	Subset S1<S2: all elements in S1 are also in S2
		Any set S has {} and S as subsets
	Powerset P(S): The set of all the subsets of S

Mathematical structure:
	Defined in a type/set and several related mathematical objects:
	measures, algebraic structures, topologies, metrics measures,
	orders, equivalence relation, differential structures...
	By mapping one set to another but also mapping the structure
	we can extrapolate the properties of the structure.

Algebraic structure:
	A set closed under a collection of operations defined by axioms.
	Operations take 0 to inf elements and return an element a.
	By reducing the axiomatic requirements of one structure to get its
	properties, we ease mapping those properties from one known
	set to a new unknown one.
	wp:Algebraic_structure

Homomorphism: Exists a map (morphism) from one algebraic structure
	to another so that the algebraic structure is preserved.
	A function f:A->B such that, for any n-ary op \mu, 
	there exists an operator \mu_B such that, that for any a_i€A,
		f(\mu_a(a_1,..,a_n)) = \mu_b(f(a_1),..,f(a_n))
	Other homomorphisms:
		Epimorphism: Surjective (No element in the target gets unrelated)
		Monomorphism: Injective (No element in the target gets related more than once)
		Isomorphism: Bijective (Surjective and Injective)
		Endomorphism: Of an object to itself
		Automorphism: (Bijective and Endomorphic)
Isomorphism: When the map can be reversed by an homomorphic inverse map

Substructure: A subset of the structure that still fullfils axioms
Product: "cartesian product of the set, redefining the ops"

Why is that useful?

Everything you learn about an algebraic structure
you can also apply it to a different new one if the axioms are meet.

Typical axioms for algebraic structures:
	(Binary) Closure(S,%): %:X,X->X ~:X->X
	Totality: Defined for any element in the domain
	Conmutativity: a%b=b%a
	Absortion law: a$(a%b)=a%(a$b)=a  (like in boolean)
	Associativity of %: (a%b)%c=a%(b%c)
	Distributivity % over $: a$(b%c)=(a%b)$(a%c)
		No conmutative -> left, right, two-sided (above is left)
	Identity: Exists a I so that a%I=a fore every a
		No conmutative -> left, right or two-sided identity (above right)
	Invertibility: For each a, exist b | a%b=I
		No conmutative -> left (a) and right (b) inverses
		No associative, left or right inverses might not be unique
		R,+ negation
		R(but 0),· inverse
	Idempotence Unary: f(f(a))=f(a), f(a,a)=a
		ie. I(a), constantK(a), abs(a)
		If it just applies to some elements a, a is an idempotent element
	Idempotence (version 2): f(f(a))=a 
		ie. complex negation, conjugation, multiplicative inversion...
	Cancelation: a%b=a%c -> b=c (generalizes invertivility)
		No conmutative, left, rigth or two-side cancellable (above left)

Closure operator C(S) on a operator %:
	C$(S) = {
	Gives minimum set that is closed for a given operation that 
	includes S.
	ie. Closure of naturals respect the substraction operator is the integer set
Inverse operator of an operation:

Single binary op structures:
	Magma: {S,+} + binary
		Closure
	Semigroup: (S, ·_S)
		Closure, Associativity
	Monoid: Algebraic structure of a set S and an operation $ with axioms:
		Closure, Associative, Identity
	Group: Algebraic structure of a set S and an operation $ with axioms:
		Closure, Associability, Identity, Invertibility
	Abelian group:
		Closure, Associability, Identity, Invertibility, Conmutative

Two binary ops structures:
	Ring: Algrebraic structure with notion of +,-
		Abelian group for +
		Monoid for ·
		Distributibity on · over +

Conmutative Ring:
	Ring
	Conmutative ·

Field: Algebraic structure with notion of +,-,·,/. and 
	Closure on + and ·
	Associativity on + and ·
	Additive (O) and multiplicative (I) identities (O!=I)
	Additive (-x) and multiplicative (1/x) inverses (implies - and / ops)
	Distributivity of · over +
	Examples:
		Naturals (N): 0,1,2,3... (NOOO!)
		Integers (Z): ...,-3,-2,-1,0,1,2,3,...
		Rational (Q): 
		Algebraic (A):
		Complex: (C): 

Product space: TODO

Vector space over a field F: {V,F,+,·}
		V is the space
		F is a field (naming F·, F+, F1, F0)
		+ is a binary operator VxV->V
		· is a binary operator FxV->V
	Math. structure, formed by a collection of objects (called vectors)
	that can be added each other and multiplied by a member of the
	field (called scalar) with the following axioms:
	Abelian {V,+}
		Associativity +: u+(v+w)=(u+v)+w
		Conmutativity +: u+v=v+u
		Identity +: u+0=u, 0 is zero vector
		Invertibility on +: foreach v, exist w | v+w=0. v additive inverse of w
	Ring Homoformism f (·) from F to endomorphism ring of the V
		Distributivity of · respect +: a·(v+w) = (a·v)+(a·w)
		Distributivity of · respect F+: (a+b)·v = (a·v)+(b·v)
		Compatibility of · with F·: a·(b·v) = (a·b)v
		Identity on ·: FI·v = v

	TODO: wp:vector space

Vector space does not imply: nearness, angles, distances


Metric space: A set where the notion of distance is introduced
	(M,d), distance function d:MxM->R, with axiomas:
	1 Non-negativity: d(x,y)>=0
	2 Identity of indiscernibles: d(x,y)=0 <-> x=y
	3 Symmetry: d(x,y)=d(y,x)
	4 Triangle inequality: d(x,z) <= d(x,y) + d(y,z)
	You can get 1 from 2+3+4 but often we drop one to form
		Pseudometric: dropping 2
		Quasimetric: dropping 3 (d'x,y=(dxy+dyx)/2 to get a metric)
		semimetric: dropping 4

	A map f is an isometry if d2(f(y),f(x)) = d1(x,y)

Complete metric space: 

Normed vector space: (V,||·||) an V.S. with notion of length of vector
	||.||:V->F, a norm in V (F is C or R), axioms
	1. Positive definitenes: ||x||=0 <-> x=0
	2. Positive homogeneity: ||ax|| = |a| ||x||
	3. Triangle inequality: ||x+y|| <= ||x||+||y||
	1+2 -> p(v)>=0 <-> v!=0
	Aka Euclidean vector space
	Dropping 1 we have a seminormed space and the seminorm

Inner product space: (V,<·,·>)
	Vector Space with an inner product <·,·>
	<·,·>: VxV->F, with axioms:
	1. Conjugate (Hermitian) symmetry: <x,y> = \overline{<y,x>}
	2. Linearity in the first argument (Sesquilinearity):
		<ax, y> = \overline{a}<x,y>,  <x+y,z>=<x,z>+<y,z>
	3. Positive definitenes: <x,x> > 0, if x!=0
	* Properties:
	Implies 1,3: <x,x>=0 <-> x=0
	Implies 1,2: <x,ay>=\overline{x}<x,y>
	Implies 1,2: <x,y+z>=<x,y>+<x,z>
	||x|| := sqrt(<x,x>) is a norm so is a Normed Vector Space
	So sesquilinear and hermitian symmetric with F being C
	So biliniar and symmetric with F being R
	angle(x,y)=arcos(<x,y>/sqrt(<x,x>*<y,y))
	x and y are orthogonal when <x,y>=0 (linear independence)
	* Notes:
	Phisics and matrix algebra <|> is defined with Sesquilinearity on the second argument instead of the first.
	for V=C^n, <x,y> = y*·M·x where 
		M is a Hermitian matrix (TODO)
		y* is the conjugate transpose of y
	For V=C^R (functions)

Completely normed space:
	TODO: Que no viene a ser una esponja?

Euclidean space: 

Hilbert space: Inner product space over R or C with its 
	norm definned by ||x||=sqrt(<x,x>)
Bannach space: Completely normed space over R or C


Preorder: binary relation (<~) on a set X which is:
	Reflexive: a<~a
	Transitive: a<~b<~c -> a<~c
	Examples:
		Logical implication x->y
		Nets
		x<=y <=> f(x)<=f(y) f:X->Y and Y is POset
Equivalence: binary relation (~) on a set X which is:
	Preorder (Reflexive and Transitive props)
	Symetric: a~b <-> b~a
	"A given common trait"
	Examples: congruence
	Equivalence class of a: [a] = {x€X|x~a} (Set of equivalent to a)
	Quotient set: X/~ := {[x]|x€X} (the set of classes of X on ~)
	Projection: \pi: X -> X/~  (maps an element to its class)
	Equivalence kernel of a function x~y <=> f(x)~f(y)
Equality: binary operation (=) which is:
	Equivalence (Reflexive, Transitive, Symetric)
	Anti-symmetric: a=b and b=a -> a'='b
	* For all property P, P(x) <=> P(y) (not identity but 
Partial order: binary relation (<=) on a set X which is:
	Preorder:
		Reflexive: a<=a
		Transitive: a<=b<=c -> a<=c
	Anti-symmetric: a<=b and b<=a -> a=b
Strict partial order (<):
	Irreflexivity: no x<x
	Asymmetry: x<y <-> no y<x
	Transivity: x<y, y<z -> x<z
	* Follows:
	Trichotomous: Either one of a<b, b<a, a=b is true
Strict and non-strict PO's correspond 1-to-1 by:
	a<b  <=>  a ≤ b and not a=b
	a<=b  <=>  a<b or a=b
The inverse relation of <= is > which is a strict PO
Thi inverse relation of < is >= which is a weak PO
So, defining one of the four operators defines the other three.

Total order: a partial order which also fullfils:
	Totality: a<=b or b<=a (if not it is a partial order)
	Totality implies reflexivility, so no need to check
	Examples non-total orders but still partial:
	- Subset €=: Not being a subset does not imply being a superset
	- Divisible a|b: Not being divisible does not imply being a multiple

Partially ordered set (poset): {P,<=
Interval: a subset of a partially ordered set so that
	its members 
	
Ordered field: A field which is total ordering and axioms:
	a<=b -> a+c<=b+c
	0<=a and 0<=b -> 0<=a·b
	* Follows:
		-a<=0<=a or -a<=0<=a
		a<=b and c<=d -> a+c<=b+d
		a<=b and c<=0 -> ac <= bc

Ordinal number: The one used to describe the position of a term in a sequence
Cardinal number: The one used to describe the size of a set
	Size(S1)<=Size(S2) if exists injective mapping S1->S2

Lattice (Reticulo): a poset (L,<=,v,^) that fullfils:
	Two definitions: 
		by axioms and infering <=
		by <= and deducing axioms as properties
	A join (avb) (supremum) is defined for every a,b€L
		Commutative xvy=yvx
		Associative xv(yvz) = (xvy)vz
		Idempotency xvx=x
		Consequences, we can define x<=y <=> xvy=y
	A meet (a^b) (infimum) LxL->L
		Conmutativity x^y=y^x
		Associativity  x\land(y\land z)=(x\land y)\land z
		Idempotency: x^x=x
	Join/meet Semilatices: just one of the two.
Completeness:
	The existence of a? supremum and and infimum whithin the set
Interval: A subset I containing all the elements of a set S
	which has a supremum and an infima in S
	Open or closed depending on the infima/supremum being also in I

Sequence: an ordered list of objects (called terms)
	A function from N+->S,
	Finite: (a1,a2,...,an) a function s:Z+->S
	Infinite: (a1,a2,...)
	(an)
Subsequence: removing terms without altering relative order
Directed set:
	A Preorder set (reflexive, transitive)
	Every pair of elements have an upper bound 
	* UB but not least UB, as join latices
	* Generalizes sequences

Sigma-Algebra: Subset Σ of the power set of X so that 
	1. Not empty
	2. Closed under complements
	3. Closed under countable unions

Measure space: (X,Σ,μ)
	Measure: μ:Σ->RU{+-inf}
	Measurable sets: Σ is a σ-algebra on X, and
	1. Non-negativity: μ(E)>=0
	2. Null empty set: μ(Ø)=0
	3. Countable additivity: Ei are countable disjounts sets in Σ
		the measure of the union is the sum of the measures
	Related:
	Measurable space: (X,Σ)
	Signed measure, if the first axiom is out
	Probability space: (X,Σ,μ) so that μ(X)=1 (prob. measure)
	* Properties
	Monotonicity E1€=E2 -> mu(E1)<=mu(E2)
	See wp:Measure for more

Topological Space:
	Allow formal definition of: convergence, connectedness, continuity.
	A set X and a collection T of subsets on X, so that:
		The empty set is in T
		The union of any collection of sets in T is also in T
		The intersection of any collection of sets in T is also in T
	T is named a topology on X
	Neighbourhood of a point x: any set in the topology that cointains x
	Neighbourhood system of x: Any set that is neighbourhood of x
Net: any function from some directed set A to a topological space X
Directed set: A set with a reflexive and transitive binary relation <=,
	so that every pair of elements has an upper bound

Continuity of a map f:X->Y at x:
	Given a neighbourhood of V€Y of f(x) exist a neighbourhood U€X
	so that f(U)€V.
	Generalizes real functions continuity without involving distances.
	* Properties given f:X->Y, g:Y->z continuous:
		gof:X->Z is cont.
		X compact -> f(X) compact
		X connected -> f(X) connected
		X path-connected -> f(X) path-connected


Coordinate space F^n: Space of the tuples of n objects of the field F
	n is finite
	Alternative def: TODO: Product space? of F over a finite index set J
	Elements can be seen as functions from index in J to values in F,
		f: J->F
	Element notation x^ = (x_1, x_2,...,x_n) 
	Also as row or column vector in matrix algebra
	Coordinate space forms a vector space by defining
	x^ + y^ = (x_1+y_1, ..., x_2+y_2)
	a·x = (a·x_1,...,a·x_2)
	0^ = (0,...,0)
	-x^ = -1·x^

Every n-Dimensional vector space V over F is isomorphic to F^n
Not a canonical isomorphism, it depends on the chosen basis
to make the map.

Function space:

Euclidean Vector: 


Linear map f:X1->X2, X1 and X2 vector spaces over the same field K
	Additivity: f(x+y) = f(x)+f(y)
	Homogeneity of degree 1: f(ax) = af(x)
	Follows: f(a1x1+a2x2+...+anxn)=a1f(x1)+...+anf(xn)
	Follows: f(0)=0

K-Linear map: X1, X2 are vector spaces over different fields and K is the one so that the scalars in 
A linear map f can be represented by a matrix nxm 
	
Linear functional: A linear map from a function to its Field
	Rieman (definite) integral over the functional vector space
	Evaluation of polinomials Pn
	Distributions

Lie Algebra: Vector space R over some field F with op [·,·] such that:
	1 Bilinearity: [ax+by,z] = [ax,z] + [by,z]
	2 Anticonmutative: [x,y] = -[y,x]
	3 Jacobi Identity: [x,[y,z]] + [y,[z,x]] + [z,[x,y]] = 0
	Follows:
	4 From 2: Alternating: [x,x] = 0
	Examples: 
		R3 and vectorial product



TODO: wp:quaternion






