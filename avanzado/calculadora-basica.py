'''
Creación de uan calculadora con las operaciones más básicas.
Qué vamos a ver:
    - Condicionales
    - Bucles (while)
    - Control de errores (try - except)
    - Utilización de funcionalidades built-in
    - Toma de datos por teclado

Pequeño diccionario de uso:
    - \n --> es un retorno de carro, es decir, salto de línea
    - nombre_variable.lower() --> pone el texto que tenga dentro la variable
    en minúsculas. Es una función built-in.
    - ValueError --> es un error en la carga del valor, utilizado para evitar
    que los valores que se impriman o envíen no tengan problemas de carga o similares.
'''

while True:
    # Menú principal (por llamarlo de algún modo)
    print('\n# ~ # ~ # ~ # CALCULADORA MUY BÁSICA # ~ # ~ # ~ #')
    print("Pulsa 's' para salir de la aplicación.\n")

    print("Elige la operación a realizar:\n")
    print("· Pulsa '+' para la suma")
    print("· Pulsa '-' para la resta")
    print("· Pulsa '*' para la multiplicación")
    print("· Pulsa '/' para la división\n")
    operacion = input("¿Qué eliges? Dime: ")

    # Realización de la operación elegida

    # 
    if operacion.lower() == 's':
        print('\nSaliendo del programa...')
        break # corte en la ejecución, para el bucle

    if operacion not in ['+', '-', '*', '/']:
        print("\nOperación no válida... ¡¡Listillo!!")
        continue # vuelve al principio del programa, no para la ejecución

    # Intentamos las cosas hasta que nos "hagamos daño"
    try:
        num1 = float(input("\nIntroduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        # Revisión de la operación y realización de la misma
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                print("\nError, no puedes dividir entre 0")
                continue
            else:
                resultado = num1 / num2

        print(f"\nResultado: {resultado}")

    except ValueError:
        print("\nError, introduce un valor válido")