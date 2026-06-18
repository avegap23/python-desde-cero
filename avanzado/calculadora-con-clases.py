'''
Creación de una calculadora con clases

EXPLICACIÓN DE NUEVAS ESTRUCTURAS Y APAÑOS:
    def division(self, a, b):
        if b == 0:
            print("Error")
        return a / b
    
    Aquí tenemso un problema porque, como es evidente, si se imprime el error, el programa
    continuará la ejecución, realizando la división y dando como resultado ZeroDivisionError.
    Evitamos el problema con RAISE:

    def division(self, a, b):
        if b == 0:
            raise ValueError("No podemos dividir entre 0")
        return a / b
    
    Con raise detenemos el método que se está ejecutando para dar el error

'''

# CLASS -----------------------------------------
class Calculadora:
    # métodos de clase
    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b == 0:
            raise ValueError("No podemos dividir entre 0")
        return a / b
    
    def potencia(self, a, b):
        return a ** b

    def raizCuadrada(self, a):
        if a < 0:
            raise ValueError("No puedo calcular raíces de negativos")
        return a ** 0.5 # raíz cuadrada = potencia de 1/2

class AppCalculadora:
    # método constructor
    def __init__(self):
        self.calculadora = Calculadora() # con esto cargamos todos los métodos de arriba

    # métodos de clase
    def mostrar_menu(self):
        print("\n --- CalCuLADoRa ---")
        print("[1] Sumar")
        print("[2] Restar")
        print("[3] Multiplicar")
        print("[4] Dividir")
        print("[5] Potencia")
        print("[6] Raíz cuadrada")
        print("[0] Salir")
    
    def pedir_numeros(self, mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Introduce un número válido...")
    
    # método que llamará a todos los demás
    def ejecutar(self):
        while True:
            # a.- mostramos menu y pedimos la opción que queramos
            self.mostrar_menu() # llamamos al método mostrar_menu()
            opcion = input("Elige una opción: ")

            # b.- ahora nos toca hacer la operación que hemos elegido
            try:
                if opcion == '1':
                    print("\n")
                    a = self.pedir_numeros("Introduce primer sumando: ")
                    b = self.pedir_numeros("Introduce segundo sumando: ")
                    print(f"Resultado de la suma = {self.calculadora.suma(a, b)}")

                elif opcion == '2':
                    print("\n")
                    a = self.pedir_numeros("Introduce minuendo: ")
                    b = self.pedir_numeros("Introduce sustraendo: ")
                    print(f"Resultado de la resta = {self.calculadora.resta(a, b)}")

                elif opcion == '3':
                    print("\n")
                    a = self.pedir_numeros("Introduce primer factor: ")
                    b = self.pedir_numeros("Introduce segundo factor: ")
                    print(f"Resultado de la multiplicación = {self.calculadora.multiplicacion(a, b)}")

                elif opcion == '4':
                    print("\n")
                    a = self.pedir_numeros("Introduce dividendo: ")
                    b = self.pedir_numeros("Introduce divisor: ")
                    print(f"Resultado de la división = {self.calculadora.division(a, b)}")
                
                elif opcion == '5':
                    print("\n")
                    a = self.pedir_numeros("Introduce base: ")
                    b = self.pedir_numeros("Introduce exponente: ")
                    print(f"Resultado de la potencia = {self.calculadora.potencia(a, b)}")
                
                elif opcion == '6':
                    print("\n")
                    a = self.pedir_numeros("Introduce base: ")
                    print(f"Resultado de la raíz cuadrada = {self.calculadora.raizCuadrada(a)}")

                elif opcion == '0':
                    print("Saliendo del programa...")
                    break

                else:
                    print("\n")
                    print("Opción no válida...")
                
            except ValueError as error: # no me complico con ValueError, creo un alias
                print(f"Error encontrado: {error}")


# MAIN ------------------------------------------
if __name__ == "__main__":
    # instanciar un objeto de tipo calculadora
    app = AppCalculadora()
    
    # comenzamos a trabajar
    app.ejecutar()