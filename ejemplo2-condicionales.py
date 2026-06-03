'''
EJERCICIO DE CALCULADORA: Tenemos que crear una calculadora en Python con las funcionalidades más básicas (suma, resta, multiplicación y división).
A utilizar:
    · Condicionales
    · Pedir los datos por teclado
    · Imprimir en pantalla
    · Se ha de utilizar el casting para evitar errores

CONDICIONALES -----------------------------------

 === Condicional "simplón" ===

SI (CONDICIÓN A EVALUAR) ENTONCES:
    SI ES VERDAD HAGO X COSA
    SI NO ES VERDAD, ¿PA QUÉ HAGO NÁ?

 === Condicional múltiple o anidado ===

SI TENGO QUE SUMAR ENTONCES:
    HAGO LA SUMA

SINO, SI TENGO QUE RESTAR ENTONCES:
    HAGO LA RESTA

Y asín sucesivamente hasta el final

SI NO PASA NADA DE LO ANTERIOR ENTONCES:


'''

print(" === SUPERCALCULADORA BÁSICA === ")

# Petición de datos por teclado: ¡¡Hacemos casting!!
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Opciones disponibles
print("\nOPCIONES DE LA CALCULADORA:") # \n es un salto de renglón
print("[1] Suma (+)")
print("[2] Resta (-)")
print("[3] Multiplicación (*)")
print("[4] División (/)")

opcion = str(input("\nElige una opción (1-4 o símbolo): "))
while (opcion not in ['+', '1', '-', '2', '*', '3', '/', '4']): # el bucle se ejecuta mientras la tecla introducida no esté en la lista
    opcion = str(input("\nNo has introducido una opción. Prueba otra vez (1-4 o símbolo): "))

# Bloque de operaciones: '==' significa que compara el contenido de la variable con un valor
if (opcion == '+' or opcion == '1'):
    resultado = numero1 + numero2
    print(resultado)
elif (opcion == '-' or opcion == '2'): # 'elif' es "sino..."
    resultado = numero1 - numero2
    print(resultado)
elif (opcion == '*' or opcion == '3'):
    resultado = numero1 * numero2
    print(resultado)
elif (opcion == '/' or opcion == '4'):
    if (numero2 != 0): # '!=' significa "distinto de"
        resultado = numero1 / numero2
        print(resultado)
    else:
        print("Error, estás dividiendo entre 0 y eso no se puede hacer")