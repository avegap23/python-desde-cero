'''
Definir una lsita que almacene por asignación los nombres de 5 personas.
Después, contaremos qué nombres tienen 5 carácteres o más.

for i in range(variable):
    lo que tengamos que hacer...
para una variable, hasta que llegue el final:
    hacemos lo que tengamos que hacer

while j > len(nombres):
minetras que un contador no llegue a la longitud completa de la lista...
'''

# Definición de variables e inicialización
nombres = []
cantidad = 0
j = 0

# Petición por teclado
cantidad_nombres = int(input("¿Cuántos nombres vas a introducir en la lista?: "))

for i in range(cantidad_nombres):
    nombre = input(f"Introduce nombre en la posición {i+1}: ")
    nombres.append(nombre) # append añade un elemento al final de la lista

# Chequeo de número de caracteres
while j < len(nombres):
    if len(nombres[j]) >= 5: # Si la palabra de la posición actual tiene más de 5 caracteres...
        cantidad += 1
    j += 1

print(f"Lista de nobmres:\n{nombres}")
print(f"Cantidad de palabras con más de 5 caracteres: {cantidad}")
