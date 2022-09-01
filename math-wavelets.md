# Wavelets

Alternativa a las funciones trigonometricas para analizar señales.

Las funciones trigonometricas son infinitas y no son buenas para tener resolución temporal.

Duda: Se usaba la DFT con enventanado, porque no es bueno?

Una familia de wavelets son un conjunto de funciones que permiten extraer informacion frecuencial y temporal de la señal.
Las wavelets no son un conjunto de funciones concreto.
Podemos inventarnos las nuestras si cumplen una serie de condiciones.

## Condiciones necesarias para una familia de wavelets

- **Zero mean:**
 Integral de todas las funciones de la familia ha de ser cero.
 Ha de tener tanta area positiva como negativa.

- **Finite energy:**
  The integral of the square is finite.
  This localizes it in time


Ejemplo Morlet family: Es una sinusoide multiplicada por una gausiana.

e(iwt) e^(-t¹/2)




