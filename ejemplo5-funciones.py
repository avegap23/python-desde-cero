'''
Funciones: son bloques de código reutilizables que realizan una tarea determinada.
Sirve para:
    - no repetir el código, evitando problemas de duplicidad
    - organizo de forma eficiente todo el código, ahorrando líneas
    - el mantenimiento es más fácil de llevar así
    - a la hora de blindar la seguridad, se hace más fácil

¿Cómo lo codifico?

def nombre_función(parámetros/argumentos):
    lo que queramos que haga...
    (return) retornar el resultado

llamamos a nombre_función() para ejecutarla
    
'''
# Función sencilla
def saludar():
    print("Hola, mundo!!")

saludar()

# Función con argumentos de entrada (algo con lo que tiene que trabajar)
def saludame(nombre):
    print(f"Hola, {nombre}")

saludame("Diego")

# Función con argumentos por posición
def suma(num1,num2):
    #suma = num1 + num2 - suma tiene scope local, al igual que num1 y num2
    #return suma
    return num1 + num2 # forma eficiento, no hay que crear ná de ná

# ------------------------------------
print(f"El resultado es: {suma(6,7)}")

# Función con argumentos por nombre
print(f"El resultado es: {suma(num1=20,num2=20)}")
# print(f"El resultado es: {suma(a=10,b=10)}") --> da error, no conoce a o b

# Función con argumentos por defecto
def multiplicar(a,b,c=1):
    return a*b*c # si se da el argumento, lo utiliza, sino es un 0 por defecto

print(f"Resultado: {multiplicar(5,5,5)}")
print(f"Resultado: {multiplicar(4,4)}")
# print(f"Resultado: {multiplicar(10)}") --> faltan argumentos

# Función con argumentos de longitud variable
def sumatorio(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
# ----------------------
print(f"Resultado: {sumatorio([1,2,34,4,5,6,7,87,8,34,5,534,543,54,534,534,5])}")
print(f"Resultado: {sumatorio([1,2,34,4,5,6,7,87,8])}")

# Función con argumentos de longitud variable (tupla)
def sumatorio(numeros): # * empaqueta la lista en una tupla
    total = 0
    for n in numeros:
        total += n
    return total
# ----------------------
print(f"Resultado: {sumatorio([1,2,34,4,5,6,7,87,8,34,5,534,543,54,534,534,5])}")
print(f"Resultado: {sumatorio([1,2,34,4,5,6,7,87,8])}")

# Vamos con lo mismo de antes, pero aún más complicado...
def sumar_toito(*args): # me dice que *args es cantidad variable de argumentos
    return sum(args)
print(sumar_toito(1,2,3,4))


def sumatorio(**kwargs): # kwargs: keyword arguments, argumentos con nombre
    suma = 0
    for key, value in kwargs.items():
        print(key,value) # lista en forma clave y valor
        suma += value
    return suma

print(f"Resultado sumatorio: {sumatorio(a=5, b=22, c=38)}")
# dentro de la función sería {'a':5, 'b':22, 'c':38}

diccionario = {'a':25, 'b':50, 'c':100}
print(f"Resultado sumatorio: {sumatorio(**diccionario)}")

# Función... un problema si no la documentamos -> DOCSTRING
def mi_funcion(a,b):
    """
    Esta función es un rollo, pero como hay que rellenarlo con algo, pues
    aquí te dejo ese algo...
    """
    return a + b

help(mi_funcion)

# Funciones con anotación de tipos: type hints
def resta(a:int, b:int) -> int:
    return a - b
# a es entero, b es entero y me devuelves un entero (-> int)
def mostrar_nombre(nombre:str, edad:int) -> str:
    return f"{nombre} tiene {edad} añitos..."

def saludito(nombre: str = "amiguito") -> str:
    return f"Hola, {nombre}"

print(mostrar_nombre("Diego",49))
print(saludito())
print(saludito("Perico el de los palotes"))

# con listas de un tipo determinado
def promedio(numeros: list[float]) -> float:
    # list[float] dice que la lista es de tipo float
    return sum(numeros) / len(numeros)

print(promedio([1,55,55,8,7,8,89,894,10]))

''' 
A partir de la versión 3.10 de Python... muchas veces los parámetros 
suelen ser un valor perooooooooooooooooooo, también pueden ser el tipo
de dato más puñetero del mundo: None
'''
def buscar_user(id:int) -> str | None:
    pass # se pone para que complete la estructura, no vale "pa ná"

# Función lambda: el existe que no existe
'''
Lambda es un tipo de función que tiene:
    - forma corta
    - sin nombre
    - utilizando 1 única línea

lambda argumentos: expresión

se revisan los argumentos y se evalúa automáticamente la expresión
'''
def cuadrado(x): # la forma más natural...
    return x ** 2

cuadrado = lambda x:x ** 2
suma = lambda a,b: a + b

print(cuadrado(7))
print(suma(6,7))