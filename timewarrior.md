## Intervalos y tags

Timewarrior guarda intervalos de tiempo con ciertos tags asociados.
Sumariza el tiempo total de cada tag.


```bash
$ timew start 'Read chapter 12' # Empezar ahora
$ timew start 3pm 'Read chapter 12' # La llevo haciendo desde las 3pm
$ timew cancel  # Borra el intervalo activo (nada si no lo hay)
$ timew track 9am - 11am 'Staff Meeting'  # A posteriori
$ timew continue @1 
```



## Corrigiendo intervalos

A menudo no grabamos a tiempo o cometemos errores al especificar los tags.
Se pueden editar los intervalos a posteriori.
Los intervalos se identifican con un `@n`, pe. `@1`

```bash
$ timew summary :ids   # Muestras los ids de los intervalos
$ timew untag @1 tag1 tag2 # quitar tags
$ timew tag @1 tag1 "tag largo2" # añadir tags
$ timew lengthen @1 20mins  # añadir 20 minutos
$ timew shorten @1 1hour # acortar una hora
$ timew move @1 8:30am # Mover el inicio (manteniendo la duracion?)
$ timew split @1 # parte un intervalo en dos (se puede indicar el punto?)
$ timew join @1 @1 # Junta los dos intervalos (el hueco entre los dos se elimina?)
$ timew delete @1 @4

```

