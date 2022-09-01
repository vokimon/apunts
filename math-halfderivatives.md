# Half derivaties


Intuitivamente si las derivadas de un monomio, decrementan el exponente en uno,
las derivadas fraccionales deberiamos obtener monomios de exponentes fraccionarios.
Nos permitiria obtener funciones intermedias a las derivadas de ordenes enteros.

## Properties

(d/dx)^(1/2) (d/dx)^(1/2) f(x) = d/dx f(x)

Integral fraccional

Cauchy formula for repeated integration (using gamma instead of factorial for non-integers)
Se convierte en la forma Riemman-Liouville Fractional Integral

integral^p (a,t) f(x) dx^p = 1/Gamma(p) integral (a,t) (t-x)^(p-1) f(x) dx

(la variable de la integral resultante es t)

integral^p integral^q f(x) = integral^(p+q) f(x)

Gamma no esta definida para negativos enteros asi que no podemos usar la formula para derivar.

Pero podemos derivar en orden entero una integral fraccional para tener una derivada en orden fraccionario.


Riemman-Liouville

(d/dt)^p f(t) = (d/dt)^k int^æ (a,t) f(x) dx^æ
1/gamma(æ) d/dt^k int (a,t) (t-x)^(æ-1) f(x) dx

where k = p+æ and k is integer

A diferencia de las derivadas enteras que son operadores locales
las derivadas 

Hay otras formas de definir la derivada fraccional que mantienen la propiedad.

Por ejemplo, si invertimos en la formula el orden de la integracion y la derivada entera,
no da el mismo resultado.






