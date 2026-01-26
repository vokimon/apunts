# Android ViewModel

ViewModel és un coordinador de l'estat de l'aplicació.

- Enmagatzema l'estat de l'aplicació
- Fa de mediació entre les fonts externes i l'ui
    - API's, BBDD, fitxers
    - Asincronia, transformacions
- Observable per les Views i Composables
- Sobreviu a la recreació de Fragments, Composables, Activities...
- Sobreviu als canvis de configuració


## `UiState`

Es una data class inmutable que representa les dades que necessita una vista.

La produeix el ViewModel, la consumeix la View/Composable.

Dades pures sense estat canviant, per simplificar la logica.

## Sincronització

### LiveData

- Part de Android JetPack
- Quite old/stable
- Mostly with XML Views
- Only updates active components (lifecycle aware)
- Thread safe but Android -> Test with instrumentation

```kotlin
class MyViewModel : ViewModel() {
    val state = MutableLiveData<UiState>()
}

// A la vista

private val vm: MyViewModel by viewModels()
vm.state.observe(viewLifecycleOwner) { state ->
    textView.text = state.title
}
```

### StateFlow / SharedFlow

- Part de la llibreria de corrutines de kotlin
- StateFlow sempre te un valor actual
- SharedFlow per esdeveniments
- Funciona per Views i Compose
- Kotlin native

```kotlin
class MyViewModel : ViewModel() {
    private val _state = MutableStateFlow(UiState())
    val state: StateFlow<UiState> = _state
}

@Composable
fun MyScreen(vm: MyViewModel = viewModel()) {
    val state by vm.state.collectAsState()
    Text(state.title)
}

// In XML Views
lifecycleScope.launch {
    vm.state.collect { state ->
        textView.text = state.title
    }
}

// TODO: Com seria el SharedFlow

```

## Mutable state

- Compose only
- No persistent
- Not even on status change
- For local transient state

```kotlin
var counter by remember { mutableStateOf(0) }
Button(onClick = { counter++ }) { Text(counter.toString()) }
```

## Repositories

```kotlin
class StationRepository {
    fun getStations(): Flow<List<Station>> = networkApi.fetchStations()
}
```

TODO: How to update the state in the ViewModel?

## Partial update


private val _state = MutableStateFlow(UiState())
val state: StateFlow<UiState> = _state

_state.value = state.value.copy(attr1 = value1, attr2 = values)




