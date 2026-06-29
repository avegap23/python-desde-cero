# módulo de control de JSON - Paquete GESTOR_JSON

# IMPORTS ---------------------------------------
import json # https://docs.python.org/3/library/json.html
from pathlib import Path # https://docs.python.org/3/library/pathlib.html

# FUNCTIONS -------------------------------------
def leer_json(ruta_archivo):
    ruta = Path(ruta_archivo) # convertimos la ruta que le pasamos en un objeto

    # comprobación si existe la ruta, es decir, si existe el archivo como tal
    if not ruta.exists():
        return {} # si no existe, devolvemos un diccionario vacío
    
    # si todo está OK, abrimos el archivo ¡¡siempre en modo lectura!!
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo) # volcado de datos en una variable, se lee archivo json

    return datos # retornamos el contenido del archivo al principal

def guardar_json(ruta_archivo, datos):
    ruta = Path(ruta_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        # indent: para formatear el archivo correctamente
        # ensure_ascii: permite guardar caracteres especiales (ñ, tildes...)

def modificar_json(ruta_archivo, clave, valor):
    # 1º se carga el archivo, es decir, se lee:
    datos = leer_json(ruta_archivo)

    # 2º se cambian los datos pertinentes
    datos[clave] = valor

    # 3º se guarda el archivo nuevo
    guardar_json(ruta_archivo, datos)

    return datos