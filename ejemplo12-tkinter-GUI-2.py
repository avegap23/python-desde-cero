'''
# IMPORTS ---------------------------------------
import tkinter as tk # https://docs.python.org/3.14/library/tkinter.html

# CLASS -----------------------------------------
class Seleccion:
    # método constructor
    def __init__(self):
        # creamos una ventana
        self.ventana = tk.Tk()

        # creamos una variable
        self.seleccion = tk.IntVar() # variable que recogerá únicamente enteros
        self.seleccion.set(2) # seteamos un valor por defecto

        # creamos el radiobutton
        self.radioSi = tk.Radiobutton(self.ventana, text="Me flipa programar", variable=self.seleccion, value=1)
        self.radioSi.grid(column=0, row=0)

        self.radioNo = tk.Radiobutton(self.ventana, text="Paso de programar", variable=self.seleccion, value=2)
        self.radioNo.grid(column=0, row=1)

        # creamos un botón de mostrando los resultados
        self.resultado = tk.Button(self.ventana, text="Mostrar selección: ", command=self.mostrarSeleccion)
        self.resultado.grid(column=0, row=2)

        self.etiqueta_resultado = tk.Label(self.ventana, text="Opción seleccionada: ")
        self.etiqueta_resultado.grid(column=0, row=3)

        # ejecución
        self.ventana.mainloop()

    # métodos de la clase
    def mostrarSeleccion(self):
        if self.seleccion.get() == 1:
            self.etiqueta_resultado.configure(text="Te flipa programar, es tu opción", bg="green")
        elif self.seleccion.get() == 2:
            self.etiqueta_resultado.configure(text="Odias programar, no eres de este mundillo", bg="grey")

# MAIN ------------------------------------------
sel = Seleccion()
'''

'''
NOTAS PARA ARCHIVOS: MODOS DE APERTURA EN PYTHON

Modos "normales":
    'r' - lectura (por defecto) - El archivo debe existir
    'w' - escritura (por defecto) - El archivo lo crea o sobreescribe si ya está creado
    'a' - añade al final o crea el archivo si no existe

Modos "raritos":
    'x' - creación exclusiva - Da error si el archivo ya existe
    'r+' - lectura/escritura - El archivo debe estar ya creado
    'w+' - lectura/escritura - EL archivo lo sobreescribe, no tiene que estar creado
    'a+' - lectura/escritura, añade al final - el archivo no tiene que estar creado
    'x+' - lectura/escritura - El archivo se crea si no existe

Otros modos sorprendentes:
    - Modos binarios: graban la información en binario, es decir, es la información pura (muy utilizada
    para imágenes, vídeos...) - 'rb+', 'wb+', 'ab+'
    - Modos texto: graba la información en txt, muy utilizada a la hora de guardar rutas de archvo,
    carpetas, etc. - 'rt', 'wt', 'at'

Posibles errores que se pueden producir con los archivos:
    - fileExistsError: el archivo ya existe, lo produce el modo 'x'.
    - fileNotFound: el archivo ya existe o no se encuentra.
    - PermissionError: no tenemos permisos para leer/escribir (777 - control completo)
    - IsADirectoryError: intenta abrir una carpeta como si fuese un archivo
    - NotADirectoryError: parte de la ruta no es una carpeta
    - UnicodeDecodeError: error en la decodificación del archivo (lectura)
    - UnicodeEncodeError: error (escritura) por la incompatibilidad de los caracteres
    - OSError: error general (HD lleno, ruta inválida...)
    - IOError: error de entrada/salida
    - ValueError: operación sobre el archivo cerrado o es un modo de apertura incorrecto
'''
# IMPORTS ---------------------------------------
import tkinter as tk # https://docs.python.org/3.14/library/tkinter.html
from tkinter import messagebox

# CLASS -----------------------------------------
class FormularioApp:
    # método constructor
    def __init__(self, root):
        # construcción de ventana principal
        self.root = root # root, realmente es una ventana
        self.root.title("Formulario Tkinter Completo")
        self.root.geometry("420x520")

        # definición de variables que recogerán información y valores por defecto
        self.rol_var = tk.StringVar(value="Usuario")
        self.activo_var = tk.BooleanVar(value=True)
        self.notif_var = tk.BooleanVar()
        self.pais_var = tk.StringVar(value="España")

        # llamada a los métodos de la clase
        self.crear_widgets()

    # métodos de clase
    # 1.- Creación de todo el formulario
    def crear_widgets(self):
        # creación de inputs normales
        tk.Label(self.root, text="Nombre").pack(anchor="w", padx=10, pady=(10, 0))
        # .pack(anchor"alineación del widget, putnos cardinales", padx=margen_horizontal, pady=(arriba, abajo))
        self.entry_nombre = tk.Entry(self.root, width=40)
        self.entry_nombre.pack(padx=10)

        tk.Label(self.root, text="Email").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_email = tk.Entry(self.root, width=40)
        self.entry_email.pack(padx=10)

        # creación de Radiobutton para los roles
        tk.Label(self.root, text="Rol").pack(anchor="w", padx=10, pady=(10, 0))
        tk.Radiobutton(self.root, text="Usuario", variable=self.rol_var, value="Usuario").pack(anchor="w", padx=20)
        tk.Radiobutton(self.root, text="Administrador", variable=self.rol_var, value="Administrador").pack(anchor="w", padx=20)

        # creación de Checkbutton, para activa y notificaciones
        tk.Checkbutton(self.root, text="Cuenta activa", variable=self.activo_var).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Checkbutton(self.root, text="Recibir notificaciones", variable=self.notif_var).pack(anchor="w", padx=10)

        # mis amigos, los raros
        tk.Label(self.root, text="País").pack(anchor="w", padx=10, pady=(10, 0))
        tk.OptionMenu(self.root, self.pais_var, "España", "Rumanía", "Francia", "Italia", "Otros no citados").pack(anchor="w", padx=10)

        tk.Label(self.root, text="Comentarios").pack(anchor="w", padx=10, pady=(10, 0))
        self.text_comentarios = tk.Text(self.root, width=40, height=5)
        self.text_comentarios.pack(padx=10)

        # creación de frame, donde irán los botones
        frame_botones = tk.Frame(self.root) # dónde se creará
        frame_botones.pack(pady=15)

        # creación de botones -- Guardado en TXT
        tk.Button(frame_botones, text="Guardar", command=self.guardar, width=12).pack(side="left", padx=15)

        # salir de la app (con destrucción)
        tk.Button(frame_botones, text="Salir", command=self.root.destroy, width=12).pack(side="left", padx=5)

    # 2.- Guardado de la informacióln en archivo
    def guardar(self):
        try:
            # with open("nombre_archivo", "apertura", encoding)
            with open("datos.txt", 'w', encoding="utf-8") as archivo:
                archivo.write(f"Nombre: {self.entry_nombre.get()}\n")
                archivo.write(f"Email: {self.entry_email.get()}\n")
                archivo.write(f"Rol: {self.rol_var.get()}\n")

                archivo.write(f"Activo: {'Si' if self.activo_var.get() else 'No'}\n")
                archivo.write(f"Notificaciones: {'Si' if self.notif_var.get() else 'No'}\n")

                archivo.write(f"País: {self.pais_var.get()}\n")
                archivo.write(f"Comentarios:\n")
                archivo.write(self.text_comentarios.get("1.0", tk.END)) # --> recoge todo el contenido desde la línea 1 hasta el final de contenido

                messagebox.showinfo("Guardar", "Datos guardados correctamente")

        except Exception as err:
            messagebox.showerror(f"Error: {str(err)}")

# MAIN ------------------------------------------
if __name__ == "__main__":
    root = tk.Tk() # creación del objeto de clase X
    app = FormularioApp(root) # creación de todo el entorno (ventana + widgets)
    root.mainloop() # ejecución de la app