import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
import os
from game_data import GAME_STRUCTURE
import methods_engine as me 

# --- COLORES GENERALES ---
COLOR_FONDO = "#001F3F"
COLOR_BOTON = "#40E0D0"
COLOR_TEXTO_BTN = "#FFFFFF" # Texto blanco para resaltar en botones oscuros/vibrantes
COLOR_TEXTO_LBL = "#FFFFFF"
COLOR_BOTON_CLARO = "#1F8686"
COLOR_BORDE_OSCURO = "#008080"
COLOR_BOTON_ROJO = "#FF6B6B"

# --- COLORES DE DIFICULTAD (Basados en tu imagen) ---
BTN_EASY_COLOR = "#00E676"      # Verde/Cyan vibrante
BTN_INTER_COLOR = "#FFAB00"     # Naranja/Amarillo
BTN_ADV_COLOR = "#F50057"       # Rosa/Rojo intenso
BTN_FINAL_COLOR = "#D500F9"     # Violeta brillante

# --- COLORES DE FRANJAS ---
COLOR_STRIP_EXPL = "#FFD700"
COLOR_STRIP_PRAC = "#FF8C00"
COLOR_STRIP_EXAM = "#FF4500"

HEADER_HEIGHT = 70

# ... (Mantén tu clase RoundedButton y ScrollableFrame EXACTAMENTE IGUAL que antes) ...
# ... (Copia aquí las clases RoundedButton y ScrollableFrame de tu código anterior) ...

class RoundedButton(tk.Canvas):
    # PEGA AQUÍ TU CLASE RoundedButton ORIGINAL
    def __init__(self, parent, text, command, width=None, height=60, corner_radius=20, 
                 color=COLOR_BOTON, text_color=COLOR_TEXTO_BTN, bg_color=COLOR_FONDO,
                 outline_color=None, border_width=0):
        
        if width is None:
            font = tkfont.Font(family="Arial", size=14, weight="bold")
            text_width = font.measure(text)
            width = text_width + 60

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

        self.configure(width=width, height=height)
        self.draw_button()
        
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self._on_hover)
        self.bind("<Leave>", self._on_leave)

    def draw_button(self):
        self.delete("all")
        r = self.corner_radius
        w = self.width
        h = self.height
        bw = self.border_width
        x0, y0 = bw, bw
        x1, y1 = w - bw, h - bw

        self.create_arc((x0, y0, x0+2*r, y0+2*r), start=90, extent=90, fill=self.color, outline=self.color, tags="btn")
        self.create_arc((x1-2*r, y0, x1, y0+2*r), start=0, extent=90, fill=self.color, outline=self.color, tags="btn")
        self.create_arc((x1-2*r, y1-2*r, x1, y1), start=270, extent=90, fill=self.color, outline=self.color, tags="btn")
        self.create_arc((x0, y1-2*r, x0+2*r, y1), start=180, extent=90, fill=self.color, outline=self.color, tags="btn")
        self.create_rectangle((x0+r, y0, x1-r, y1), fill=self.color, outline=self.color, tags="btn")
        self.create_rectangle((x0, y0+r, x1, y1-r), fill=self.color, outline=self.color, tags="btn")
        
        self.create_text(w/2, h/2, text=self.text, fill=self.text_color, font=("Arial", 14, "bold"), tags="btn")

    def _on_press(self, event): self.move("btn", 1, 1)
    def _on_release(self, event): 
        self.move("btn", -1, -1)
        if self.command: self.command()
    def _on_hover(self, event): self.config(cursor="hand2")
    def _on_leave(self, event): self.config(cursor="")

class ScrollableFrame(tk.Frame):
    # PEGA AQUÍ TU CLASE ScrollableFrame ORIGINAL
    def __init__(self, container, bg_color=COLOR_FONDO, *args, **kwargs):
        super().__init__(container, bg=bg_color, *args, **kwargs)
        self.canvas = tk.Canvas(self, bg=bg_color, highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=bg_color)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.window_id = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.bind_mouse_scroll(self.canvas)

    def _on_canvas_configure(self, event): self.canvas.itemconfig(self.window_id, width=event.width)
    def bind_mouse_scroll(self, canvas):
        def _on_mousewheel(event):
            try:
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            except Exception:
                pass

        # Bind only when mouse is over the canvas and unbind when leaves to avoid callbacks to destroyed widgets
        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))


class GradientRoundedButton(tk.Canvas):
    """Canvas-based rounded button with a simple horizontal gradient fill."""
    def __init__(self, parent, text, command, width=420, height=70, corner_radius=35,
                 colors=("#20D0C6", "#FF7A4D"), text_color="#ffffff", bg_color=COLOR_FONDO):
        tk.Canvas.__init__(self, parent, borderwidth=0, relief="flat", highlightthickness=0, bg=bg_color)
        self.command = command
        self.text = text
        self.colors = colors
        self.text_color = text_color
        self.width = width
        self.height = height
        self.corner_radius = corner_radius
        self.bg_color = bg_color
        self.configure(width=width, height=height)
        self.draw_button()

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self._on_hover)
        self.bind("<Leave>", self._on_leave)

    def draw_button(self):
        self.delete("all")
        r = self.corner_radius
        w = self.width
        h = self.height

        # Draw gradient by drawing many narrow vertical lines interpolating colors
        steps = max(2, int(w / 2))
        r1, g1, b1 = self._hex_to_rgb(self.colors[0])
        r2, g2, b2 = self._hex_to_rgb(self.colors[-1])
        for i in range(steps):
            t = i / (steps - 1)
            ri = int(r1 + (r2 - r1) * t)
            gi = int(g1 + (g2 - g1) * t)
            bi = int(b1 + (b2 - b1) * t)
            col = f"#{ri:02x}{gi:02x}{bi:02x}"
            x0 = i * (w / steps)
            x1 = (i + 1) * (w / steps)
            # Clip corners by drawing over full rect then using arcs to mask look
            self.create_rectangle(x0, 0, x1, h, fill=col, width=0)

        # Mask corners by drawing rounded border shapes (drawn over gradient to give rounded look)
        self.create_arc((0, 0, 2*r, 2*r), start=90, extent=90, fill=self.colors[0], outline=self.colors[0])
        self.create_arc((w-2*r, 0, w, 2*r), start=0, extent=90, fill=self.colors[-1], outline=self.colors[-1])
        self.create_arc((w-2*r, h-2*r, w, h), start=270, extent=90, fill=self.colors[-1], outline=self.colors[-1])
        self.create_arc((0, h-2*r, 2*r, h), start=180, extent=90, fill=self.colors[0], outline=self.colors[0])

        # Draw central rounded rectangle overlay to smooth edges
        self.create_rectangle((r, 0, w-r, h), fill="", outline="")

        # Add subtle outer glow (thin outline)
        self.create_round_rect = None

        # Play icon (triangle) on left
        tri_size = int(h * 0.34)
        cx = r
        cy = h / 2
        self.create_polygon(cx - tri_size/2, cy - tri_size/1.2,
                            cx - tri_size/2, cy + tri_size/1.2,
                            cx + tri_size/1.2, cy,
                            fill=self.text_color, outline="")

        # Text centered
        self.create_text(w/2 + 30, h/2, text=self.text, fill=self.text_color,
                         font=("Arial", 18, "bold"))

    def _hex_to_rgb(self, hexcol):
        hexcol = hexcol.lstrip('#')
        return tuple(int(hexcol[i:i+2], 16) for i in (0, 2, 4))

    def _on_press(self, event):
        self.scale("all", self.width/2, self.height/2, 0.995, 0.995)

    def _on_release(self, event):
        try:
            self.scale("all", self.width/2, self.height/2, 1/0.995, 1/0.995)
        except Exception:
            pass
        if self.command:
            self.command()

    def _on_hover(self, event):
        self.config(cursor="hand2")

    def _on_leave(self, event):
        self.config(cursor="")


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
        
        # --- CARGAR IMAGEN DE "VOLVER" ---
        self.back_icon = None
        img_path = os.path.join("imgs", "red-go-back-arrow.png")
        if os.path.exists(img_path):
            try:
                original_image = tk.PhotoImage(file=img_path)
                orig_height = original_image.height()
                target_height = HEADER_HEIGHT - 10 
                if orig_height > 0:
                    zoomed = original_image.zoom(target_height)
                    self.back_icon = zoomed.subsample(orig_height)
                else:
                    self.back_icon = original_image
            except Exception as e:
                print(f"Error imagen: {e}")

        # --- CARGAR IMAGEN DE PERFIL ---
        self.profile_icon = None
        profile_path = os.path.join("imgs", "profile.png")
        if os.path.exists(profile_path):
            try:
                pimg = tk.PhotoImage(file=profile_path)
                pw = pimg.width()
                ph = pimg.height()
                target = 48
                # scale down by integer factor if image is larger than target
                if pw > target and ph > target:
                    factor_w = max(1, int(pw/target))
                    factor_h = max(1, int(ph/target))
                    factor = max(factor_w, factor_h)
                    pimg = pimg.subsample(factor, factor)
                self.profile_icon = pimg
            except Exception as e:
                print(f"Error cargando profile.png: {e}")

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
        if self.back_icon:
            btn = tk.Button(parent, image=self.back_icon, command=command,
                            bg=bg_color, activebackground=bg_color,
                            bd=0, highlightthickness=0, relief="flat", cursor="hand2")
        else:
            btn = RoundedButton(parent, text="VOLVER", width=100, height=40,
                                color=COLOR_BOTON_ROJO, bg_color=bg_color, command=command)
        return btn

    def add_header_with_back(self, title_text, back_cmd, bg_color=COLOR_FONDO, text_color=COLOR_TEXTO_LBL):
        header_frame = tk.Frame(self.current_screen, bg=bg_color, height=HEADER_HEIGHT)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        
        btn_back = self.create_back_button(header_frame, back_cmd, bg_color)
        btn_back.pack(side=tk.RIGHT, anchor="center", padx=10) 
        
        tk.Label(header_frame, text=title_text, font=("Arial", 22, "bold"), 
                 bg=bg_color, fg=text_color).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # ... (show_main_menu y show_user_menu quedan IGUAL) ...
    def show_main_menu(self):
        self.clear_screen()

        # Top banner with title and subtitle
        banner_h = 100
        banner = tk.Canvas(self.current_screen, height=banner_h, bg=COLOR_FONDO, highlightthickness=0)
        banner.pack(fill=tk.X, side=tk.TOP, pady=(20,10))
        bw = 760
        bx = 20
        by = 10
        br = 40
        # Draw rounded dark panel
        banner.create_arc((bx, by, bx+2*br, by+2*br), start=90, extent=90, fill="#0f2940", outline="#0f2940")
        banner.create_arc((bx+bw-2*br, by, bx+bw, by+2*br), start=0, extent=90, fill="#0f2940", outline="#0f2940")
        banner.create_arc((bx+bw-2*br, by+banner_h-2*br, bx+bw, by+banner_h), start=270, extent=90, fill="#0f2940", outline="#0f2940")
        banner.create_arc((bx, by+banner_h-2*br, bx+2*br, by+banner_h), start=180, extent=90, fill="#0f2940", outline="#0f2940")
        banner.create_rectangle((bx+br, by, bx+bw-br, by+banner_h), fill="#0f2940", outline="#0f2940")
        banner.create_text(bx + bw/2, by + banner_h/2 - 8, text="MÉTODOS NUMÉRICOS - EL JUEGO", fill="white", font=("Arial", 22, "bold"))
        banner.create_text(bx + bw/2, by + banner_h/2 + 22, text="¡Aprende, Juega, Domina!", fill="#dfefff", font=("Arial", 12))

        # Profile icon (use image if available, otherwise fallback to canvas placeholder)
        if self.profile_icon:
            profile_btn = tk.Button(self.current_screen, image=self.profile_icon, bg=COLOR_FONDO,
                                    bd=0, relief="flat", activebackground=COLOR_FONDO,
                                    cursor="hand2", command=self.show_user_menu)
            profile_btn.place(relx=0.95, y=30, anchor="n")
        else:
            pr_x = bx + bw + 10
            profile = tk.Canvas(self.current_screen, width=56, height=56, bg=COLOR_FONDO, highlightthickness=0)
            profile.place(relx=0.95, y=30, anchor="n")
            profile.create_oval(4,4,52,52, fill="#ffffff", outline="#dddddd")
            profile.create_oval(14,12,42,40, fill="#0f2940", outline="")
            profile.bind("<Button-1>", lambda e: self.show_user_menu())
            profile.bind("<Enter>", lambda e: profile.config(cursor="hand2"))
            profile.bind("<Leave>", lambda e: profile.config(cursor=""))

        # Main buttons area
        btn_area = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        btn_area.pack(expand=True)

        # Large gradient Play button
        play = GradientRoundedButton(btn_area, text="JUGAR", width=650, height=80,
                                     colors=("#20E0D0", "#FF8C5A"), text_color="#00303a",
                                     command=self.show_chapter_menu)
        play.pack(pady=(20, 18))

        # Secondary buttons: Configuración + Salir (stacked vertically, left aligned)
        second_frame = tk.Frame(btn_area, bg=COLOR_FONDO)
        second_frame.pack(pady=10, anchor="w", padx=60)

        RoundedButton(second_frame, text="  CONFIGURACIÓN", width=360, height=58,
                      color="#103d56", text_color="#dfefff",
                      command=lambda: messagebox.showinfo("Configuración", "Ajustes no implementados aún")).pack(pady=10)

        RoundedButton(second_frame, text="  SALIR", width=200, height=48,
                      color=COLOR_BOTON_ROJO, text_color="#ffffff",
                      command=self.root.quit).pack(pady=8)

    def show_user_menu(self):
        self.clear_screen()
        self.add_header_with_back(f"PERFIL DE: {self.username}", self.show_main_menu)
        tk.Label(self.current_screen, text=f"TIEMPO: {self.time_elapsed}", bg=COLOR_FONDO, fg="white", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.current_screen, text=f"ERRORES: {self.errors_committed}", bg=COLOR_FONDO, fg="white", font=("Arial", 14)).pack(pady=5)
        tk.Label(self.current_screen, text="MEDALLAS:", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg="white").pack(pady=20)
        for m in self.medals: tk.Label(self.current_screen, text=f"🏅 {m}", bg=COLOR_FONDO, fg="white").pack()

    def show_chapter_menu(self):
        self.clear_screen()
        self.add_header_with_back("LECCIONES", self.show_main_menu)
        
        scroll_container = ScrollableFrame(self.current_screen, bg_color=COLOR_FONDO)
        scroll_container.pack(fill="both", expand=True, pady=10)

        for chapter_name in GAME_STRUCTURE.keys():
            btn = RoundedButton(scroll_container.scrollable_frame, 
                                text=chapter_name, width=None, height=55,
                                color=COLOR_BOTON_CLARO, outline_color=COLOR_BORDE_OSCURO, border_width=3,
                                command=lambda c=chapter_name: self.show_level_menu(c))
            btn.pack(pady=8)
            
    def show_level_menu(self, chapter_name):
        self.clear_screen()
        self.add_header_with_back(chapter_name, self.show_chapter_menu)
        
        scroll_container = ScrollableFrame(self.current_screen, bg_color=COLOR_FONDO)
        scroll_container.pack(fill="both", expand=True, pady=10)

        levels = GAME_STRUCTURE[chapter_name]['levels']
        for level_name in levels.keys():
            # AQUI CAMBIA: En lugar de start_lesson, vamos a show_difficulty_menu
            btn = RoundedButton(scroll_container.scrollable_frame, 
                                text=level_name, width=None, height=55,
                                color=COLOR_BOTON_CLARO, outline_color=COLOR_BORDE_OSCURO, border_width=3,
                                command=lambda l=level_name: self.show_difficulty_menu(chapter_name, l))
            btn.pack(pady=8)

    # --- NUEVA FUNCIÓN: MENÚ DE DIFICULTAD (Estilo Imagen Adjunta) ---
    def show_difficulty_menu(self, chapter, level):
        self.clear_screen()
        
        # Header con botón volver al menú de niveles
        self.add_header_with_back(level, lambda: self.show_level_menu(chapter))
        
        # Contenedor centrado
        container = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        container.pack(expand=True)

        # Botón FÁCIL (Verde/Cyan)
        RoundedButton(container, text="Fácil   ☆", width=300, height=60,
                      color=BTN_EASY_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Fácil", 0)).pack(pady=15)

        # Botón INTERMEDIO (Naranja)
        RoundedButton(container, text="Intermedio   ☆☆", width=300, height=60,
                      color=BTN_INTER_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Intermedio", 0)).pack(pady=15)

        # Botón AVANZADO (Rojo/Rosa)
        RoundedButton(container, text="Avanzado   ☆☆☆", width=300, height=60,
                      color=BTN_ADV_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Avanzado", 0)).pack(pady=15)

        # Botón PRUEBA FINAL (Violeta)
        RoundedButton(container, text="Prueba Final   🏆", width=300, height=60,
                      color=BTN_FINAL_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Prueba Final", 0)).pack(pady=15)


    # --- MODIFICADO: AHORA ACEPTA EL PARÁMETRO 'difficulty' ---
    def start_lesson(self, chapter, level, difficulty, lesson_index):
        self.clear_screen()
        
        # Acceder al diccionario anidado: Capitulo -> Nivel -> Dificultad
        try:
            lessons = GAME_STRUCTURE[chapter]['levels'][level][difficulty]
        except KeyError:
            messagebox.showinfo("Aviso", "Este nivel de dificultad aún no tiene contenido.")
            self.show_difficulty_menu(chapter, level)
            return
        
        if not lessons:
            messagebox.showinfo("Aviso", "No hay lecciones en esta sección todavía.")
            self.show_difficulty_menu(chapter, level)
            return

        if lesson_index >= len(lessons):
            messagebox.showinfo("¡Felicidades!", f"¡Has completado '{level}' en modo {difficulty}!")
            # Lógica de medallas podría refinarse por dificultad
            medal_name = f"{level} ({difficulty})"
            if medal_name not in self.medals:
                self.medals.append(medal_name)
            self.show_difficulty_menu(chapter, level)
            return

        current_lesson = lessons[lesson_index]
        lesson_type = current_lesson['type']
        
        # Configurar colores de franja
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
            
        strip_frame = tk.Frame(self.current_screen, bg=strip_color, padx=0, height=HEADER_HEIGHT)
        strip_frame.pack(fill=tk.X, side=tk.TOP)
        strip_frame.pack_propagate(False)

        # Botón volver al menú de DIFICULTAD
        btn_back = self.create_back_button(strip_frame, 
                                           command=lambda: self.show_difficulty_menu(chapter, level),
                                           bg_color=strip_color)
        btn_back.pack(side=tk.RIGHT, anchor="center", padx=10)

        tk.Label(strip_frame, 
                 text=f"{difficulty} - Lección {lesson_index + 1}", 
                 font=("Arial", 20, "bold"), 
                 bg=strip_color, 
                 fg=title_fg_color).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Pasar 'difficulty' a las funciones de renderizado para mantener el contexto al avanzar
        if lesson_type == 'explicativa':
            self.show_explicativa(current_lesson, chapter, level, difficulty, lesson_index)
        elif lesson_type == 'practica' or lesson_type == 'examen':
            self.show_practica(current_lesson, chapter, level, difficulty, lesson_index)
            
    def show_explicativa(self, lesson, chapter, level, difficulty, lesson_index):
        lbl_content = tk.Label(self.current_screen, text=lesson['content'], 
                               wraplength=700, justify=tk.LEFT, 
                               font=("Arial", 12), bg=COLOR_FONDO, fg="white")
        lbl_content.pack(pady=20, padx=40)
        
        RoundedButton(self.current_screen, text="CONTINUAR", width=200, height=50,
                      command=lambda: self.start_lesson(chapter, level, difficulty, lesson_index + 1)).pack(pady=10)

    def show_practica(self, lesson, chapter, level, difficulty, lesson_index):
        tk.Label(self.current_screen, text=f"Pregunta: {lesson['content']}", 
                 wraplength=700, font=("Arial", 14), bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack(pady=20, padx=40)
        
        options_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        options_frame.pack(pady=10)

        if 'options' in lesson:
            for option in lesson['options']:
                btn = RoundedButton(options_frame, text=option, width=None, height=50,
                                    color=COLOR_BOTON_CLARO, outline_color=COLOR_BORDE_OSCURO, border_width=2,
                                    command=lambda o=option: self.check_answer(o, lesson, chapter, level, difficulty, lesson_index))
                btn.pack(pady=5)
                
        elif 'problem_id' in lesson:
            tk.Label(self.current_screen, text=f"(Mostrando problema: {lesson['problem_id']})", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack(pady=10)
            tk.Label(self.current_screen, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack()
            entry = tk.Entry(self.current_screen, font=("Arial", 12))
            entry.pack(pady=10)
            RoundedButton(self.current_screen, text="REVISAR", width=200, height=50,
                      command=lambda: messagebox.showinfo("WIP", "Lógica de revisión no implementada")).pack(pady=20)

    def check_answer(self, user_answer, lesson, chapter, level, difficulty, lesson_index):
        correct_answer = lesson['answer']
        lesson_type = lesson['type']
        
        if user_answer == correct_answer:
            messagebox.showinfo("¡Correcto!", "¡Muy bien!")
            self.start_lesson(chapter, level, difficulty, lesson_index + 1)
        else:
            self.errors_committed += 1
            if lesson_type == 'practica':
                messagebox.showerror("Incorrecto", f"Respuesta correcta: '{correct_answer}'.")
                # En práctica, a veces se retrocede o se repite. Aquí simplemente retrocedemos uno.
                self.start_lesson(chapter, level, difficulty, max(0, lesson_index - 1))
            elif lesson_type == 'examen':
                messagebox.showerror("Incorrecto", "Fallo crítico. Reiniciando sección.")
                self.start_lesson(chapter, level, difficulty, 0)