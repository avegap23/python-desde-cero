# archivo main.py de calculadora con funciones (lógica)

# IMPORTS -----------------------------------------------------------
import operaciones

# MAIN --------------------------------------------------------------

while True:
    # Mostrado de menú y selección de opción
    operaciones.mostrar_menu()
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
    num1, num2 = operaciones.pedir_numeros()
    
    # Ejecutar "Switch" de opciones
    if (op == 1):
        print(f"\nResultado: {operaciones.sumar(num1,num2)}")

    elif (op == 2): # elif significa -> sino, si (condición a evaluar)
        print(f"\nResultado: {operaciones.restar(num1,num2)}")

    elif (op == 3): 
        print(f"\nResultado: {operaciones.multiplicar(num1,num2)}")

    elif (op == 4): 
        print(f"\nResultado: {operaciones.dividir(num1,num2)}")
    
    input("Pulsa cualquier tecla para continuar para continuar: ")
    operaciones.limpiar_pantalla()