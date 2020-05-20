# TimeWarrior

Timewarrior es una herramienta de linia de comandos
para llevar el conteo del tiempo que dedica a diferentes tareas.

Almacena intervalos de tiempo a los cuales asignamos una o varias etiquetas (tags).

Ofrece comandos para crearlos, editarlos y visualizarlos.


## Intervalos y tags

```bash
$ timew start 'Read chapter 12' # Empezar ahora
$ timew start 3pm 'Read chapter 12' # La llevo haciendo desde las 3pm
$ timew cancel  # Borra el intervalo activo (nada si no lo hay)
$ timew track 9am - 11am 'Staff Meeting'  # A posteriori
$ timew continue  # Copia ultimo intervalo abierto con los mismos tags empezando ahora
$ timew continue  8min ago # Copia ultimo intervalo abierto con los mismos tags empezando hace 8min
$ timew continue @3 9:30 - 10:40 # Copia ultimo # Copia el intervalo @3
$ timew undo  #  deshace la ultima acción
```

## Visualizando

```bash
$ timew summary # Resumen del dia
$ timew summary :week # Resumen de la semana
$ timew day  # Timing visual del dia
$ timew week  # Timing visual de la semana
$ timew month  # Timing visual del mes
$ timew export  # muestra un json con toda la info
```

## Corrigiendo intervalos

A menudo no grabamos a tiempo o cometemos errores al especificar los tags.
Se pueden editar los intervalos a posteriori.
Los intervalos se identifican con un `@n`, pe. `@1`

```bash
$ timew summary :ids   # Muestras los ids de los intervalos
$ timew untag @1 tag1 tag2 # quitar tags
$ timew tag @1 tag1 "tag largo2" # añadir tags
$ timew modify start @1 14:00 # Mueve el inicio del intervalo
$ timew modify end @1 15:00 # Mueve el final del intervalo
$ timew lengthen @1 20mins  # añadir 20 minutos
$ timew shorten @1 1hour # acortar una hora
$ timew move @1 8:30am # Mover el inicio manteniendo la duracion?
$ timew split @1 # parte un intervalo en dos (iguales, no se puede especificar el punto)
$ timew join @2 @1 # Junta los dos intervalos usando el start de @2 i el end de @1
$ timew delete @1 @4 # Borra los intervalos especificados
```

