# Comentario en una única línea

'''
Es un comentario multilínea, muy utilizado en documentación, claro está...
'''

# -----------------------------------------------

'''
Sí... ¿Pero qué es Python?
    - Lenguaje interpretado, no compilado.. ¡No necesita ejecutable!
    - Se programa en scripting
    - Tiene un tipado dinámico, es decir, cuando "me da la gana", cambio de tipo de dato
    - No se cambia de tipo "así por así", es decir, de forma repentina
    - Es un lenguaje multiplataforma: Linux, Windows, MacOS y otros lo pueden ejecutar con o sin "ayudas"

Empecemos con nomenclaturas "raras":

    -> VARIABLE:
        · Es un cajón que contiene información que quiero que contenga
        · A lo largo de la vida del programa, puede cambiar (y cambia)
    
    -> CONSTANTE:
        · Es un cajón cuyo contenido "no debería" variar en el ciclo de la vida del programa
        · En Python se escribe: PI = 3.14159

Ahora vamos con los tipos de datos:
    -> DATOS SIMPLES (Primitivos)
        · Números enteros (int):
            - Números "normales": 1, 2, 159941
            - Números en binario: 010010
            - Números en hexadecimal: #000
        · Números decimales (float): flotante o de coma flotante: 0.1 5.87 6.87897987 .02
        · Booleanos (bool / boolean):
            - True: verdadero, se cumple
            - False: falso, no se cumple
        · Cadenas de caracteres (string): cualquier texto, siempre entre comillas ' o "
            - 'a'               - "359586515981"
            - 'Hola, olita!!'   - "Si o no"
            - "a"               - "25.58"

    -> DATOS COMPUESTOS (Avanzados / complejos)
        · Listas colección de datos ordenada y mutable:
            - Mutable: me permite añadir o qutiar elementos sin problema.
            - Ejemplo números = [1,22,5.5,"opcion",True]

        · Tuplas: colección de datos ordenada e inmutable
            - Inmutable: los elementos mantienen una posición fija y, además, una vez se crea la tupla, no se podrá modificar porque nos dará un error
            - Se utilizan los ( )
            - Ejemplo: coordenadas = (40.4168, -3.7038)
        
        · Conjuntos (set): colección NO ordenada de elementos únicos
            - Se utilizan las { }
            - Ejemplo: colores = {"rojo","verde","azul","rojo"}     Al imprimirla, NO imprime rojo 2 veces
        
        · Diccionarios: almacenan todos los datos por pares clave-valor
            - Se utilizan las { }, pero a la hora de trabajar con lso datos que están dentro, los separamos de la siguiente manera:     clave: valor, ... ClaveN: ValorN
            - Lo utilizamos en (casi) todos los lenguajes de programación:
                · JSON:
                  {"rojo":"#f00","verde":"#0f0","azul":"#00f","cyan":"#0ff","magenta":"#f0f",
                  "amarillo":"#ff0","negro":"#000"}
                
                · XML:
                  <catalog>
                    <book id="1">
                        <author>Gambardella, Matthew</author>
                        <title>XML Developer's Guide</title>
                        <genre>Computer</genre>
                        <price>44.95</price>
                        <publish_date>2000-10-01</publish_date>
                        <description>An in-depth look at creating applications with XML.</description>
                    </book>
                  </catalog>
            
            - Ejemplo:
              persona = {
                "nombre":"Álvaro",
                "edad": 23,
                "ciudad":"Toledo"
              }
    
    -> DATOS COMPUESTOS COMPLEJOS
        · Lista de diccionarios: se utiliza de forma común para los registros.
            - Ejemplo:
              alumnos = [
                    {"nombre":"Juan","nota":8.5},
                    {"nombre":"Ramón","nota":9.5},
                    {"nombre":"Lucía","nota":7.5}
              ]
        
        · Diccionario de listas:
            - Ejemplo:
              curso = {
                    "nombres": ["Juan", "Ramón", "Lucía"],
                    "notas": [8.5, 9.5, 7.5]
              }
        
        · Diccionario anidado:
            - Ejemplo:
              empresa = {
                    "empleado_1":{
                        "nombre":"Perico",
                        "edad":38,
                        "dpto":"comercial"
                    },
                    "empleado_2":{
                        "nombre":"Mariana",
                        "edad":30,
                        "dpto":"CTO"
                    }
              }

        · Lista multidimensional: conocidas como matrices
            - Ejemplo:
              matriz = [
                    [1,33,58],
                    [1,23,59],
                    [1,3,5]
              ]
'''
# ----------------------------------------------- #
'''
PALABRAS RESERVADAS: ¡¡OJO AL "TACO"!!
A la hora de nombrar las variables, no podemos utilizar alguanas palabras:

False   await   else    import  pass    None    break
True    except  in      raise   class   is      finally
return  and     for     lambda  def     as      continue
from    while   assert  del     global  if      nonlocal
elif    async   not     with    or      yield

En ocasiones, las variables pueden tener 2 espacios de trabajo (scope - alcance o ámbito):
    - Local: scope local, sólo se conoce en una parte del código
    - Global: scope global, la variable es conocida en todo el programa
'''

# Ejemplo basiquito total:
nombre = 'Álvaro'

print(nombre) # imprimir el contenido de una variable
print(type(nombre)) # imprimir el tipo de contenido que puede tener esta variable (ahora mismo)

# Comenzamos el Juego: llamando las cosas por su nombre
# 1. Nombrando a las varialbes de una forma correcta: asignación
_variable = 1
var_iable = 1
variable1 = 1
varIable = 1

snake_case = "frasecita"
nombre_apellidos = "Fulanito Benganito"

camelCase = "otra frasecita"
nombreApellidos= "Fulanito Benganito"

# 2. Lo que NUNCA tenemos que hacer, ya que nos produce un GRAN ERROR
# """2variable = 2
# var-iable = 2
# var iable = 2
# 2variable = 2
# variable"" = 2
# "variable" = 2
# 'variable' = 2

# 3. Asignación de valores: nombre de la variable = valor que contiene
nombre = "Álvaro"
edad = 23
casado = False
altura = 1.72

a = 10
b = 20
c = 30
a, b, c = 10, 20, 30

# En Python, el límite visual son 79 caracteres
suma = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 +\
14 + 15 + 16 + 17 + 18 + 19 + 20

# 4. Inicializaicón
num1 = 0
num2 = 0
nombre = "" # no se pone espacio ya que el espacio es un dato ya como tal

# 5. Una de cosas raras en programación: los poltergeist
z = h = j = d = 0 # inicialización múltiple
y = ((((z*3) + (h/7) / j) + (8 + 9)) + d) # uso de los paréntesis