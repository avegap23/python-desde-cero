'''
Normalmente está vacío, si bien indica a nuestro intérprete que
esta capreta va a ser un paquete... Pero, ¿qué hace realmente?

    - inicialización: podemos introducir una carga de librerías, variables globales...
    - organización de APIs: importación de ciertas partes de una aplicación externa,
    la cual puede ser una llamada a un servidor, un recurso...
    - control de visibilidad a veces podemos determinar qué es público y qué es privado

Este archivo se está empezando a determinar como un tipo de archivo antiguo, si bien nos
lo dejamos "guardado" para que garanticemos la compatibilidad (estructura del programa/proyecto,
control de inicialización y demás).

Distinción:
    -> módulos: unidad básica de organización, se importa de forma directa.
        import math
    -> paquetes: jerarquía que nos permite organizar directorios completos con múltiples
    módulos u otros paquetes.
'''

from .archivo_json import leer_json, guardar_json, modificar_json
# se hace una precarga con todo lo que necesitamos
# .archivo... significa "busca dentro del mismo paquete el archivo XXXX"