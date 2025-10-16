# Kotlin

## Què és?

Llenguatge pensat per substituir Java com a llenguatge multiplataforma.
Te caracteristiques més modernes com a llenguatge
però compila igualment a ByteCode de JVM.
Com comparteixen el format binari, ambdós llenguatges
es poden cridar entre ells com si fossin crides natives,
el que els fa totalment interoperables.

## Fortament tipat pero automàtic

Les variables són fortament tipades com el Java.
Pero no és necesari declarar els tipus sempre.
Sovint els tipus es poden deduir del context.

```kotlin
var a = 1
var b: Int = 1
```

Explicit casts `y.asX()`

Smart casts: Si abans d'un bloc de codi, ens assegurem que sigui quelcom ho sera
```
var a: A = whatever
if (a is B) {
    Aquí podem fer servir a com si fos un B.
}

var optional: A? = whatever
if (a != null) {
    Aquí podem fer servir a sense que sigui A i no A?
}
```

## Tipus bàsics

## Numèrics

Només els literals es converteixen de forma implicita
a un altre tipus numèric.
Per convertir dos variables o expressions
cal cridar el mètode `.toType` corresponent.
On Type seria qualsevols dels tipus:

- Sencers: `Byte` (8b), `Short` (16b), `Int` (32b), `Long` (64b)
- Positius: `UByte` (8b), `UShort` (16b), `UInt` (32b), `ULong` (64b) (Kotlin>=1.5)
- Decimals: `Float`, `Double`

Podem fer servir suffixos per forçar el tipus del literal.

- `l` força Long
- `u` força Unsinged
- `f` força Float (a un Double)

Es pot fer servir l'underline com a separador de millars o bytes

Es poden fer servir prefixos `0b` o `0x` per binari i hexadecimal.

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




## Functors

- declarats com a `myFunctor: (String) -> Boolean`
- Lambdas { param, param2 -> body }
- Si no es defineixen parameters implicitament `it`
- Function references with `::` as prefix
- The last sentence of a lambda is the return value
- If the lambda is the last parameter it can be placed outside the calling parenthesis
    - `myFunction(1) {...}`

- `object.apply(f)`: runs f with the object as this (so any variable is an attribute and function a method)


## Puzzling syntax twist

`X.method({})` can be rewriten as `X method {}`
only if method has a single parameter and the parameter is a block.
thats why we find code like:

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

## Coroutines

Coroutines are task to be run within threads.
Let you write async non-blocking code in a sequential style (or not so...)

Coroutine Scope:

- A manager for a set of coroutines.
- Defines a context.
- Defines it's life cycle.

- `launch {}` starts the block as a new coroutine
    - TOASK: is a method of a Scope

- Dispatcher decide a que thread van ciertas coroutinas
    - TOASK: Relacion entre dispatcher y scope

    - Dispatchers.Main — runs on Android’s main UI thread.
    - Dispatchers.IO — optimized for blocking IO tasks (network, file).
    - Dispatchers.Default — for CPU-intensive tasks.
    - Unconfined — starts coroutine in current thread but can resume in different thread.
    - Test dispatcher — special dispatcher used in tests (runTest), controlling virtual time and execution order.
- Funcion `suspend` 
- `withContext(Dispatchers.Default) {}` Ejecuta el bloque en un grupo de threads concretos



## The context


Get app info

val packageName = context.packageName
val appInfo = context.applicationInfo

Acces resources:

val appName = context.getString(R.string.app_name)
val color = ContextCompat.getColor(context, R.color.primary)

Start activities:

val intent = Intent(context, SettingsActivity::class.java)
context.startActivity(intent)

Access preferences

val prefs = context.getSharedPreferences("app_settings", Context.MODE_PRIVATE)
val darkMode = prefs.getBoolean("dark_mode", false)

Inflate layouts

val view = LayoutInflater.from(context).inflate(R.layout.item_station, parent, false)

val locationManager = context.getSystemService(Context.LOCATION_SERVICE) as LocationManager
val vibrator = context.getSystemService(Context.VIBRATOR_SERVICE) as Vibrator


## Flow



## Unit

Unit is like None in python.
- A void value but you can pass it, return it...

In Python None is also used as empty optional value.
Not Unit. We use `null` for that.

- `null` missing optional object
- `Unit` no meaningfull value





















