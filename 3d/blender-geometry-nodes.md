# Blender: Geometry nodes

## Concepto

- Es un modifier que podemos definir lo que hace modularmente juntando nodos
    - Nodos funcionales interconectados por _sockets_ o connectores
    - Los datos que se comunican por los sockets son tipados
- Modifican la geometría a la que se aplican generando de forma **no destructiva**
- Como otros modifiers se pueden encadenar uno detrás de otro, la salida de uno es la entrada del siguiente
- Los nodos de un modifier forman un _node group_, siempre tienen dos nodos especiales:
    _group input_ que recibe la entrada y _group output_ que envia la salida.
    - Por defecto vienen directamente conectados. Si lo desconectamos nos quedamos sin salida.
- Se pueden aplicar a distintos tipos de geometrías:
    - Mayas (meshes)
    - Curvas (curves)
    - Point coulds (puntos)
    - Volúmenes (volumns)
    - Instancias (instances)

Hay dos conceptos que suelen ser la misma cosa en programación pero en GN son distintos.


- Attribute:
    - Dato que cada elemento (vertex, edge, face, control point...) tiene.
    - Columnas en la tabla de datos
    - Tienen un tipo
        - Integer, 2D Integer vector, Integer Vector (3D)
        - Float, Boolean, Integer, Vector, Color(o ByteColor), String, 2D Vector (UV),
          Integer Vector, 2D Integer Vector
        - 4X4 matrix (transforms)
        - Quaternion (for rotations
    - Se hacen conversiones implícitas
        - Color y Vector (vector 0..1 clampeado)
        - Float y Color (grayscale o tomar el rojo)
    - Tienen un domain (conjunto de valores válidos)

- Fields:
    - Es una instrucción que indica de donde coger un valor que se evalua en un contexto.
    - Si, acaba cogiendo atributos, pero en un lugar concreto
    - TODO: Aun no entiendo todo
    - https://www.youtube.com/watch?v=a-4oCHe-hDE



## Debugar

- Hover en los sockets, dice que valores pasaron la ultima vez por el socket, si pasaron
    - La red funciona por pull, si no esta conectado a la salida no se evalua







## Sockets

## Selección de Tutoriales

- Bases de los GN haciendo legos
    - https://www.youtube.com/watch?v=4yrsAiTdMj4

 
