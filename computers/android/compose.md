# Jetpack Compose

És una forma declarativa i reactiva de definir les interfícies.
Similar a React i a QML.


## Conceptes bàsics

### Funcions composables

Una funció composable declara l'estructura d'una interfície similarment a com ho faria React.
Retorna una estructura de components amb crides a d'altres composables.

```kotlin
@Composable
fun Greeting(name: String) {
    Column {
        Text("Hola $name!")
        Text("This is Compose!")
    }
}
```

L'equivalent a React seria:

```jsx
function Greeting({ name }) {
  return 
    <Column>
        <Text>Hola {name}!</Text>
        <Text>This is Compose!</Text>
    </Column>
}
```

També igual que React, la funció es crida,
en inserir el component en l'arbre (composició)
i després (recomposicions) només quan canvien les seves dependències,
que venen per diferents vies.


### Compte amb els falsos amics

Molts conceptes i mecanismes de React i Compose s'assemblen,
pero això ens pot arribar a portar a errors per falsa expectativa.

Faig compilació de les falses expectatives que m'he trobat:

A diferencia de React, els paràmetres no són dependències implícites.
Els paràmetres o qualsevol valor que pugui generar una reacció
al seu canvi, ha d'estar declarat explicitament com a tal.

El redibuixos són molt estrictes,
un valor propagat com a paràmetre,
encara que estigui declarat per generar reacció,
afecta només al lloc final on es fa servir el valor.
Les funcions composables intermitges que el propaguen no es reexecuten.

Una altra diferència notable son les inner functions
que sovint es fan servir de callback amb nom o lambdas.
A Javascript una funció interna es un objecte different
a cada execució de la funcio continent, es a dir, a cada redibuixada.
Per tant, quan accedeixen a les variables locals de la funció continent,
agafen el valor de la darrera execució.

A Compose l'scope es defineix a la primera cridada de cada instància,
i els valors de les variables als que accedeix son els de la primera execució de cada instància.
Si volem accedir al valor actualitzat del darrer render,
cal definir un wrapper que contingui el valor i de forma persistent.
El wrapper serà el mateix entre crides,
inclosa la primera crida a la que accedeix la inner function,
pero el contingut del wrapper canviarà.

### Estat persistent

Quan tornem a fer una recomposició, tornem a cridar la funció.
Com podem recuperar els valors que teníem a la crida anterior?
Creant un estat persistent entre recomposicions.

```kotlin
var count by remember { mutableStateOf(0) }
```

L'equivalent a React seria el `useState`.

```jsx
const [count, setCount] = useState(9)
```

Podem fer-ho servir com a conjur, però,
sintàcticament té molta manteca:

- `remember` és una funció de Compose que
crea un slot a la instància del component
per guardar el valor entre crides.
Aquests slots s'identifiquen per l'index o sigui que
és molt important mantenir l'ordre dels estats entre crides (ifs, loops...)

- `mutableStateOf` es un delegat que notifica a Compose
cada vegada que algú el canvia el valor.
Aquesta notificació serveix per marcar el component
com a brut per la següent recomposició.

- `by` declara una delegació, això vol dir que mutableStateOf
implementa `setValue` i `getValue`,
quan asignem o fem servir el valor,
estarem cridant a aquests mètodes.

- El 0 es el valor inicial, de la primera vegada que s'executi per la instància del composable.

TODO: This paragraph does not go here

S'aconsella que l'estat estigui el més amunt possible en l'arbre.
Quan els fills necessiten modificar estat,
ofereixen paràmetres per passar-los callbacks (blocs de codi)
on el pare pot inserir codi per a que els fills canviin el seu estat.
(`onClick`...).


### Maquetació amb modificadors

La majoría de composables, per convenció,
accepten com a primer paràmetre opcional un objecte Modifier.
Aquest especifica parametres comuns, normalment de layout
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

Aquest idioma construeix una llista de instancies de subclases de Modifier.

Hi ha diversos tipus:

- `LayoutModifier`: `padding`, `fillMaxWidth`, `size`
- `DrawModifier`: `background`, `border`, `clip`
- `PointerInputModifier`: `clickable`, `draggable`
- `SemanticModifier`: `semmantics = { contentDescription = ""... }`

https://developer.android.com/develop/ui/compose/modifiers-list

També podem definir els nostres propis pels nostres components.
Els components reben tots els tipus, però cadascun decideix a quins fa cas.

**Compte: No funcionen com els atributs CSS o HTML.**
Aplicant-los dues vegades no descartem la primera s'apliquen els dos additivament.
També l'ordre en que els apliquem es significatiu.
La llista de modificadors s'aplica en ordre
com si fossin decorators i l'efecte es additiu.

Si appliquem dos vegades padding, farà dos paddings.
Si apliquem un background entre mig dels dos, s'aplicarà només al primer.

Com combinar modifiers locals amb els especificats pel pare?

Si el pare crida `Fill(modifier = Modifier.a.b)`,
el fill pot fer `modifier.c.d` i la cadena sera `a.b.c.d`.
Si el fill fa `modifier.then(Modifier.c.d)`, la cadena serà `c.d.a.b`.

Com passar modifiers a diferents nets?

La convencío diu que el paràmetre es `modifier` pero si
call aplicar aquests modifiers a dos net,
el fill pot exposar dos paràmetres `modifierNet1` i `modifierNet2`.


### Efectes disposables `DisposableEffect`

Un DisposableEffect permet insertar codi que s'executa:
- quan el composable entre a l'arbre
- quan canvien certs valors (observables), o
- quan el composable surt de l'arbre.

Paral·lelisme total amb useEffect de React.

- Els objectes observats són els primers paràmetres de la funció
- Si l'únic paràmetre és `Unit` només s'executa un cop, en entrar a l'arbre.
- El darrer paràmetre es el bloc de codi que s'executa
- El context té un métode `onDispose` que si el cridem amb un altre block s'executarà quan el composable surti de l'arbre.

```kotlin
    // dins d'una funció composable
    DisposableEffect(Unit) { // Unit o valors observables
        // Codi per inicialitzar o bé actualitzar coses pels canvis als observables
        legacy.start()
        onDispose {
            // Codi per netejar
            legacy.stop()
        }
    }
```

Es fa servir sobretot per a mantenir elements externs sincronitzats amb el composable
o per mantenir el cicle de vida d'altres recursos aliniat amb el del composable.

Amb `Unit` es equivalent a `useEffect` amb una llista de dependències buida.
Amb observables es equivalent a `useEffect` amb una llista de dependencies plena.
`onDispose` es equivalent al callback que retorna `useEffect`.

`useEffect` amb null (s'executa incondicionalment cada composició,
no es pot fer amb DisposableEffect, sinó amb  `SideEffect`


### Efectes laterals `SideEffect`

S'executen incondicionalment després de cada composició.
Equivalent a `useEffect` de React sense dependencies (null, no pas array buit).

És útil per sincronitzar elements legacy (Views).
També per sincronitzar amb sistemes externs.

https://developer.android.com/develop/ui/compose/side-effects#remembercoroutinescope


### Estat derivat `derivedStateOf`

Hi ha estat que deriva d'un altre estat, en diem estat derivat.
Com és derivat, es redundant, enmagatzemar-ho implica una duplicació.
Ho evitarem, i sempre que poguem el recalculem en cada composition a partir de l'estat original.

Normalment aquest recàlcul és trivial, però a vegades te un cert impacte en l'eficiència.
Per evitar aquest impacte farem servir el `derivedStateOf`.

```kotlin
import androidx.compose.runtime.derivedStateOf
@Composable
fun myComponent(state1: int) {
    val state2 by rememmer { mutableState(3) }
    val derived = remember { derivedStateOf { recompute(state1, state2) }}
    subComponent(derived)
}
```

Compose detecta les dependències i recalcularà només quan es modifiquin.

Com havia dit abans, si el recàlcul no és molt car,
potser paga la pena el cost de comparar les dependències
i enmagatzemar el darrer estat.

Equivalent al `useMemo` de React.

### Estat produit `produceState`

Converteix estat no composable en composable.
Per exemple, pero no limitat a, estat provinent d'un Flow o LiveData.

`produceState<T>(initialValue: T, dependencies..., producer: suspend T ()): State<T>``


Sovint es fa servir en combinació amb la classe `Result` que ve a ser una promesa.

- `Result.Loading` es un resultat pendent.
- `Result.Success(value)` la resol favorablement
- `Result.Error` la resol amb error






### Estat persistent centralitzat (ViewModel)

<https://developer.android.com/jetpack/compose/state#viewmodel-state>
<https://developer.android.com/topic/libraries/architecture/viewmodel>

Un ViewModel es un lloc centralitzat
tenir i accedir a l'estat compartit.
A més es persisteix als canvis de configuracio
(rotacions, canvis de idioma...)
No persisteix a sortir de l'activity i tornar a entrar.
Tenim el problema que quan cambiem la configuració i recreem la interficie
perdem l'estat que hi havia als components, `remember` no és prou.

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


## Catàlog de composables

### Estructurals/Layouts

- androidx.compose.foundation.layout
    - Box: Acomoda els components lliurement per posició amb z-index
    - BoxWithConstraints: Acomoda els components en referència al pare i els germans
    - Column: Acomoda els components verticalment
    - Row: Acomoda els components horitzontalment
    - FlowRow/Column: Quan esgoten l'espai fan wrapping en la seguent row/column
    - Spacer: Element buit
    - Divider: Línia sense estil

- androidx.compose.foundation.lazy
    - LazyColumn/Row: No renderitzen tots els fills, només els visibles

### Widgets

- androidx.compose.foundation
    - Image
    - Camvas

- androidx.compose.foundation.text
    - BasicText
    - BasicTextField

### Modificadors

Els imports extenen Modifier per afegir els mètodes:

- Interacció: androidx.compose.foundation
    - clickable(onClick={}): Simple click event
    - combinedClickable(onClick, onLongClick, onDoubleClick...)
    - focusGroup() def
    - focusable() 
    - hoverable() responds to pointer hovering
    - indication() marks interaction occurring
    - horizontalScroll() fes desplaçable 
    - verticalScroll() enables v scrolling when surpassing v constraintsa
    - overScroll(overScrollEffect) 
    - scrollableArea() shortcut per tots els parametres d'scroll
    - basicMarquee() Anima el desplaçament del contingut quan no hi cap
    - magnifier ???
    - preferKeepClear() marca zona de no oclusió per a popups
- Semantica
    - progressSemantics() Indica que el component es un indicador de progrés
- Visualització
    - background(color, shape)
    - border(width, shape)
- Ui: androidx.compose.ui
    - padding(length), padding(t,b,l,r)
    - paddingFromBaseLine(top, bottom)
    - offset(x=0, y=0)
    - size(width, height), width(), height(): preferred size/width/height
    - requiredSize/Width/Height(): size regardless the constraints
    - fillMaxHeight/Width/Size()
    - absoluteOffset(x, y)
    - aspectRatio(ratio)
    - captionBarPadding() adds padding to accomodate caption bar insets
    - consumeWindowInsets(insets)

### Material 3 `androidx.compose.material3`


- MaterialTheme
- Surface
- Scafold: estructura para una pantalla material: barra superior
- 

| Composable                                                              | Qué hace / cuándo usarlo                                                                                                                             |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AppBar / TopAppBar**                                                  | Barra de aplicación superior para título, navegación, acciones. Material 3 tiene varias versiones (CenterAligned, TwoRows, etc.). ([Composables][2]) |
| **Button** / **ElevatedButton** / **FilledButton** / **OutlinedButton** | Botones con diferentes estilos (relleno, tono, contorno…).                                                                                           |
| **FloatingActionButton (FAB)**                                          | Botón flotante para acción principal. También hay variantes extendidas.                                                                              |
| **Card**                                                                | Tarjeta para agrupar contenido con elevación y forma. En M3, `Card` requiere un `ColumnScope` para su contenido. ([Stack Overflow][3])               |
| **Text**                                                                | Para mostrar texto con estilo de tema.                                                                                                               |
| **Icon** / **IconButton**                                               | Iconos y botones con icono. Material 3 provee íconos coherentes con el tema.                                                                         |
| **Checkbox**, **RadioButton**, **Switch**, **TriStateCheckbox**         | Componentes de selección.                                                                                                                            |
| **Chip** (AssistChip, FilterChip, SuggestionChip, etc.)                 | Pequeños elementos interactivos tipo “etiqueta” que pueden tener acciones o estados. ([Composables][2])                                              |
| **ProgressIndicator** (circular, linear, wavy)                          | Indicadores de progreso.                                                                                                                             |
| **Slider**, **RangeSlider**                                             | Controles deslizables para seleccionar valores.                                                                                                      |
| **TextField**, **OutlinedTextField**, **SecureTextField**               | Campos de texto para entrada, con variantes. ([Composables][2])                                                                                      |
| **Dialog / AlertDialog**                                                | Ventanas modales para alertas, confirmaciones, diálogos de material.                                                                                 |
| **DropdownMenu** / **DropdownMenuItem**                                 | Menús desplegables.                                                                                                                                  |
| **NavigationBar**, **NavigationRail**, **NavigationDrawer**             | Componentes de navegación: barra inferior, rail lateral o cajón (“drawer”). ([Composables][2])                                                       |
| **Snackbar** / **SnackbarHost**                                         | Mensajes que aparecen temporalmente desde la parte inferior.                                                                                         |
| **DatePicker**, **TimePicker**, **DateRangePicker**                     | Selectores de fecha y hora en Material 3. ([Composables][2])                                                                                         |
| **PullToRefreshBox**                                                    | Para realizar “pull to refresh” con Material 3. ([Composables][2])                                                                                   |

[1]: https://developer.android.com/develop/ui/compose/designsystems/material3?utm_source=chatgpt.com "Material Design 3 in Compose  |  Jetpack Compose  |  Android Developers"
[2]: https://composables.com/material3?utm_source=chatgpt.com "Material 3 Compose API Reference – Material 3 Compose"
[3]: https://stackoverflow.com/questions/77772184/why-does-the-jetpack-compose-material-3-card-composable-require-a-columnscope-fo?utm_source=chatgpt.com "Why does the Jetpack Compose Material 3 Card composable require a ColumnScope for its content? - Stack Overflow"

- App and Navigation
    -  `AppBar`, `TopAppBar`, `BottomAppBar?`: Barres d'applicació superior i inferior M3
    - `CenterAlignedTopAppBar`: App bar amb títol centrat
    - `BottomAppBar`: Barra inferior M3
    - `Scaffold`: Layout bàsic amb top/bottom bars i floating action button
- Text
    - `Text`: Text amb estil i color de M3
    - `TextField`: Camp de text amb estil M3
    - `OutlinedTextField`: TextField amb border M3             |
- Visual
    - `MaterialTheme`: Conté colorScheme, typography, shapes
    - `ColorScheme`: Colors principals i secundaris M3
    - `Shapes`: Cantonades, radii de M3
- Buttons
    - `Button`: Botó elevat M3
    - `OutlinedButton`: Botó amb border
    - `TextButton`: Botó de text
    - `IconButton`: Botó amb icona
- Selectors
    - `Checkbox`: Checkbox M3
    - `RadioButton`: Botó radio M3
    - `Switch`: Switch M3
- Surfaces
    - `Card`: Container amb elevació i cantonades M3
    - `Surface`: Base estilitzada per colors i shapes
- Popups
    - `AlertDialog`: Diàleg M3
    - `DropdownMenu`: Menú desplegable
    - `ModalBottomSheet`: Full de tipus bottom sheet M3
- Decorations
    - `Icon`: Mostra un vector drawable o M3 icon
    - `Badge`: Petit indicador de notificació 
    - `FilterChip`, `InputChip`, `SuggestionChip` : Composables tipus chip amb estil M3


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

Problema: El cos d'una funció composable
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

L'estat viatja cap avall. Els esdeveniments viatjen cap amunt.



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


## Otros

`rememberSaveable` survives configuration changes and process

- Language (single language):
  `import androidx.compose.ui.platform.LocalContext`
    ```kotlin
        val context = LocalContext.current
        var text = context.getString(R.string.string_id)
    ```

- Orientation dependencies:
  `import androidx.compose.ui.platform.LocalConfiguration`
    ```kotlin
        val configuration = LocalConfiguration.current
        val isLandscape = configuration.orientation == Configuration.ORIENTATION_LANDSCAPE
        if (isLandscape) {
            Row { ... }
        } else {
            Column { ... }
        }
    ```
- Language (with language changes):

```kotlin
fun Context.updateLocale(newLocale: Locale): Context {
    val configuration = resources.configuration
    configuration.setLocale(newLocale)
    return createConfigurationContext(configuration)
}
class MainActivity : ComponentActivity() {
    private val localeState = mutableStateOf(Locale.getDefault())

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            val locale = localeState.value
            val context = LocalContext.current.updateLocale(locale)

            CompositionLocalProvider(LocalContext provides context) {
                MyApp()
            }
        }
    }

    fun changeAppLanguage(newLocale: Locale) {
        localeState.value = newLocale
    }
}
import androidx.compose.ui.res.stringResource

fun myComponent() {
    Text(text = stringResource(R.string.greeting, userName, messageCount))
}
```

`key(id)` es un composable que serveix per identificar els fills del mateix tipus quan hi ha més d'un.
Equivalent a la funció que fa el parametre `key` a React.

Alguns contenidors ja tenen la key integrada:
`LazyColumn{ items(persons, key=functor) { person ->  DetailView(person) }`

`val movableContent = remember(content) { movableContentOf(content) }`
Declara una part del tree que es mourà de lloc depenent del contexte
pero volem tenir aquesta part identificada sent la mateixa en els dos contextes.
Per exemple, els mateixos elements d'una llista que estaran en Row en apaisat, i Column en vertical.


## Stability

L'estabilitat és una caractarística dels tipus de dades.
Un tipus és estable, bé si és immutable
o si és mutable però compose té una forma de saber si el contingut
ha canviat entre recomposicions.

TODO: Com ha de saber compose que ha canviat?


 
## Scopes

Els scopes són una técnica útil per fer disponibles mètodes d'ús exclusiu
dintre del block de contingut d'un composable contenidor concret.

Per fer-ho, cal definir el contingut, no pas com a funció composable de primer nivell,
sinó com a extensió d'una interfície que al mateix temps podem extendre amb
les extensions que volguem afegir.


```kotlin
interface MyContainerScope {}

class MyContainer(
    ...
    content: @Composable MyContainerScope.() -> Unit,
    ) {
        ...
        val scope = object : MyContainerScope {}
        scope.content()
        ...
    }
}

/// This method will be available inside MyContainer content
fun MyContainerScope.myExtension(...) {
    ...
}

/// So you can use
MyContainer {
    myExtension....
}
```

Alguns usos típics son per definir amb un sol content differents placeholders,
definir subcomponents que només tenen sentit dintre d'un contenidor,
o definir modificadors que els passa el mateix.

Els mètodes d'scope que retornen un modifier estan disponibles
com a modificadors a dintre de l'scope per les regles d'encadentat.

## Regles d'encadenat

Podem aplicar `.metode()` a un objecte si retornen modifier.
















