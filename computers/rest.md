# REST APIs

https://www.youtube.com/watch?v=CVBpYfPKGlE

## The base HTTP

Explota la expresividad del protocolo HTTP.

Petición

```http
POST /api/myobject HTTP/1.1
Host: canvoki.net/
User-Agent: Mozilla/5.0 Linux
Content-Type: application/json
Accept: application/json
Content-Length: 1232
Conneciton: Keep-alive

{myobject: {field1: "value"}}
```

- Header y content separados por una linia en blanco.
- La primera línia del header: verbo, endpoint y protocolo
- El verbo infrautilizado en la web ordinaria: POST, GET pero tambien PUT, PATCH, DELETE...

Respuesta:

```http
HTTP/1.1 200 OK
Date: Tue, 21 May 2023 10:00:00 GMT
Server: nginx/ (Ubuntu)
Last-Modified: Tue, 21 May 2023 10:00:00 GMT
Content-Type: application/json
Content-Length: 1232
Connection: close

{myobject: {field1: "value"}}
```

## Principios arquitectónicos

- Uniform interface
	- Las peticiones tienen la misma pinta sea cual sea su origen: browser, applicación, mobil...
- Client-server
	- Interficie asimétrica. El cliente hace peticiones, el servidor las responde.
- Stateless
	- La petición está auto contenida. El cliente no guarda información de quien es el cliente, ni que peticiones ha hecho antes. (Esto excluye el estado de la aplicación)
- Layered System
	- El cliente desconoce de las capas que su petición debe atravesar para resolverse
		- Proxies, Caching, Security layers, Load balancing...
- Cacheable
	- El servidor incluye en la respuesta información sobre si el resultado se puede cachear (el cliente o los intermediarios).
- Code on Demand
	- Opcionalmente el cliente puede pedir al servidor código a ejectuar para hacer alguna acción
	- Es un poco turbio e inseguro.

## Rest Maturity Model

Niveles de adherencia a estandard (Leonard Richadson)

- Level 0: Swamp of POX
- Level 1: Resource based URLs
- Level 2: HTTP Verbs
- Level 3: HATEOAS (hipermedia links to discover the api)

## Stateless

Los clientes no estan vinculados a un servidor específico.
Los servidores no mantienen estado de sessión.

Esto hace la arquitectura escalable:
En un entorno multi servidor con autobalanceado,
los clientes pueden cambiar de servidor sin que nada cambie.

Esto hace la arquitectura disponible:
Incluso en un entorno de servidor único,
el servidor no ha de memorizar las interacciones previas.
Si el servidor peta, otro servidor puede reemplazarlo sin perder información.

También hace que sea más fácil de cachear.
Toda la información de la petición esta en la propia petición.
Se puede retornar respuestas idénticas a peticiones idénticas.

Que la sesión no tenga estado no implica que la aplicación no lo tenga.
Acciones del cliente pueden modificar el estado de la aplicación.
Es un estado compartido por los servidores normalmente en una base de datos.

Tambié se permite estado propi de sesión (por ejemplo, un carro de compra)
con dos condiciones.

- El estado se almacena externamente al servidor, en una base de datos o en una cache compartida (redis).
- La identificación de la sesión/usuario se almacena en la petición (ie, un token jwt en la cabecera)

## Security considerations

- API Validation and Sanitization
- Monitoring and logging
- Data Encryption (https not http)
- Regular Database Audits
- Penetration testing
- Authentication and Authorization

## Endpoints

Focaliza en recursos, no en las acciones o verbos.
Usa los verbos disponibles en HTTPS (Son muy limitados a CRUD!!)

- Create -> POST
- Read -> GET
- Update -> PUT  (PATCH si només s'envien els camps editats)
- Delete -> DELETE

Rules:

- No trailing slash
- Use hierarchical relationships (also insert ids in path)
- Use hyphens for greater scanneability
- Focus on resources, not actions
- Use plurals instead of singlulars (for consistency)

```
# Contra example
/api/GetOrderActiveItems/?id=122

# No trailing slash
/api/GetOrderActiveItems?id=122

# Hierarchical relationships
/api/order/122/getActiveItems

# Use hyphens
/api/order/122/get-active-items

# Focus on 
GET /api/order/122/active-items

# Plural names
GET /api/orders/122/active-items

# Complexity (contra example, amb l'order ja sabem que customer i store tenim)
GET /api/costumer/34/store/1/orders/122/active-items

# Not a rule but more consistent with other item queries
GET /api/orders/122/items/active

# Por ejemplo:
GET /api/orders/122/items
GET /api/orders/122/items/1
GET /api/orders/122/items/inactive  # Other filter
POST /api/orders/122/deliver  # Non CRUD action

```

## Resource format

Se hacen servir varios formatos:

- JSON (`application/json`): Simple, efficient, widely supported
- XML (`application/xml`): Verbose, large, slow
- YAML (`application/x-yaml`)): Més expressiu, suport limitat

Por ser el más usado y mejor soportado por las librerias, se recomienda JSON.

Para algunas aplicaciones se usa JSONP, codigo javascript con el json incrustado.
Se hace para evitar incompatibilidades con CORS.
En estos casos, como el contenido es javascript, el content type será `application/javascript`.

Como los indicamos

- Request Header `Content-Type`: Formato en el que envio la petición
	- Error 415: Unsupported Media Type, si el servidor no soporta ese tipo en la petición
- Request Header `Accept`: Que formatos me gustaria recibif como respuesta, separados por comas
	- Error 406: Not Acceptable, si el servidor no puede servir ninguno de los propuestos
- Response Header: `Content-Type`: El formato que el servidor ha escogido para responder

Otra forma de especificarlo es añadiendo extension a la url.

## Exceptions

Usar en lo posible los códigos de estado HTTP

https://restfulapi.net/http-status-codes/

- 1xx: informational
- 2xx: successfull
	- 200 OK: Request exitosa con contenido en el body
	- 201 Created: Exito y recurso creado
	- 202 Accepted: Acceptada pero no concluidaa
	- 204 No content: Peticion exitosa sin contenido (normalmente POST, PUST, DELETE, si no retorna el estado modificado)
- 3xx: redirects
	- 301 Moved Permanently: Cuando el modelo de recursos ha cambiado
	- 302 Found: Redirección temporal, normalment la resuelve el navegador
	- 303 See Other: Proporciona un enlace donde ver el resultado, normalmente para operaciones largas cuyo estado se puede monitorizar
	- 304 Not Modified: Para peticiones con headers If-Modified-Since o If-None-Match, va sin body, para ahorrar ancho de banda
	- 307 Temporary redirect: Si posteriores peticiones tienen que seguir usando la url originals
		- Ejemplo: si temporalmente se mueve a otro servidor
		- La nueva url temporal en el header `Location:`.
		- Aun así el body debe contener html con el enlace por si el agente no redirige o mientras lo hace o si falla.
- 4xx: client errors
	- 400 Bad request: La petición es incorrecta (validación...)
	- 401 Unauthorized: El usuario no se ha autenticado, repita la petición una vez se haya autenticado
	- 403 Unauthorized: Un usuario autenticado no tiene acceso al recurso
	- 404 Not found: Not such a resource
	- 405 Method not allowed: 
		- Retorna els metodes permesos en la capcelera `Allow:  GET, POST`
	- 406 Not Acceptable: ninguno de los media types indicados en `Accept:` se pueden retornar
	- 410 Gone: El servidor ha reconocido el recurso como existente en el pasado pero ya no
    - 412 Precondition Failed: one or more conditions in the request header fields evaluated to false
	- 415 Unsupported Media Type: Content-Type recibido no se soporta (406 es para el requerido por la peticion para la respuesta, 415 es el de la peticion misma)
- 5xx: server errors
	- 500 Internal Server Error: Errores inexperados
	- 501 Not implemented: El punto de entrada o el método no esta disponible, pero si en un futuro
	- 502 Bad Gateway: Error en el backend
    - 503 Service Unavailable: El servicio está temporalmente inaccesible (mantenimiento, ataques...)a


Y el Payload?? No hay una sola forma de hacerlo.

https://www.baeldung.com/rest-api-error-handling-best-practices

- `error`: código
- `message`: Mensaje leible corto, presentable a los usuarios finales
- `detail`: Detalles específicos para el caso, para los desarrolladores del cliente, no del usuario
- `help`: (opcional) 

IETF RFC 7807. Poca gente lo sigue.

- `title`:
	- descripción generica del error para humanos (internacionalizado)
	- ex: "Incorrect username or password."
- `type`
	- uri, identifica el error y se puede usarse para obtener mas info del error
	- ex: "/errors/incorrect-user-pass"
- `status`:
	- Igual que el status HTTP
	- ex: 400
- `detail`:
	- Especificidades del error para esta instancia del error.
	- ex: "Authentication failed due to incorrect username or password."
	- ex: "Missing attribute: badfield"
- `instance`:
	- uri con la info más específica del error
	- ex: "/login/log/abc123"

Cualquier otro atributo se acepta y es considerado como una extensión.


## Versionado

Las API's sirven para independizar el desarrollo de cliente y servidor.
Los cambios en las APIs afectan a los clientes, han de ser estables.
Cuando se modifican de una forma no compatible,
una buena practica es mantener la version anterior,
o como mínimo que la nueva esté disponible en una url diferente.

Si hacemos el versionado en la url será cache friendly:

- `/api/v2/...`
- `/api/...?version=2`

## HATEOAS

**H**ypermedia **A**s **T**he **E**ngine **O**f **A**pplication **S**tate

Un cliente puede usar la API sin ningún conocimiento previo de la API
simplemente interaccionando con ella.
La respuesta no solo devuelve el contenido de la petición
sino una lista de links a las acciones relacionadas.

Si los clientes usan esos links,
el servidor podría cambiar la API sin romper los clientes.

- Performance cost
- No hay standard
- Muy poco adoptado


## Puntos de entrada más allá de CRUD

Aunque los métodos recogen los verbos de CRUD,
REST no restringe la funcionalidad a CRUD.

### Procesos

Un proceso es un recurso que representa una acción.
Puede colgar del recurso al que se aplica.

```http
POST /api/orders/122/deliver
```

Podemos retornar el resultado.

También tenemos la opcion de retornar `202 Accepted`
si el proceso no retorna inmediatamente.
Linkat al recurso que representa al estado del proceso.

```http
202 Accepted

{
	"_links": [
		{
			"rel": "self",
			"href": "/api/orders/122",
		}
	]
}
```

Ventajas sobre CRUD:

- Lógica de negocio encapsulada en las acciones, workflow explícito
	- No hemos de saber que campos hay que modificar para dar de baja a un usuario
- Podemos controlar el acceso a las acciones que se pueden hacer
	- No hablamos de campos que podemos alterar sino de acciones que podemos hacer
- Podemos usar los links hypermedia para poner de manifiesto las acciones disponibles
	- según el estado del recurso
	- según el usuario que lo pida


### Acciones sobre múltiples objetos: Batch y bulk

Ambos sirven para crear/afectar múltiples objetos en una sola peticion.

- Bulk: Pueden fallar y se retorna el estado de cada uno en un 200
- Batch: Si uno falla, fallan todos

Estas operaciones suelen tardar mucho.
Considerar en ese caso, crear un proceso


## Variants

### Zoom-embed patterns

Permeten controlar la quantitat d'informació que inclourà la resposta.

Zoom: Escull els camps inclosos.
Podría ser invers si excloem camps.

`GET /accounts/12345?fields=id,name,description`

Incrustar recursos relacionats.

`GET /accounts/12345?include=preferences`

Puede ahorrar el anti-pattern del "n+1 query problem".
La peticion de un objecto acaba en N queries de los objetos relacionados.
En un profile de queries no es visible porque todas acaban en un tiempo razonable.





