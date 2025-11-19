import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
import os # Para rutas de carpetas
# Asumimos que estos archivos existen en tu carpeta de proyecto
from game_data import GAME_STRUCTURE
import methods_engine as me 

# --- COLORES ---
COLOR_FONDO = "#001F3F"       # Azul Marino oscuro
COLOR_BOTON = "#40E0D0"       # Turquesa Claro (Menú Principal)
COLOR_TEXTO_BTN = "#000000"   # Negro
COLOR_TEXTO_LBL = "#FFFFFF"   # Blanco
COLOR_BOTON_CLARO = "#AFEEEE"   # Turquesa Pálido (PaleTurquoise)
COLOR_BORDE_OSCURO = "#008080"  # Teal (Para el contorno oscuro)
COLOR_BOTON_ROJO = "#FF6B6B"    # Rojo suave (fallback si no hay imagen)

# --- COLORES DE FRANJAS POR TIPO DE LECCIÓN ---
COLOR_STRIP_EXPL = "#FFD700"    # Amarillo (Gold) para explicativas
COLOR_STRIP_PRAC = "#FF8C00"    # Naranja (DarkOrange) para prácticas
COLOR_STRIP_EXAM = "#FF4500"    # Rojo para exámenes

# --- DIMENSIONES ---
HEADER_HEIGHT = 70 # Altura constante para franjas y encabezados

class RoundedButton(tk.Canvas):
    """
    Clase personalizada para crear botones con esquinas redondeadas.
    Calcula el ancho automáticamente según el texto si width=None.
    """
    def __init__(self, parent, text, command, width=None, height=60, corner_radius=20, 
                 color=COLOR_BOTON, text_color=COLOR_TEXTO_BTN, bg_color=COLOR_FONDO,
                 outline_color=None, border_width=0):
        
        # Calcular ancho basado en el texto si no se provee uno
        if width is None:
            font = tkfont.Font(family="Arial", size=14, weight="bold")
            text_width = font.measure(text)
            width = text_width + 60 # Padding horizontal (30px por lado)

        tk.Canvas.__init__(self, parent, borderwidth=0, 
                           relief="flat", highlightthickness=0, bg=bg_color)
        self.command = command
        self.text = text
        self.color = color
        self.text_color = text_color
        self.width = width
        self.height = height
        self.corner_radius = corner_radius
        
        self.outline_color = outline_color if outline_color else color
        self.border_width = border_width

        # Configurar tamaño del canvas
        self.configure(width=width, height=height)

        # Dibujar el botón
        self.draw_button()
        
        # Bindings de eventos
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self._on_hover)
        self.bind("<Leave>", self._on_leave)

    def draw_button(self):
        self.delete("all") # Limpiar canvas
        
        r = self.corner_radius
        w = self.width
        h = self.height
        bw = self.border_width
        
        x0, y0 = bw, bw
        x1, y1 = w - bw, h - bw

        # --- 1. DIBUJAR FORMA RELLENA ---
        self.create_arc((x0, y0, x0+2*r, y0+2*r), start=90, extent=90, fill=self.color, outline=self.color, tags="btn")
        self.create_arc((x1-2*r, y0, x1, y0+2*r), start=0, extent=90, fill=self.color, outline=self.color, tags="btn")
        self.create_arc((x1-2*r, y1-2*r, x1, y1), start=270, extent=90, fill=self.color, outline=self.color, tags="btn")
        self.create_arc((x0, y1-2*r, x0+2*r, y1), start=180, extent=90, fill=self.color, outline=self.color, tags="btn")
        
        self.create_rectangle((x0+r, y0, x1-r, y1), fill=self.color, outline=self.color, tags="btn")
        self.create_rectangle((x0, y0+r, x1, y1-r), fill=self.color, outline=self.color, tags="btn")
        
        # --- 2. DIBUJAR CONTORNO (Si aplica) ---
        if self.border_width > 0:
            oc = self.outline_color
            b = self.border_width
            self.create_arc((x0, y0, x0+2*r, y0+2*r), start=90, extent=90, style=tk.ARC, outline=oc, width=b, tags="btn")
            self.create_arc((x1-2*r, y0, x1, y0+2*r), start=0, extent=90, style=tk.ARC, outline=oc, width=b, tags="btn")
            self.create_arc((x1-2*r, y1-2*r, x1, y1), start=270, extent=90, style=tk.ARC, outline=oc, width=b, tags="btn")
            self.create_arc((x0, y1-2*r, x0+2*r, y1), start=180, extent=90, style=tk.ARC, outline=oc, width=b, tags="btn")
            
            self.create_line(x0+r, y0, x1-r, y0, fill=oc, width=b, tags="btn")
            self.create_line(x1, y0+r, x1, y1-r, fill=oc, width=b, tags="btn")
            self.create_line(x1-r, y1, x0+r, y1, fill=oc, width=b, tags="btn")
            self.create_line(x0, y1-r, x0, y0+r, fill=oc, width=b, tags="btn")
        
        # Texto centrado
        self.create_text(w/2, h/2, text=self.text, fill=self.text_color, font=("Arial", 14, "bold"), tags="btn")

    def _on_press(self, event):
        self.move("btn", 1, 1)

    def _on_release(self, event):
        self.move("btn", -1, -1)
        if self.command:
            self.command()

    def _on_hover(self, event):
        self.config(cursor="hand2")

    def _on_leave(self, event):
        self.config(cursor="")

class ScrollableFrame(tk.Frame):
    """
    Un frame que contiene un Canvas y Scrollbar para permitir scroll vertical.
    Se ajusta automáticamente al ancho para mantener el contenido centrado.
    """
    def __init__(self, container, bg_color=COLOR_FONDO, *args, **kwargs):
        super().__init__(container, bg=bg_color, *args, **kwargs)
        
        self.canvas = tk.Canvas(self, bg=bg_color, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        # Frame interno donde irán los widgets
        self.scrollable_frame = tk.Frame(self.canvas, bg=bg_color)

        # Configurar el scroll cuando el frame interno cambie de tamaño
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Crear la ventana dentro del canvas
        self.window_id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Binding CRÍTICO para que el frame interno se estire al ancho del canvas
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Empaquetar scrollbar primero a la derecha para que quede en el borde
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.bind_mouse_scroll(self.canvas)

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.window_id, width=event.width)

    def bind_mouse_scroll(self, canvas):
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        def _on_linux_scroll_up(event):
            canvas.yview_scroll(-1, "units")
        def _on_linux_scroll_down(event):
            canvas.yview_scroll(1, "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all("<Button-4>", _on_linux_scroll_up)
        canvas.bind_all("<Button-5>", _on_linux_scroll_down)


class NumericalMethodsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Métodos Numéricos - El Juego") 
        self.root.geometry("800x600")
        self.root.configure(bg=COLOR_FONDO)
        
        self.username = "Jugador 1"
        self.errors_committed = 0
        self.time_elapsed = "0h 0m"
        self.medals = []
        
        # --- CARGAR IMAGEN DE "VOLVER" EN CARPETA IMGS ---
        self.back_icon = None
        # Nueva ruta: imgs/red-go-back-arrow.png
        img_path = os.path.join("imgs", "red-go-back-arrow.png")
        
        if os.path.exists(img_path):
            try:
                # Cargar la imagen base
                original_image = tk.PhotoImage(file=img_path)
                
                # --- REDIMENSIONAR IMAGEN A HEADER_HEIGHT (Pure Tkinter) ---
                # Truco: zoom(objetivo) -> subsample(original) escala la altura a 'objetivo'
                # Esto evita necesitar la librería PIL (Pillow)
                orig_height = original_image.height()
                target_height = HEADER_HEIGHT - 10 # Un poco de margen (padding)
                
                if orig_height > 0:
                    # 1. Zoom para multiplicar tamaño
                    zoomed = original_image.zoom(target_height)
                    # 2. Subsample para dividir por el tamaño original
                    # Resultado final ~= target_height
                    self.back_icon = zoomed.subsample(orig_height)
                else:
                    self.back_icon = original_image

            except Exception as e:
                print(f"Error cargando o procesando imagen: {e}")
        else:
            # Crear la carpeta si no existe para evitar errores futuros, o avisar
            print(f"Imagen no encontrada en: {os.path.abspath(img_path)}")
            # Opcional: crear carpeta
            if not os.path.exists("imgs"):
                try:
                    os.makedirs("imgs")
                    print("Carpeta 'imgs' creada. Por favor coloque la imagen ahí.")
                except:
                    pass

        self.main_frame = tk.Frame(root, bg=COLOR_FONDO)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.current_screen = None
        self.show_main_menu()

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = tk.Frame(self.main_frame, bg=COLOR_FONDO)
        self.current_screen.pack(fill=tk.BOTH, expand=True)

    def create_back_button(self, parent, command, bg_color):
        """
        Crea el botón de regreso. Usa la imagen si está disponible,
        si no, usa el botón redondeado rojo.
        """
        if self.back_icon:
            # Botón de Imagen
            btn = tk.Button(parent, image=self.back_icon, 
                            command=command,
                            bg=bg_color, 
                            activebackground=bg_color,
                            bd=0, 
                            highlightthickness=0,
                            relief="flat",
                            cursor="hand2")
        else:
            # Fallback: Botón de Texto Rojo
            btn = RoundedButton(parent, text="VOLVER", width=100, height=40,
                                color=COLOR_BOTON_ROJO, 
                                bg_color=bg_color,
                                command=command)
        return btn

    def add_header_with_back(self, title_text, back_cmd, bg_color=COLOR_FONDO, text_color=COLOR_TEXTO_LBL):
        """
        Crea una barra superior con el Título CENTRADO ABSOLUTAMENTE y el botón a la derecha.
        """
        # Usamos HEADER_HEIGHT constante
        header_frame = tk.Frame(self.current_screen, bg=bg_color, height=HEADER_HEIGHT)
        header_frame.pack(fill=tk.X, side=tk.TOP, pady=(0, 0), padx=0)
        header_frame.pack_propagate(False) # Forzar altura fija

        # 1. Botón a la DERECHA (usando pack, con padding derecho)
        btn_back = self.create_back_button(header_frame, back_cmd, bg_color)
        btn_back.pack(side=tk.RIGHT, anchor="center", padx=10) 

        lbl = tk.Label(header_frame, text=title_text, font=("Arial", 22, "bold"), 
                       bg=bg_color, fg=text_color)
        lbl.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_main_menu(self):
        self.clear_screen()
        
        tk.Label(self.current_screen, 
                 text="¡Aprende, Juega, Domina!", 
                 font=("Arial", 28, "bold"),
                 bg=COLOR_FONDO, 
                 fg=COLOR_TEXTO_LBL).pack(pady=40)
        
        btn_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        btn_frame.pack(pady=20, anchor="center")

        RoundedButton(btn_frame, text="JUGAR", width=250, command=self.show_chapter_menu).pack(pady=15)
        RoundedButton(btn_frame, text="VER PERFIL", width=250, command=self.show_user_menu).pack(pady=15)
        RoundedButton(btn_frame, text="SALIR", width=125, color=COLOR_BOTON_ROJO, command=self.root.quit).pack(pady=15)

    def show_user_menu(self):
        self.clear_screen()
        
        self.add_header_with_back(f"PERFIL DE: {self.username}", self.show_main_menu)
        
        tk.Label(self.current_screen, text=f"TIEMPO TRANSCURRIDO: {self.time_elapsed}", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL, font=("Arial", 14)).pack(pady=20) 
        tk.Label(self.current_screen, text=f"ERRORES COMETIDOS: {self.errors_committed}", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL, font=("Arial", 14)).pack(pady=5) 
        
        tk.Label(self.current_screen, text="MEDALLAS GANADAS:", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack(pady=20)
        for medal in self.medals:
            tk.Label(self.current_screen, text=f"🏅 {medal}", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL, font=("Arial", 12)).pack()
        if not self.medals:
            tk.Label(self.current_screen, text="(Aún no hay medallas)", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack()
        
    def show_chapter_menu(self):
        self.clear_screen()
        
        self.add_header_with_back("LECCIONES", self.show_main_menu)
        
        scroll_container = ScrollableFrame(self.current_screen, bg_color=COLOR_FONDO)
        scroll_container.pack(fill="both", expand=True, pady=10)

        for chapter_name in GAME_STRUCTURE.keys():
            btn = RoundedButton(scroll_container.scrollable_frame, 
                                text=chapter_name, 
                                width=None, 
                                height=55,
                                color=COLOR_BOTON_CLARO,
                                outline_color=COLOR_BORDE_OSCURO,
                                border_width=3,
                                command=lambda c=chapter_name: self.show_level_menu(c))
            btn.pack(pady=8)
            
    def show_level_menu(self, chapter_name):
        self.clear_screen()
        
        self.add_header_with_back(chapter_name, self.show_chapter_menu)
        
        scroll_container = ScrollableFrame(self.current_screen, bg_color=COLOR_FONDO)
        scroll_container.pack(fill="both", expand=True, pady=10)

        levels = GAME_STRUCTURE[chapter_name]['levels']
        for level_name in levels.keys():
            btn = RoundedButton(scroll_container.scrollable_frame, 
                                text=level_name,
                                width=None, 
                                height=55,
                                color=COLOR_BOTON_CLARO,
                                outline_color=COLOR_BORDE_OSCURO,
                                border_width=3,
                                command=lambda l=level_name: self.start_lesson(chapter_name, l, 0))
            btn.pack(pady=8)
            
    def start_lesson(self, chapter, level, lesson_index):
        self.clear_screen()
        
        lessons = GAME_STRUCTURE[chapter]['levels'][level]
        
        if lesson_index >= len(lessons):
            messagebox.showinfo("¡Felicidades!", f"¡Nivel '{level}' completado!")
            if f"{level}" not in self.medals:
                self.medals.append(f"{level}")
            self.show_level_menu(chapter)
            return

        current_lesson = lessons[lesson_index]
        lesson_type = current_lesson['type']
        
        # --- LÓGICA DE FRANJA DE COLOR ---
        strip_color = COLOR_FONDO 
        title_fg_color = COLOR_TEXTO_LBL 
        
        if lesson_type == 'explicativa':
            strip_color = COLOR_STRIP_EXPL
            title_fg_color = "#000000"
        elif lesson_type == 'practica':
            strip_color = COLOR_STRIP_PRAC
            title_fg_color = "#000000"
        elif lesson_type == 'examen':
            strip_color = COLOR_STRIP_EXAM
            title_fg_color = "#FFFFFF"
            
        # Frame de la franja con altura fija HEADER_HEIGHT
        strip_frame = tk.Frame(self.current_screen, bg=strip_color, padx=0, height=HEADER_HEIGHT)
        strip_frame.pack(fill=tk.X, side=tk.TOP)
        strip_frame.pack_propagate(False) # Mantener altura fija

        # 1. Botón VOLVER (Imagen o Fallback)
        btn_back = self.create_back_button(strip_frame, 
                                           command=lambda: self.show_level_menu(chapter),
                                           bg_color=strip_color)
        btn_back.pack(side=tk.RIGHT, anchor="center", padx=10)

        # 2. Título CENTRADO ABSOLUTO (usando place relativo al frame)
        tk.Label(strip_frame, 
                 text=f"{level} - Lección {lesson_index + 1}", 
                 font=("Arial", 20, "bold"), 
                 bg=strip_color, 
                 fg=title_fg_color).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Contenido de la lección
        if lesson_type == 'explicativa':
            self.show_explicativa(current_lesson, chapter, level, lesson_index)
        elif lesson_type == 'practica' or lesson_type == 'examen':
            self.show_practica(current_lesson, chapter, level, lesson_index)
            
    def show_explicativa(self, lesson, chapter, level, lesson_index):
        lbl_content = tk.Label(self.current_screen, text=lesson['content'], 
                               wraplength=700, justify=tk.LEFT, 
                               font=("Arial", 12), bg=COLOR_FONDO, fg="white")
        lbl_content.pack(pady=20, padx=40)
        
        RoundedButton(self.current_screen, text="CONTINUAR", width=200, height=50,
                  command=lambda: self.start_lesson(chapter, level, lesson_index + 1)).pack(pady=10)

    def show_practica(self, lesson, chapter, level, lesson_index):
        tk.Label(self.current_screen, text=f"Pregunta: {lesson['content']}", 
                 wraplength=700, font=("Arial", 14), bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack(pady=20, padx=40)
        
        options_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        options_frame.pack(pady=10)

        if 'options' in lesson:
            for option in lesson['options']:
                btn = RoundedButton(options_frame, text=option, width=None, height=50,
                                    color=COLOR_BOTON_CLARO, outline_color=COLOR_BORDE_OSCURO, border_width=2,
                                    command=lambda o=option: self.check_answer(o, lesson, chapter, level, lesson_index))
                btn.pack(pady=5)
                
        elif 'problem_id' in lesson:
            tk.Label(self.current_screen, text=f"(Mostrando problema: {lesson['problem_id']})", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack(pady=10)
            tk.Label(self.current_screen, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack()
            entry = tk.Entry(self.current_screen, font=("Arial", 12))
            entry.pack(pady=10)
            
            RoundedButton(self.current_screen, text="REVISAR", width=200, height=50,
                      command=lambda: messagebox.showinfo("WIP", "Lógica de revisión no implementada")).pack(pady=20)

    def check_answer(self, user_answer, lesson, chapter, level, lesson_index):
        correct_answer = lesson['answer']
        lesson_type = lesson['type']
        
        if user_answer == correct_answer:
            messagebox.showinfo("¡Correcto!", "¡Muy bien! Pasando a la siguiente lección.")
            self.start_lesson(chapter, level, lesson_index + 1)
        else:
            self.errors_committed += 1
            if lesson_type == 'practica':
                messagebox.showerror("Incorrecto", f"La respuesta correcta era '{correct_answer}'. \nRegresando a la lección anterior. ")
                self.start_lesson(chapter, level, lesson_index - 1)
            elif lesson_type == 'examen':
                messagebox.showerror("Incorrecto", f"Respuesta incorrecta. \nReiniciando la lección. ")
                self.start_lesson(chapter, level, lesson_index)

