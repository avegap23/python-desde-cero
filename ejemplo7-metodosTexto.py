texto = "hola, Mundo Mundial"

# Modifica el texto en caso de asignación, en el resto de los casos, sólo es visual
print(texto.upper()) # texto en mayúsculas
print(texto.lower()) # texto en minúsculas
print(texto.capitalize()) # 1º letra en mayúsculas
print(texto.title()) # texto en modo título
print(texto.swapcase()) # transformación del texto mayúsculas-minúsculas y viceversa
print("\n")

# Búsqueda de texto
print(texto.find("Mundo"))
print(texto.find("mundo")) # devuelve -1 si no encuentra el texto
print(texto.count("u"))
print("\n")

# Reemplazar textos
print(texto.replace("Mundo", "Python"))
print(texto)
print("\n")

# Dividiendo y uniendo cadenas
print(texto.split(","))

texto2 = ["Python", "SQL", "HTML/CSS"]
print(",".join(texto2))
# print(texto2.join(",")) -- no es un método para trabajar con las listas
print("\n")

texto3 = "                  six     seven                                                  "

print(texto3.strip()) # eliminación de espacios
print(texto3.lstrip()) # por la izquierda
print(texto3.rstrip()) # por la derecha
print("\n")

# Comprobando el contenido, cómo empezamos y terminamos
texto4 = "SuperPython1234"
print(texto4.isalpha()) # Falso porque hay números
print("#@!".isalpha()) # Falso porque son caracteres especiales
char = "@"
print("Aquí", not char.isalnum()) # No es un número ni una letra
print("Aquí - ","#@!".isascii())
print("Python bonito".isalpha())
print(texto4.isdigit()) # Falso porque hay letras
print("465454113".isdigit())
print(texto4.isalnum()) # Verdadero
print(texto4.islower()) # Falso, deberían ser todas minúsculas
print(texto4.isupper()) # Falso, deberían ser toas mayúsculas
print("\n")

texto5 = "programacionPython.py"
print(texto5.startswith("ro")) # Falso, no comienza con estas letras
print(texto5.startswith("pro")) # Verdadero
print(texto5.endswith(".py"))
print(len(texto5))
print(texto5[::-1])