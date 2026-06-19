'''
Programando GUIs: Graphic User Interface
Disponemos de muhcas bibliotecas para programar GUI:
    - wxPython: https://wxpython.org/index.html
        - está un poco anticuado, lo que puede llevar a problemas de compatibilidad
        - más antiguo, menos protegido (más CVE, vulnerabilidades comunes expuestas)
        - muchas funcionalidades
    -  PyQt:
        https://wiki.python.org/main/PyQt
        https://riverbankcomputing.com/
        https://pythonpyqt.com/
        - está genial, pero cuando pides más componentes... ¡¡tachán, factura!!
        - es compatible con C/C++...
    - DearPyGui:
        - es una biblioteca que luego podemos encontrar en varios tipos de framework
        - mucho framework, pero poco programar en formato original de la biblioteca
        - tienes demasiados "sublenguajes" derivados
    
    - ** Tkinter **:
    https://docs.python.org/3.14/library/tkinter.html
        - es totalmente free
        - se van añadiendo más y más componentes con sublibrerías diferenciadas
        - puedo programar versiones antiguas y nuevas de código

Tkinter - tk interface
'''

'''
** Versión simple de Tkinter **
# IMPORTS ---------------------------------------
import tkinter as tk # creamos un alias para poder programar mejor

# MAIN ------------------------------------------

ventana_principal = tk.Tk() # creamos un objeto de tipo tkinter
ventana_principal.title("Ventanuco") # creamos un título para la ventana
ventana_principal.mainloop() # mostramos la nueva ventana

-------------------------------------------------------------------------------

** Versión P.O.O. de Tkinter **
# IMPORTS ---------------------------------------
import tkinter as tk # creamos un alias para poder programar mejor

# CLASS -----------------------------------------
class Aplicacion:
    # método construcotr
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("EEEoooooooo")
        self.ventana.mainloop()

# MAIN ------------------------------------------

app = Aplicacion()
'''

'''
# IMPORTS ---------------------------------------
import tkinter as tk # creamos un alias para poder programar mejor
import sys # https://docs.python.org/3/library/sys.html

# CLASS -----------------------------------------
class Aplicacion:
    # método construcotr
    def __init__(self):
        self.valor = 1 # definir valores iniciales
        self.ventana = tk.Tk() # creamos un objeto de clase Tk
        self.ventana.title("Controles")

        # label: construcción de etiquetas tk.Label(donde, el qué)
        self.label1 = tk.Label(self.ventana, text=self.valor)
        self.label1.grid(column=0, row=0) # colocación en rejilla
        self.label1.configure(foreground="red") # método configure

        # button: construcción de botones tk.Button(donde, el qué, qué hacer)
        self.boton1 = tk.Button(self.ventana, text="Incrementa", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2 = tk.Button(self.ventana, text="Decrementa", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.botonFin = tk.Button(self.ventana, text="Finalizar", command=self.finalizar)
        self.botonFin.grid(column=0, row=3)

        # algunos "condicionales" de la ventana
        self.ventana.resizable(False, True) # .resizable(height, width)

        # ejecución de la ventana. Estando en el constructor, se ejecuta nada más se declare el objeto
        self.ventana.mainloop()        

    # métodos de la clase
    def incrementar(self):
        self.valor += 1
        self.label1.config(text=self.valor) # configuro de nuevo la etiqueta con el nuevo valor

    def decrementar(self):
        self.valor -= 1
        self.label1.config(text=self.valor) # configuro de nuevo la etiqueta con el nuevo valor

    def finalizar(self):
        sys.exit(0) # Salida correcta. Si fuese 1, no es una salida correcta

# MAIN ------------------------------------------

app = Aplicacion()
'''

'''
# IMPORTS ---------------------------------------
import tkinter as tk # creamos un alias para poder programar mejor
import sys # https://docs.python.org/3/library/sys.html

# CLASS -----------------------------------------
class Aplicacion:
    # método construcotr
    def __init__(self):
        self.ventana = tk.Tk() # creamos un objeto de clase Tk
        self.ventana.title("Inputs de toda la vida")

        # label: construcción de etiquetas tk.Label(donde, el qué)
        self.label1 = tk.Label(self.ventana, text="Introduce tu valor")
        self.label1.grid(column=0, row=0) # colocación en rejilla

        # input como tal: toma de dato y "cajita" donde insertarlo
        self.dato = tk.StringVar() # vínculo programa-widget
        self.entrada = tk.Entry(self.ventana, width=10, textvariable=self.dato)
        self.entrada.grid(column=0, row=1)

        # label: construcción de etiquetas tk.Label(donde, el qué)
        self.salida = tk.Label(self.ventana, text="Resultado: ")
        self.salida.grid(column=0, row=2)

        # button: construcción de botones tk.Button(donde, el qué, qué hacer)
        self.boton1 = tk.Button(self.ventana, text="Calcular 2", command=self.cuadrado)
        self.boton1.grid(column=0, row=3)

        # button: construcción de botones tk.Button(donde, el qué, qué hacer)
        self.botonFin = tk.Button(self.ventana, text="Finalizar", command=self.finalizar)
        self.botonFin.grid(column=0, row=4)

        # ejecución de la ventana. Estando en el constructor, se ejecuta nada más se declare el objeto
        self.ventana.mainloop()        

    # métodos de la clase
    def cuadrado(self):
        valor = int(self.dato.get()) # guardamos el dato introducido
        res_cuadrado = valor * valor
        self.salida.configure(text=f"Resultado: {res_cuadrado}")

    def finalizar(self):
        print("Saliendo del programa...")
        sys.exit(0) # Salida correcta. Si fuese 1, no es una salida correcta

# MAIN ------------------------------------------

app = Aplicacion()
'''

# IMPORTS ---------------------------------------
import tkinter as tk # https://docs.python.org/3.14/library/tkinter.html
from tkinter import messagebox # cuadros de diálogo

# CLASS -----------------------------------------
class Formulario:
    # método constructor
    def __init__(self):
        # 1.- construcción de la ventana
        self.ventana = tk.Tk()
        self.ventana.title("Formulario")
        self.ventana.geometry("350x250") # dimensiones de la ventana (por defecto)

        # 2.- definición de variable para recepción de datos
        self.nombre = tk.StringVar()
        self.apellidos = tk.StringVar()
        self.edad = tk.StringVar()
        self.email = tk.StringVar()
        self.telefono = tk.StringVar()

        # 3.- llamada al método de creación visual del formulario
        self.componentes()

        # ejecución de la ventana
        self.ventana.mainloop()
    
    # método de clase: ceración visual de componentes
    def componentes(self):
        # CAMPOS ---
        # nombre
        tk.Label(self.ventana, text="Nombre:").grid(row=0, column=0, padx=10) # etiqueta
        # padx y pady nos permite añadir separación
        tk.Entry(self.ventana, textvariable=self.nombre).grid(row=0, column=1, pady=2) # input
        # apellidos
        tk.Label(self.ventana, text="Apellidos:").grid(row=1, column=0, padx=10)
        tk.Entry(self.ventana, textvariable=self.apellidos).grid(row=1, column=1, pady=2)
        # edad
        tk.Label(self.ventana, text="Edad:").grid(row=2, column=0, padx=10)
        tk.Entry(self.ventana, textvariable=self.edad).grid(row=2, column=1, pady=2)
        # email
        tk.Label(self.ventana, text="Email:").grid(row=3, column=0, padx=10)
        tk.Entry(self.ventana, textvariable=self.email).grid(row=3, column=1, pady=2)
        # teléfono
        tk.Label(self.ventana, text="Teléfono:").grid(row=4, column=0, padx=10)
        tk.Entry(self.ventana, textvariable=self.telefono).grid(row=4, column=1, pady=2)

        # GUARDADO ---
        tk.Button(self.ventana, text="Guardar", command=self.guardar).grid(row=5, column=0, pady=15, padx=10)

        # LIMPIEZA ---
        tk.Button(self.ventana, text="Limpiar", command=self.limpiar).grid(row=5, column=1, pady=15)

    def guardar(self):
        datos = f"""
            Nombre: {self.nombre.get()}
            Apellidos: {self.apellidos.get()}
            Edad: {self.edad.get()}
            Email: {self.email.get()}
            Teléfono: {self.telefono.get()}
        """
        messagebox.showinfo("Datos: ", datos)

    def limpiar(self):
        self.nombre.set("") # setter: "setea" lo que yo quiera en la variable
        self.apellidos.set("")
        self.edad.set("")
        self.email.set("")
        self.telefono.set("")

# MAIN ------------------------------------------
if __name__ == "__main__":
    Formulario()