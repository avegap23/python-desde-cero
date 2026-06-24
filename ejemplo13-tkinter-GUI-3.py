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

    # creación de interfaz
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
            command=self.limpiar_resultado
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

        ttk.Label(frame_http, text="Timeout: ").grid(row=1, column=0, sticky='w', pady=8)
        self.timeout = tk.IntVar(value=15) # tiempo va a ser 15 segundos por defecto
        ttk.Spinbox(frame_http, from_=3, to=60, textvariable=self.timeout).grid(row=1, column=1, sticky='w', padx=8)

        frame_http.columnconfigure(1, weight=1) # separador

        # área de configuración para filtros
        frame_filtro = ttk.LabelFrame(self.tab_config, text="Filtros", padding=10)
        frame_filtro.pack()

        self.eliminar_scripts = tk.BooleanVar(value=True) # eliminación de lectura JS
        self.eliminar_estilos = tk.BooleanVar(value=True) # eliminación de lectura CSS

        ttk.Checkbutton(
            frame_filtro, text="Eliminar scripts (JS)",
            command=self.eliminar_scripts
        ).pack(anchor='w')

        ttk.Checkbutton(
            frame_filtro, text="Eliminar estilos (CSS)",
            command=self.eliminar_estilos
        ).pack(anchor='w')

    # creación de interfaz de la pestaña ayuda
    def crear_tab_ayuda(self):
        frame = ttk.Frame(self.tab_ayuda, padding=15)
        frame.pack(fill="both", expand=True)

        texto = """
        Esta aplicación permite extraer contenido básico de una URL cualquiera.

        - Pestaña EXTRACCIÓN:
            --> Cómo lo hago:
            · Introducimos una URL
            · Se elige el tipo de contenido a rapsar
            · Pulsamos el botón "Extraer contenido"

            --> Modos de extracción:
            · Sólo posts: intenta extraer los artículos/bloques principales
            · Posts y fechas: busca títulos y fechas dentro de ciertas tags (<article>)
            · Toda la información: extrae todo el contenido visible de la página
        
        - Pestaña INFORMACIÓN:
            --> Qué podemos re-configurar:
            · Se puede modificar el User-Agent
            · Se puede cambiar el timeout (tiempo límite)
            · Se puede activar/desactivar ciertos filtros básicos
        """
        ttk.Label(frame, text=texto, justify="left").pack(anchor='nw')

    # métodos de clase: acciones necesarias ---------------------------------------------

    # 1.- Preparando todo

    # Normalización de protocolos
    def normalizar_url(self, url):
        url = url.strip()

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        return url

    # obtención de código y conversión a texto
    def obtener_html(self, url):
        url = self.normalizar_url(url)

        headers = {"User-Agent": self.useragent.get()} # información adicional para el server

        # solicitamos la respuesta al servidor
        respuesta = requests.get(
            url,
            headers=headers,
            timeout=self.timeout.get()
        )

        # comprobación de errores --> https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status
        respuesta.raise_for_status() # comprobación de errores automática

        # recogemos la respuesta y la convertimos en texto
        return respuesta.text

    # limpieza de "cosas raras": tabulaciones, saltos... NORMALIZACIÓN del texto
    def limpiar_texto(self, texto):
        return " ".join(texto.split())
        # split: división del texto en la lista de palabras, eliminando espacios, \t, \n
        # join: une las palabras en una lista, con un separador determinado (" " es espacio)

    # 2.- Comenzamos a "jugar con los mayores": buscando la información requerida

    # preparación de la sopa: HTML parser
    def preparar_soup(self, html):
        soup = BeautifulSoup(html, "html.parser") # parseo a HTML

        # comprobación de opciones
        if self.eliminar_scripts.get():
            for etiqueta in soup("script"):
                etiqueta.decompose() # eliminación completa de la etiqueta y su contenido
        # <script>alert("Holis!!")</script>

        if self.eliminar_estilos.get():
            for etiqueta in soup("style"):
                etiqueta.decompose() # eliminación completa de la etiqueta y su contenido
        # <style>a {color: "red"}</style>

        for etiqueta in soup("noscript"):
            etiqueta.decompose() # etiqueta tipo <noscript>Activa tu JS</noscript>

        return soup

    # 3.- Dando caña al tema: extracción real, comprobación de problemas y demás
    def extraer_contenido(self):
        # a) recogemos el valor de la URL
        url = self.entrada_url.get().strip()

        # b) comprobaciones mínimas
        if not url:
            messagebox.showwarning("URL requerida", "Introduce una URL válida")

        # c) arreando que es gerundio
        try:
            html = self.obtener_html(url)
            soup = self.preparar_soup(html)

            self.salida.delete("1.0", tk.END) # vaciamos el cuadro de resultado

            if self.modo.get() == "Sólo posts":
                self.extraer_posts(soup)

            elif self.modo.get() == "Posts y fechas":
                self.extraer_posts_fechas(soup)

            elif self.modo.get() == "Toda la información":
                self.extraer_todo(soup)
        
        except requests.exceptions.RequestException as err:
            messagebox.showerror(title="Error de conexión", message=f"Error de conexión: {str(err)}") # error de conexión con el servidor

        except Exception as err:
            messagebox.showerror(title="Error", message=f"Error: {str(err)}") # error de cualquier tipo

    def extraer_posts(self, soup):
        articulos = soup.find_all("article") # búsqueda de todas las tags con este nombre

        if not articulos:
            articulos = soup.find_all(["h1","h2","h3","p"])
        
        if not articulos:
            self.salida.insert(tk.END, "¡No se encontraron posts!\n")
            return
        
        for i, articulo in enumerate(articulos, start=1):
            texto = self.limpiar_texto(articulo.get_text(" ", strip=True))

            if texto:
                self.salida.insert(tk.END, f"POST {i}\n")
                self.salida.insert(tk.END, "-" * 70 + "\n")
                self.salida.insert(tk.END, texto + "\n\n")

    def extraer_posts_fechas(self, soup):
        articulos = soup.find_all("article") # búsqueda de todas las tags con este nombre

        if not articulos:
            self.salida.insert(
                tk.END,
                "No se encontraron etiquetas <article>. Mostraremos posts básicos\n\n"
            )
            self.extraer_posts(soup)
            return

        for i, articulo in enumerate(articulos, start=1):
            titulo = articulo.find(["h1","h2","h3"])
            fecha = articulo.find("time")

            texto_titulo = (
                self.limpiar_texto(titulo.get_text(" ", strip=True))
                if titulo else "Sin título reconocido"
            )

            texto_fecha = (
                fecha.get("datetime") or self.limpiar_texto(fecha.get_text(" ", strip=True))
                if fecha else "No se encontró la fecha"
            )

            resumen = self.limpiar_texto(articulo.get_text(" ", strip=True))

            # se escriben datos en la zona de resultados
            self.salida.insert(tk.END, f"POST {i}\n") # número de post
            self.salida.insert(tk.END, "-" * 70 + "\n")
            self.salida.insert(tk.END, f"Título: {texto_titulo}")
            self.salida.insert(tk.END, f"Fecha: {texto_fecha}")
            self.salida.insert(tk.END, f"Contenido: {resumen}")

    def extraer_todo(self, soup):
        texto = self.limpiar_texto(soup.get_text(" ", strip=True))

        if texto:
            self.salida.insert(tk.END, texto) # insertamos el resultado en su correspondiente
        else:
            self.salida.insert(tk.END, "No se pudo obtener información visible")

    def limpiar_resultado(self):
        self.salida.delete("1.0", tk.END)

# MAIN ------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ExtractorWebApp(root)
    root.mainloop()