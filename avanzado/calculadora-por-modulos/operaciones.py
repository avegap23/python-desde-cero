# IMPORTS -----------------------------------------------------------
import os # https://docs.python.org/3/library/os.html
import platform # https://docs.python.org/3/library/platform.html
import subprocess # https://docs.python.org/3/library/subprocess.html

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

'''
# Versiones anteriores a Python 3.12
def limpiar_pantalla():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # Linux/MacOS
    else:
        os.system("clear")
'''

def OLD_limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Para evitar el deprecated:

def limpiar_pantalla():
    comando = "cls" if platform.system() == "Windows" else "clear"
    subprocess.run(comando, shell=True)