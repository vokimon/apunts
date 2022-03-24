# Docker

## Qué ès?

Com les màquines virtuals serveix per aillar processos.
A diferència de les MV's, no duplica recursos.

Es basa en dues tecnologies de Linux:

- cgroups: per limitar els recursos (memoria, cpu...) dels processos
- namespaces: Limita l'avast que pot veure el procés (altres processos, xarxa, sistema de fitxers...)

Docker afegeix una capa per sobre:

- Aporta una forma uniforme de definir i accedir a les aplicacions

## Containers

Creem una container interactiu (-it) de docker, basant-nos en una imatge d'Ubuntu.

```bash
docker run -it ubuntu
```

- Executa una comanda dintre d'un sistema de fitxers "copiat" de la imatge.
- Les modificacions que fem sobre el sistema de fitxers no afecten a altres instancies d'ubuntu que llencem.
- Els processos que llencem a dintre son visibles des de el sistema pare, pero no al reves.
- Quan termina el proces (en aquest cas es bash, per defecte) la imatge creada queda parada (no es destrueix)
- Des de fora podem parar el process amb `docker stop 451bccb8de1c`

```bash
docker ps -a  # L'opció -a es per veure tambe els que estan parats
CONTAINER ID   IMAGE    COMMAND   CREATED         STATUS                      PORTS     NAMES
5fabbdd99c65   ubuntu   "bash"    5 minutes ago   Exited (0) 5 minutes ago              heuristic_lamarr
```

Podem fer servir tant els id's com els noms per referir-nos a les instàncies.

```bash
docker log 5fabbdd99c65 # ens mostra la sortida estandard del procés principal, util sobretot si no l'hem executat interactiu o hem sortit
docker log -f 5fabbdd99c65 # 'follow' sigue monitorizando lo que sale despues
docker stop 5fabbdd99c65
docker start -i 5fabbdd99c65 # para arrancarlo otra vez
docker rm 5fabbdd99c65 # para borrarlo definitivamente del sistema
docker run -it ubuntu # volveria a arrancar uno diferente
docker exec -it 5fabbdd99c65 ls -alF
```

## Imatges

Les imatges de partida les trobem a la web [Docker Hub](https://hub.docker.com/explore)

```bash
docker images # Llista les imatges descarregades
```

Las images tienen tags (versiones)

## Dockerfile

```docker
FROM scratch
ADD mytarball.tar.gz
RUN tar xvfz mytarball.tar.gz
COPY file /var/www/html
CMD ['/bin/bash']
```

- `FROM` es la imagen de base  imagen:tag
- `ADD` copia del sistema de ficheros local a dentro del container
- `RUN` ejecuta comando dentro del container
- `ENV` establece una variable de entorno para los comandos que se ejecuten (Sobrescribible desde fuera)
- `CMD` fija el comando inicial, es una array estilo argv (elemento por parametro)
	- Sobreescribible por cli con el parametro del run
- `ENTRYPOINT` fija el comando para arrancar el comando inicial `sh -c`
	- Sobreescribible por cli con `--entrypoint`
- `LABEL` metadata de la imagen  mylabel="value"
	- maintaner, application...
- `WORKDIR` cambia al directorio para los siguientes comandos

Per a executar el Dockerfile

```bash
docker build -t myapp .
```

La imatge es dirà _myapp_

```bash
docker run -it --rm myapp -p8000:80
```

- Per obrir i mapejar  ports -pOUTER:INNER
- Per esborrar el container en acabar el run, `--rm`
- `-f mydockerfile` si el fichero no se llama `Dockerfile` (por ejemplo para tener varios en un directorio)

## Environ

Patron util usar las variables de entorno para modificar la configuración.

- Se usa ENV en el Dockfile para definir el valor por defecto
- Se sobrescribe en CLI `docker run` con la opcion `-e VAR=value`
- Los programas lo cogen usando 
- Se usa en los ficheros copiados substituyendo ${VAR}

## Cache

- Docker crea capas cada comando sacando el checksum como id.
- Se reaprovechan los pasos de anteriores ejecuciones.
- Interesa poner abajo los comandos que más a menudo vayan a alterar la imagen.
- Puede interesarnos juntar varias sentencias RUN con `&&` para reducir las capas

## Multistage build

Útil per a no incloure a la imatge final tot el que cal per construir l'aplicació,
com ara l'es eines de build i les dependencies de desenvolupament (composer, babel, cython...).

- Tamany: Ocupa menys
- Seguretat: Es redueix la superficie d'atac

Construim l'aplicació en una imatge i després copiem els fitxers construits a l'imatge final.

```dockerfile
# Partim d'una imatge amb les eines de construcció
FROM composer AS dependencies
WORKDIR /app
# Copiem nomes els fitxers de dependències
COPY dependencies.json /app
RUN make dependencies
# Fins aquí la imatge no depén del nostre codi
COPY . /app
RUN make build
# Inclou l'aplicació muntada pero també les eines de construccio
# Creem una nova imatge neta
FROM ubuntu
# Copiem no des del host sino de la imatge inicial
COPY --from dependencies dist/ /var/www/html
RUN ...
```

## Xarxa

Els ports d'escolta del container no son visibles a l'exterior per defecte.
Tampoc colisionen, que això es bó.

Un Dockerfile defineix un port publicable amb `EXPOSE`, pe `EXPOSE 80`.
Això vol dir que podem mapejar aquest port a un port del host.

L'opció `-P` mapeja tots els ports exposats a ports aleatoris del host.
Podem esbrinar els ports mapejats amb `docker ps`.

Normalment volem exposar-ho a un port concret: run amb `-p hostport:containerport`
Si no ponem un `OUTER:`, s'assignen ports aleatoris.

Els ports exposats s'hereten.
Per exemple, les imatges oficials d'apache exposen el port 80.
Els docker de que depenen de la imatge d'apache tambe el tindran.

## Reinici automàtic

```bash
composer run --restart=no|always|onfailure:3|unless-stop
```

## Recursos

- `--memory 4g` Mata el proceso cuando se pasa
- `--cpus 1.5` Reserva como maximo ese slot de cpu (multiproceso)
- `--cpu-shares N` peso para repartir la CPU si hay escasez (1024 defecto)

## Volúmenes

Util para mantener el estado entre ejecuciones.
Por ejemplo las bases de datos, uploads...
Son directorios que se montan en las imagenes.

Tambien es muy util para montar el codigo en desarrollo
para acelerar el flujo de desarrollo.

- `-v /data` crea una carpeta random
- `-v volumename:/data` reusa un volumne por nombre
- `-v ruta/:/data` reusa un volumne por path

```bash
docker volume ls # lista los volumentes
docker volume create name #  crea un volumen especifico
docker inspect -f  "{{json .Mounts}}" my-app  # Lista los volumenes montados por el container my-app
```

Por defecto los guarda en un directorio de docker (var/lib/docker/).
Podemos especificar el directorio que montamos.

Tambien se puede especificar el VOLUME en el Dockerfile.
En ese caso, si no le especificamos nada, docker lo creara
donde crea los dockers aunque no digamos nada en cli.

```dockerfile
VOLUME 
```


## Publicacion

Crear una cuenta en docker hub.
En settings linkad con la cuenta del repo (github, bitbucket...).

## Composición de servicios

`docker-compose` es una capa por encima de docker
que agrupa diversos contenedores en una aplicación
especificando los parametros con los que llamariamos a `docker run`.

Se define en el 

```yaml
# docker-compose.yaml
version: 2.3
services:
  myservice:
    images: ubuntu         # Esta imagen la toma tal cual
    volumes:               # Monta el directorio actual en /var/www/html
      -${PWD}:/var/www/html
    ports:
      - 8000:80
  myapp:
    build:                   # Esta imagen es construida
      context: ${PWD}           # Path en el que se construira la imagen, tomamos PWD del entorno de usuario
      dockerfile: Dockerfile    # Fichero Dockerfile para construir la imagen
    ports:                   # Expondra el puerto 80 interno como 8001 en localhost
      - 8001:80
    environment:             # Pasara estas variables de entorno
      - VAR=value
    depends_on: # Esperara a que el otro servicio este levantado
      - myservice
```
 
```bash
docker-compose up -d 
```

- `-d` para detach (background)

Ofrece comandos que se aplican a la vez a todos los containers definidos en el fichero:

- `docker-compose ps` Estado de los containers
- `docker-compose log` Salida combinada de los containers
- `docker-compose top` Top de procesos en los containers
- `docker-compose stop` Para los procesos pero sin eliminarlos
- `docker-compose down` Elimina los contenedores
- `docker-compose build` Solo construye las imagenes


La imagen construida se llama por defecto, como el directorio y el nombre del servicio: `myproject_myapp`.

- `myproject` por el directorio en el que está el yaml
- `myapp` por la etiqueta del servicio

Las siguientes ejecuciones reusan la imagen creada.
Hace falta forzar con `docker-compose up --build`

## Componiendo para multiples entornos

No es buena idea hardcodear el environment en el compose

- Cambiar de tipo de entorno: devel, testing, prod...
- Secrets en el repositorio!

```yaml
  ...
    environment:
      - VAR  # No igualamos a nada, se coge del entorno
  ...
```

## Networking en compose

Por defecto, con `docker-compose` cada docker tiene su propia red.
Para que dos contenedores se vean, tienen que estar en la misma red.
Podemos crear redes y mover contenedores entre ellas.
En ese caso, el nombre de contenedor hace de servername.

Utilidades de red:

- `docker network ls`
- `docker network create NETWORK`
- `docker network connect NETWORK CONTAINER`
- `docker network disconnect NETWORK CONTAINER`

Los servicios en un docker-compose se levantan, por defecto, como hosts diferentes de la misma red local `default`.
Los composers se ven entre ellos usando como dns el nombre del servicio.
Pero podemos crear estructuras de red mas complejas.
Todos los contenedores se ven entre ellos si comparten red.

Cada servicio define sus `networks` cuando queremos no ponerlas en `default`:

- Las aplicaciones solo se pueden ver si tienen una red en común.
- Esto permite aislar servicios para más seguridad

```yaml
...
services:
  myservice:
    ...
    networks:
      - mynetwork
networks:
  mynetwork:
  myexistingnetwork:
    external:    # creada fuera del docker-compose con docker-network
      name: myothernetwork
```



























