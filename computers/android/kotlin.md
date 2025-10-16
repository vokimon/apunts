# Kotlin

## Què és?

Llenguatge pensat per substituir Java com a llenguatge multiplataforma.
Te caracteristiques modernes pero compila a ByteCode de JVM.
També pot cridar funcions de java com si fossin natives.





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





















