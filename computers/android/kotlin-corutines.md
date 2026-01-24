# Kotlin: Corutines

## Concepte

Una co-rutina (coroutine) és una tasca
que s'executa de forma concurrent a d'altres
que cooperen per tenir el fil d'execució (thread) aprofitat.

Conway, M. E. (1963). Design of a separable transition-diagram compiler.

**Suspensió cooperativa:**
Una co-rutina podria ocupar el fil d'execució fins que s'acabés,
evitant canvis de context que trenquen l'eficiència,
però, si fem operacions bloquejants,
voldríem que el cedís (yield)
a altres co-rutines per a que l'aprofitin.

En contrast, els fils (threads) i processos de sistema,
no cooperen sinó que el sistema aplica preempció,
es a dir, un canvi de tasca forçat per un supervisor.
En aquest cas ha de ser així perque els processos i fils
no cooperen sinó que competeixen pel temps de CPU.
Les corutines son totes del mateix programa i poden cooperar
per estalviar tant infrastructura de gestió com canvis de contexts innecessaris.

## Funcions suspendibles (`suspend`)

Una funció suspendible o `suspend`,
té la capacitat de parar la seva execució,
guardant-se l'estat de l'execució
(variables locals i punt d'execució)
i rependre-la quan se li indiqui.

Es declaren amb la paraula clau `suspend`:

```kotlin
suspend func mySuspendable() {
    // Here we might call other suspend functions or regular function
}
```

Només una funció suspend pot cridar a una altra funció suspend.
Una funció suspend pot cridar a una funció normal, pero no pas a l'inrevés.
D'aquesta manera Kotlin assegura en temps de compilació que
les funcions suspend formen part d'un context de  corutina.
Sent la primera funció suspend de la corutina
la que se li passa en forma de bloc a una funció
_creadora de corutines_ o _coroutine builder_.
Per exemple:

```kotlin
launch { // funció creadora de corutines
    // Aquest bloc és un paràmetre declarat a la funció launch com a suspend
    // Pot cridar funcions suspend o funcions normals
}
```

## Detalls d'implementació de les funcions suspend

Això ajuda a entendre què està passant amb les funcions suspend.

Si del nostre bloc es fa una cascada de crides a funcions suspend
i la darrera fa una suspensió real o primitiva,
cada funció suspend guarda l'estat i notifica a la seva cridadora `COROUTINE_SUSPENDED`,
per que faci el mateix fins que tot l'stack a guardat l'estat.

Per tant, els punts de suspensió possibles d'una funcio suspendible
son les crides a d'altres funcions `suspend`.
No es pararà en mig de la resta de codi,
ni a una funció no suspend.

D'una altra banda, el fet de que es cridi a una funció suspend
no té perque generar una suspensió
si al final no es crida cap funció suspend _primitiva_.

## Creadores de corutines

A kotlin fem servir funcions especials anomenades
_creadores de corutines_ o _courutine builders_,
a les quals passem com a paràmetre un block suspend.

Els coroutine builders son:

- `runBlocking`: Bloqueja fins que la corutina acaba i retorna el resultat.
- `launch`: Dispara i oblida-te'n.
- `async`: Quan volem un resultat pero no esperar-nos.
- `coroutineScope`: crea una corunina mare per agrupar un grup de corutines filles en un Job.
- `supervisorScope`: igual que `coroutineScope` però, aïlla les filles de la mare (podem cancelar les filles sense cancel·lar la mare)

### `runBlocking`

- `runBlocking {...}`/`runBlocking(context) {...}`
- `import kotlinx.coroutine.runBlocking`
- Es una funció lliure
- Retorna el resultat del bloc
- Bloqueja el fill actual fins que acabi la corutina
- Es fa servir pel main o per fer testos de corutines

### `launch` dispara i oblida

- `CoroutineScope.launch {...}`
- Crea una corutina sense resultat, `fire and forget`
- Es una extensio de CoroutineScope, pero cal fer l'import
    - `import kotlinx.coroutine.launch`
- Retorna un Job, que permet
    - cancelar: `job.cancel()`
    - esperar el final: `job.join()`
    - consultar l'estat: `job
- Abans d'acabar, la corutina mare s'espera a les filles
- Excepcions no gestionades:
    - cancel·la totes les corutines de l'abast (mare, germanes, filles...)
    - Això no vol dir que es parin les que estan en execució
    - TODO: Cancel para les suspended? Cal escolar els cancels de forma activa?

### `async` calcula i ja em donaràs el resultat

- `CoroutineScope.async {...}`
- Quan volem obtindre el resultat, però no parar-nos
- Es una extensio de CoroutineScope, pero cal fer l'import
    - `import kotlinx.coroutine.async`
- Retorna `Deferred` que deriva de Job, i permet
    - Totes les operacions de Job, i
    - `deferred.await()` s'espera al resultat (suspenent la funció si no està disponible encara)
- La mare també espera a les filles abans d'acabar
- Excepcions, es guarden i es llencen
    - En fer l'await
    - Quan la mare espera a les filles.
    - Si es fa join, s'ignora l'excepció

## Funcions suspendibles (`suspend`)

Una funció suspend pot no arribar a suspendre l'execució.
Les que ho fan son les primitives de suspensió (evidentment, tambe `suspend`):

- `kotlinx.coroutine.delay(ms)` Cedeix el fil i espera un temps com a mínim
- `kotlinx.coroutine.yield()` Cedeix el fil directament
- `kotlinx.coroutine.await(deferred)` Extensió de Deferred, cedeix i espera a que Deferred es resolgui (ve d'un `await`)
- `kotlinx.coroutine.join(job)` Extensió de Job, cedeix i espera a que el Job es resolgui (ve d'un `launch`)
- `kotlinx.coroutine.withContext(context) { ... }` No crea una co-rutina nova, simplement canvia el context d'execució de la actual (IO <-> Main) i espera que s'acabi alliberan el thread actual.
- `kotlinx.coroutine.suspendCancellableCoroutine { cont -> ... }` Adapta apis asincrones tipus callback a suspend. `cont` té funcions per resoldre resultat, excepció o cancel·lar.

::: warning
    No barrejar el `kotlinx.coroutines.CoroutineContext` d'execució de co-rutines (withContext)
    amb Context de les Activities d'Android `android.content.Context`.

- CoroutineScope (abast): un objecte proporciona creadors de corutines en un mateix CoroutineContext.
    - El veiem com a this a un creador de corutines, proporciona `launch`, `async`...
- Corutina filla: Creada des del CorutineScope d'una altra corutina, la mare
    - Al final de la mare espera (join) totes les filles abans d'acabar-se
    - Si el job es cancel·la, es cancel·len totes les filles

    - Quan mor la mare s'espera a que acabin les filles
    - Si es cancela el job, es maten totels les filles
    - Excepcions als Launch
    - Si volem aillar cal fer un `supervisorScope {...}` i crear les filles a dins.
        - Cancel·lar la mare encara cancel·la les filles pero no a la inversa.
        - Retorna un SupervisorJob amb interfície similar a Job.
    - Les excepcions arriben a dalt de una corutina la cancel·la.
        - try/catch a la mare no agafa excepcions de la filla.
- CoroutineContext: Entorn d'execucio d'una corutina i les seves filles. Conté:
    - Job: permet esperar, cancellar o executar la 
    - CoroutineDispatcher: on s'executa
    - CoroutineExceptionHandler: Defineix com reaccionar a les excepcions
    - Altres metadades
- CoroutineDispatcher: Determina en quin grup de threads s'executa.
    - Dispatchers.Main: UI, intentarem deixar-ho lliure pero si fem UI ho hem de fer aqui.
    - Dispatchers.IO: Entrada i sortida bloquejant
    - Dispatchers.Default: CPU intensiu


### Coroutine Scopes

Un àmbit de co-rutines ofereix funcions  `launch`, `async`...
normalment mantenint el mateix Job i CoroutineContext.
D'aquesta manera es cancellen juntes de forma controlada.

- `kotlinx.coroutine.coroutineScope { ... }` Ofereix les funcions `launch`, `async`... que fan servir totes el mateix Job i CoroutineContext. Es cancellen juntes. Espera a que s'acabin.

A Android es creen Jobs específics que es cancelen quan ho determina el cicle de vida d'una Activity, ViewModel...
Això ens assegura que durant l'execució de la coroutina els recursos de l'Activity o el ViewModel són vàlids.
Es crea un coroutine scope amb aquests jobs `lifecycleScope` i `viewModelScope`.
Son coroutineScope's i tenen `launch`, `async`...
Per defecte s'executen a `Dispatchers.Main`, si no es el que volem cal fer un `withcContext` a dins

```kotlin
lifecycleScope.launch { ... } // A activities
viewModelScope.lauch { ... } // A view models
```

Les views no tenen lifecycle.
Si ho volem fer servir:

- Heretar LifeCycleOwner
- `private val lifecycleRegistry = LifecycleRegistry(this)`
- Sobrecarregar els hollywoods de vincular a window:
    ```kotlin
    override fun onAttachedToWindow() {
        super.onAttachedToWindow()
        findViewTreeLifecycleOwner()?.lifecycle?.addObserver(lifecycleRegistry)
        lifecycleRegistry.markState(Lifecycle.State.STARTED)
    }

    override fun onDetachedFromWindow() {
        super.onDetachedFromWindow()
        lifecycleRegistry.markState(Lifecycle.State.DESTROYED)
    }
    ```
- Per fer-ho servir:
    ```kotlin
    val scope = LifecycleCoroutineScope(lifecycle, Dispatchers.Main.immediate)
    scope.launch { ... }
    ```
- O podem passar un scope des de fora.

A compose farem servir `LaunchedEffect(key) {...}` per executar una tasca en background.
Es cancel·larà quan el composable deixi de ser visible.
Es reiniciarà si canvia la `key`.

Per callbacks millor fer servir:
```
val scope = rememberCoroutineScope()
```
Creara un scope amb la vida del composable que podem accedir des del callback.


### Coroutine contexts and dispatchers


Coroutine Scope:

- A manager for a set of coroutines.
- Defines a context.
- Defines it's life cycle.

- Dispatcher decide a que thread van ciertas coroutinas
    - TOASK: Relacion entre dispatcher y scope

    - Dispatchers.Main — Fil que actualitza l'UI. No posar tasques bloquejants o CPU intensives. En depen la responsibitat.
    - Dispatchers.IO — Optimitzar per tasques IO bloquejants. Te molts fills esperant dades.
    - Dispatchers.Default — Optimitzat per tasques que fan ús intensiu de la CPU.
    - Unconfined — starts coroutine in current thread but can resume in different thread.
    - Test dispatcher — special dispatcher used in tests (runTest), controlling virtual time and execution order.
- Funcion `suspend` 
- `withContext(Dispatchers.Default) {}` Ejecuta el bloque en un grupo de threads concretos


`suspend` marks that a function or method is asynchronous.



## Flow

Flows are object that asynchronously emits a sequence of objects.



