'''
Diccionario:
    - Colección de elementos, donde cada uno de ellos tiene la estructura siguiente:
        dic {
            key: value,
            key_n: value_n
        }

    - Es lo más parecido a JSON y BSON, es decir, lo podemos utilizar como un simil a BBDD:
        -- ejemplo JSON --
        {
            "nombre": "Edi",
            "edad": 38,
            "activo": true,
            "hobbies": {"deporte", "viajes"}
        }

        -- ejemplo BSON --
        {
            "address": {
            "street": "Pizza St",
            "zipcode": "10003"
            },
            "coord": [-73.982419, 41.579505],
            "cuisine": "Pizza",
            "name": "Mongo's Pizza"
        }

    - MongoDB utiliza este tipo de estructuras
    - Son estructuras dinámicas (crear y decrecer), indexadas (siempre accesibles por la key, no por su posición)
    y, además, podemos tener varios anidados
'''
'''
ejemplo1 = {
    "Nombre": "Fulano",
    "Edad": 38,
    "Email": "email@example.com"
}

print(ejemplo1)
print(ejemplo1["Email"])
#print(ejemplo1[2]) -- nos daría error en la llave, no existe ningún elemento 2
#print(ejemplo1["edad"]) -- se han de nombrar las keys tal y como se deberían nombrar
print("\n")

# Añadiendo elementos
ejemplo1["Dirección"] = "Mi casa, 12345"
print(ejemplo1)
print("\n")

# Imprimiendo los elementos
for d in ejemplo1:
    print(ejemplo1[d])

for x,y in ejemplo1.items():
    print(x,y)
print("\n")

# Diccionarios anidados
dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}

diccionario = {"anidado1": dic1, "anidado2": dic2}
print(diccionario)
print("\n")

# -- Métodos que podemos utilizar --
# clear: eliminamos todo el contenido del diccionario
d = {"a": 1, "b": 2}
d.clear()
print(d)
print("\n")

# getter: consultando ciertos valores
d2 = {'aa': 1, 'bb': 2}
print(d2.get('aa')) # aquí debe decirme el contenido de esta key
print(d2.get('z', "No econtrado en el diccionario"))
print("\n")

# items: lista de items
d3 = {'aaa': 1, 'bbb': 2}
it = d3.items() # convertir en lista indexada

print(it)
print(list(it))
print(list(it)[0][0])
print("\n")

# Imprimiendo con control
k = d3.keys() # imprimimos todas las llaves del diccionario
print(k)

print(list(d3.values())) # Ahora, sólo los valores del diccionario
print("\n")

# Búsqueda y eliminación
d4 = {'aaa': 1, 'bbb': 2, 'ccc': 3}
print(d4)
d4.pop('ccc')
print(d4)
print("\n")

d4.popitem() # eliminación aleatoria de un elemento del diccionario
print(d4)
print("\n")

# Actualización
d5 = {'aaa': 1, 'bbb': 2, 'ccc': 3}
d6 = {'aaa': 0, 'bbb': 20, 'ccc': 0}

d5.update(d6)
print(d5)
print("\n")
'''

'''
    Queremos almacenar 3 alumnos de la siguiente forma:
        - carga de alumno con su DNI, asignatura y nota
        - listado de alumnos con sus notas
        - Búsqueda de alumnos por DNI, mostrando asignatura y nota
    
    ¿Qué estoy viendo?
        - 1 diccionario con los alumnos
        - La clave es el DNI
        - El valor es una lista de elementos inmutable, es decir, 1 tupla
'''

# FUNCTIONS -------------------------------------
def cargarAlumnos():
    # inicialización
    alumnos = {}

    # carga de elementos
    for x in range(3):
        dni = input("\nIntroduce el DNI del alumno: ")
        # no ponemos str(...) porque ya devuelve un string

        # cargamos las asignaturas
        listaAsignaturas = [] # inicialización
        continuar = 's' # para poder controlar las asignaturas que introducimos

        # continuar.lower() -- te aseguras que es minúscula
        while continuar.lower() == 's':
            asignatura = input("Introduce asignatura: ")
            nota = float(input("Introduce la nota: "))

            listaAsignaturas.append((asignatura, nota)) # añadimos elementos a la lista

            continuar = input("¿Quieres continuar [S/N]")
        alumnos[dni] = listaAsignaturas
        # diccionario[key] = value
        # diccionario = {key: value, key: value}
        # diccionario = {dni: listaAsignaturas, dni: listaAsignaturas}

    return alumnos # retornamos todo el diccionario completo

def listarAlumnos(alumnos):
    for dni in alumnos:
        print(f"\nDNI: {dni}")
        print("- Asignaturas y nota - ")
        for asignatura, nota in alumnos[dni]:
            print(asignatura, nota)

def buscarAlumnos(alumnos):
    busqueda = input("\nIntroduce el dni a buscar: ")

    # buscamos el dni e imprimimos su "contenido"
    if busqueda in alumnos:
        for asignatura, nota in alumnos[busqueda]:
            print(asignatura, nota)

# MAIN ------------------------------------------
alumnos = cargarAlumnos() # carga de alumnos en diccionario
listarAlumnos(alumnos) # lista de alumnos (todos)
buscarAlumnos(alumnos) # buscar un alumno determinado