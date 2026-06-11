'''
Creamos un programa que reciba una palabra por teclado. Debe verificar si es o no capicúa,
es decir, que se lee de derecha a izquierda o de izquierda a derecha indistintamente.
'''

# FUNCTIONS -------------------------------------
def capicua(texto):
    indice = -1 # en negativo, contamos desde el final, el último caracter
    cuentaiguales = 0

    for x in range(0, len(texto)//2):
        if texto[x] == texto[indice]:
            cuentaiguales += 1
        indice -= 1 # el índice aumenta en -1, es decir, la 2ª vuelta sería -2 y así...
    
    if cuentaiguales == (len(texto)//2):
        print(f"{texto} es una palabra capicúa")
    else:
        print(f"{texto} NO es una palabra capicúa")

# MAIN ------------------------------------------
texto = input("Introduce una palabra: ")
capicua(texto)
