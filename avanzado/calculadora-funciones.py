'''
Calculadora básica utilizando funciones simples.
Dispone de:
    - repetición del menú hasta que se pulse 0
    - revisión de errores (de usuario)
    - validación de datos de entrada
'''

# FUNCTIONS ---------------------------------------------------------
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if (num2 == 0):
        return "Error, estamos dividiendo entre 0"
    
    return num1 / num2

def mostrar_menu():
    print("Selecciona la opción deseada: \n")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("0.- Salir")

def pedir_numeros():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    return num1, num2

# MAIN --------------------------------------------------------------

while True:
    # Mostrado de menú y selección de opción
    mostrar_menu()
    opcion = input("\n¿Qué opción eliges? Selecciona para continuar: ")
    
    # Validar que sea un número
    if not opcion.isdigit():
        print("Error: introduce un número válido")
        continue # vuelve a ejecutar desde el principio
    
    op = int(opcion)

    # Salir del programa
    if op == 0:
        print("¡Hasta luego!")
        break  # rompe el bucle y termina el programa

    # Validar opción
    if (op < 1) or (op > 4):
    #  if op not in [1,2,3,4] -- Utilizando una lista de opciones
        print(f"Error: {op} no es una opción válida")
        continue

    # Petición de números (solo si no va a salir)
    num1, num2 = pedir_numeros()
    
    # Ejecutar "Switch" de opciones
    if (op == 1):
        print(f"Resultado: {sumar(num1,num2)}")

    elif (op == 2): # elif significa -> sino, si (condición a evaluar)
        print(f"Resultado: {restar(num1,num2)}")

    elif (op == 3): 
        print(f"Resultado: {multiplicar(num1,num2)}")

    elif (op == 4): 
        print(f"Resultado: {dividir(num1,num2)}")