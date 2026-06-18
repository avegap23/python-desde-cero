'''
CLASES EN PYTHON (y en casi todos los demás lenguajes de programacion también)

Clase:
    - es un molde o plantilla
    - define los atributos del tipo que tenga la clase
    - define los métodos (funciones) que la clase puede realizar

Ejemplo:
    Robot:
        - características: alto, bajo, grande, pequeño...
        - métodos: levantar paso, correr, andar...
    
Pasos a seguir para trabajar con Clases:
    1.- Instanciar la clase: crear un objeto de ese tipo
    2.- Definir los atributos:
        - Atributos de instancia: son los atributos particulares
        - Atributos de clase: son los atributos "genéricos" o comunes en la clase
    3.- A la hora de crear las clases, lo mejor es seguir esta estructura:
        - Imports: Importaciones de bibliotecas y módulos externos
        - Def: creación de funciones. ¡¡Cuidado!! Esto depende de:
            a.- Que utilicemos o no una determinada clase dentro de la función
            b.- Que no utilicemos la clase y hagamos después lo que queramos...
        - Class: las funciones que creamos en esta parte, siempre serán MÉTODOS
        - Main
'''
'''
# CLASS -----------------------------------------
class Persona:
    #1.- método constructor
    def __init__(self, nombre):
        # 1.1.- Atributos de instancia: atributos particulares del objeto creado
        self.nombre = nombre
    
    # 2. métodos de la clase: las acciones que puede realizar
    def imprimir(self):
        print(f"Mi nombre es {self.nombre}")

# MAIN ------------------------------------------
persona1 = Persona("Fulano") # 1.- Crear un objeto del tipo que me define la clase
persona1.imprimir()
'''
# CLASS -----------------------------------------
class Perro:

    # Atributos de clase
    especie = "mamífero"

    # método constructor
    def __init__(self, nombre, raza):
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

        print(f"Creando perro: {nombre}, {raza}")
    
    # métodos de la  clase
    def ladra(self):
        print("Reguaaauuuu!!")
    
    def camina(self, pasos):
        print(f"Caminando, llevo {pasos} pasos")

# MAIN ------------------------------------------
miPerro = Perro("Coco", "caniche")
print(type(miPerro)) # Para ver qué tipado tiene la variable creada
print("\n")

print(miPerro.nombre)
print(miPerro.raza)
print("\n")

print(miPerro.especie)
print("\n")

miPerro.ladra()
miPerro.camina(55)