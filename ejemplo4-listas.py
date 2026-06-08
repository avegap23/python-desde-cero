'''
Definir una lsita que almacene por asignación los nombres de 5 personas.
Después, contaremos qué nombres tienen 5 carácteres o más.

for i in range(variable):
    lo que tengamos que hacer...
para una variable, hasta que llegue el final:
    hacemos lo que tengamos que hacer

while j > len(nombres):
minetras que un contador no llegue a la longitud completa de la lista...
---------------------------------------------------------------------------------------------------
TRUCANDO A LOS FOR
texto = "Python"
nombres = ["Perico", "Juanito", "Marianito"]

# itera al revés (recorre la lista/cadena al revés)
for i in texto[::-1]:
    print(i)

# 1 elemento sí, 1 elemento no
for i in texto[::2]
    print(i)

# Recorrer de 2 en 2 con un range
for i in range(0, 10, 2) # inicio 0, límite 10, cada 2 números
    print(i)

# Recorrer al revés con un range
for i in range(10, 0, -1) # inicio 0, límite 10, cada 2 números
    print(i)

# Recorrer varias listas a la vez
nombres = ["Perico", "Juanito", "Marianito"]
edades = [30, 60, 90]

for nombre, edad in zip(nombres, edades):
    print(nombre, edad)

# listas con compresión
cuadrados = [x**2 for x in range(1,6)]
print(cuadrados)

# filtrado con compresión
pares = [x for x in range(100) if x % 2 == 0]
print(pares)
'''

# Definición de variables e inicialización
nombres = []
cantidad = 0
j = 0

# Petición por teclado
cantidad_nombres = int(input("¿Cuántos nombres vas a introducir en la lista?: "))
print("\n")

for i in range(cantidad_nombres):
    nombre = input(f"Introduce nombre en la posición {i+1}: ")
    nombres.append(nombre) # append añade un elemento al final de la lista

# Chequeo de número de caracteres
while j < len(nombres):
    if len(nombres[j]) >= 5: # Si la palabra de la posición actual tiene más de 5 caracteres...
        cantidad += 1
    j += 1

print("\nLISTA DE NOMBRES:")
for i, nombre in enumerate(nombres):
    print(i, nombre)
print(f"\nCantidad de palabras con más de 5 caracteres: {cantidad}")

'''
SLICES (ATAJOS MAJOS) MÁS UTILIZADOS:

lista[:] # lista completa
lista[::-1] # lista invertida (reversa)
lsita[::2] # lista de 2 en 2
lista[1::2] # lista posiciones impares
lista[1:4] # lista desde 1 hasta 3
lista[:-1] # lista completa menos la última
lista[-1] # último elemento
lista[-2:] # 2 últimos elementos
---------------------------------------------------------------------
LISTAS COMPRIMIDAS (list comprehensions):

lista = [expresión for elemento in iterable]
lista = [expresión for elemento in iterable if condición]
---------------------------------------------------------------------
RANGE SON RANGOS:

range(inicio, fin, salto)
---------------------------------------------------------------------
SLICES (ATAJOS MAJOS) BUILT-IN:

lista =  [1, 2, 3]

lista.apend(4) # añadir al final
print(lista)
lista[len(lista):] = [5]
print(lista)

lista =  [1, 2, 3]

lista.extend([4, 5, 6]) # extender al final
print(lista)
lista[len(lista):] = [7, 8, 9]
print(lista)

lista = [1, 2, 5]

lista[:0] = [0] # insertar al principio "del todo"
print(lista)

lista = [1, 2, 5]

print(lista)
lista[2:2] = [3,4] # insertar en una posición determinada
print(lista)

lista = [1, 2, 3, 4, 5]

del lista[1:3] # borrar elementos
print(lista)

lista [1:4] = [25,38] # sustituyendo parte de la lista
print(lista)
'''

lista = []
x = y = z = 0

# operación con las listas
lista.append(x) # añadimos un elemento
lista.extend(y, z) # añadimos más de un elemento al final
lista.insert(i, x) # insertar en una posición específica (i = posición, x = valor)
lista.pop() # sacar el último
lista.remove(x) # borrar un valor determinado
lista.clear() # vaciando la lista o array

'''
Las LISTAS son:
    - ordenadas según el orden definido al principio
    - pueden ser formadas por cualqueir tipo de variable
    - pueden ser indexadas (con [i])
    - pueden estar anidadas (matrices), es decir, una dentro de otra
    - son mutables, es decir, sus elementos pueden modificarse
    - son dinámicas, se pueden añadir/qutiar elementos
'''

ejemplito = [49, "Fulanito Fulánez del Fulano", 1.78]
print(ejemplito[0])
print(ejemplito[1])
print(ejemplito[2])
print(ejemplito[3]) # daría error, está fuera del rango

print(ejemplito[-1]) # acceso al último elemento
print(ejemplito[-2]) # acceso al penúltimo elemento

ejemplito[0] = 38 # cambio el contenido de la posición que quiero

# listas complejas: anidando...
x = [1, 2, 3, 4, ['p', 'q', [5, 6, 7]]]
print(x[4][0]) # para imprimir la 'p'
print(x[4][2][0]) # para imprimir el 5

# sustitución de elementos
l = [1, 2, 3, 4, 5, 6]
l[0:3] = [0, 0, 0]
print(l)
l += [7, 8] # añado al final la nueva lista

# Iterando las listas
lista = [5, 9, 11]
# la forma má normal
for l in lista:
    print(l)

# acompañada de índice
for index, l in enumerate(lista):
    print(index,l)

lista1 = [5, 9, 11]
lista2 = ["Pop", "Indie", "Rock"]

# iteración concurrente
for l1,l2 in zip(lista1,lista2):
    print(l1,l2)

# iteración con índice
for i in range(0, len(lista1)):
    print(lista1[i])

'''
BUILT-IN MÁS COMPLEJAS

l.reverse() # ordenación al revés
l.sort() # ordenación de menor a mayor
l.sort(reverse=True) # ordenación de mayor a menor
'''