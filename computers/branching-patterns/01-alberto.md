## Healthy branching

Problema: Código de la rama principal remota con errores, falta confianza en puesta producción.

Solución: Conjunto de test automatizados para control de errores.

Fuerzas: Grado de pruebas para proporcionar suficiente confianza. Crear test que cubran todos los casos es complicado.

# Integration Patterns

## Mainline Integration

Problema: Dificultad de integrar varios desarrollos dentro de un equipo de trabajo.

Solución: Los desarrolladores integran su trabajo dentro de una rama principal.

Fuerzas: En el caso que nuestro desarrollo en producción sea la rama mainline.

## Feature Branching

Problema: Dificultad de integrar funcionalidades en mainline.

Solución: Crear rama por funcionalidad e integración en mainline cuando se complete la funcionalidad.

Fuerzas: Agrupar funcionalidades en ramas permite activar y desactivar la nueva función. 

La función es muy grande(desarrollo de varios dias) dificulta la integración en mainline.

Alternativa: **Continuous Integration** integrar en mainline diariamente) vs integrar por funcionalidad finalizada.

Alta frecuencia vs Baja frecuencia

## Integration Frequency

Problema: Grado dificultad para integrar rama local con mainline.

Solución:  Frecuencia de integración de las ramas locales con mainline. 

Baja frecuencia vs Alta frecuencia.

Fuerzas: Fusiones grandes y pocas(complejidad alta) vs fusiones pequeñas y frecuentes(complejidad baja)

## Continuous Integration

Problema: A mayor diferencia entre el código local y mainline, mayor dificultad de integración.

Solución: Alta frecuencia de integración, desacopla la longitud de la función de la frecuencia de integración.

Las integraciones son más pequeñas y requieren menos trabajo.

Fuerzas: Mayor dificultad en un mainline saludable vs funcionalidad acoplada a una rama.

Uso de Keystone Interface para evitar uso de la funcionalidad hasta finalizar el desarrollo.
