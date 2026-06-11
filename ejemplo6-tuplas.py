'''
Tupla: es algo similar a la lista perooooooo:
    - es inmutable: no se puede agregar, borrar o modificar sus elementos
    - permite almacenar una colección de datos, como las listas
    - da igual qué tenga dentro, sus elementos no tienen por qué coincidir el tipo

Colección es lo más aproximado a un array, arreglo o vector en programación.

IMPORTANTE:
    - la lista se define con []
    - la tupla se define con ()
    - el diccionario se define con {}

Para convertir una lista en tupla, lo que debemos hacer es: tuple(lista). Es similar a int(...)
'''

# Ejemplo 1: definir varias tuplas e imprimir su contenido
fecha_nacimiento = (6, 9, 1959)
persona = ("Fulano", "Fulánez", 67)

print(f"Datos: {persona}\n {fecha_nacimiento}\n")
print(f"Datos: {persona[0]}\n {fecha_nacimiento}\n")

# # Ejemplo 2: cargar la fecha de nacimiento e insertarla en una tupla
# # FUNCTIONS -------------------------------------
# def cargarFecha():
#     dd = int(input("Introduce el día: "))
#     mm = int(input("Introduce el mes: "))
#     aa = int(input("Introduce el año: "))

#     return dd, mm, aa

# def imprimirFecha(fecha):
#     print(f"Fecha nacimiento: {fecha[0]}/{fecha[1]}/{fecha[2]}")

# # MAIN ------------------------------------------
# fecha = cargarFecha()
# imprimirFecha(fecha)

# Operaciones con tuplas
tupla = (1, 2, 3)
print(tupla)
# tupla[1] = 77 -- esta operación da error porque este tipo de dato no posibilita esta acción

tupla = 1, 2, ('a', 'b'), 3 # elementos de diferentes tipos
print(tupla)
print(tupla[2][0])

# Liastas a tuplas casteando
lista = [1, 2, 3]

# Iterando elementos
tupla = (1, 2, 3)
print(type(tupla))
for t in tupla:
    print(f"Valor: {type(t)}")

tupla = (1, )
print(type(tupla))
for t in tupla:
    print(f"Valor: {type(t)}")

'''
Métodos para las listas:
    - append(x) -- añadir un elemento al final
    - extend(iterable) -- añadir varios elementos
    - insert(iterable,x) -- inserta un elemento en la posición que digamos (iterable)
    - remove(x) -- elimina la primera aparición del sistema
    - pop([iterable]) -- eliminar y devolverme un elemento
    - index(x) -- devuelve la posición de un elemento determinado
    - count(x) -- cuenta las ocurrencias del elemento
    - sort() -- ordena la lista
    - reverse() -- invierte el orden
    - del lista(iterable) -- borramos un elemento en la posición que determinemos

Métodos para las tuplas:
    - count(x) -- cuenta las ocurrencias del elemento
    - index(x) -- devuelve la posición de un elemento determinado
    - len(x) -- me da la longitud de la tupla
    - max(x) -- valor máximo
    - min(x) -- valor mínimo
    - sum(x) -- suma de valores
    - sorted(x) -- ordenación
    - reversed(x) -- inversa
'''

# Ejemplo de métodos con listas
numeros = [3, 1, 5, 1]
print(numeros)

numeros.append(9)
print(numeros)
numeros.insert(0, 11)
print(numeros)
numeros.remove(1)
print(numeros)
numeros.sort()
print(numeros)
del numeros[3]
print(numeros)

# Ejemplo de métodos para las tuplas
numeros = (3, 1, 5, 1)
print(numeros.count(1)) # muchos métodos se utilizan: variable.metodo()
print(numeros.index(3))

# Funciones típicas de Python
print(len(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros))
print(sorted(numeros))