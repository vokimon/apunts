# New features of C++11 I should be starting to use:

## Initializer lists

Formerly initializer lists could be used just with old C arrays and of old C values.

```c++
int myarray[] = {3, 4, 5};
```

Now any class with a constructor accepting an `std:initializer_list<T>` can be initialized like that.

```c++
std::vector <int> i = {4, 5, 2};
```

Without being a constructor you can pass pass such structures to any function
by accepting `std:initializer_list<T>` and using it as a regular const iterable.


Similarly, structs could be initialized like this:
```c++
struct Point {int x, int y};
int mypoint = {3, 4};
int mypoint2{3, 4}; // optional =
```

Now this can be used to call any constructor.

Convining it:

```c++
std::vector <std::pair<std::string, int> > i = {
	{'oranges,4},
	{'apples,3},
	{'lemons,7},
	};
```


# auto

Takes the type deduced by the rvalue expression.

You can also use decltype to extract tye type of an expression to declare a derivated type.

```c++
auto c = mycontainer;
decltype(*c.begin()) defaultValue();
```


# range for

```c++
for (auto& value: container) {
	// use value
}
for (const auto x : { 1,2,3,5,8,13,21,34 }) cout << x << '\n';
```

Si no esta definido `container.begin()` se busca `begin(container)`.

# Templates acabados con `>>`

Se acepta a diferencia de C++ que colisionaba.

# Move constructors and copies

Reciben el origen como `T && t`


# Default y delete

Igualar un metodo a:
- `default` indica que se usa la implementacion por defecto de ese método (constructores, asignacion...)
- `delete` indica que no se use la implementacion por defecto

Es util para:

- prohibir copia o movimiento de objetos, haciendo delete
- evitar que se se use conversiones, haciendo delete en las sobrecargas para tipos que no quieres convertir.
- explicitar o recuperar el comportamiento por defecto


# Declaraciones constexpr, extern template

Permite que funciones y metodos se llamen donde hace falta una expresion contstante,
si la funcion devuelve algo calculable en compilacion.

extern template permite instanciar un template sin que se instancie en esa unidad de compilación.

# Nuevos Enums

- Se declaran como `enum class`.
- NO hay conversión implicita a `int`. 
- Tienen como base el `int` pero podemos derivar de otro.
- Se usan con el scope de la classe `MyEnum::enum1`
- para coger el valor `static_cast<std::underlying_type<MyEnum>::type>(anenum)`
- Las forward declaration incluyen la herencia.
- Aun no resuelven mapeo a texto




# lambdas

```c++
[](int x, int y) -> int { return x + y; }
```

Se puede obviar el retorno si coincide con la expresion de retorno.


# Construction delegation


- Delegacion en otros constructores: Se puede hacer en los inicializadores.
- Valores por defecto: cuando declaramos atributos, podemos igualarlos a otro valor, si no lo inicializamos explicitamente, toma ese.


# Attributos declarativos: override, final, noexcept

Van al final de la declaracion y no son palabras clave, son identificadores.


Para evitar el error tipico de que sobrecargamos una funcion en vez de sobre escribirla.
Se puede explicitar que se trata de una sobrecarga y si no coincide con ninguna en la base, se queja.

```c++
virtual void some_func(int) override;
```

La palabra `final` se toma del Java. Declara clases no derivables y funciones no sobreescribibles.

noexcept da un error 



# nullptr

En vez de NULL para evitar inconsistencias de tipo.


# explicit a operadores de conversion

Se usaba para los constructores para evitar conversiones por defecto via constructor.
Justamente el problema tambien existe con los operadores de conversion.
Ahora podemos hacerlos explicitos.


# Parametros variables para templates

```c++
template <typename T, typename... OtherTs>

class ClassName : public OtherTs... {
public:

    ClassName (OtherTs&&... base_classes) : OtherTs(base_classes)... {}
};
```

# string literals


```c++
u8"texto utf-8"
u"texto utf-16"
U"texto utf-32"
R"(texto con " por medio)"
R"EOT(texto con () y "" por medio)EOT"
```

# custom literals

Podemos añadir sufijos a los literales (tanto numericos como textos)
ara convertirlos en el dato que queramos.

Se define el operador `ResultingType operator "" mysufix(...)`.

- integer: `ResultingType operator "" mysufix(unsigned long long)`
- float: `ResultingType operator "" mysufix(long double)`
- string: `ResultingType operator "" mysufix(const char* s, size_t n)`
- char: `ResultingType operator "" mysufix(char)`

En los anteriores operadores obtenemos el valor cocinado del literal.
En floating point y integer se acepta el parametro `(const char*)` sin el size
para recibir la cadena de texto tal cual sin convertir.
Esto es muy util cuando el tipo por defecto no acepta bien el resultado.
Por ejemplo, un tipo BigInt con literales que no caben en un long.
 `ResultingType operator "" mysufix(const char *)`

# libreria estandard


## Tuples

Se definen:

	#include <tuple>
	typedef std::tuple <char, short , const char * > tuple_2 t2 ('X', 2, "Hola!");

O usando `auto` y `make_pair`:

	auto record = std::make_tuple("Hari Ram", "New Delhi", 3.5, 'A');

Podemos unfoldear la tupla:

	std::string name ; float gpa ; char grade;
	std::tie(name, std::ignore, gpa, grade) = tupla;

	// Si queremos ignorar uno
	std::tie(name, std::ignore, std::ignore, grade) = tupla;

	// Para coger el elemento n y el tipo del elemento n
	size_t size = std::tuple_size<decltype(tupla)>::value;
	std::tuple_element<1, decltype(tuple)>::type v = std::get<1>(tuple); // auto es mejor


## Hash sets

Type of hash table        | Associated values | Equivalent keys
--------------------------+-------------------+-----------------
`std::unordered_set`      | No                | No
`std::unordered_multiset` | No                | Yes
`std::unordered_map`      | Yes               | No
`std::unordered_multimap` | Yes               | Yes

# Regular expresions


```c++
#include <regexp>

std::regexp r=R"\d{4}-\d{2}-\d{2}"; // La R es de raw

std::cmatch match;
if (std::regexp_search("estamos en 2015-23-22", match, rgx)) {
	for(auto m: match) {
		
	}
}

```

# Smart pointers

- `unique_ptr`: (transferible) ownership pointer.
- `shared_ptr`: reference counted pointer.
- `weak_pointer`: non owner pointer



# C++14

- Literales binarios 0b0001001
- Comilla ignorada en los literales para legibilidad:  10'200'231,0012
- Sufijos standards para literales:
	- "lala"s  -> std::string
	- h, min, s, ms, us, ns -> std::chrono::duration
	- i, il, is -> std::complex
- get<type>(tuple) si solo hay un elemento de esa tipo en la tupla.
- attributes:
	- `[[deprecated]]` and [[deprecated("reason"]: warns if declaration used
	- `[[noreturn]]` a function does not return to the caller (abort, exit...)
	- `[[carries_dependency]]` extra information about dependency chains
	- `[[deprecated]]` an entity is deprecated
	- `[[deprecated("reason")]]` provides additional message about the deprecation
- folding ops
	- `args + ...` -> `(arg1 + (arg2 + (...)))`
	- `... + args` -> `arg1 + (arg2 + (...)))`
	- `val + ... + args` ->  (val + (arg1 + (arg2 +(...))))
	- `args + ...` reduces (op may be `+ * & | , && ||`)
	- `args + ...` -> `(arg1 + (arg2 + (...)))`
	- when args empty, suitable default returns for the operator
	- sizeof ...value
- libreria standard
	- `<filesystem>`: `path`!!!, `space_info`, `copy`...


# C++17
	
- Templates:
	- params of constructors can now be deduced: `pair a {34, 'mary's};`
	- `auto` non-type template parameters adapts to whatever the type `template <auto value> decl`  
- Structured binding `auto [a, b, c] = tuple, array, class or struct with 3 static public items.
	- modifiers like `&` `&&` `const` `constexpr` `[[attr]]`... can be added outside the `[]`
- init statement for if: like the one in `for` semicoloned between parenthesis, with scope...
- Inline declaration of static members: `class A { static inline int seed = rand(); }`
- Lambdas can be `constexpr`
- Lambdas capturing this within a class: simplifies the idiom `[this=self] () { self->method() }` into `[*this] () { method()`
- `from_chars` and `to_chars` fast and controllable serialization for ints and floats
- nested namespace declaration `namespace A { namespace B { decl }}` can be compacted as `namespace A::B { decl }`
- preprocessor `if __hasinclude(<include>)` to check for the existance of a header (can be "" for local headers)
- new attributes:
	- `[[falltrough]]` to note a switch case misses a break intentionally, avoids warning
	- `[[maybeunused]]` to note a declaration might not be used, avoids warning
	- `[[nodiscard]]` warns if the return value is not captured by the caller (ie. important error status, allocated resource...)
	- `[[deprecated("reason"]] will show the reason if used




