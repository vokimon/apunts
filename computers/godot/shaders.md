# Godot Shaders (es)

## Referencias

- <https://thebookofshaders.com/>
- [Godot Shader Tutorial](https://docs.godotengine.org/en/stable/tutorials/shaders/index.html_)
- [Godot Shading language Documentation](https://docs.godotengine.org/en/3.0/tutorials/shading/shading_language.html)

## Intro

### Ejecución paralela

Un shader contiene código que se ejecuta en la targeta gráfica (GPU),
en contraste con el código que se ejecuta en la CPU.
Son útiles porque permiten personalizar la cascada de renderizado,
beneficiandose de las capacidades de paralelización de la targeta gráfica.

Por ejemplo, en vez de escribir un doble bucle para cambiar el valor
de cada pixel (para toda columna x, para toda fila y),
una rutina shader se ejecuta en paralelo para cada uno de los píxeles.

Hay varios lugares donde se pueden realizar estas paralelizaciones,
por ejemplo:
cuando emulamos la física de muchos elementos repetidos (partículas, por ejemplo para simular multitudes, fluidos...),
cuando procesamos la geometría (para cada vértice),
cuando la geometría se rasteriza (para cada píxel o mejor dicho 'fragmento'),

Este procesado paralelo introduce ciertas limitaciones:
Como todas las unidades se ejecutan en paralelo,
cada una no puede acceder a lo que hacen las otras.
Además como no pueden mantener memoria interna
de un fotograma al siguente hay que recurrir a ciertos trucos para mantener la continuidad.

### Como se crean los shaders

La mayoria de plataformas permiten escribirlos en el lenguagi GLSL,
que seria muy parecido a C, pero no exactamente igual.

En Godot, a parte tenemos el lenguaje GDShader,
similar a GLSL pero facilitando ciertas cosas.
Y también proporciona los visual shaders,
que es una forma gráfica de programarlos conectando módulos.

En concreto Godot tiene shaders estandars parametrizados,
que no tienes porque ver, pero que Godot permite convertirlos
en código de shader para, a partir de ese estandard y personalizar lo que quieras.

Usemos el método que usemos, dicho programa se compila
y se sube a la targeta donde se ejecutaŕa para aquellos elementos que especifiquemos.

### Pipeline principal

Los shaders se ejecutan para distintas unidades paralelizables
(partículas, vértices, fragmentos, luces, entorno...)
y a veces, en diferentes momento del procesado.
Según a qué se aplique hablaremos de un
particle shader, vertex shader, fragment shader....

El pipeline de renderizado, es algo más complejo que lo que vamos a explicar ahora,
pero baste esto para entender los dos tipos más comunes de shaders:
los de vertice y los de fragmento.
El pipeline sería como sigue:

- La CPU sube o actualiza a la GPU las geometrías a renderizar
en forma de vertices y polígonos (triángulos) formados con ellos.

- En ese punto se ejecutan los **vertex shaders**.
Para cada vertice de la geometría puede modificar tanto su posición
como otros atributos: normales, coordenadas de textura, color de albedo,
componente metálico, reflectividad...

- Una vez ejecutados los vertex shaders, la GPU **rasteriza**
los polígonos, es decir, los proyecta en la pantalla como píxeles,
e interpola las propiedades de cada pixel a partir de las
propiedades de los vértices que definen el polígono.
El resultado no es solo un pixel con una posición y el color que pintamos,
sino que es lo que llamamos **fragmentos**, que ademas tiene
un monton de las otras propiedades interpoladas.

- Después de este primer rasterizado, se ejecutan los **fragment shaders**,
que se ejecutan para cada fragmento/píxel.
Obtienen todas esas propiedades ya interpoladas que podemos
consultar y cambiarlas.

Los vertex y fragment shaders son los más comunes.
Pero hay mas tipos de shaders.
En glsl, el tipo de shader se indica con un enum cuando se carga en la targeta,
y los ficheros se suelen guardar con una extension que
sugiere el tipo `.frag`, `.vert`...
pero como se carga como texto en memoria,
es solo una convención.
El punto de entrada es la función `main`.

En Godot, se asocia un fichero `.gdshader`
con los shaders que van vinculados a un cierto nodo.
Cuando un nodo tiene un atributo de tipo material,
podemos asignarle un material de tipo gdshader (o visual shader)
y asignar un fichero `.gdshader`.
En estos ficheros pueden ir mas de un tipo de shader,
por ejemplo una malla 3D puede tener un gdshader con
un vertex y un fragment shader, identificados por
el nombre de la función (no es un `main`).

- **Spacial shader:**
	- Material of any 3D object
	- Directive: `shader_type spatial;`
	- Entry point gdshader: `vertex()`, `fragment()`, `ligth()`
    - Extension glsl: `.vert`
- **CanvasItem shaders:**
	- Material of any 2D/Canvas item
	- Directive: `shader_type canvas_item;`
	- Entry points: `vertex()`, `fragment()`, `ligth()`
- **Particle shaders:**
	- Directive: `shader_type particles`
	- Used to compute the particle properties when they are generated they are computed before the pipeline
	- Entry points: `start()`, `process()`
- **Sky shaders:**s
	- Directive: `shader_type sky;`
	- Entry points: `sky()`
- **Fog shaders** 
	- Directive: `shader_type fog;`
	- Entry points: `fog()`
- **Compute shaders:**
	- glsl
	- Directive: `#[compute]`
- **Compose shader:**
	- glsl

- `vertex()`: runs over all the vertices in the mesh and sets their positions and some other per-vertex variables
- `fragment()` runs for every pixel covered by the mesh (similar parameters than the vertex but interpolated)
- `light()` for every pixel, for every light
- `start()` for every particle at its begining
- `process()` for every particle for each frame
- `fog()` for every 'fogxel' volumetric buffer
- `sky()' for every eye ray reaching infinite
- ...

Los shaders se aplican a los nodos como materiales.
Entre los tipos de materiales que podemos asignar
estan los gdshaders, los visual shaders Y el standar material.

Los standard material es un shader típico con un monton de parámetros
que podemos manejar.
Por ejemplo, el fragment shader standard aplica un sombreado realista:
albedo, rugosidad, normales, metalicidad, anisotropia, texturas...
Si queremos modificarlo hay una opcion en el material para convertirlo
en shader y poderlo editar o examinar.

### Sky shaders

- Applied to WorldEnvironment material attribute.
- Set the Background/Mode to Sky
- Set the Sky/Sky Material.
- `shader_type sky`
- Entry point `sky()`
- Uniforms:
    - EYEDIR: vec3 +z up -z down
    - LIGHT_ENERGY (from environment parameter)
    - UV: para proyectar environ maps textures
    - COLOR (out)

- [Sky shaders in Godot]()
- [How to model realistic sky in Godot](https://www.youtube.com/watch?v=_EeVDI-PVRw)



## Input and outputs

Un shader tiene entradas y salidas.
Dependiendo del framework se accederan como
parametros de la función o como globales.
Eso si, las globales se tienen que definir en el fichero
para que la targeta gráfica sepa que datos tiene que mover.

- `uniform`: values assigned from host code, accessible by all the shader types.
- `attribute`: assigned from vertexes attributes, only available in vertex shaders
- `varying`: assigned from vertex attributes, modifiable by vertex shaders, available interpolated in fragment shaders

The pipeline provides the shader a set of input data
and gives the option to set a set of output data.
These are accessed as they were global variables.
Many input variables are in fact global,
but most input and all outputs are local
to the processed element: a vertex, a fragment, a particle...

In glsl those variables are prefixed `gl_`.
In gdshader those variables are `UPPERCASED`.

## Storage attributes

## Uniforms

Uniforms are data that is injected by the CPU into the GPU:

- Floating point parameters
- Colors
- Textures
- ...

## Uniform hints


## vecN types

Constructors of `vec2`, `vec3` and `vec4`
overloaded to receive either scalar or lesser vecs as parameters.
The sum of dimensions, should match.

    vec4(vec2(1.0,2.0), 3.0, 4.0) == vec4(1.0, 2.0, 3.0, 4.0) == vec4(1.0, vec3(2.0, 3.0, 4.0))

Single scalar propagates to all components.

    vec4(5.0) == vec(5,5,5,5)

Accessors (read and write):

- `[0] [1] [2]...`
- `.x .y .z .w` for vectors
- `.r .g .b .a` for colors
- `.s .t .p .q` for texture coordinates
- `.zysw` vec4 of those components (swizzle notation)

    v4.xyzw = v4.zxyw; // component swap

They are float vectors but you can use prefixes to have other base types:
`bvecN` (bool), `ivecN` (int)

Operations between vectors of the same component number is performed component-wise.

vec2(4,18) / vec2(2,3) == vec2(

## Errores típicos

- Punto y coma, you pythoner
- Using integer constants instead of floats, you Cer.
- Target vector dimensions number missmatch with assigned values.

## Functions

Built-in functions:

- `step(threshold, value)` 0 if lesser 1 if greater
- `smoothstep(start, stop, value)
- `pow(exp)`
- `ceil(value)` greater integer
- `floor(value)` lesser integer
- `fract(value)` value - floor(value)
- `sign(value)` +1 -1 (or 0?)
- `abs(value)`
- `clamp(value, max, min)`
- `min(value, value)`
- `max(value, value)`

## Spatial Shaders

<https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html>

Spatial Shader for 3D materials




- Fragments are not called Pixels because they have lots of more information:
	- Color
	- Screen location
	- UV coordinates
	- Normals
	- Light information
	- ....

In Godot, we can use either a shader node editor (`VisualShader`) or shader code (`Shader`).

Create a resource, choose either `Shader` or `VisualShader`, drag the file as material of the target object.

::: tip
	By creating a standard material you can modify it and later save it as an equivalent shader.

For VisualShader, a node editor will open with an output node.
Input nodes have to be added by hand.
Change the shader type (vertex, fragment...) with the dropdown selector.

Exponer valores con `uniform`.

```shader
uniform float myparameter = 3
```


## GLSL vs gdShader

- joined programs:
	- GLSL have several programs (vertex, fragment) with a main()
	- gdShader have a single program with several functions vertex() fragment()
- 

## Global uniforms

https://godotengine.org/article/godot-40-gets-global-and-instance-shader-uniforms/

Uniforms declared globals are setup in a game level configuration (
Any shader accessing them will access the same object.
They save having to set the uniforms in every shader in every object.

Examples of usage:

- Wind/turbulence texture: provide wind vector for the whole scene, so that shaders for particles or materials affected by wind can access it.
- User presence: a textures telling how far the user is, for example to bend vegetation.
- Interaction status, use a texture to say whether the grass has been cut, burned...
- World status: For example it it raining, so that materials can change their properties.

Instance uniforms are uniforms that do not live on the material but in the node.
(CanvasItem for 2D, GeometryInstance3D for 3D).
Mostly this is practical: Instead of navigating through the properties to look for the material you can change it directly in the node.
But if a single node contains many shaders these uniforms are shared by all of them.

It has limitations though due to hardware:

- they must be vector or scalars, not textures
- You can only have 16 per instance
- they are allocated by position and they should match
    - You can overcome that by specifying which index you refer
        `instance uniform vec4 hello : instance_index(5);`


## Normalización de coordenadas (Encuadre y relación de aspecto)

Un shader recibe las coordenadas de cada fragmento (`gl_FragmentCoords`)
en unidades de pixel, con el [0,0] en la esquina inferior izquierda.
Normalmente la resolucion concreta del dispositivo es algo de lo que nos queremos abstraer.
Lo que queremos es encuadrar nuestro objeto en el espacio disponible.
En ese caso, es más sencillo trabajar con coordenadas relativas al tamaño total de la pantalla.

La siguiente función convierte coordenadas de pantalla al intérvalo [0,1].

```glsl
vec2 normalize(in vec2 pixel_coords) {
    return pixel_coords / u_resolution.xy;
}
```

Si queremos el origen en el centro y las coordenadas en el intérvalo [-1,+1] entonces:

```glsl
vec2 normalize(in vec2 pixel_coords) {
    return pixel_coords / u_resolution.xy * 2.0 - 1.0;
}
```

Sin embargo, la relación de aspecto de la pantalla distorsiona las formas.
Por ejemplo, si tenemos una pantalla apaisada, alargará en horizontal las formas.

La siguiente función encaja el intervalo [-1, +1] verticalmente,
pero horizontalmente, en vez de ajustar lo centra,
usando la misma escala que para las y manteniendo así las proporciones:

```glsl
vec2 normalize(in vec2 pixel_coords) {
    vec2 result = pixel_coords / u_resolution.y;
    result.x -= (result.x-result.y)/u_resolution.y/2.0;
    return result*2.0/1.0;
}
```

Si queremos que también pase lo mismo en pantallas verticales,
la dimensión a centrar es la y.

```glsl
vec2 normalize(in vec2 pos) {
  vec2 result = pos;
  float offset = (u_resolution.x-u_resolution.y)/2.0;
  result.x -= step(0.0, +offset) * offset;
  result.y += step(0.0, -offset) * offset;
  result /= min(u_resolution.y, u_resolution.x);
  return result*2.0 -1.0;
}
```

Minimizando las operaciones:

```glsl
vec2 normalize(in vec2 pos) {
  float min_size = min(u_resolution.x, u_resolution.y);
  float scale = 1.0/min_size;
  float offset = u_resolution.y-u_resolution.x;
  return vec2(
    scale * (2.0*pos.x + step(0.0, -offset) * offset) - 1.0,
    scale * (2.0*pos.y - step(0.0, +offset) * offset) - 1.0
  );
}
```

También podemos generar una matriz de transformación afín.
Problema: No se como sacar la matriz de la función
para no recalcularla en cada mapeo,
y tampoco sé que si son más rápidas son las matrices
que las operaciones individuales.

```glsl
vec2 normalize(in vec2 pos) {
  float min_size = min(u_resolution.x, u_resolution.y);
  float scale = 1.0/min_size;
  float offset = u_resolution.y-u_resolution.x;
  return (vec3(pos, 1.0) * mat3(
    2.0*scale, 0.0, +step(0.0, -offset)*offset*scale -1.0,
    0.0, 2.0*scale, -step(0.0, +offset)*offset*scale -1.0,
    0.0, 0.0, 1.0
  )).xy;
}
```

## Distance field

One difference between classical computer shape drawing
and shaders is that the flow control is inverted.
In classical computer drawing, you pick the pixels belonging to a shape,
say a line segment or a polygon, and change its color.
You only change the pixels related to a given shape.
In shaders, you get a pixel, every pixel in the screen,
and you have to determine whether it belongs to the shape or not,
in order to change its color.

Because of that, distance field functions are very useful.
A distance field function returns how far a point is from a certain feature.
For example the perimeter of a circle, a shape or a font type.
Usually negative for inner points to discriminate them.
Given such a function you can use it.

For example, the distance function of a circle
of radius R centered in `c=ve2(cx, cy)` will have a distance function:
`distance(pixel, c)-R`.


¿Qué podemos hacer con los distance fields?

- Dando color a los pixel que tengan distancia negativa rellena la figura
    - `step(0.0, my_step(point))`
- Dandoselo a los pixeles alrededor de cero, con cierta tolerancia, pintaremos el perímetro.
    - Podemos marcar el borde por fuera, por dentro o por los dos lados escogiendo donde aplicamos la tolerancia.
    - `step(0.01, distance_field(pixel)) - step(-0.01, distance_field(pixel))`
- Podemos obtener antialiasing aplicando `smooth_step` en vez de `step` en las funciones anteriores.
- Podemos rotar/escalar/trasladar/sesgar una figura transformando las coordenadas de los pixeles antes de calcular la distancia.
- Mezclando dos funciones de distancia, podemos conseguir un [morphing entre figuras](https://thebookofshaders.com/edit.php?log=160414040957)
- Podemos fusionar dos figuras (blob merge) 
- Podemos tener una textura con las fuentes, codificadas como distance map, nos permite escribir las fuentes escaladas y rotadas, reduciendo el aliasing.



## Scaling field

This is my own variation of the distance field.
Is a function that determines to which scale of a shape a given point its inside the shape.
This can be used for scaling shapes, concentrical shapes, bordering...
The shape is preserved but distance to lines is not uniform, but depends on the angle to the center.


## Deterministic random number generators

¿Porqué necesitamos un generador aleatorio determinista?
Principalmente porque los shaders se ejecutan cada frame,
si introducimos elementos aleatorios y estos cambian en cada frame
perderiamos la continuidad temporal.

Una forma de tenerlos sería pregenerar los números aleatorios
en una textura y obtenerlos de la textura.
A menudo es suficiente pero:

- Limita la variabilidad al tamaño de la textura
- Ocupa memoria

La otra opción es una función dado un valor de entrada
entregue el mismo valor de salida pero que dicho valor
genere un campo parecido al ruido blanco:
Sin frequencias predominantes más alla de la de sampleo,
que rellene de forma uniforme el intervalo de valores posibles
y sin características direccionales detectables.

Una idea seria basarnos en la parte fraccional de una función
que devuelva valores mayor que uno.

[Goden Noise](https://www.shadertoy.com/view/ltB3zD) (based on the golden ratio phi and tangent function).

```glsl
float PHI = 1.61803398874989484820459;  // Φ = Golden Ratio   

float gold_noise(in vec2 xy, in float seed){
       return fract(tan(distance(xy*PHI, xy)*seed)*xy.x);
}
```
Tried and Golden noise is quite shitty.
Only some zones of the field is really noise like.
Most of the field has directional patterns.
I could have made something wrong, though.

El que usan en los ejemplos del libro:

```glsl
float random (vec2 st) {
    return fract(sin(
        dot(st.xy, vec2(12.9898, 78.233))
    )*43758.5453123);
}
```

Sin embargo las funciones trigonométricas son lentas
y cuando se van a valores altos pierden precision
y comienzan a generar patrones direccionales (por el redondeado?)

Por eso se desarrollaron en 2019 funciones de hash
para obtener resultados similares que por ser
operaciones simples son más rápidas y no tuvieran esos artefactos.

- [Hash based functions (paper)](https://jcgt.org/published/0009/03/02/)
- [Implementacoin en ShaderToy](https://www.shadertoy.com/view/4djSRW)

Normalmente los generadores tienen indican con dos numeros
dimensión de entrada y de salida.
Por ejemplo los ejemplos mapean un vector 2D a un escalar,
serian 2->1.
Si quisieramos uno que, a partir de un punto 2D nos retornara un color
necesitariamos un 2->3.
El hash propuesto para 2->1 es:

```glsl
float hash12(vec2 p)
{
	vec3 p3  = fract(vec3(p.xyx) * .1031);
    p3 += dot(p3, p3.yzx + 33.33);
    return fract((p3.x + p3.y) * p3.z);
}
```

## Perlin Noise

https://en.wikipedia.org/wiki/Perlin_noise

Los procesos naturales no son tan aleatorios como el ruido blanco.
La aletoriedad aparece dentro de una cierta continuidad.
El Perlin Noise emula esto muestreando la función aleatoria
solo en ciertos puntos que coinciden con los nodos de una rejilla.
El resultado de la función aleatoria se toma como gradiente
y se interpola los valores intermedios respetando dicho gradiente.

En 1D, el random controlaria la pendiente.
En 2D, controlaria un vector de pendiente.

Según la continuidad que se pretenda,
usaremos una interpolación de Hermite de diferente grado.
Para interpolar se usa por ejemplo Hermite de 3er grado
`t*t*(3-2*t)`
o si se quiere continuidad C2 usar Hermite de 5o grado
`t*t*t(10+t*(-15.0 + 6.0*t)`

Por ejemplo, en 2D,

```glsl
vec2 hash22(vec2 p)
{
	vec3 p3 = fract(vec3(p.xyx) * vec3(.1031, .1030, .0973));
    p3 += dot(p3, p3.yzx+33.33);
    return fract((p3.xx+p3.yz)*p3.zy);

}

float interp(float t) {
    // 3th grade hermite C1 continuity
    return t*t*(3.0 -2.0*t);
    // 5th grade hermite C2 continuity
    return t*t*t*(10.0+t*(-15.0 + t*6.0));
}

float perlin_noise_2d(vec2 xy) {                                                     
    // Determinamos el quad i,j en el que estamos (usando floor)                     
    vec2 ij = floor(xy);                                                             

    // Determinamos la posición relativa dentro del quad (usando fract)              
    vec2 uv = fract(xy);

    // Sampleamos hash 2->2 para las esquinas del cuadro
    vec2 g00 = hash22(ij);
    vec2 g01 = hash22(ij+vec2(0.0, 1.0));
    vec2 g10 = hash22(ij+vec2(1.0, 0.0));
    vec2 g11 = hash22(ij+vec2(1.0, 1.0));

    // Producto escalar entre las muestras de las esquinas
    // y el vector de las esquinas al pixel a calcular
    // Esto no se pa que
    float n00 = dot(g00, uv);
    float n01 = dot(g01, uv - vec2(0.0,1.0));
    float n10 = dot(g10, uv - vec2(1.0,0.0));
    float n11 = dot(g11, uv - 1.0);

    // Interpolamos interp(t) sera la hermite que escojamos
    float fu = interp(uv.x);
    float fv = interp(uv.y);
    float nx0 = n00 * (1.0-fu) + n10 * fu;
    float nx1 = n01 * (1.0-fu) + n11 * fu;
    float nxy = nx0 * (1.0-fv) + nx1 * fv;
    return nxy+0.5;
}
```




## Simplex noise

https://en.wikipedia.org/wiki/Simplex_noise

Ruido Simplex es un algoritmo, también desarrollado por Perlin,
que da mejores resultados, y es computacionalmente mejor.
Hace menos operaciones por vertice, haciendo sumas en vez de interpolaciones
y escala mejor con la dimension pasando de considerar
O(2^N) vertices por pixel a O(N^2) vertices por pixel
donde N es la dimensión.

Un simplex es la forma más sencilla en una determinada dimensión.
La rejilla ahora no esta formada por cuadrados, cubos, hipercubos...
sinó por triangulos, tetraedros, hipertetraedros...
Esto reduce los puntos a considerar cuando interpolamos un punto.

Podemos definir los triangulos partiendo los cuadrados de la rejilla de Perlin,
definiendo en que triangulo estamos con la condicion `u > v`.
Pero esos triangulos no son regulares.

Primero se sesga la rejilla cuadrada para que los puntos generen
simplex regulares.



TODO: Algorithm


## Fractal noise


**Fractal Brownian Motion / Fractal noise:**
Given a noise signal, a fractal noise is generated by
adding several versions of increasing frequency (sampled at greater distance) and decreasing amplitude.
This is analog to fft sinusoid addition but with noise.

**lacunarity:** this is the step between 'harmonics' (analog to frequency)

**octaves:** 






