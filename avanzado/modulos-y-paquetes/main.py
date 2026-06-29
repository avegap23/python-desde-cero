'''
proyecto_JSON/
    |
    |-- main.py: lógica de negocio, donde cargamos cosas y llamamos a funcionalidades
    |
    |-- gestor_JSON/
            |
            |-- __init__.py: inicialización de paquetes
            |-- archivo_json.py: lógica de funcionamiento de mi programa
'''
# IMPORTS ---------------------------------------
from gestor_json import leer_json, guardar_json, modificar_json # importación paquete gestor_json

# VARIABLES GLOBALES ----------------------------
RUTA = "datos.json" # constante, nombre del archivo y su extensión

persona = {
    "nombre": "Fulano",
    "edad": 28,
    "ciudad": "Zaragoza"
} # diccionario, casualmente, con la misma estructura que un JSON

# Después de crear el diccionario, lo vuelco al disco
guardar_json(RUTA, persona)

# Podría leer el archivo a ver que tiene dentro
datos_leidos = leer_json(RUTA)
print(f"Datos leídos: {datos_leidos}")

# Podría modificar uno de los valores
datos_modificados = modificar_json(RUTA, "nombre", "Nito")
print(f"Datos modificados: \n{datos_modificados}")