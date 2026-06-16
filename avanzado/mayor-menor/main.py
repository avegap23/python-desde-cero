# archivo main.py: lógica de negocio

from mayor_menor import mayor # modularidad: cargamos un módulo externo

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print(f"El número más grande es {mayor(num1, num2)}")