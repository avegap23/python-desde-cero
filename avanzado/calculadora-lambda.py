'''
Calculadora básica utilizando funciones lambda en Python.
Dispone de:
    - Menú de opciones con símbolo (diccionario)
    - Contemplamos el 0 com salida del bucle
    - El menú se repetirá mientras no pulsemos el 0
'''

# DEFINITIONS -----------------------------------
operaciones = {
    "+": lambda num1, num2: num1 + num2,
    "-": lambda num1, num2: num1 - num2,
    "*": lambda num1, num2: num1 * num2,
    "/": lambda num1, num2: num1 / num2 if num2 != 0 else "Error, no puedes dividir entre 0"
}

# MAIN ------------------------------------------
while True:
    operador = input("Introduce el operador (+, -, *, /) o 0 para salir: ")

    if operador == '0':
        print("\nBye!")
        break

    if operador not in operaciones:
        print("\n¡¡Operación no válida!!")
        continue

    num1 = float(input("\nIntroduce el primer número: "))
    num2 = float(input("Introudce el segundo número: "))

    resultado = operaciones[operador](num1, num2)
    print(f"Resultado: {resultado}\n")