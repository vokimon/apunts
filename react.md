# React / Redux

## React

[React](https://reactjs.org/) is a web ui framework created by Facebook.

- **Component based:** Build application by defining and combining autocontained graphical components.
- **Declarative:** You say what to show up each time, bassed on the current state, and the library updates the changed elements into the DOM.
	- **Virtual DOM:** To achieve that, it generates a virtual DOM structure and compares to the previous one, it is cheaper that recreating or comparing the DOM all the time
- **Widely adopted:** This means that a lot of libraries, tools and documentation is available

https://dev.to/hb/react-vs-vue-vs-angular-vs-svelte-1fdm

What it is not:

- A widget library/css framework: there is a lot of libraries that adapts widget (bootstrap, material ui...) as react components.
- A router: to map urls to pages, you can use `react-router`
- A state keeper: you can use libraries like `react-redux` for that

## Setup

To generates a full project from scratch:

```bash
$ npx create-react-app myapp
```

It applies a lot of best practices and hides a lot of setup under `react-scripts` command.
How to modify this setup is documented [here](https://create-react-app.dev/docs/)

It hides tools like dotenv, webpack, babel... you will use.
Applications that with good defaults, like the ones provided by `react-scripts`,
you may not need to modify.

But sometimes you need to go beyond this configuration.
You can use `npm run eject` to expose the hidden configuration files, so that you can modify them.
This is a non reversible step and you will not get improvements in future versions of `react-scripts`.

```
my-app/
  README.md
  node_modules/      # Installed dependencies
  package.json       # Project metadata (dependencies, settings...)
  public/         # Files copied without webpack processing
    index.html       # unique html file, just loads index.js, you can use some templating here
    favicon.ico      # application icon
  src/            # Contains files processed by webpack
    App.css          # App component example - style
    App.js           # App component example - code
    App.test.js      # App component example - tests
    index.css        # global style
    index.js         # main js entry point
    logo.svg         # example resource
```

### Environment vars

- A file .env contains shell variables you can use in code and templates.
- They are loaded in compile time and can be used in run time.
- A [method]() exists to load some of them in runtile

Access it:

- `window.env`
- `process.env`
- `dotenv.env` # dotenv is the 
- Inside index.html like in `<link rel="icon" href="%PUBLIC_URL%/favicon.ico" />`

Variables are filtered.

- Any custom variable starting with `REACT_APP_`
- `NODE_ENV`: either production, development or test
- `PUBLIC_URL`: url where the assets will be visible
- ... ??
- `REACT_APP_*`: Any custom add should have this prefix



Each command looks for a given

- npm start: .env.development.local, .env.local, .env.development, .env
- npm run build: .env.production.local, .env.local, .env.production, .env
- npm test: .env.test.local, .env.test, .env (note .env.local is missing)

## Rendering (JSX)

```javascript
const MyComponent = () => {
    return <div>Hello world</div>
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent/>);
```

- JSX parsing starts is when a starting `<` is found until the element is closed.
- That parsing returns an object representing a React element.
- Because of the parsing, a single root element is required
- If you want a fragment with more than one element, you have to enclose them inside inside a void element `<>whatever</>`.
- If the html goes for several lines it is nice to wrap the jsx expresion by parenthesis, not required though

Some naming conventions:

- Standard tag elements are always lower case `div`
- Use uper camell case for components `MyComponent`
- Use lower  camell case for attributes
	- `tabindex` -> `tabIndex`
	- `onclick` -> `onClick`
- Some javascript reserved words, had to be renamed
	- `class` -> `className`

## Embeding javascript into JSX

- Inside JSX you can openup curly braces to insert javascript values.
- The result of curly braces expresion is inserted safely (escaped) into html.

```javascript
const MyComponent = () => {
    return <div>Hello world {234+1000}</div> // Resolves to 1234
}
```

- Inner javascript could contain JSX as well, so they can be alternatively nested JS -> JSX -> JS -> JSX....
- For attribute values quotes are appended as necessary
- Inside the tag, dicts `{...mydict}` are expanded as attributes
- Attribute values can be full JS objects
- For callback attributes `onX`, the expresion to insert is the callback, not its call as you would do in vanilla javascript
	- `onClick={handleClick}` not `onClick={handleClick()}`


## Receiving attributes

```javascript
const MyComponent = ({props}) => {
    // alternatively props.name
    {name} = props  // aqui el recollim
    return <div>Hello {name}</div>
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyComponent name="Perico"/>); // Aquí donem el valor
```

## Receiving and providing children

Children are received by the component as `props.children`

- children:
	- null, booleans (also true), undefined -> do not render
	- string literalls
	- other jsx
	- a function (useful to avoid execution on declaration)
	- a javascript expresion between curly braces
	- an array of all the above
	- a combination of all the above


## Declarative conditionals and loops

For single branch conditionals use `&&` and `||` operators.

```javascript
function Garage(props) {
  const cars = props.cars;
  return (
    <>
      <h1>Garage</h1>
      {cars.length>0 ||
         <h2>You have no cars in your garage.</h2>
      }
      {cars.length>0 &&
        <h2>You have {cars.length} cars in your garage.</h2>
      }
    </>
  );
}
```

Caution: falsy values like `cars.length` is not a bool, evaluates to 0 that is rendered '0'.

In order to render undefined, null, true or false, `{String(value)}`

For two branches conditionals use `?:` triplets


For loops use `map` and other Array funtional looping.

```javascript
function Garage() {
  const cars = ['Ford', 'BMW', 'Audi'];
  return (
    <>
      <h1>Who lives in my garage?</h1>
      <ul>
        {cars.map((car) => <Car brand={car} />)}
      </ul>
    </>
  );
}

```

## Hooks

Els hooks son funcions que es criden dintre del callback de render del component.

Normalment els podem cridar diverses vegades i s'identiquen per l'ordre de crida.


### ```useState```

- Gestiona valors propis de la instància del component, que es mantenen entre execucions del render.
- Canvis als valors provocaran una crida asincrona al render

```javascript
const { myValue, setMyValue } = useState(initialValue)
```

- `initialValue` és el valor inicial del value
- `myValue` variable receives the current value of the state
- `setMyValue(value)` és el setter

Internament el que identifica l'atribut no son els noms dels setters/getters sinó l'ordre en que es criden.

COMPTE: La conseqüència és que si la seva execució depén d'ifs, la liariem parda.

Per això, és bo posar-los a dalt de la funció abans de cap lògica.


### ```useEffect```

Serveix per executar callbacks en diferents moments del cicle de vida del component.

Executa callbacks després de fer el render quan ja tenim el DOM creat/actualitzat.

El segon paràmetre determina quan s'executa:

- Si no existeix, s'executa a cada render incondicionalment
- Si és un array de valors, s'executa cada vegada que els valors son diferents
- Si és un array buit, s'executa només a l'inici (l'array sempre serà el mateix les successives vegadess)

El callback pot retornar un altre callback que s'executarà abans de desmuntar el component.
Es pot fer servir per fer un clean up del que fa l'efecte o del component mateix.


### ```useContext```

Serveix per compartir un estat comú en un seguit de components fills d'un mateix pare, el provider.

```javascript
const MyContext = React.createContext(initialValue);

function App() {
  return (
    <MyContext.Provider value={currentValue}>
      <Toolbar />
    </MyContext.Provider>
  );
}

function Toolbar(props) {
  return (
    <div>
      <ThemedButton />
    </div>
  );
}

function ThemedButton() {
  const mycontext = useContext(MyContext);
  return (
    <button style={{ background: mycontext.background, color: mycontext.foreground }}>
      I am styled by theme context!
    </button>
  );
}

```

Los componentes que usan `useContext` se renderizaran siempre que el contexto cambie.


## Utility components


### lazy

It is used to avoid to load all components, when some of them
are not used in all cases.



the lazy function wraps another function that will be called on execution.




### `Suspense`

## Redux

Funcion: implementa la gestion del estado de la aplicación.

Ese estado se podria implementar con objetos de dominio (aplicacion), unittesting...
Pero el hecho de usar una implementación genérica, tiene ciertas ventajas:

- nos obliga a ser cuidadosos de donde y como se modifica el estado
- podemos usar herramientas de desarrollo que ofrecen:
	- Monitorear el estado de la aplicacion
	- Ver el historico de eventos que ha llevado a ese punto
	- Deshacer acciones (Undo pattern)

Tambien ciertas desventajas (de la web de Redux):

- Obliga a hacer las cosas de cierta manera
- Añade una indirección en el código
- Hay que entender nuevos conceptos

El estado se representa como un diccionario.
Solo una funcion llamada _reducer_ modifica dicho estado.

Un _reducer_ es una funcion que implementa una maquina de estados.
Recibe un diccionario con el estado actual, `state`, y otro con el evento, `action`.
Retorna un diccionario con el nuevo estado.
Se define el estado inicial mediante el valor por defecto del estado de entrada.

`(state = initialState, action) => newState`

Por convencion, el action tiene atributos:

- type: string con el tipo
- payload: datos del evento

Un ejemplo de definición de reducer:

```javascript
const initialState = {
  // initial values for all attributes
  myattribute = 1000,
}

function myReducer(state = initialState, action) {
  const {type, payload} = action
  switch (type) {
    case 'myevent':
      return {
        ...state, // take the original state, by copy, and update
        myattribute = payload.myparameter + payload.otherparameter,
      }
    (...)
    default: // not interested in that event
      return state // return same object
   }
}
```

La arquitectura de Redux está orientada a evitar
modificaciones del estado fuera del reducer.
Para evitarlo, el estado está controlado por el `store`.
Lo creamos así:

```javascript
// Nota: la documentacion usa el toolkit, Oscar usaba la libreria a pelo
import { configureStore } from '@reduxjs/toolkit'

const store = configureStore({ reducer: myReducer })
```

Podemos consultar el estado actual:

```javascript
state = store.getState()
console.log(state.myattribute)
```

El objeto retornado es una copia del estado interno.
Si lo modificamos no afecta al estado real.

Para hacer los cambios hay que emitir acciones (eventos) con el método `dispatch` del `store`.

```javascript
store.dispatch({ type: 'counter/increment', payload: {quantity: 2} })
```

Para completar la jerga, hay dos tipos de functores que se usan comunmente.

_Action creators_: Son funciones que retornan una accion a partir de los parametros.
A menudo, es más cómodo que hardcodear la estructura.

```javascript
const addTodo = text => {
  return {
    type: 'todos/todoAdded',
    payload: text
  }
}
```

_Selectors_: Son funciones que mapean una parte del estado.
Són útiles para desacoplar de la estructura del estado


```javascript
const selectCounterValue = state, i => state.counters[i].value

const currentValue = selectCounterValue(store.getState(), i)
```

### Flujo de aplicación

En una aplicación Redux existen tres elementos:

- Storage
- Interfaz
- Gestor de eventos

El flujo seria como sigue:

- El storage se inicializa con el diccionario inicial
- El interfaz se inicializan con los valores del storage
- Cuando se genera un evento en el interfaz el gestor de eventos puede acabar emitiendo una acción
- El storage calcula el nuevo estado con esa acción
- El storage notifica a los componentes que estan subscriptos a alguna parte del estado que haya sido modificada
- Los componentes subscritos consultan el valor y se actualizan

El flujo es circular pero solo va en un sentido.

### Integracion en React

- Un elemento `Provider` hace accesible el estado a todos los hijos
- El store se pasa como atributo del Provider
- Los componentes que quieran acceder al estado, usan `useSelector`
	- El parametro es un functor que recibe el estado y retorna la fraccion que necesitamos.
	- Se usa para optimizar que componentes necesitan actualizacion, igual que el useEffect
- Los componentes que quieran modificar el estado, usan `useDispatch`
	- No acabo de entender porque no podemos usar el storage directamente (normas de React?)

Por arriba del componente de más alto nivel que use el estado añadir el atributo store:

```javascript
import { Provider } from 'react-redux'
const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <Provider store={store}>
    <App />
  </Provider>
)
```

En los elementos que usen el estado:

```javascript
import { useSelector, useDispatch } from 'react-redux'

export function MyComponent() {
  const value = useSelector((state) => state.myslice.value)
  const dispatch = useDispatch()

  return (
    <control
      // uso del estado
      value={ value() }
      // modificacion del estado
      onClick={()=>dispatch({type: 'MYTYPE', payload: {....} } );
  )
}
```




### Slices

Los slices es una parte del toolkit que facilita separar
la logica de la maquina de estados por aspectos independientes
y por otro tener una definición más orientada a objetos, que un switch.

Cuando la aplicación crece hay mucho estado que gestionar
y dificil de mantener en una sola funcion reducer.


## Estilos

### Plain CSS files

Al importar el fichero css, webpack lo incorpora como recurso.

```javascript
import "MyComponent.css"
```

Convención: Usar el mismo nombre que el componente react que lo usa y dejarlo en la misma carpeta.

Problema: Aunque hagas un css por cada modulo,
es dificil evitar problemas de colision entre nombres de clases en diferentes componentes.

Se puede usar una clase encapsuladora que tenga el top-level del componente
y condicionar todos los estilos a esa clase.

### Estilos en linea

Se pueden insertar los estilos como atributos objetos/diccionarios como valor de `style` en el JSX.
Incluso podemos interpolar.

```javascript
<div style={{
    backgroundColor: 'red'; // notice the camell case instead of background-color. could be also quoted 'background-color'
    color: 'white';
}}>
```

Dentro del css podemos tambien interpolar JS.

Es mas ordenado si creamos los estilos fuera y los referenciamos en el JSX.

```javascript
const MyComponentStyle = {
    backgroundColor: 'red';
    color: 'white';
}
...
    return (
        <div style={ MyComponentStyle }>
	</div>
    )
```

Si hay muchos estilos el codigo generado puede ser muy verboso.


### CSS Modules

Genera nombres de clase generadas automaticamente para ser diferentes.

```javascript
const styles = import "MyComponent.module.css"
...

return (
  <div className={styles.myclass}>
  </div>
)
```

```css
myclass {
    background: 'red';
    color: 'white';
}
```

Todas las classes referenciadas en el css estan disponibles como atributos de `styles`.
Pero el valor es el identificador generado `MyComponent_MyComponent_hash` (fichero, clase original, hash)

Para usar classes comunes con otros modules
```
.myclass {
  composes: otherClass from './other.component.css';
  color: red;
}


### Normalización de estilos

Restaurar los estilos a un common ground sea cual sea el navegador.
Arriba del index.css:

```css
@import-normalize;
```

### Styled-components

Libreria externa 

```
import styled from 'style-components'

// standard html tags
export Button = styled.button`
  color: red;
  background: ${myvar}`
`
// react components
export StyledLink = styled(Link)`
  color: green;
`
// standard html tags
export Button = styled.button`
  color: red;
  background: ${props=>props.myattr};`
`
```

Genera una hoja de estilo con clases basadas en hash.

Funcionalidades de Sass (nesting...)

### Linara

[Linara](https://linaria.dev/) (runtime optimized)

Permite generar componentes como los de styled-components con una sintaxis calcada, pero ademas añade otro idioma:

```javascript
var myclass=css`
  font-size: 10pt
  &:hover {
     color: ${mycolor}
  }
`
```

Esto permite usar classes con nombres generados.
Todo va a hojas de estilo, que es más rápido.
Los inserts los convierte en variables css que se modifican con javascript,
y eso va también mucho mas rápido que generar la hoja de estilo cada vez.
También permite reusar los estilos.

Cons: La integracion con webpack aun no esta integrada en react-scripts y hay que configurar loaders del webpack a mano.


### Emotion

Integrable con @emotion/react

Tiene el tag css como el linara. Tambien tiene otros:

- `css` genera un nombre de classe con los estilos del template (como el css de linara)
- `keyframes` genera nombres de animaciones con los keyframes del template
- `injectGlobal` simplemente genera css tal cual sin generar classes (de hecho hay que poner selectores)
- `cx` no es un tag, es una funcion que combina varias clases con preferencia de las ultimas.
- `styled.tag`/`styled(Component)` simula styled components







### JSS



