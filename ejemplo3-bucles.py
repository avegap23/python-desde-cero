'''
Un bucle es algo que se repite y que termina según la condición que pongamos.

PSEUDOCÓDIGO:

MIENTRAS QUE SE PRODUZCA LA CONDICIÓN QUE TE DIGO, HAZME:
    EJECUCIÓN DE CÓDIGO...

Otras notas que nos interesan:
    - Imprimir una llave:
        print(f"{{ {contador} }}")
'''

contador = 0 # se inicializa en el momento de su creación

while True:
    opcion = input("Pulsa 's' para parar el programa: ")

    # evaluación de la posible condición de salida
    if (opcion == 's') or (opcion == 'S'):
        break # ¡¡Cuidadín con esto!! Es un corte de bucle o trabajo

    else:
        contador += 1 # contador = contador + 1

        print(f"Te estoy contando las veces que pulsas Enter. Llevas {contador} veces")
    #   print("Te estoy contando las veces que pulsas Enter. Llevas " + str(contador) + " veces")
    #   print("Te estoy contando las veces que pulsas Enter. Llevas ",contador," veces")