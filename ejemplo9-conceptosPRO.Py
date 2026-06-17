'''
IMPORTACIÓN DE BIBLIOTECAS DE PYTHON:
    math: biblioteca de matemáticas completa
    factorial: es uno de los "módulos" que podemos cargar por independiente

RECURSIVIDAD:
    1.- se contempla un caso base: cuando se deja de llamar a la función
    2.- se realiza la llamada recursiva, siempre después del caso base
    SIN CASO BASE, ¡¡SURPRISE!! TENEMOS UN BUCLE INFINITO
'''

# Ejemplo factorial: importación de bibliotecas estándar
from math import factorial

valor = int(input("Introduce el valor para factorial: "))
print(f"Factorial: {factorial(valor)}")

# ejemplo recursividad: números del 5 al 1

# sin cafeína
for i in range(5, 0, -1):
    print(i)
print("\n")

# con cafeína: recursividad
def cuenta_patras(numero):
    if numero == 0:
        return
    
    print(numero)
    cuenta_patras(numero - 1)

print(cuenta_patras(10))

# ejemplo del factorial con cafeína: recursividad
def factorial_l(num):
    if num == 1:
        return 1
    
    return num * factorial_l(num - 1) # cada llamada, es un número menos...

print(factorial_l(10))