import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
import os
import json
from game_data import GAME_STRUCTURE
import methods_engine as me 
from music_manager import MusicManager
try:
    from PIL import Image, ImageDraw, ImageTk
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False

def create_rounded_rect_image(width, height, radius, color1, color2=None):
    """Create a rounded rectangle PIL Image with optional horizontal gradient.
    Returns a PIL Image.
    """
    if not PIL_AVAILABLE:
        return None
    img = Image.new("RGBA", (max(2, int(width)), max(2, int(height))), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if color2 is None:
        # solid fill
        draw.rounded_rectangle([(0, 0), (img.width, img.height)], radius=radius, fill=color1)
    else:
        # horizontal gradient between color1 and color2
        r1, g1, b1 = tuple(int(color1.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        r2, g2, b2 = tuple(int(color2.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        for x in range(img.width):
            t = x / max(1, img.width - 1)
            ri = int(r1 + (r2 - r1) * t)
            gi = int(g1 + (g2 - g1) * t)
            bi = int(b1 + (b2 - b1) * t)
            draw.line([(x, 0), (x, img.height)], fill=(ri, gi, bi))
        # mask to rounded rect
        mask = Image.new("L", (img.width, img.height), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.rounded_rectangle([(0, 0), (img.width, img.height)], radius=radius, fill=255)
        img.putalpha(mask)

    return img

# --- COLORES GENERALES ---
COLOR_FONDO = "#001F3F"
COLOR_BOTON = "#40E0D0"
COLOR_TEXTO_BTN = "#FFFFFF" # Texto blanco para resaltar en botones oscuros/vibrantes
COLOR_TEXTO_LBL = "#FFFFFF"
COLOR_BOTON_CLARO = "#1F8686"
COLOR_BORDE_OSCURO = "#008080"
COLOR_BOTON_ROJO = "#FF6B6B"

# --- COLORES DE DIFICULTAD (Basados en tu imagen) ---
# Colores para botones de dificultad
BTN_EASY_COLOR = "#00e676"      # Fácil: gradiente de #00e676 a #24a7d3
BTN_INTER_COLOR = "#f8cf39"     # Intermedio: gradiente de #f8cf39 a #f67345
BTN_ADV_COLOR = "#f94255"       # Avanzado: gradiente de #f94255 a #b3319e
BTN_FINAL_COLOR = "#ac35e4"     # Prueba Final: color sólido

# --- COLORES DE FRANJAS ---
COLOR_STRIP_EXPL = "#FFD700"
COLOR_STRIP_PRAC = "#FF8C00"
COLOR_STRIP_EXAM = "#FF4500"

# --- RESOLUCIÓN Y ESCALADO ---
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
SCALE_FACTOR = 1.5  # Factor de escala global para toda la interfaz

HEADER_HEIGHT = int(70 * SCALE_FACTOR)

# --- FUNCIÓN AUXILIAR PARA ESCALAR ---
def scale_value(value):
    """Escala un valor numérico según SCALE_FACTOR"""
    return int(value * SCALE_FACTOR)

def scale_font(size):
    """Escala tamaño de fuente según SCALE_FACTOR"""
    return max(8, int(size * SCALE_FACTOR))

# ... (Mantén tu clase RoundedButton y ScrollableFrame EXACTAMENTE IGUAL que antes) ...
# ... (Copia aquí las clases RoundedButton y ScrollableFrame de tu código anterior) ...

class RoundedButton(tk.Canvas):
    # PEGA AQUÍ TU CLASE RoundedButton ORIGINAL
    def __init__(self, parent, text, command, width=None, height=60, corner_radius=20, 
                 color=COLOR_BOTON, text_color=COLOR_TEXTO_BTN, bg_color=COLOR_FONDO,
                 outline_color=None, border_width=0, icon_image=None, icon_padding=14):
        
        # Escalar dimensiones
        height = scale_value(height)
        corner_radius = scale_value(corner_radius)
        icon_padding = scale_value(icon_padding)
        
        if width is None:
            font = tkfont.Font(family="Arial", size=scale_font(14), weight="bold")
            text_width = font.measure(text)
            width = text_width + 60
        else:
            width = scale_value(width)

        tk.Canvas.__init__(self, parent, borderwidth=0, 
                           relief="flat", highlightthickness=0, bg=bg_color)
        self.command = command
        self.text = text
        self.color = color
        self.text_color = text_color
        self.width = width
        self.height = height
        self.corner_radius = corner_radius
        self.icon_image = icon_image
        self.icon_padding = icon_padding
        self.dynamic = width is None
        self.outline_color = outline_color if outline_color else color
        self.border_width = border_width

        self.configure(width=width, height=height)
        self.draw_button()
        # If width is dynamic (None), bind parent resize to update width
        try:
            if self.dynamic and hasattr(parent, 'bind'):
                parent.bind('<Configure>', self._on_parent_config)
        except Exception:
            pass
        
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
        
        # If there's an icon, draw it to the left and shift text
        text_x = w/2
        if self.icon_image:
            try:
                # keep a reference so image is not garbage collected
                self._icon_ref = self.icon_image
                icon_x = x0 + self.icon_padding
                self.create_image(icon_x, h/2, image=self._icon_ref, anchor='w', tags="btn")
                text_x = (x0 + x1) / 2 + self.icon_padding/2
            except Exception:
                pass

        self.create_text(text_x, h/2, text=self.text, fill=self.text_color, font=("Arial", scale_font(14), "bold"), tags="btn")

    def _on_press(self, event): self.move("btn", 1, 1)
    def _on_release(self, event): 
        self.move("btn", -1, -1)
        if self.command: self.command()
    def _on_hover(self, event): self.config(cursor="hand2")
    def _on_leave(self, event): self.config(cursor="")

    def _on_parent_config(self, event):
        # Adjust width to be a fraction of parent width when dynamic
        try:
            pw = event.width
            new_w = max(120, int(pw * 0.45))
            if new_w != self.width:
                self.width = new_w
                self.configure(width=self.width)
                self.draw_button()
        except Exception:
            pass

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
        
        # Escalar dimensiones
        width = scale_value(width)
        height = scale_value(height)
        corner_radius = scale_value(corner_radius)
        
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

        # allow dynamic width if width is None
        self.dynamic = width is None
        try:
            if self.dynamic and hasattr(parent, 'bind'):
                parent.bind('<Configure>', self._on_parent_config)
        except Exception:
            pass

        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self._on_hover)
        self.bind("<Leave>", self._on_leave)

    def draw_button(self):
        self.delete("all")
        r = self.corner_radius
        w = self.width
        h = self.height

        # If Pillow is available, generate a rounded-rect gradient image and use it.
        if PIL_AVAILABLE:
            try:
                # create an RGBA image with horizontal gradient
                img = Image.new("RGBA", (max(2, int(w)), max(2, int(h))), (0, 0, 0, 0))
                draw = ImageDraw.Draw(img)
                # horizontal gradient
                r1, g1, b1 = self._hex_to_rgb(self.colors[0])
                r2, g2, b2 = self._hex_to_rgb(self.colors[-1])
                for x in range(img.width):
                    t = x / max(1, img.width - 1)
                    ri = int(r1 + (r2 - r1) * t)
                    gi = int(g1 + (g2 - g1) * t)
                    bi = int(b1 + (b2 - b1) * t)
                    draw.line([(x, 0), (x, img.height)], fill=(ri, gi, bi))

                # mask for rounded rectangle
                mask = Image.new("L", (img.width, img.height), 0)
                mdraw = ImageDraw.Draw(mask)
                # rounded rectangle (full pill)
                mdraw.rounded_rectangle([(0, 0), (img.width, img.height)], radius=r, fill=255)
                img.putalpha(mask)

                # convert to Tk image and display
                tkimg = ImageTk.PhotoImage(img)
                # keep reference
                self._tkimg = tkimg
                self.create_image(0, 0, anchor="nw", image=self._tkimg)
            except Exception:
                # fallback to simple canvas drawing below
                pass
        # If Pillow not available or fallback, use canvas drawing (existing method)
        if not PIL_AVAILABLE or not hasattr(self, '_tkimg'):
            # Draw gradient only in the central band (between the rounded corners)
            central_width = max(0, w - 2 * r)
            steps = max(2, int(central_width / 2))
            r1, g1, b1 = self._hex_to_rgb(self.colors[0])
            r2, g2, b2 = self._hex_to_rgb(self.colors[-1])
            for i in range(steps):
                t = i / (steps - 1)
                ri = int(r1 + (r2 - r1) * t)
                gi = int(g1 + (g2 - g1) * t)
                bi = int(b1 + (b2 - b1) * t)
                col = f"#{ri:02x}{gi:02x}{bi:02x}"
                x0 = r + i * (central_width / steps)
                x1 = r + (i + 1) * (central_width / steps)
                self.create_rectangle(x0, 0, x1, h, fill=col, width=0)

            # Draw rounded corner arcs to create pill shape (use end colors so corners blend)
            self.create_arc((0, 0, 2*r, 2*r), start=90, extent=90, fill=self.colors[0], outline=self.colors[0])
            self.create_arc((w-2*r, 0, w, 2*r), start=0, extent=90, fill=self.colors[-1], outline=self.colors[-1])
            self.create_arc((w-2*r, h-2*r, w, h), start=270, extent=90, fill=self.colors[-1], outline=self.colors[-1])
            self.create_arc((0, h-2*r, 2*r, h), start=180, extent=90, fill=self.colors[0], outline=self.colors[0])

        # Play icon (triangle) on left
        tri_size = int(h * 0.34)
        cx = r
        cy = h / 2
        self.create_polygon(cx - tri_size/2, cy - tri_size/1.2,
                            cx - tri_size/2, cy + tri_size/1.2,
                            cx + tri_size/1.2, cy,
                            fill=self.text_color, outline="")

        # Text centered
        self.create_text(w/2, h/2, text=self.text, fill=self.text_color,
                 font=("Arial", scale_font(18), "bold"))

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

    def _on_parent_config(self, event):
        try:
            pw = event.width
            new_w = max(200, int(pw * 0.7))
            if new_w != self.width:
                self.width = new_w
                self.configure(width=self.width)
                self.draw_button()
        except Exception:
            pass


class NumericalMethodsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Métodos Numéricos - El Juego") 
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)  # No permitir redimensionar
        self.root.configure(bg=COLOR_FONDO)
        
        # Centrar la ventana en la pantalla
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
        
        self.username = "Jugador 1"
        self.errors_committed = 0
        self.time_elapsed_seconds = 0  # Contador en segundos
        self.medals = []
        
        # Posición del scroll en el menú de lecciones
        self.chapter_menu_scroll_position = 0
        
        # Archivo de guardado
        self.save_file = "game_progress.json"
        
        # Estado de sonido
        self.music_enabled = True
        self.music_volume = 0.7
        
        # Cargar datos guardados
        self._load_progress()
        
        # Iniciar temporizador
        self._start_timer()
        
        # --- INICIALIZAR GESTOR DE MÚSICA ---
        self.music_manager = MusicManager(songs_folder="songs")
        if not self.music_enabled:
            self.music_manager.set_volume(0.0)
        else:
            self.music_manager.set_volume(self.music_volume)
        
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

        # --- CARGAR ICONOS PARA BOTONES ---
        self.icon_config = None
        self.icon_exit = None
        icon_config_path = os.path.join("imgs", "iconoconfig.png")
        icon_exit_path = os.path.join("imgs", "iconosalir.png")
        try:
            if os.path.exists(icon_config_path):
                ic = tk.PhotoImage(file=icon_config_path)
                # scale to ~48 px if larger
                if ic.width() > 72:
                    ic = ic.subsample(max(1, int(ic.width()/48)))
                self.icon_config = ic
            if os.path.exists(icon_exit_path):
                ie = tk.PhotoImage(file=icon_exit_path)
                if ie.width() > 72:
                    ie = ie.subsample(max(1, int(ie.width()/48)))
                self.icon_exit = ie
        except Exception as e:
            print(f"Error cargando iconos: {e}")

        self.main_frame = tk.Frame(root, bg=COLOR_FONDO)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.current_screen = None
        
        # Guardar progreso al cerrar la aplicación
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        
        self.show_main_menu()

    def _on_closing(self):
        """Guarda el progreso cuando se cierra la aplicación"""
        self._save_progress()
        self.root.destroy()

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
        
        tk.Label(header_frame, text=title_text, font=("Arial", scale_font(22), "bold"), 
                 bg=bg_color, fg=text_color).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # ... (show_main_menu y show_user_menu quedan IGUAL) ...
    def show_main_menu(self):
        self.clear_screen()
        
        # Iniciar la música (solo si no está ya reproduciendo)
        try:
            if not hasattr(self, 'music_started'):
                if self.music_enabled:
                    self.music_manager.play()
                self.music_started = True
        except Exception as e:
            print(f"Error iniciando música: {e}")

        # Top banner with title and subtitle (use PIL-generated rounded image for pixel-perfect corners)
        banner_h = 100
        banner = tk.Canvas(self.current_screen, height=banner_h, bg=COLOR_FONDO, highlightthickness=0)
        banner.pack(fill=tk.X, side=tk.TOP, pady=(20,10))

        def _draw_banner(event=None):
            bw = max(200, banner.winfo_width() - 40)
            bx = 20
            by = 10
            br = 30
            # generate rounded image
            if PIL_AVAILABLE:
                img = create_rounded_rect_image(bw, banner_h, br, "#0f2940")
                try:
                    tkimg = ImageTk.PhotoImage(img)
                    banner.delete("all")
                    banner._img_ref = tkimg
                    banner.create_image(bx, by, anchor="nw", image=tkimg)
                except Exception:
                    banner.delete("all")
                    banner.create_rectangle(bx, by, bx + bw, by + banner_h, fill="#0f2940", outline="")
            else:
                banner.delete("all")
                banner.create_rectangle(bx, by, bx + bw, by + banner_h, fill="#0f2940", outline="")

            # title text centered on the banner area
            banner.create_text(bx + bw/2, by + banner_h/2 - 8, text="MÉTODOS NUMÉRICOS - EL JUEGO", fill="white", font=("Arial", scale_font(22), "bold"))
            banner.create_text(bx + bw/2, by + banner_h/2 + 22, text="¡Aprende, Juega, Domina!", fill="#dfefff", font=("Arial", scale_font(12)))

        banner.bind('<Configure>', _draw_banner)
        # initial draw
        banner.after(10, _draw_banner)

        # Profile icon (use image if available, otherwise fallback to canvas placeholder)
        if self.profile_icon:
            profile_btn = tk.Button(self.current_screen, image=self.profile_icon, bg=COLOR_FONDO,
                                    bd=0, relief="flat", activebackground=COLOR_FONDO,
                                    cursor="hand2", command=self.show_user_menu)
            profile_btn.place(relx=0.95, y=30, anchor="n")
        else:
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
        play = GradientRoundedButton(btn_area, text="JUGAR", width=570, height=105,
                                     colors=("#20E0D0", "#FF8C5A"), text_color="#00303a",
                                     command=self.show_chapter_menu)
        play.pack(pady=(30, 22))

        # Secondary buttons: Configuración + Salir (stacked vertically and centered)
        second_frame = tk.Frame(btn_area, bg=COLOR_FONDO)
        second_frame.pack(pady=15)

        RoundedButton(second_frame, text="CONFIGURACIÓN", width=570, height=105,
                  color="#103d56", text_color="#dfefff",
                  icon_image=self.icon_config,
                  command=self.show_config_menu).pack(pady=22)

        RoundedButton(second_frame, text="SALIR", width=570, height=105,
                  color=COLOR_BOTON_ROJO, text_color="#ffffff",
                  icon_image=self.icon_exit,
                  command=self.root.quit).pack(pady=22)

    def show_user_menu(self):
        self.clear_screen()
        # Add gradient blue header banner (full width, no rounded corners)
        header_frame = tk.Frame(self.current_screen, bg="#0052CC", height=HEADER_HEIGHT)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        
        # Title
        tk.Label(header_frame, text="MENÚ DE USUARIO", font=("Arial", scale_font(20), "bold"), 
                 bg="#0052CC", fg="white").pack(side=tk.LEFT, padx=20, pady=15)
        
        # Back button with icon
        btn_back = self.create_back_button(header_frame, self.show_main_menu, "#0052CC")
        btn_back.pack(side=tk.RIGHT, anchor="center", padx=10)

        # Main content area
        content = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Two columns: Time (cyan) and Errors (orange-red)
        row_frame = tk.Frame(content, bg=COLOR_FONDO)
        row_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        row_frame.columnconfigure(0, weight=1)
        row_frame.columnconfigure(1, weight=1)

        # TIME card (cyan-to-blue gradient)
        time_canvas = tk.Canvas(row_frame, height=scale_value(120), bg=COLOR_FONDO, highlightthickness=0)
        time_canvas.grid(row=0, column=0, padx=10, sticky="nsew")
        if PIL_AVAILABLE:
            img_time = create_rounded_rect_image(time_canvas.winfo_width() or 150, scale_value(120), 15, "#20D0C0", "#00A8CC")
            try:
                tkimg_time = ImageTk.PhotoImage(img_time)
                time_canvas._img_time = tkimg_time
                time_canvas.create_image(0, 0, anchor="nw", image=tkimg_time)
            except:
                time_canvas.create_rectangle(0, 0, 200, 120, fill="#20D0C0")
        else:
            time_canvas.create_rectangle(0, 0, 200, 120, fill="#20D0C0")
        time_canvas.create_text(20, 35, text="⏱", font=("Arial", scale_font(24)), anchor="w", fill="white")
        time_canvas.create_text(75, 25, text="TIEMPO TRANSCURRIDO", fill="white", font=("Arial", scale_font(11), "bold"), anchor="w")
        time_text_id = time_canvas.create_text(75, 65, text=self._format_time(), fill="white", font=("Arial", scale_font(18), "bold"), anchor="w")
        
        # Actualizar tiempo cada segundo mientras se está viendo el menú y guardar progreso
        def _update_time_display():
            try:
                time_canvas.itemconfig(time_text_id, text=self._format_time())
                # Guardar progreso cada 5 segundos
                if self.time_elapsed_seconds % 5 == 0:
                    self._save_progress()
                # Programar la siguiente actualización en 1000 ms
                self.root.after(1000, _update_time_display)
            except:
                pass  # Canvas destruido, detener actualizaciones
        
        _update_time_display()

        # ERRORS card (orange-to-red gradient)
        error_canvas = tk.Canvas(row_frame, height=scale_value(120), bg=COLOR_FONDO, highlightthickness=0)
        error_canvas.grid(row=0, column=1, padx=10, sticky="nsew")
        if PIL_AVAILABLE:
            img_err = create_rounded_rect_image(error_canvas.winfo_width() or 150, scale_value(120), 15, "#FF8C42", "#E63946")
            try:
                tkimg_err = ImageTk.PhotoImage(img_err)
                error_canvas._img_err = tkimg_err
                error_canvas.create_image(0, 0, anchor="nw", image=tkimg_err)
            except:
                error_canvas.create_rectangle(0, 0, 200, 120, fill="#FF8C42")
        else:
            error_canvas.create_rectangle(0, 0, 200, 120, fill="#FF8C42")
        error_canvas.create_text(20, 35, text="✕", font=("Arial", scale_font(24)), anchor="w", fill="white")
        error_canvas.create_text(75, 25, text="ERRORES COMETIDOS", fill="white", font=("Arial", scale_font(11), "bold"), anchor="w")
        error_canvas.create_text(75, 65, text=str(self.errors_committed), fill="white", font=("Arial", scale_font(18), "bold"), anchor="w")

        # Medals section
        medals_label = tk.Label(content, text="MEDALLAS:", font=("Arial", scale_font(16), "bold"), bg=COLOR_FONDO, fg="white")
        medals_label.pack(pady=(20, 10), anchor="w")
        
        # Medals display (scrollable if needed)
        medals_frame = tk.Frame(content, bg=COLOR_FONDO)
        medals_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        if self.medals:
            medals_text = "\n".join([f"🏅 {m}" for m in self.medals])
        else:
            medals_text = "Sin medallas aún"
        
        tk.Label(medals_frame, text=medals_text, font=("Arial", scale_font(12)), bg=COLOR_FONDO, fg="white", justify=tk.LEFT).pack(anchor="w", padx=10)

    def show_config_menu(self):
        """Menú de configuración con opciones de sonido, idioma, créditos y reinicio"""
        self.clear_screen()
        
        # Header azul con título
        header_frame = tk.Frame(self.current_screen, bg="#003366", height=HEADER_HEIGHT)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="CONFIGURACIÓN", font=("Arial", scale_font(20), "bold"), 
                 bg="#003366", fg="white").pack(side=tk.LEFT, padx=20, pady=15)
        
        btn_back = self.create_back_button(header_frame, self.show_main_menu, "#003366")
        btn_back.pack(side=tk.RIGHT, anchor="center", padx=10)

        # Contenido principal - centrado
        content = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        content.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Contenedor interno para centrar los botones
        buttons_container = tk.Frame(content, bg=COLOR_FONDO)
        buttons_container.pack(expand=True, anchor="center")

        # Botones de configuración con gradientes
        # SONIDO - Gradiente cyan a verde
        def _toggle_music():
            self.music_enabled = not self.music_enabled
            if self.music_enabled:
                self.music_manager.set_volume(self.music_volume)
                self.music_manager.play()
                status_msg = "Música activada ✓"
            else:
                self.music_manager.set_volume(0.0)
                status_msg = "Música desactivada ✗"
            messagebox.showinfo("Sonido", status_msg)
            self._save_progress()
            self.show_config_menu()
        
        music_action = "Ensordecer" if self.music_enabled else "Desensordecer"
        music_status = "🔊" if self.music_enabled else "🔇"
        RoundedButton(buttons_container, text=f"{music_status}  {music_action}", width=380, height=105,
                  color="#20D0C0", text_color="#ffffff",
                  command=_toggle_music).pack(pady=22)

        # IDIOMA - Gradiente cyan a naranja
        btn_idioma = tk.Canvas(buttons_container, width=750, height=105, bg=COLOR_FONDO, highlightthickness=0)
        btn_idioma.pack(pady=22)
        
        if PIL_AVAILABLE:
            img_idioma = create_rounded_rect_image(750, 105, 30, "#20D0C0", "#FF8C5A")
            if img_idioma:
                tkimg_idioma = ImageTk.PhotoImage(img_idioma)
                btn_idioma._img = tkimg_idioma
                btn_idioma.create_image(0, 0, anchor="nw", image=tkimg_idioma)
        
        btn_idioma.create_text(375, 52, text="🌐  IDIOMA", fill="white", font=("Arial", scale_font(24), "bold"), anchor="c")
        btn_idioma.bind("<Button-1>", lambda e: messagebox.showinfo("Idioma", "Funcionalidad próximamente"))
        btn_idioma.bind("<Enter>", lambda e: btn_idioma.config(cursor="hand2"))
        btn_idioma.bind("<Leave>", lambda e: btn_idioma.config(cursor=""))

        # CRÉDITOS - Gradiente cyan a naranja
        btn_creditos = tk.Canvas(buttons_container, width=750, height=105, bg=COLOR_FONDO, highlightthickness=0)
        btn_creditos.pack(pady=22)
        
        if PIL_AVAILABLE:
            img_creditos = create_rounded_rect_image(750, 105, 30, "#20D0C0", "#FF8C5A")
            if img_creditos:
                tkimg_creditos = ImageTk.PhotoImage(img_creditos)
                btn_creditos._img = tkimg_creditos
                btn_creditos.create_image(0, 0, anchor="nw", image=tkimg_creditos)
        
        btn_creditos.create_text(375, 52, text="ℹ️  CRÉDITOS", fill="white", font=("Arial", scale_font(24), "bold"), anchor="c")
        
        credits_text = """Juego de Métodos Numéricos

EQUIPO 1:
• Jorge Aaron Cuellar Fuentes
  (2007916)
• Gerardo Ulloa Loredo
  (2001913)
"""
        
        btn_creditos.bind("<Button-1>", lambda e: messagebox.showinfo("Créditos", credits_text))
        btn_creditos.bind("<Enter>", lambda e: btn_creditos.config(cursor="hand2"))
        btn_creditos.bind("<Leave>", lambda e: btn_creditos.config(cursor=""))

        # BIBLIOGRAFÍA - Gradiente cyan a naranja
        btn_bibliografia = tk.Canvas(buttons_container, width=750, height=105, bg=COLOR_FONDO, highlightthickness=0)
        btn_bibliografia.pack(pady=22)
        
        if PIL_AVAILABLE:
            img_bibliografia = create_rounded_rect_image(750, 105, 30, "#20D0C0", "#FF8C5A")
            if img_bibliografia:
                tkimg_bibliografia = ImageTk.PhotoImage(img_bibliografia)
                btn_bibliografia._img = tkimg_bibliografia
                btn_bibliografia.create_image(0, 0, anchor="nw", image=tkimg_bibliografia)
        
        btn_bibliografia.create_text(375, 52, text="📚  BIBLIOGRAFÍA", fill="white", font=("Arial", scale_font(24), "bold"), anchor="c")
        
        bibliography_text = """Referencias Bibliográficas

Zamora Pequeño, O., Zamora Pequeño, R. S., & Del Ángel Ramírez, A. (2020). Métodos numéricos (2.ª ed.). Universidad Autónoma de Nuevo León."""
        
        btn_bibliografia.bind("<Button-1>", lambda e: messagebox.showinfo("Bibliografía", bibliography_text))
        btn_bibliografia.bind("<Enter>", lambda e: btn_bibliografia.config(cursor="hand2"))
        btn_bibliografia.bind("<Leave>", lambda e: btn_bibliografia.config(cursor=""))

        # REINICIAR PROGRESO - Gradiente rojo a púrpura
        btn_reset = tk.Canvas(buttons_container, width=750, height=105, bg=COLOR_FONDO, highlightthickness=0)
        btn_reset.pack(pady=22)
        
        if PIL_AVAILABLE:
            img_reset = create_rounded_rect_image(750, 105, 30, "#FF3333", "#D500F9")
            if img_reset:
                tkimg_reset = ImageTk.PhotoImage(img_reset)
                btn_reset._img = tkimg_reset
                btn_reset.create_image(0, 0, anchor="nw", image=tkimg_reset)
        
        def _on_reset_click(event):
            response = messagebox.askyesno("Reiniciar Progreso", 
                                          "¿Estás seguro de que deseas reiniciar tu progreso?\nEsta acción no se puede deshacer.")
            if response:
                self._reset_progress()
        
        btn_reset.create_text(375, 52, text="⚠️  REINICIAR PROGRESO", fill="white", font=("Arial", scale_font(24), "bold"), anchor="c")
        btn_reset.bind("<Button-1>", _on_reset_click)
        btn_reset.bind("<Enter>", lambda e: btn_reset.config(cursor="hand2"))
        btn_reset.bind("<Leave>", lambda e: btn_reset.config(cursor=""))

    def show_chapter_menu(self):
        """Menú unificado de capítulos y niveles con diseño desplegable"""
        self.clear_screen()
        self.add_header_with_back("LECCIONES", self.show_main_menu)
        
        scroll_container = ScrollableFrame(self.current_screen, bg_color=COLOR_FONDO)
        scroll_container.pack(fill="both", expand=True, pady=20, padx=15)

        for chapter_name in GAME_STRUCTURE.keys():
            # Marco del capítulo
            chapter_frame = tk.Frame(scroll_container.scrollable_frame, bg=COLOR_FONDO)
            chapter_frame.pack(fill=tk.X, pady=15)

            # Título del capítulo (azul como en la imagen)
            chapter_title_canvas = tk.Canvas(chapter_frame, height=50, bg=COLOR_FONDO, highlightthickness=0)
            chapter_title_canvas.pack(fill=tk.X, pady=(0, 10))
            
            if PIL_AVAILABLE:
                img_title = create_rounded_rect_image(600, 50, 12, "#0047AB", "#0047AB")
                if img_title:
                    tkimg_title = ImageTk.PhotoImage(img_title)
                    chapter_title_canvas._img = tkimg_title
                    chapter_title_canvas.create_image(0, 0, anchor="nw", image=tkimg_title)
            
            chapter_title_canvas.create_text(20, 25, text=chapter_name, fill="white", font=("Arial", scale_font(16), "bold"), anchor="w")
            chapter_title_canvas.configure(height=50, width=600)

            # Niveles dentro del capítulo
            levels = GAME_STRUCTURE[chapter_name]['levels']
            for level_name in levels.keys():
                # Marco del nivel con ícono de botón a la derecha
                level_frame = tk.Frame(chapter_frame, bg="#1a3a52", highlightthickness=0)
                level_frame.pack(fill=tk.X, pady=8, padx=10)
                
                # Contenido del nivel (texto)
                level_label = tk.Label(level_frame, text=level_name, 
                                      font=("Arial", scale_font(13), "bold"), 
                                      bg="#1a3a52", fg="white", 
                                      padx=15, pady=12, anchor="w")
                level_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
                
                # Botón con imagen a la derecha (navegación)
                def _on_level_click(event, c=chapter_name, l=level_name):
                    # Guardar posición del scroll antes de salir
                    self.chapter_menu_scroll_position = scroll_container.canvas.yview()[0]
                    self.show_difficulty_menu(c, l)
                
                try:
                    # Cargar imagen botonnivel.png
                    if PIL_AVAILABLE:
                        from PIL import Image as PILImage, ImageTk as PILImageTk
                        btn_img_pil = PILImage.open(os.path.join('imgs', 'botonnivel.png'))
                        # Redimensionar a 40x40
                        btn_img_pil.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
                        btn_img_tk = PILImageTk.PhotoImage(btn_img_pil)
                    else:
                        btn_img_tk = tk.PhotoImage(file=os.path.join('imgs', 'botonnivel.png'))
                        if btn_img_tk.width() > 40:
                            factor = max(1, int(btn_img_tk.width() / 40))
                            btn_img_tk = btn_img_tk.subsample(factor)
                    
                    level_btn = tk.Label(level_frame, image=btn_img_tk, 
                                        bg="#1a3a52", padx=15, pady=12, cursor="hand2")
                    level_btn.image = btn_img_tk  # Keep reference
                    level_btn.pack(side=tk.RIGHT)
                    level_btn.bind("<Button-1>", _on_level_click)
                    
                except Exception:
                    # Fallback: usar flecha de texto si la imagen no carga
                    level_btn = tk.Label(level_frame, text="➤", 
                                        font=("Arial", scale_font(18), "bold"), 
                                        bg="#1a3a52", fg="white", 
                                        padx=15, pady=12, cursor="hand2")
                    level_btn.pack(side=tk.RIGHT)
                    level_btn.bind("<Button-1>", _on_level_click)
                
                # Cambiar cursor y color del fondo al pasar el mouse (solo en el frame y el botón)
                def _on_enter(event, frame=level_frame):
                    frame.config(bg="#2a4a62")
                    level_label.config(bg="#2a4a62")
                    level_btn.config(bg="#2a4a62")
                
                def _on_leave(event, frame=level_frame):
                    frame.config(bg="#1a3a52")
                    level_label.config(bg="#1a3a52")
                    level_btn.config(bg="#1a3a52")
                
                level_frame.bind("<Enter>", _on_enter)
                level_frame.bind("<Leave>", _on_leave)
                level_label.bind("<Enter>", _on_enter)
                level_label.bind("<Leave>", _on_leave)
                level_btn.bind("<Enter>", _on_enter)
                level_btn.bind("<Leave>", _on_leave)
        
        # Restaurar la posición del scroll después de renderizar todo
        self.root.after(100, lambda: self._restore_scroll_position(scroll_container))
            
    def show_level_menu(self, chapter_name):
        """Este método está deprecado - Se usa show_chapter_menu en su lugar"""
        pass

    def _restore_scroll_position(self, scroll_container):
        """Restaura la posición del scroll en el menú de lecciones"""
        try:
            if self.chapter_menu_scroll_position > 0:
                # Usar yview_moveto para restaurar la posición
                scroll_container.canvas.yview_moveto(self.chapter_menu_scroll_position)
        except Exception as e:
            print(f"Error al restaurar posición del scroll: {e}")
    
    # --- NUEVA FUNCIÓN: MENÚ DE DIFICULTAD (Estilo Imagen Adjunta) ---
    def show_difficulty_menu(self, chapter, level):
        self.clear_screen()
        
        # Reanudar música con fade in cuando vuelves
        try:
            if self.music_enabled:
                self.music_manager.fade_in(duration=3.0, target_volume=self.music_volume)
        except Exception as e:
            print(f"Error en fade in de música: {e}")
        
        # Header con botón volver al menú de lecciones
        self.add_header_with_back(level, self.show_chapter_menu)
        
        # Contenedor centrado
        container = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        container.pack(expand=True)

        # Botón FÁCIL (Verde/Cyan) con estrellas pequeñas
        RoundedButton(container, text="Fácil   ★", width=300, height=60,
                      color=BTN_EASY_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Fácil", 0)).pack(pady=15)

        # Botón INTERMEDIO (Naranja) con estrellas pequeñas
        RoundedButton(container, text="Intermedio   ★★", width=300, height=60,
                      color=BTN_INTER_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Intermedio", 0)).pack(pady=15)

        # Botón AVANZADO (Rojo/Rosa) con estrellas pequeñas
        RoundedButton(container, text="Avanzado   ★★★", width=300, height=60,
                      color=BTN_ADV_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Avanzado", 0)).pack(pady=15)

        # Botón PRUEBA FINAL (Violeta)
        RoundedButton(container, text="Prueba Final   🏆", width=300, height=60,
                      color=BTN_FINAL_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Prueba Final", 0)).pack(pady=15)


    # --- MODIFICADO: AHORA ACEPTA EL PARÁMETRO 'difficulty' ---
    def start_lesson(self, chapter, level, difficulty, lesson_index):
        # --- FADE OUT DE LA MÚSICA ---
        try:
            if self.music_enabled:
                self.music_manager.fade_out(duration=5.0)
        except Exception as e:
            print(f"Error en fade out de música: {e}")
        
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
        
        # Caso especial: Lagrange Intermedio, Avanzado y Prueba Final (manejan su propio banner)
        try:
            is_lagrange_special = 'Lagrange' in level and difficulty.lower() in ['intermedio', 'avanzado', 'prueba final']
        except Exception:
            is_lagrange_special = False
        
        if is_lagrange_special:
            self.show_practica(current_lesson, chapter, level, difficulty, lesson_index)
            return
        
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
                 font=("Arial", scale_font(20), "bold"), 
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
                               font=("Arial", scale_font(12)), bg=COLOR_FONDO, fg="white")
        lbl_content.pack(pady=20, padx=40)
        
        RoundedButton(self.current_screen, text="CONTINUAR", width=200, height=50,
                      command=lambda: self.start_lesson(chapter, level, difficulty, lesson_index + 1)).pack(pady=10)

    def _show_lagrange_intermedio(self, chapter, level, difficulty, lesson_index):
        """Nivel intermedio de Lagrange con tabla de datos y problema"""
        import random
        
        # === BANNER SUPERIOR ===
        banner_frame = tk.Frame(self.current_screen, bg="#ac35e4", height=70)
        banner_frame.pack(fill=tk.X, side=tk.TOP)
        banner_frame.pack_propagate(False)
        
        banner_text = f"Capítulo 1 Nivel 1. Lagrange. {difficulty}"
        tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"), 
                bg="#FF8C42", fg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=15)
        
        # Botón de retroceso
        try:
            if PIL_AVAILABLE:
                from PIL import Image as PILImage, ImageTk as PILImageTk
                pil_img = PILImage.open(os.path.join('imgs', 'red-go-back-arrow.png'))
                pil_img.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
                back_arrow_img = PILImageTk.PhotoImage(pil_img)
            else:
                back_arrow_img = tk.PhotoImage(file=os.path.join('imgs', 'red-go-back-arrow.png'))
                if back_arrow_img.width() > 40:
                    factor = max(1, int(back_arrow_img.width() / 40))
                    back_arrow_img = back_arrow_img.subsample(factor)
            
            back_btn = tk.Label(banner_frame, image=back_arrow_img, bg="#FF8C42", cursor="hand2")
            back_btn.image = back_arrow_img
            back_btn.pack(side=tk.RIGHT, padx=20, pady=15)
            back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        except Exception:
            back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"), 
                               bg="#FF8C42", fg="#FFFFFF", cursor="hand2")
            back_btn.pack(side=tk.RIGHT, padx=20, pady=15)
            back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        
        # Contenido principal
        main_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título del problema
        tk.Label(main_frame, text="Obtener g(x)", font=("Arial", scale_font(18), "bold"), 
                bg=COLOR_FONDO, fg="#20E0D0").pack(pady=10)
        
        # Frame para tabla y x = 3
        top_content_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        top_content_frame.pack(pady=15, fill=tk.X)
        
        # Mostrar x = 3 (izquierda)
        tk.Label(top_content_frame, text="x = 3", font=("Arial", scale_font(16), "bold"), 
                bg=COLOR_FONDO, fg="white").pack(side=tk.LEFT, padx=20)
        

        # Tabla de datos (centro)
        table_frame = tk.Frame(top_content_frame, bg="white", highlightthickness=2, highlightbackground="#20E0D0")
        table_frame.pack(side=tk.LEFT, padx=20)
        
        # Encabezados
        header_x = tk.Label(table_frame, text="x", font=("Arial", scale_font(14), "bold"), 
                           bg="#20E0D0", fg="white", width=15, height=2)
        header_x.grid(row=0, column=0, sticky="nsew")
        
        header_y = tk.Label(table_frame, text="y", font=("Arial", scale_font(14), "bold"), 
                           bg="#20E0D0", fg="white", width=15, height=2)
        header_y.grid(row=0, column=1, sticky="nsew")
        
        # Datos de la tabla (mismos que en la imagen)
        data = [(1.7, 0.35), (2.4, 0.87), (3.1, 1.03)]
        
        for i, (x_val, y_val) in enumerate(data, 1):
            cell_x = tk.Label(table_frame, text=str(x_val), font=("Arial", scale_font(13)), 
                             bg="white", fg="black", width=15, height=2, relief=tk.RIDGE)
            cell_x.grid(row=i, column=0, sticky="nsew")
            
            cell_y = tk.Label(table_frame, text=str(y_val), font=("Arial", scale_font(13)), 
                             bg="white", fg="black", width=15, height=2, relief=tk.RIDGE)
            cell_y.grid(row=i, column=1, sticky="nsew")
        
        # Temporizador a la derecha
        timer_container = tk.Frame(top_content_frame, bg=COLOR_FONDO)
        timer_container.pack(side=tk.RIGHT, padx=20)
        
        tk.Label(timer_container, text="⏱", font=("Arial", scale_font(24)), 
                bg=COLOR_FONDO, fg="white").pack(pady=5)
        tk.Label(timer_container, text="Tiempo restante", font=("Arial", scale_font(12), "bold"), 
                bg=COLOR_FONDO, fg="white").pack()
        
        timer_label = tk.Label(timer_container, text="20:00", font=("Arial", scale_font(20), "bold"), 
                              bg=COLOR_FONDO, fg="#20E0D0")
        timer_label.pack(pady=5)
        
        # Temporizador de 20 minutos (1200 segundos)
        timer_state = {'seconds': 1200, 'timer_id': None}
        
        def _update_timer():
            timer_state['seconds'] -= 1
            minutes = timer_state['seconds'] // 60
            seconds = timer_state['seconds'] % 60
            time_str = f"{minutes}:{seconds:02d}"
            timer_label.config(text=time_str)
            
            if timer_state['seconds'] > 0:
                timer_state['timer_id'] = self.root.after(1000, _update_timer)
            else:
                messagebox.showinfo("Tiempo agotado", "Se acabó el tiempo para resolver el problema.")
                self.show_difficulty_menu(chapter, level)
        
        _update_timer()
        
        # Marco con opciones
        options_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        options_frame.pack(pady=30, fill=tk.BOTH, expand=True)
        
        # Etiqueta g(x) =
        tk.Label(options_frame, text="g(x) =", font=("Arial", scale_font(16), "bold"), 
                bg=COLOR_FONDO, fg="white").pack(pady=15)
        
        # Opciones con RoundedButton (como nivel fácil)
        btn_frame = tk.Frame(options_frame, bg=COLOR_FONDO)
        btn_frame.pack(pady=20)
        
        # Opciones sin revelar la correcta
        options_values = ["1.029183673", "1.019183673", "1.039183673", "1.049183673"]
        correct_answer = "1.019183673"
        
        # Randomizar el orden de las opciones
        random.shuffle(options_values)
        
        def _make_handler(option_text):
            def _handler():
                if timer_state['timer_id']:
                    self.root.after_cancel(timer_state['timer_id'])
                
                if option_text == correct_answer:
                    messagebox.showinfo("¡Correcto!", f"¡Excelente!")
                    self.start_lesson(chapter, level, difficulty, lesson_index + 1)
                else:
                    messagebox.showinfo("Incorrecto", "Lo siento, esa respuesta no es correcta.")
                    self.errors_committed += 1
                    self._save_progress()
                    self.show_difficulty_menu(chapter, level)
            return _handler
        
        # Crear botones en fila horizontal (como nivel fácil)
        for opt_text in options_values:
            btn = RoundedButton(btn_frame, text=opt_text, width=200, height=90,
                              color=BTN_EASY_COLOR, text_color="#000000",
                              command=_make_handler(opt_text))
            btn.pack(side=tk.LEFT, padx=15)

    def _show_lagrange_avanzado(self, chapter, level, difficulty, lesson_index):
        """Nivel avanzado de Lagrange con tabla extendida (5 filas) y 30 minutos"""
        import random
        
        # === BANNER SUPERIOR ===
        banner_frame = tk.Frame(self.current_screen, bg="#ac35e4", height=70)
        banner_frame.pack(fill=tk.X, side=tk.TOP)
        banner_frame.pack_propagate(False)
        
        banner_text = f"Capítulo 1 Nivel 1. Lagrange. {difficulty}"
        tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"), 
                bg="#FF8C42", fg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=15)
        
        # Botón de retroceso
        try:
            if PIL_AVAILABLE:
                from PIL import Image as PILImage, ImageTk as PILImageTk
                pil_img = PILImage.open(os.path.join('imgs', 'red-go-back-arrow.png'))
                pil_img.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
                back_arrow_img = PILImageTk.PhotoImage(pil_img)
            else:
                back_arrow_img = tk.PhotoImage(file=os.path.join('imgs', 'red-go-back-arrow.png'))
                if back_arrow_img.width() > 40:
                    factor = max(1, int(back_arrow_img.width() / 40))
                    back_arrow_img = back_arrow_img.subsample(factor)
            
            back_btn = tk.Label(banner_frame, image=back_arrow_img, bg="#FF8C42", cursor="hand2")
            back_btn.image = back_arrow_img
            back_btn.pack(side=tk.RIGHT, padx=20, pady=15)
            back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        except Exception:
            back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"), 
                               bg="#FF8C42", fg="#FFFFFF", cursor="hand2")
            back_btn.pack(side=tk.RIGHT, padx=20, pady=15)
            back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        
        # Contenido principal
        main_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título del problema
        tk.Label(main_frame, text="Obtener g(x)", font=("Arial", scale_font(18), "bold"), 
                bg=COLOR_FONDO, fg="#20E0D0").pack(pady=10)
        
        # Frame para tabla y x = 2.4
        top_content_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        top_content_frame.pack(pady=15, fill=tk.X)
        
        # Mostrar x = 2.4 (izquierda)
        tk.Label(top_content_frame, text="x = 2.4", font=("Arial", scale_font(16), "bold"), 
                bg=COLOR_FONDO, fg="white").pack(side=tk.LEFT, padx=20)
        
        # Tabla de datos con 5 filas (avanzado)
        table_frame = tk.Frame(top_content_frame, bg="white", highlightthickness=2, highlightbackground="#20E0D0")
        table_frame.pack(side=tk.LEFT, padx=20)
        
        # Encabezados
        header_x = tk.Label(table_frame, text="x", font=("Arial", scale_font(12), "bold"), 
                           bg="#20E0D0", fg="white", width=12, height=2)
        header_x.grid(row=0, column=0, sticky="nsew")
        
        header_y = tk.Label(table_frame, text="y", font=("Arial", scale_font(12), "bold"), 
                           bg="#20E0D0", fg="white", width=12, height=2)
        header_y.grid(row=0, column=1, sticky="nsew")
        
        # Datos de la tabla (5 filas para avanzado)
        data = [(2.2, 2.54), (2.5, 2.82), (2.8, 3.21), (3.1, 3.32), (3.4, 3.41)]
        
        for i, (x_val, y_val) in enumerate(data, 1):
            cell_x = tk.Label(table_frame, text=str(x_val), font=("Arial", scale_font(11)), 
                             bg="white", fg="black", width=12, height=2, relief=tk.RIDGE)
            cell_x.grid(row=i, column=0, sticky="nsew")
            
            cell_y = tk.Label(table_frame, text=str(y_val), font=("Arial", scale_font(11)), 
                             bg="white", fg="black", width=12, height=2, relief=tk.RIDGE)
            cell_y.grid(row=i, column=1, sticky="nsew")
        
        # Temporizador a la derecha (30 minutos)
        timer_container = tk.Frame(top_content_frame, bg=COLOR_FONDO)
        timer_container.pack(side=tk.RIGHT, padx=20)
        
        tk.Label(timer_container, text="⏱", font=("Arial", scale_font(24)), 
                bg=COLOR_FONDO, fg="white").pack(pady=5)
        tk.Label(timer_container, text="Tiempo restante", font=("Arial", scale_font(12), "bold"), 
                bg=COLOR_FONDO, fg="white").pack()
        
        timer_label = tk.Label(timer_container, text="30:00", font=("Arial", scale_font(20), "bold"), 
                              bg=COLOR_FONDO, fg="#20E0D0")
        timer_label.pack(pady=5)
        
        # Temporizador de 30 minutos (1800 segundos)
        timer_state = {'seconds': 1800, 'timer_id': None}
        
        def _update_timer():
            timer_state['seconds'] -= 1
            minutes = timer_state['seconds'] // 60
            seconds = timer_state['seconds'] % 60
            time_str = f"{minutes}:{seconds:02d}"
            timer_label.config(text=time_str)
            
            if timer_state['seconds'] > 0:
                timer_state['timer_id'] = self.root.after(1000, _update_timer)
            else:
                messagebox.showinfo("Tiempo agotado", "Se acabó el tiempo para resolver el problema.")
                self.show_difficulty_menu(chapter, level)
        
        _update_timer()
        
        # Marco con opciones
        options_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        options_frame.pack(pady=30, fill=tk.BOTH, expand=True)
        
        # Etiqueta g(x) =
        tk.Label(options_frame, text="g(x) =", font=("Arial", scale_font(16), "bold"), 
                bg=COLOR_FONDO, fg="white").pack(pady=15)
        
        # Opciones con RoundedButton
        btn_frame = tk.Frame(options_frame, bg=COLOR_FONDO)
        btn_frame.pack(pady=20)
        
        # 5 opciones para avanzado
        options_values = ["2.67646", "2.77646", "2.57646", "3.67646", "1.67646"]
        correct_answer = "2.77646"
        
        # Randomizar el orden
        random.shuffle(options_values)
        
        def _make_handler(option_text):
            def _handler():
                if timer_state['timer_id']:
                    self.root.after_cancel(timer_state['timer_id'])
                
                if option_text == correct_answer:
                    messagebox.showinfo("¡Correcto!", f"¡Excelente!")
                    self.start_lesson(chapter, level, difficulty, lesson_index + 1)
                else:
                    messagebox.showinfo("Incorrecto", "Lo siento, esa respuesta no es correcta.")
                    self.errors_committed += 1
                    self._save_progress()
                    self.show_difficulty_menu(chapter, level)
            return _handler
        
        # Crear botones en fila horizontal
        for opt_text in options_values:
            btn = RoundedButton(btn_frame, text=opt_text, width=180, height=90,
                              color=BTN_EASY_COLOR, text_color="#000000",
                              command=_make_handler(opt_text))
            btn.pack(side=tk.LEFT, padx=12)

    def _show_lagrange_final(self, chapter, level, difficulty, lesson_index):
        """Prueba Final de Lagrange con tabla extendida, 25 minutos e intento único"""
        import random
        
        # Verificar si ya se intentó esta prueba
        medal_str = f"{level} ({difficulty})"
        if medal_str in self.medals:
            messagebox.showinfo("Prueba Final", "Ya completaste la Prueba Final. No puedes volver a intentarla.")
            self.show_difficulty_menu(chapter, level)
            return
        
        # === BANNER SUPERIOR ===
        banner_frame = tk.Frame(self.current_screen, bg="#ac35e4", height=70)
        banner_frame.pack(fill=tk.X, side=tk.TOP)
        banner_frame.pack_propagate(False)
        
        banner_text = f"Capítulo 1 Nivel 1. Lagrange. {difficulty}"
        tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"), 
                bg="#FF8C42", fg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=15)
        
        # Botón de retroceso
        try:
            if PIL_AVAILABLE:
                from PIL import Image as PILImage, ImageTk as PILImageTk
                pil_img = PILImage.open(os.path.join('imgs', 'red-go-back-arrow.png'))
                pil_img.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
                back_arrow_img = PILImageTk.PhotoImage(pil_img)
            else:
                back_arrow_img = tk.PhotoImage(file=os.path.join('imgs', 'red-go-back-arrow.png'))
                if back_arrow_img.width() > 40:
                    factor = max(1, int(back_arrow_img.width() / 40))
                    back_arrow_img = back_arrow_img.subsample(factor)
            
            back_btn = tk.Label(banner_frame, image=back_arrow_img, bg="#FF8C42", cursor="hand2")
            back_btn.image = back_arrow_img
            back_btn.pack(side=tk.RIGHT, padx=20, pady=15)
            back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        except Exception:
            back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"), 
                               bg="#FF8C42", fg="#FFFFFF", cursor="hand2")
            back_btn.pack(side=tk.RIGHT, padx=20, pady=15)
            back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        
        # Contenido principal
        main_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título del problema
        tk.Label(main_frame, text="Obtener g(x)", font=("Arial", scale_font(18), "bold"), 
                bg=COLOR_FONDO, fg="#20E0D0").pack(pady=10)
        
        # Frame para tabla y x = 2.4
        top_content_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        top_content_frame.pack(pady=15, fill=tk.X)
        
        # Mostrar x = 2.4 (izquierda)
        tk.Label(top_content_frame, text="x = 2.4", font=("Arial", scale_font(16), "bold"), 
                bg=COLOR_FONDO, fg="white").pack(side=tk.LEFT, padx=20)
        
        # Tabla de datos con 5 filas (igual que avanzado)
        table_frame = tk.Frame(top_content_frame, bg="white", highlightthickness=2, highlightbackground="#20E0D0")
        table_frame.pack(side=tk.LEFT, padx=20)
        
        # Encabezados
        header_x = tk.Label(table_frame, text="x", font=("Arial", scale_font(12), "bold"), 
                           bg="#20E0D0", fg="white", width=12, height=2)
        header_x.grid(row=0, column=0, sticky="nsew")
        
        header_y = tk.Label(table_frame, text="y", font=("Arial", scale_font(12), "bold"), 
                           bg="#20E0D0", fg="white", width=12, height=2)
        header_y.grid(row=0, column=1, sticky="nsew")
        
        # Datos de la tabla (5 filas para prueba final)
        data = [(2.2, 2.54), (2.5, 2.82), (2.8, 3.21), (3.1, 3.32), (3.4, 3.41)]
        
        for i, (x_val, y_val) in enumerate(data, 1):
            cell_x = tk.Label(table_frame, text=str(x_val), font=("Arial", scale_font(11)), 
                             bg="white", fg="black", width=12, height=2, relief=tk.RIDGE)
            cell_x.grid(row=i, column=0, sticky="nsew")
            
            cell_y = tk.Label(table_frame, text=str(y_val), font=("Arial", scale_font(11)), 
                             bg="white", fg="black", width=12, height=2, relief=tk.RIDGE)
            cell_y.grid(row=i, column=1, sticky="nsew")
        
        # Temporizador a la derecha (25 minutos)
        timer_container = tk.Frame(top_content_frame, bg=COLOR_FONDO)
        timer_container.pack(side=tk.RIGHT, padx=20)
        
        tk.Label(timer_container, text="⏱", font=("Arial", scale_font(24)), 
                bg=COLOR_FONDO, fg="white").pack(pady=5)
        tk.Label(timer_container, text="Tiempo restante", font=("Arial", scale_font(12), "bold"), 
                bg=COLOR_FONDO, fg="white").pack()
        
        timer_label = tk.Label(timer_container, text="25:00", font=("Arial", scale_font(20), "bold"), 
                              bg=COLOR_FONDO, fg="#20E0D0")
        timer_label.pack(pady=5)
        
        # Temporizador de 25 minutos (1500 segundos)
        timer_state = {'seconds': 1500, 'timer_id': None}
        
        def _update_timer():
            timer_state['seconds'] -= 1
            minutes = timer_state['seconds'] // 60
            seconds = timer_state['seconds'] % 60
            time_str = f"{minutes}:{seconds:02d}"
            timer_label.config(text=time_str)
            
            if timer_state['seconds'] > 0:
                timer_state['timer_id'] = self.root.after(1000, _update_timer)
            else:
                messagebox.showinfo("Tiempo agotado", "Se acabó el tiempo para resolver el problema.")
                self.errors_committed += 1
                self._save_progress()
                self.show_difficulty_menu(chapter, level)
        
        _update_timer()
        
        # Marco con opciones
        options_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        options_frame.pack(pady=30, fill=tk.BOTH, expand=True)
        
        # Etiqueta g(x) =
        tk.Label(options_frame, text="g(x) =", font=("Arial", scale_font(16), "bold"), 
                bg=COLOR_FONDO, fg="white").pack(pady=15)
        
        # Opciones con RoundedButton
        btn_frame = tk.Frame(options_frame, bg=COLOR_FONDO)
        btn_frame.pack(pady=20)
        
        # 5 opciones para prueba final
        options_values = ["2.67646", "2.77646", "2.57646", "3.67646", "1.67646"]
        correct_answer = "2.77646"
        
        # Randomizar el orden
        random.shuffle(options_values)
        
        def _make_handler(option_text):
            def _handler():
                if timer_state['timer_id']:
                    self.root.after_cancel(timer_state['timer_id'])
                
                if option_text == correct_answer:
                    messagebox.showinfo("¡Correcto!", f"¡Excelente! ¡Prueba Final completada!")
                    # Agregar medalla de prueba final
                    if medal_str not in self.medals:
                        self.medals.append(medal_str)
                    self._save_progress()
                    self.show_difficulty_menu(chapter, level)
                else:
                    messagebox.showinfo("Incorrecto", "Lo siento, fallaste la Prueba Final. No se otorga medalla.")
                    self.errors_committed += 1
                    self._save_progress()
                    # No permite reintentar
                    self.show_difficulty_menu(chapter, level)
            return _handler
        
        # Crear botones en fila horizontal
        for opt_text in options_values:
            btn = RoundedButton(btn_frame, text=opt_text, width=180, height=90,
                              color=BTN_EASY_COLOR, text_color="#000000",
                              command=_make_handler(opt_text))
            btn.pack(side=tk.LEFT, padx=12)

    def show_practica(self, lesson, chapter, level, difficulty, lesson_index):
        """Renderiza preguntas de práctica. Si es dificultad 'Fácil', aplica estética especial.
        Caso especial: Nivel Lagrange (Fácil) — muestra la fórmula, luego preguntas individuales de cada imagen.
        Caso especial: Nivel Lagrange (Intermedio) — ejercicio de interpolación de Lagrange.
        Caso especial: Nivel Lagrange (Avanzado) — ejercicio con tabla extendida y 30 minutos.
        Caso especial: Nivel Lagrange (Prueba Final) — ejercicio con tabla extendida, 25 minutos, intento único.
        """
        import random
        
        # Caso especial: Lagrange Intermedio (formato con tabla y problema)
        try:
            is_lagrange_intermedio = 'Lagrange' in level and difficulty.lower() == 'intermedio'
        except Exception:
            is_lagrange_intermedio = False
        
        if is_lagrange_intermedio:
            return self._show_lagrange_intermedio(chapter, level, difficulty, lesson_index)
        
        # Caso especial: Lagrange Avanzado (tabla extendida, 30 minutos)
        try:
            is_lagrange_avanzado = 'Lagrange' in level and difficulty.lower() == 'avanzado'
        except Exception:
            is_lagrange_avanzado = False
        
        if is_lagrange_avanzado:
            return self._show_lagrange_avanzado(chapter, level, difficulty, lesson_index)
        
        # Caso especial: Lagrange Prueba Final (tabla extendida, 25 minutos, intento único)
        try:
            is_lagrange_final = 'Lagrange' in level and difficulty.lower() == 'prueba final'
        except Exception:
            is_lagrange_final = False
        
        if is_lagrange_final:
            return self._show_lagrange_final(chapter, level, difficulty, lesson_index)
        
        
        # Caso especial: Lagrange Fácil (formato con imágenes)
        try:
            is_lagrange = 'Lagrange' in level and difficulty.lower() == 'fácil'
        except Exception:
            is_lagrange = False

        if is_lagrange:
            # Directorio de imágenes
            img_dir = os.path.join('imgs', 'Lagrange')
            if not os.path.exists(img_dir):
                tk.Label(self.current_screen, text="Carpeta de imágenes de Lagrange no encontrada.", bg=COLOR_FONDO, fg='white').pack(pady=20)
                return

            # Estado para rastrear el progreso en las preguntas
            lagrange_state = {
                'current_question_index': 0,
                'total_correct': 0,
                'formula_seen': False,
                'questions_list': []  # Lista de (imagen_file, answer_text)
            }

            # Obtener lista de preguntas (todas las imágenes excepto FormulaOriginal)
            question_images = []
            for f in os.listdir(img_dir):
                name, ext = os.path.splitext(f)
                if name.lower().startswith('formulaoriginal'):
                    continue
                if ext.lower() not in ('.png', '.jpg', '.gif', '.bmp'):
                    continue
                question_images.append(f)

            # Barajar el orden de las preguntas
            random.shuffle(question_images)
            lagrange_state['questions_list'] = question_images

            # Diccionario de respuestas falsas similares para cada concepto
            fake_answers = {
                'yi': ['y', 'yi+1', 'y(i)', 'yn'],
                'n': ['m', 'k', 'l', 'i'],
                'x-xj': ['x-xi', 'x-x0', 'x-xn', 'xi-x'],
                'xi-xj': ['xi-xk', 'xj-xi', 'xk-xi', 'x-xj'],
                'Σ': ['Σ', 'Π', '∫', 'Δ'],
                'Nada': ['?', '*', '·', '—']
            }

            def _show_formula():
                """Muestra la pantalla inicial con la fórmula."""
                for w in self.current_screen.winfo_children():
                    w.destroy()

                top_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
                top_frame.pack(fill=tk.BOTH, expand=False, pady=10)

                formula_path = None
                for f in os.listdir(img_dir):
                    if f.lower().startswith('formulaoriginal'):
                        formula_path = os.path.join(img_dir, f)
                        break

                if formula_path and os.path.exists(formula_path):
                    try:
                        pimg = tk.PhotoImage(file=formula_path)
                        # scale down if too large - más grande ahora
                        if pimg.width() > 1200:
                            factor = max(1, int(pimg.width() / 1200))
                            pimg = pimg.subsample(factor)
                        lbl_img = tk.Label(top_frame, image=pimg, bg=COLOR_FONDO)
                        lbl_img.image = pimg
                        lbl_img.pack(pady=10)
                    except Exception:
                        pass

                tk.Label(top_frame, text="¡Esta es la formula de lagrange, memorizala!", font=("Arial", scale_font(16), "bold"), bg=COLOR_FONDO, fg="white").pack(pady=(6,12))

                def _continue_to_questions():
                    lagrange_state['formula_seen'] = True
                    _show_next_question()

                RoundedButton(self.current_screen, text="OK", width=120, height=48, color="#20D0C0", text_color="#00303a", command=_continue_to_questions).pack(pady=12)

            def _show_next_question():
                """Muestra la siguiente pregunta de imagen."""
                for w in self.current_screen.winfo_children():
                    w.destroy()

                # Verificar si hemos terminado todas las preguntas
                if lagrange_state['current_question_index'] >= len(lagrange_state['questions_list']):
                    # Todas las preguntas completadas
                    messagebox.showinfo("¡Completado!", f"¡Felicidades! Has completado el nivel Lagrange Fácil.")
                    medal_str = f"{level} ({difficulty})"
                    if medal_str not in self.medals:
                        self.medals.append(medal_str)
                    self._save_progress()
                    self.start_lesson(chapter, level, difficulty, lesson_index + 1)
                    return

                # === BANNER SUPERIOR ===
                banner_frame = tk.Frame(self.current_screen, bg="#20E0D0", height=60)
                banner_frame.pack(fill=tk.X, side=tk.TOP)
                banner_frame.pack_propagate(False)
                
                banner_text = f"Capítulo 1 Nivel 1. Lagrange. {difficulty}"
                tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"), 
                        bg="#20E0D0", fg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=10)
                
                # Botón de retroceso en la esquina derecha del banner con imagen
                try:
                    if PIL_AVAILABLE:
                        # Usar PIL para redimensionar correctamente
                        from PIL import Image, ImageTk as PILImageTk
                        pil_img = Image.open(os.path.join('imgs', 'red-go-back-arrow.png'))
                        # Redimensionar a 40x40 manteniendo aspecto
                        pil_img.thumbnail((40, 40), Image.Resampling.LANCZOS)
                        back_arrow_img = PILImageTk.PhotoImage(pil_img)
                    else:
                        # Fallback: cargar como PhotoImage normal
                        back_arrow_img = tk.PhotoImage(file=os.path.join('imgs', 'red-go-back-arrow.png'))
                        if back_arrow_img.width() > 40:
                            factor = max(1, int(back_arrow_img.width() / 40))
                            back_arrow_img = back_arrow_img.subsample(factor)
                    
                    back_btn = tk.Label(banner_frame, image=back_arrow_img, bg="#20E0D0", cursor="hand2")
                    back_btn.image = back_arrow_img  # Keep reference
                    back_btn.pack(side=tk.RIGHT, padx=15, pady=10)
                    back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
                except Exception:
                    # Fallback al botón de texto si la imagen no carga
                    back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"), 
                                       bg="#20E0D0", fg="#FF5733", cursor="hand2")
                    back_btn.pack(side=tk.RIGHT, padx=20, pady=10)
                    back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))

                # Obtener imagen actual
                current_image_file = lagrange_state['questions_list'][lagrange_state['current_question_index']]
                current_image_path = os.path.join(img_dir, current_image_file)
                current_answer = os.path.splitext(current_image_file)[0]

                # Mostrar la imagen centrada
                img_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
                img_frame.pack(pady=30)

                if os.path.exists(current_image_path):
                    try:
                        display_img = tk.PhotoImage(file=current_image_path)
                        # scale to height ~250 (mucho más grande)
                        if display_img.height() > 250:
                            factor = max(1, int(display_img.height() / 250))
                            display_img = display_img.subsample(factor)
                        img_lbl = tk.Label(img_frame, image=display_img, bg=COLOR_FONDO)
                        img_lbl.image = display_img
                        img_lbl.pack()
                    except Exception:
                        tk.Label(img_frame, text=f"No se pudo cargar: {current_image_file}", bg=COLOR_FONDO, fg="white").pack()

                # Pregunta: "¿Qué falta en esta parte de la fórmula de Lagrange?"
                tk.Label(self.current_screen, text="¿Qué falta en esta parte de la fórmula de Lagrange?", font=("Arial", scale_font(14), "bold"), 
                        bg=COLOR_FONDO, fg="white").pack(pady=15)

                # Generar opciones: respuesta correcta + 3 falsas
                correct_option = current_answer
                if current_answer in fake_answers:
                    fake_opts = fake_answers[current_answer]
                    wrong_options = random.sample(fake_opts, min(3, len(fake_opts)))
                else:
                    # Si no hay respuestas falsas predefinidas, crear genéricas
                    wrong_options = [f"Opción {i}" for i in range(1, 4)]

                all_options = [correct_option] + wrong_options
                random.shuffle(all_options)

                # Frame para botones en fila
                btns_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
                btns_frame.pack(pady=20)

                def _make_answer_handler(selected_option):
                    def _handler():
                        if selected_option.lower() == correct_option.lower():
                            messagebox.showinfo("¡Correcto!", f"Correcto: {correct_option}")
                            lagrange_state['total_correct'] += 1
                        else:
                            messagebox.showerror("Incorrecto", f"Respuesta incorrecta. La correcta era: {correct_option}")
                            self.errors_committed += 1

                        lagrange_state['current_question_index'] += 1
                        self._save_progress()
                        _show_next_question()

                    return _handler

                # Crear botones en fila horizontal
                for option_text in all_options:
                    btn = RoundedButton(btns_frame, text=option_text, width=120, height=50,
                                      color=BTN_EASY_COLOR, text_color="#000000",
                                      command=_make_answer_handler(option_text))
                    btn.pack(side=tk.LEFT, padx=8)

            # Iniciar el flujo: mostrar la fórmula primero
            _show_formula()
            return

        # Fin caso especial Lagrange

        # ===== ESTÉTICA FÁCIL PARA TODOS LOS NIVELES FÁCIL =====
        if difficulty.lower() == 'fácil':
            self.clear_screen()
            
            # === BANNER SUPERIOR ===
            banner_frame = tk.Frame(self.current_screen, bg="#20E0D0", height=60)
            banner_frame.pack(fill=tk.X, side=tk.TOP)
            banner_frame.pack_propagate(False)
            
            banner_text = f"Capítulo 1 {level}. {chapter.split(':')[1].strip() if ':' in chapter else chapter}. {difficulty}"
            tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"), 
                    bg="#20E0D0", fg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=10)
            
            # Botón de retroceso en la esquina derecha del banner con imagen
            try:
                if PIL_AVAILABLE:
                    from PIL import Image as PILImage, ImageTk as PILImageTk
                    pil_img = PILImage.open(os.path.join('imgs', 'red-go-back-arrow.png'))
                    pil_img.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
                    back_arrow_img = PILImageTk.PhotoImage(pil_img)
                else:
                    back_arrow_img = tk.PhotoImage(file=os.path.join('imgs', 'red-go-back-arrow.png'))
                    if back_arrow_img.width() > 40:
                        factor = max(1, int(back_arrow_img.width() / 40))
                        back_arrow_img = back_arrow_img.subsample(factor)
                
                back_btn = tk.Label(banner_frame, image=back_arrow_img, bg="#20E0D0", cursor="hand2")
                back_btn.image = back_arrow_img
                back_btn.pack(side=tk.RIGHT, padx=15, pady=10)
                back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
            except Exception:
                back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"), 
                                   bg="#20E0D0", fg="#FF5733", cursor="hand2")
                back_btn.pack(side=tk.RIGHT, padx=20, pady=10)
                back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))

            # Contenido de la lección
            content_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
            content_frame.pack(fill=tk.BOTH, expand=True, pady=30, padx=20)

            # Mostrar pregunta
            if 'content' in lesson:
                tk.Label(content_frame, text=lesson['content'], 
                        wraplength=700, font=("Arial", scale_font(14), "bold"), 
                        bg=COLOR_FONDO, fg="white").pack(pady=20)

            # Mostrar opciones en fila horizontal (izquierda a derecha)
            if 'options' in lesson:
                btns_frame = tk.Frame(content_frame, bg=COLOR_FONDO)
                btns_frame.pack(pady=20)

                for option in lesson['options']:
                    btn = RoundedButton(btns_frame, text=option, width=120, height=50,
                                      color=BTN_EASY_COLOR, text_color="#000000",
                                      command=lambda o=option: self.check_answer(o, lesson, chapter, level, difficulty, lesson_index))
                    btn.pack(side=tk.LEFT, padx=8)
            
            elif 'problem_id' in lesson:
                tk.Label(content_frame, text=f"(Problema: {lesson['problem_id']})", 
                        bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack(pady=10)
                tk.Label(content_frame, text="Ingresa tu respuesta:", 
                        bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack()
                entry = tk.Entry(content_frame, font=("Arial", scale_font(12)))
                entry.pack(pady=10)
                RoundedButton(content_frame, text="REVISAR", width=200, height=50,
                          command=lambda: messagebox.showinfo("WIP", "Lógica de revisión no implementada")).pack(pady=20)
            
            return

        # ===== COMPORTAMIENTO PARA OTRAS DIFICULTADES (NO FÁCIL) =====
        tk.Label(self.current_screen, text=f"Pregunta: {lesson['content']}", 
                 wraplength=700, font=("Arial", scale_font(14)), bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack(pady=20, padx=40)
        
        options_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        options_frame.pack(pady=10)

        if 'options' in lesson:
            for option in lesson['options']:
                btn = RoundedButton(options_frame, text=option, width=None, height=50,
                                    color=COLOR_BOTON_CLARO, outline_color=COLOR_BORDE_OSCURO, border_width=2,
                                    command=lambda o=option: self.check_answer(o, lesson, chapter, level, difficulty, lesson_index))
                btn.pack(pady=8)
                
        elif 'problem_id' in lesson:
            tk.Label(self.current_screen, text=f"(Mostrando problema: {lesson['problem_id']})", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack(pady=10)
            tk.Label(self.current_screen, text="Ingresa tu respuesta:", bg=COLOR_FONDO, fg=COLOR_TEXTO_LBL).pack()
            entry = tk.Entry(self.current_screen, font=("Arial", scale_font(12)))
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
            self._save_progress()  # Guardar error cometido
            
            # Comportamiento según dificultad
            if difficulty.lower() == 'fácil':
                # En Fácil, mostrar la respuesta correcta
                if lesson_type == 'practica':
                    messagebox.showerror("Incorrecto", f"Respuesta correcta: '{correct_answer}'.")
                    self.start_lesson(chapter, level, difficulty, max(0, lesson_index - 1))
                elif lesson_type == 'examen':
                    messagebox.showerror("Incorrecto", "Fallo crítico. Reiniciando sección.")
                    self.start_lesson(chapter, level, difficulty, 0)
            else:
                # En Intermedio y Avanzado: NO mostrar la respuesta, salir automáticamente
                messagebox.showinfo("Incorrecto", "Lo siento, esa respuesta no es correcta.")
                self.show_difficulty_menu(chapter, level)

    def _start_timer(self):
        """Inicia el temporizador que incrementa el tiempo cada segundo"""
        def _increment_time():
            self.time_elapsed_seconds += 1
            # Programar la siguiente llamada en 1000 ms
            self.root.after(1000, _increment_time)
        
        # Iniciar el temporizador
        self.root.after(1000, _increment_time)

    def _format_time(self):
        """Convierte segundos a formato 'Xh Ym'"""
        hours = self.time_elapsed_seconds // 3600
        minutes = (self.time_elapsed_seconds % 3600) // 60
        return f"{hours}h {minutes}m"

    def _save_progress(self):
        """Guarda el progreso en un archivo JSON"""
        data = {
            "time_elapsed_seconds": self.time_elapsed_seconds,
            "errors_committed": self.errors_committed,
            "medals": self.medals,
            "username": self.username,
            "music_enabled": self.music_enabled,
            "music_volume": self.music_volume
        }
        try:
            with open(self.save_file, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error guardando progreso: {e}")

    def _load_progress(self):
        """Carga el progreso desde el archivo JSON"""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, "r") as f:
                    data = json.load(f)
                    self.time_elapsed_seconds = data.get("time_elapsed_seconds", 0)
                    self.errors_committed = data.get("errors_committed", 0)
                    self.medals = data.get("medals", [])
                    self.username = data.get("username", "Jugador 1")
                    self.music_enabled = data.get("music_enabled", True)
                    self.music_volume = data.get("music_volume", 0.7)
            except Exception as e:
                print(f"Error cargando progreso: {e}")

    def _reset_progress(self):
        """Reinicia todo el progreso (tiempo, errores, medallas)"""
        self.time_elapsed_seconds = 0
        self.errors_committed = 0
        self.medals = []
        self.music_enabled = True
        self.music_volume = 0.7
        self._save_progress()
        messagebox.showinfo("Progreso Reiniciado", "Tu progreso ha sido reiniciado. ¡A jugar!")
        self.show_main_menu()