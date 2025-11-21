# Jetpack Compose

És una forma declarativa i reactiva de definir les interfícies.
Similar a React i a QML.

## Conceptes bàsics

### Funcions composables

Una funcio composable declara l'estructura d'una interfície similarment a com ho faría React.

```kotlin
@Composable
fun Greeting(name: String) {
    Text("Hola $name!")
}
```

A React seria:

```jsx
function Greeting({ name }) {
  return <p>Hola {name}!</p>;
}
```

Igual que a React, el component es recalcula
quan (i només quan) canvien els paràmetres/attributs o l'estat.


### Estat persistent

Els components poden tenir un estat persistent
que son els remembers.
L'equivalent amb React seria el `useState`.

```kotlin
var count by remember { mutableStateOf(0) }
```

```jsx
const [count, setCount] = useState(9)
```

S'aconsella que l'estat estigui el més amunt possible.
Quan els fills necessiten modificar estat,
ofereixen parametres per passar-los callbacks (blocs de codi)
on el pare pot inserir codi per a que els fills canviin el seu estat.
(`onClick`...) .

### Layouts via modifiers

El Modifier es un objecte que accepten la majoria de composables
que especifica parametres comuns, normalment de layout
pero també alguns de comportament.

Normalment s'omplen cridant mètodes setters en cascada.

```kotlin
Text(
    "Hola",
    modifier = Modifier
        .padding(16.dp)
        .background(Color.Red)
        .fillMaxWidth()
)
```

En aquest cas, que estem setejant attributs de layout
el paral·lelisme amb React serien els estils,
però també es fa servir el modifier per a establir
paràmetres d'interactivitat (disabled, clickable, scrollable...),
callbacks de resposta a esdeveniments,
atributs d'accessibilitat...

## DisposableEffect

Un DisposableEffect permet insertar codi que s'executa:
- quan hi ha certs canvis, o
- quan el composable surt de l'arbre.

Paral·lelisme total amb useEffect de React.

- Els objectes observats són els primers paràmetres de la funció.
- Si és `Unit` només s'executa un cop, en entrar a l'arbre.
- El darrer paràmetre es el bloc de codi que s'executa
- El context te un métode `onDispose` que si el cridem amb un altre block s'executarà en sortir de l'arbre.

```kotlin
    // dins d'una funció composable
    DisposableEffect(Unit) { // or observables
        // init code goes here (or update code if observables)
        onDispose {
            // cleanup code goes here
        }
    }
```

## Estat persistent centralitzat (ViewModel)

<https://developer.android.com/jetpack/compose/state#viewmodel-state>
<https://developer.android.com/topic/libraries/architecture/viewmodel>

Similar al Context de React.
Sense scope??

```kotlin
class MyViewModel : ViewModel() {
    var counter = mutableStateOf(0)
}

@Composable
fun Screen(viewModel: MyViewModel = viewModel()) {
    val count by viewModel.counter
    Button(onClick = { viewModel.counter.value++ }) {
        Text("Count: $count")
    }
}
```

- Simplifica fluxe d'informació
- Complica l'anàlisi de side effects, tot i que marca on es produeixen
- Persisteix després de recomposicions i reconfiguracions (rotacio, tema, idioma...)

### Estat derivat `derivedStateOf`

Per no duplicar estat, cal calcular l'estat que s'en deriva de l'estat del pare a cada composició.
Això pot ser car,
en aquest cas es pot fer servir `derivedStateOf`.

Equivalent al useMemo.

### Corutines LaunchedEffect

Si hem de executar coses en paral·lel o més enllà de la composició.

```kotlin
LaunchedEffect(Unit) {
    viewModel.loadData()
}
```

Es cancel·la la corutina si canvien les dependencies o surt de la composició.

Pot sortir de la composició la corutina si en una composició no s'executa.

La cancel·lació es produeix llençant un `CancellationException`.
Podem capturar-ho a la corutina si volem fer res en sortir.


### SideEffect

S'executen incondicionalment després de cada composició.
Equivalent a `useEffect` de React sense dependencies (null, no array buit).

És útil per sincronitzar elements legacy (Views).
També per sincronitzar amb sistemes externs.


## Patrons

### State: Snapshot state

https://developer.android.com/jetpack/compose/state

Les crides a la funció declarativa son stateless.
Sovint cal mantenir un cert estat persistent.
Es proporcionen els mecanismes per mantenir aquest estat:

- `remember { }` crea una variable que es mantè entre crides.
- `mutableStateOf` crea una dada observable
- Quan un observable canvia Compose actualitza els elements que la contenen.


### State: State Hoisting

https://developer.android.com/jetpack/compose/state#state-hoisting

Si l'estat d'un component fill queda dins
costa molt de testejar

El pare manté el estat sempre que sigui possible.
(lifting state up de React)
Els canvis li arriben al pare via callbacks que passem com a paràmetres al fill.

### State: Single source of truth

https://developer.android.com/jetpack/compose/state#source-of-truth

Problema: Dispersió del coneixement -> Complexitat de sincronització
Problema2: Recreació dels components (rotacio, tema, idioma...), recomposició...

L'estat s'agafa del view model.

```kotlin
val uiState by viewModel.uiState.collectAsState()
```

### State: Derive state

https://developer.android.com/jetpack/compose/state#derivedstateof

No guardis estat que ens passen duplicant-ho.
Si es derivat, recalcula'l cada cop.
Recalcular pot ser car, llavors
recalcula-ho només quan canviin les dades d'entrada.
Per facilitar-ho tenim el `derivedStateOf`

### Composició: Single responsability

https://developer.android.com/jetpack/compose/philosophy

Fer components petits per a que siguin reutilitzables i testejables.

Equivalent als components purs de React.

### Composició: Components petits i enfocats

Problema:
Encara que tingui una sola responsabilitat,
si depén de masses coses o cobreix massa part de la interficie
com el Composable es l'element de recomposició,
la recomposició es produirà masses vegades i afectarà
a masses elements de la ui.

Enfocar els elements a una unitat d'actualització.

El single responsability parla de lògica,
el components petits parla de estructura i tamany.

### Composició: Modificador com a primer paràmetre opcional

https://developer.android.com/jetpack/compose/style#parameters

Si un component gestiona l'espai intern sense exposar-ho, resulta menys reutilitzable.
D'aquesta manera el pare del component decideix coses com ara la disposició, el coixí, el marge...

### Composició: No side effects

https://developer.android.com/jetpack/compose/side-effects

Problema: El cos d'una funcio composable
s'executa múltiples vegades i d'una forma que el programador no pot controlar.
Si cal generar efectes laterals (Toast, Logs, canvis a la BBDD...),
ho hem de fer de forma controlada.

- `LaunchedEffect` per crides a corrutines
- `DisposableEffect` per cicle de vida i neteja
- `SideEffect` per sincronitzar sistemes externs

TODO: Com funcionen aquestes funcions


### Composició: Slot APIs (children equivalents)

https://developer.android.com/jetpack/compose/layouts/basics#slot-apis

Problema: Un component que té la UI interna fixa es menys reutilitzable.

Solució: Permetre passar per paràmetres parts de la UI (slots) per a que el pare pugui definir-la.

```kotlin
@Composable
fun Card(
    header: @Composable () -> Unit,
    content: @Composable () -> Unit
) {
    Column {
        header()
        content()
    }
}

@Composable
fun Example() {
    Card(
        header = { Text("Capçalera") },
        content = { Text("Cos de la card") }
    )
}
```


### Composició: Unidirectional Data Flow (UDF)

https://developer.android.com/jetpack/compose/architecture#udf


### MVVM + Compose

https://developer.android.com/topic/architecture
https://developer.android.com/jetpack/compose/architecture

### Navigation via NavHost


https://developer.android.com/jetpack/compose/navigation

### Performance patterns

https://developer.android.com/jetpack/compose/performance




## Interoperabilitat

### Composable dintre d'un layout XML

Al layout inserim un `ComposeView`

```xml
<androidx.compose.ui.platform.ComposeView
    android:id="@+id/composeView"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"/>
```

Al codi de l'activity, recuperem el `ComposeView`
li cridem al mètode `setContent` passant-li el composable.

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main_layout)

        val composeView = findViewById<ComposeView>(R.id.composeView)
        composeView.setContent {
            Greeting("Marc")
        }
    }
}
```

### Composable com a fragment

També podem crear un fragment basat en el Composable
i fer-ho servir com a tal a la nostra vista clàssica.

```kotlin
class ComposeFragment : Fragment() {
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        return ComposeView(requireContext()).apply {
            setContent {
                MyComposable()
            }
        }
    }
}
```

### Composable com a Item d'un RecyclerView


```kotlin
class ComposeViewHolder(val composeView: ComposeView) : RecyclerView.ViewHolder(composeView)

override fun onBindViewHolder(holder: ComposeViewHolder, position: Int) {
    holder.composeView.setContent {
        ItemCard(itemList[position])
    }
}
```


### View dintre d'un Composable

AndroidView és una funció embolcall de Views clàssiques.
Té dos paràmetres: `factory` i `update`.

`factory` es un callback que donat un context, crea la vista i la inicialitza,
semblant al que faría un `onCreate`.


`update` rep la vista com a paràmetre i es crida cada cop que la vista s'actualitza.

```kotlin
@Composable
fun LegacyViewInsideCompose(state) {
    AndroidView(
        factory = { context ->
            TextView(context).apply {
                text = "Hola des d'una View!"
                textSize = 20f
            }
        },
        update = { view ->
            view.text = "Text actualitzat ${state}!"
        }
    )
}
```

### Comunicació

### Cicle de vida

Si la vista legacy necessita fer crides de cicle de vida,
cal fer un DisposableEffect 






