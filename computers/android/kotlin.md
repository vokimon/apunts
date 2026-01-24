# Kotlin

## Què és?

Llenguatge pensat per substituir Java com a llenguatge multiplataforma.
Té caracteristiques més modernes com a llenguatge
però compila igualment a ByteCode de JVM.
Com comparteixen el format binari, ambdós llenguatges
es poden cridar entre ells com si fossin crides natives,
el que els fa totalment interoperables.

## Fortament tipat pero automàtic

Les variables són fortament tipades com el Java.
Pero no és necesari declarar els tipus sempre.
Sovint els tipus es poden deduir del context.

```kotlin
var a = 1  // Implícit
var b: Int = 1  // Explícit
```

Downcast segur (assignar una expressió d'un tipus derivat a una variable (o paràmetre) de tipus base).
No cal fer res, sempre és segur.

```kotlin
// Downcast: sempre segur
val pet: Animal = Dog()

// Upcast: l'objecte apuntat pot no ser l'esperat
val dog: Dog = mypet // Could be a cat! it won't compile!

// Upcast requires to be explicit
// Explicit unsafe cast, raises if not a dog
val dog: Dog = mypet as Dog
// Explicit safe cast, returns null if not a dog
val dog: Dog? = mypet as? Dog
```

Smart casts: Si abans d'un bloc de codi, ens assegurem que sigui quelcom ho sera

```
var a: A = whatever
if (a is B) {
    Aquí podem fer servir a com si fos un B.
}
```

Funciona amb sentències de control, condicionals amb drecera...

## Opcionalitat

Si un valor pot ser null, forma part del tipus.
S'indica afegint un `?` al tipus de base quan no és `null`: `String?`.
Sintàcticament ens obliga a gestionar apropiadament la possibilitat de que sigui null.
Fa que en temps de compilació estem assegurant la correcció de la gestió de nulls.

Podem asignar un no nullable a un nullable, però no a l'inrevés 

```kotlin
val nullable: String? = "value"
val nonnullable: String = nullable // ERROR de compilació
val nonnullable: String = nullable ?: "Empty" // L'operador ?: retorna el segon paràmetre si el primer es null
```

Al igual que els smarts casts, si hem assegurat abans que no es null,
el compilador considera que ja està comprovat i ho considera non-nullable a partir d'aquell punt..

```kotlin
var optional: A? = whatever
if (a != null) {
    Aquí podem fer servir a sense que sigui A i no A?
}
```

## Tipus bàsics

### Numèrics

Només els literals es converteixen de forma implicita
a un altre tipus numèric.
Per convertir dos variables o expressions
cal cridar el mètode `.toType` corresponent.
On Type seria qualsevols dels tipus:

- Sencers: `Byte` (8b), `Short` (16b), `Int` (32b), `Long` (64b)
- Positius: `UByte` (8b), `UShort` (16b), `UInt` (32b), `ULong` (64b) (Kotlin>=1.5)
- Decimals: `Float`, `Double`

Si un literal numèric te decimals, per defecte sera `Double`,
si no en té, sera `Int`.
La resta de tipus s'expliciten amb sufixos:

- `l` força Long
- `u` força Unsinged
- `f` força Float (si hi ha decimals per defecte es Double)

Es pot fer servir l'underline com a separador de millars o bytes

Es poden fer servir prefixos `0b` o `0x` per binari i hexadecimal.
No hi ha octals.
Podem fer servir `_` per separar milers, bytes, nibbles...

Només els literals es converteixen de forma implícita perque
es comproven en complilació.
En altres escenarios s'ha de fer de forma explícita amb els
metodes `.toType()`: `toInt()`, `toByte()`...


`Integer` és el tipus java encapsulat.
Els nadius es mencionen com kotlin.Int,
els de java com a java.Integer.
TODO: Conversió implícita?

Els operadors de bitwise son operadors infixos amb nom.
`shl`, `shr`, `ushl`, `inv`, `

### Boleans

- El tipus es `Boolean`
- Els literals son `true` y `false`.
- Els operadors, els de C: `&&`, `||` y `!`.
- Compte Pythoners: els infixos `or`, `and`, `not` son els operadors bitwise, no pas els lògics.

### String

- Els literals per caracters `Char` van entre cometes simples `'a'`.
- Els literals per textos `String` van entre cometes dobles `"text"`.
- Es poden fer interpolacions amb `"$variable"` o d'expresions amb `"${3+3}"`.
- Un string es pot sumar `+` amb qualsevol cosa que tingui `toString`.
- Les cometres dobles triples es fan servir per literals multi linia.
- Utilitat `.trimMargin(delimiter="|") es pot fer servir per ignorar l'indentat.
- TODO: Hi havia un altre per simplement treure la indentació sense signe.
- Prefix dolars a un text serveix per dir quants dolars calen per activar l'interpolacio.
    `$$"$${aixo s'interpola} $aixo no"` `$$$"$${aixo tampoc}"
- `"%+05.3d".format(1.432)` `"%s capitalized is %1\$S".format("hola")`

### Ranges

```kotlin
// definició
range = 1..10 // inclusiu, 10 esta inclòs
xrange = 1..<10 // exclusiu, 10 no està inclós

11 in range // false
11 !in range // true
```

### Collections

`Array`.
`List`.
...

- `emptyX()` creates an `x` without elements
- `xOf(e1, e2, ...)` creates `x` including e1, e2...
- `xOfNulls(N)` creates an array with N positions but null objects

Mutability: Most collections are inmutable.
That means that modification operators are not available
changes can be done by creating a new collection or
use `x.asMutable()` to obtain a mutable version.


- `x.forEach { it }`


## Null safety

- Tipus nulables:
    - `String` no pot ser `null`, `String?` pot ser-ho.
    - un no nullable pot assignar-se a un nullable pero no pas al revés.
    - `if (var == null)`
- Crida nulla `?.`:
    - `nullable?.method()`
    - Si nullable es null, el mètode no es crida i retorna null` 
- Coalesce (elvis) operator `?:` 
    - nullable ?: "default"
    - L'expressió retorna el valor de nullable pero si es `null` retorna `"default"`
- Idioma `.?let {...}`
    - el block s'executa només si el receptor no es null
    - El receptor dintre del block es pot referir com a `it`
    - Podem explicitar un nom diferent amb `{ name -> ... }`
    - Retorna el resultat de la lambda


## Functors

- declarats com a `myFunctor: (String) -> Boolean`
- Lambdas { param, param2 -> body }
- Si no es defineixen parameters implicitament `it`
- Function references with `::` as prefix
- The last sentence of a lambda is the return value
- If the lambda is the last parameter it can be placed outside the calling parenthesis
    - `myFunction(1) {...}`

- `object.apply(f)`: runs f with the object as this (so any variable is an attribute and function a method)


## Scope functions

Son molt similars.
Difereixen en com rep el bloc el context, i en què retornen:

El bloc pot rebre context com a paràmetre del bloc (per defecte `it`)
o com a this.
Si ho rebem com a `this` és com si el bloc fós un mètode de l'objecte,
podem fer servir els atributs i mètodes sense prefixar `receiver.`.
Per un altre banda podem retornar el resultat del bloc o recuperar el `receiver`.


- `receiver.let {...}`
    - Rep `it`, retorna el resultat.
    - Ús: Per executar blocs assegurant-nos de que no es null amb `?.`
    - Ús: Donar nom al resultat d'una expressió dins d'un bloc.
- `receiver.run {...}
    - Rep `this` retorna el resultat
    - Ús: Quan cridem molts mètodes o atributs d'un objecte
- `receiver.apply {...}`
    - Rep `this`, retorna `receiver`
    - Ús: Configuració de l'objecte. Podem aplicar-ho al constructor, applicar setters i el resultat assignar-ho.

    ```kotlin
    val person = Person().apply {
        name = "Pepito"
        age = 12
        isStudent = true
    }
- `receiver.also {...}`
    - Rep `it`, retorna `receiver`
    - Ideal per fer coses addicionals a l'objecte pero acabant retornar sempre l'objecte (side effects)

Altres similars

- `with(context) {...}`
    - Com `run` pero més idiomàtic fent servir el parametre en comptes de receptor.
- `run {...}`
    - Funció lliure no hi ha receptor
    - Retorna el resultat del block
    - Ús: Quan volem executar diverses sentències on sictàcticament hi va una expressió.


| returns  | `it`    | `this` |
+----------+---------+--------+
| block    | `.let`  | `.run` |
| receiver | `.apply`| `.also`|


Tambe tenim les condicionals que retornen els objectes o null segons la condició del bloc.

```kotlin
object.takeIf { condition } 
object.takeUnless { condition }
```

Ens permeten tornar els casos excepcionals en `null` i,
a partir d'aquest punt, gestionar el cas excepcional
fent servir els mecanismes de gestió de nulls.

## Extensions, infixos i operadors

Les extensions son mètodes que definim a posteriori
Permeten definir nous mètodes a classes ja definides, fins i tot les estàndars.

```kotlin
fun ExistingClass.newMethod(...): ... { ... }
```

Els infixos son paraules que podem insertar entre mig de dos objectes.
Semblants als operadors `or`, `and`, `not` de Python.

```kotlin
// definition:
infix fun ReceiverClass.myinfix(parameter: ParameterClass): ResultType {...}
// usage:
receiver myinfix parameter
```

De forma similar es poden definir operadors, fent servir noms donats i
la paraula clau `operator`.


```kotlin
// definition:
infix fun ReceiverClass.plus(parameter: ParameterClass): ResultType {...}
// usage:
receiver + parameter
```

Per a fer servir una extensió **cal importar-la des del mòdul on es defineix**.


Des de Java, equivalen a una crida a mètode stàtic.
Els operadors són funcions amb el nom de l'operador (plus, minus...).
Es pot canviar el nom de la classe que inclou el mètode estatic
amb la directiva `@file:JvmName("MyStaticClass")`


## Puzzling syntax twist

`X.method({})` can be rewriten as `X.method {}`
only if method has a single parameter and the parameter is a block.

Likewise infix methods appear without the `.`.

Thats why we find code like:

```kotlin
a {} b {} c {}
```


## Full featured enums: Sealed classes

- `sealed class` restricts inheritance to the subclases defined within its body.
It can be used as power enums having attributes.

```kotlin
sealed class Event {
    object Started : Event() // singleton class
    object Ready : Event()
    data class Failed(val error: String) : Event()
}

val event1: Event = Event.Started
val event2: Event = Event.Ready
val event3: Event = Event.Failed("An error")
if (event3 is Event.Ready) {
    println(event3.error) // Safe cast! kotlin knows you checked already the type
}
(event3 as Event.Failed).error // 'as' will raise if bad cast
event3 as? Event.Failed).?let { it.error } // 'as?' returns null on bad cast

RepositoryEvent.UpdateReady

```




## Unit

Unit is like None in python.
- A void value but you can pass it, return it...

In Python None is also used as empty optional value.
Not Unit. We use `null` for that.

- `null` missing optional object
- `Unit` no meaningfull value



## Generics

### Genericos vs Templates vs DuckTyping

Els templates de C++
i el duck typing de Python permeten
fer servir el mateix codi per més d'un
tipus d'objecte encara que no siguin de la mateixa
jerarquia d'objectes,
simplement que tinguin les operacións i metodes que es fan servir.

C++  en temps de compilació,
genera codi per cadascun dels tipus
pels qual el template s'instancia (fa servir).
En fer-ho simplement comprova que el tipus
instanciat funciona bé amb la definició:
Té els mètodes i operadors que es fan servir...

Python en canvi ho comprova en temps d'execució
cada cop que es criden a mètodes o operadors,
es comprova si l'objecte els te.

Per objectes de la mateixa jerarquia podem fer servir polimorfisme.
Es genera una sola implementació i es fa servir la interfície comuna.


Els generics, de fet es una encapsulació del polimorfisme
i nomes es poden definir amb tipu parametres
pertanyents a una jerarquia.


Tanto los templates de C++ en tiempo de compilación
como el Ducktyping de Python en tiempo de ejecucion,
permiten reaprovechar el mismo código para diferentes
tipos de objetos siempre que soporten los metodos y
operadores que se usan en el codigo comun.

Això no passa amb els genèrics.
Els tipus paramètrics dels genèrics
sempre parteixen d'un tipus base
i generen codi polimorfic,

els casts automatics al tipus.

Los genericos no permiten implementaciones generalizables
como los templates de C++ o el DuckTyping

### Declaracions

Permeten declarar coses deixant d'especificar un tipus.

```kotlin
fun <T> genericFunction(value: Array<T>): T { .... }
fun <T> Array<T>.extensionFunction(): T { .... }
class <T,A,B> GenericClass(...) {...} // Using more than one type
```

### Ús

Es fan servir posant el tipus concret entre `<>` despres del nom.
Tot i que podem obviar-ho si es deduible dels paràmetres.
```kotlin
genericFunction<Int>(myIntArray) // explicit
genericFunction(myIntArray) // implícit
```

### Constriccións

Dintre del cos de la funció es pot usar T com si fos
`Any?`, el tipus base de tots els objectes i a més opcional.
Si volem fer-ho servir per alguna cosa més
caldrà restringir el tipus.

```kotlin
fun <N: Number> genericFunction(array: Array<N>): N {
    val result: N = 0
    foreach(n in array) {
        // Com es un Number els podem sumar
        result += n
    }
    return n
}
```

- No, no hi ha comprovacio en instanciació com fa C++.
- Si volem que no sigui opcional hem de posar `Any`
- Oximoron: Si no 'restringeixes' el tipus, no pots fer les coses del tipus

### Variança

La variança defineix com es comporten
des del punt de vista de la jerarquia de classes
les classes templatitzades.
Es a dir si les classes templatitzades
reprodueixen o no la jerarquia dels paràmetres.

Exemple, si tenim `Any -> Number -> Int`,
es compleix la jerarquia `Array<Any> -> Array<Number> -> Array<Int>`?

Perqué es important?

Determina si una classe templatitzada es subtipus d'una altra
ens permet saber si podem assignar un valor d'un tipus a una variable d'un altre.

```kotlin
val super: MyTemplate<Super> = MyTemplate<Sub>() // nomes si T es out, variança
var sub: MyTemplate<Sub> = MyTemplate<Super>() // Nomes si T es in, contravariança
var a: MyTemplate<A> = MyTemplate<A>() // La unica que pots fer si no es ni in, ni out

```

TODO: No he acabat d'entendre l'efecte ni el sentit.
















