'''
A partir de la versión Tk 8.5 entra en juego la biblioteca TTK:
    - incluye spinbox y otras nuevas funcionalidades.
    - mejora los controles visuales.
    - todo funciona igual, sólo hay que cargar los nuevos widgets.
    - incluye ciertos nuevos aspectos como las pestañas.

--------------------------------------------------------------------------
NUEVOS CONCEPTOS:
    - CRAWLING: navegación página a página, tal y como la realizan los 
    motores de búsqueda (arañas, bots).
    - SCRAPING: navegación que "rasca" información de un site (sitio web),
    la cual se podría guardar o trata par apoder obtener lo que necesita.

INSTALACIÓN DE NUEVAS BIBLIOTECAS EN PYTHON
pip install requests

Lo malo, lo bueno, lo peor...
    - creamos dependencias, lo que hace que nuestros proyectos tengan
    mucha información de la cual "teine que alimentarse", las
    bibliotecas de terceros.
    - Python "aprende" nuevas tecnologías, pero eso conlleva más peso
    y dependencia.
    - Las cargas se hacen más pesadas, lo cual es muy "fatal" para
    el proyector.

User agent: ¿Quién soy en realidad?
    https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Headers/User-Agent
'''

# IMPORTS ---------------------------------------
import tkinter as tk # https://docs.python.org/3.14/library/tkinter.html
from tkinter import ttk, messagebox, scrolledtext # https://docs.python.org/3/library/tkinter.ttk.html
import requests # https://pypi.org/project/requests/
from bs4 import BeautifulSoup # https://pypi.org/project/beautifulsoup4/

# CLASS -----------------------------------------
class ExtractorWebApp:
    # método constructor
    def __init__(self, root):
        # ventana principal
        self.root = root
        self.root.title("Extractor Avanzado de contenido web")
        self.root.geometry("950x650")

        # llamada (recursiva) a la creación de interfaz
        self.crear_interfaz()

    # métodos de la clase
    def crear_interfaz(self):
        # 1.- Control de pestañas
        notebook = ttk.Notebook(self.root) # notebook: control de pestañas
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # 2.- Llamadas a métodos nuevos para creación de pestañas (tab)
        self.tab_extractor = ttk.Frame(notebook)
        self.tab_config = ttk.Frame(notebook)
        self.tab_ayuda = ttk.Frame(notebook)

        # 3.- Añadimos las tab al notebook
        notebook.add(self.tab_extractor, text="Extracción")
        notebook.add(self.tab_config, text="Configuración")
        notebook.add(self.tab_ayuda, text="Ayuda")

        # 4.- Llamada a los métodos de creación de cada interfaz de cada tab
        self.crear_tab_extractor()
        self.crear_tab_config()
        self.crear_tab_ayuda()

    # creación de interfaz de la pestaña extractor
    def crear_tab_extractor(self):

        # input para introducir url
        frame_url = ttk.Labelframe(
            self.tab_extractor,
            text="Datos de entrada",
            padding=10
        )
        frame_url.pack(fill='x', padx=10, pady=10)

        ttk.Label(frame_url, text="URL: ").grid(row=0, column=0, sticky='w') # sticky obliga a que se pegue
        self.entrada_url = ttk.Entry(frame_url)
        self.entrada_url.grid(row=0, column=1, sticky='ew', padx=8)

        frame_url.columnconfigure(1, weight=1)

        # selector de opciones, para seleccionar la información que se va a raspar
        frame_opciones = ttk.Labelframe(
            self.tab_extractor,
            text="Opciones de extracción",
            padding=10
        )
        frame_opciones.pack(fill='x', padx=10, pady=5)

        ttk.Label(frame_opciones, text="Contenido").grid(row=0, column=0, sticky='w')
        self.modo = tk.StringVar(value="Sólo posts")
        self.combo_modo = ttk.Combobox(
            frame_opciones,
            textvariable = self.modo,
            values=["Sólo posts", "Posts y fechas", "Toda la información"],
            state="readonly" # no modificable, sólo lectura
        )
        self.combo_modo.grid(row=0, column=1, sticky='ew', padx=8)

        frame_url.columnconfigure(1, weight=1) # separador

        # frame para los botones (típicos)
        frame_botones = ttk.Frame(self.tab_extractor, padding=10)
        frame_botones.pack(fill='x')

        ttk.Button(
            frame_botones, text="Extraer contenido",
            command=self.extraer_contenido
        ).pack(side="left")

        ttk.Button(
            frame_botones, text="Limpiar",
            command=self.limpiar_contenido
        ).pack(side="left", padx=8)

        # "Caja" de resultados
        frame_resultado = ttk.Labelframe(self.tab_extractor, text="Resultado", padding=10)
        frame_resultado.pack(fill="both", expand=True, padx=10, pady=10)

        self.salida = scrolledtext.ScrolledText(frame_resultado, wrap=tk.WORD)
        # se crea un scroll, corta el scroll por palabras, no divide palabras
        self.salida.pack(fill="both", expand=True)

    # creación de interfaz de la pestaña configuración
    def crear_tab_config(self):
        # área de configuración para "navegación tipo"
        frame_http = ttk.Labelframe(self.tab_config, text="Configuración HTTP", padding=10)
        frame_http.pack(fill='x', padx=10, pady=10)

        # creación de interfaz de introducción de parámetros para scripting
        ttk.Label(frame_http, text="Agente").grid(row=0, column=0, sticky='w')
        
        self.useragent = tk.StringVar(value="Mozilla/5.0")
        ttk.Entry(frame_http, textvariable=self.useragent).grid(row=0, column=1, sticky='ew', padx=0)

    def crear_tab_ayuda(self):
        pass

    def extraer_contenido(self):
        pass

    def limpiar_contenido(self):
        pass

# MAIN ------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ExtractorWebApp(root)
    root.mainloop()