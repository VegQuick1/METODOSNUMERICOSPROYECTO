import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
import os
import sys
import json
from game_data import GAME_STRUCTURE, PROBLEM_DATA, LAGRANGE_FAKE_ANSWERS
def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.abspath(__file__))
BASE_PATH = get_base_path()
def get_resource_path(relative_path):
    return os.path.join(BASE_PATH, relative_path)
import methods_engine as me
from music_manager import MusicManager
from numerical_methods_lessons import *
from methods_mapping import METHODS_MAPPING, get_method_info
import additional_methods
try:
    from PIL import Image, ImageDraw, ImageTk
    PIL_AVAILABLE = True
except Exception:
    PIL_AVAILABLE = False
def create_rounded_rect_image(width, height, radius, color1, color2=None):
    if not PIL_AVAILABLE:
        return None
    img = Image.new("RGBA", (max(2, int(width)), max(2, int(height))), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    if color2 is None:
        draw.rounded_rectangle([(0, 0), (img.width, img.height)], radius=radius, fill=color1)
    else:
        r1, g1, b1 = tuple(int(color1.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        r2, g2, b2 = tuple(int(color2.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        for x in range(img.width):
            t = x / max(1, img.width - 1)
            ri = int(r1 + (r2 - r1) * t)
            gi = int(g1 + (g2 - g1) * t)
            bi = int(b1 + (b2 - b1) * t)
            draw.line([(x, 0), (x, img.height)], fill=(ri, gi, bi))
        mask = Image.new("L", (img.width, img.height), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.rounded_rectangle([(0, 0), (img.width, img.height)], radius=radius, fill=255)
        img.putalpha(mask)
    return img
COLOR_FONDO = "#001F3F"
COLOR_BOTON = "#40E0D0"
COLOR_TEXTO_BTN = "#FFFFFF" # Texto blanco para resaltar en botones oscuros/vibrantes
COLOR_TEXTO_LBL = "#FFFFFF"
COLOR_BOTON_CLARO = "#1F8686"
COLOR_BORDE_OSCURO = "#008080"
COLOR_BOTON_ROJO = "#FF6B6B"
BTN_EASY_COLOR = "#00e676"      # Fácil: gradiente de #00e676 a #24a7d3
BTN_INTER_COLOR = "#f8cf39"     # Intermedio: gradiente de #f8cf39 a #f67345
BTN_ADV_COLOR = "#f94255"       # Avanzado: gradiente de #f94255 a #b3319e
BTN_FINAL_COLOR = "#ac35e4"     # Prueba Final: color sólido
COLOR_STRIP_EXPL = "#FFD700"
COLOR_STRIP_PRAC = "#FF8C00"
COLOR_STRIP_EXAM = "#FF4500"

DIFFICULTY_STYLES = {
    'fácil': {
        'banner_color': BTN_EASY_COLOR,
        'banner_text_color': '#FFFFFF',
        'button_color': BTN_EASY_COLOR,
        'button_text_color': '#000000',
        'timer_color': '#20E0D0',
        'title_color': '#20E0D0',
        'table_header_bg': '#2c3e50',
        'table_header_fg': 'white',
        'banner_height': 70
    },
    'intermedio': {
        'banner_color': '#f8cf39',
        'banner_text_color': '#FFFFFF',
        'button_color': BTN_EASY_COLOR,
        'button_text_color': '#000000',
        'timer_color': '#20E0D0',
        'title_color': '#20E0D0',
        'table_header_bg': '#2c3e50',
        'table_header_fg': 'white',
        'banner_height': 70
    },
    'avanzado': {
        'banner_color': '#f94255',
        'banner_text_color': '#FFFFFF',
        'button_color': BTN_EASY_COLOR,
        'button_text_color': '#000000',
        'timer_color': '#20E0D0',
        'title_color': '#20E0D0',
        'table_header_bg': '#2c3e50',
        'table_header_fg': 'white',
        'banner_height': 70
    },
    'prueba final': {
        'banner_color': '#ac35e4',
        'banner_text_color': '#FFFFFF',
        'button_color': BTN_EASY_COLOR,
        'button_text_color': '#000000',
        'timer_color': '#20E0D0',
        'title_color': '#20E0D0',
        'table_header_bg': '#2c3e50',
        'table_header_fg': 'white',
        'banner_height': 70
    }
}

WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768
SCALE_FACTOR = 1.0  # Factor de escala global para toda la interfaz
HEADER_HEIGHT = int(70 * SCALE_FACTOR)
def scale_value(value):
    return int(value * SCALE_FACTOR)
def scale_font(size):
    return max(8, int(size * SCALE_FACTOR))
class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, width=None, height=60, corner_radius=20,
                 color=COLOR_BOTON, text_color=COLOR_TEXTO_BTN, bg_color=COLOR_FONDO,
                 outline_color=None, border_width=0, icon_image=None, icon_padding=14):
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
        text_x = w/2
        if self.icon_image:
            try:
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
        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))
class GradientRoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, width=420, height=70, corner_radius=35,
                 colors=("#20D0C6", "#FF7A4D"), text_color="#ffffff", bg_color=COLOR_FONDO):
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
        if PIL_AVAILABLE:
            try:
                img = Image.new("RGBA", (max(2, int(w)), max(2, int(h))), (0, 0, 0, 0))
                draw = ImageDraw.Draw(img)
                r1, g1, b1 = self._hex_to_rgb(self.colors[0])
                r2, g2, b2 = self._hex_to_rgb(self.colors[-1])
                for x in range(img.width):
                    t = x / max(1, img.width - 1)
                    ri = int(r1 + (r2 - r1) * t)
                    gi = int(g1 + (g2 - g1) * t)
                    bi = int(b1 + (b2 - b1) * t)
                    draw.line([(x, 0), (x, img.height)], fill=(ri, gi, bi))
                mask = Image.new("L", (img.width, img.height), 0)
                mdraw = ImageDraw.Draw(mask)
                mdraw.rounded_rectangle([(0, 0), (img.width, img.height)], radius=r, fill=255)
                img.putalpha(mask)
                tkimg = ImageTk.PhotoImage(img)
                self._tkimg = tkimg
                self.create_image(0, 0, anchor="nw", image=self._tkimg)
            except Exception:
                pass
        if not PIL_AVAILABLE or not hasattr(self, '_tkimg'):
            try:
                r1, g1, b1 = self._hex_to_rgb(self.colors[0])
                r2, g2, b2 = self._hex_to_rgb(self.colors[-1])
                steps = max(10, int(w / 5))
                for i in range(steps):
                    t = i / (steps - 1)
                    ri = int(r1 + (r2 - r1) * t)
                    gi = int(g1 + (g2 - g1) * t)
                    bi = int(b1 + (b2 - b1) * t)
                    col = f"#{ri:02x}{gi:02x}{bi:02x}"
                    x0 = i * (w / steps)
                    x1 = (i + 1) * (w / steps)
                    self.create_rectangle(x0, 0, x1, h, fill=col, outline="", width=0)
                self.create_arc(0, 0, r*2, r*2, start=90, extent=90, fill=self.bg_color, outline=self.bg_color, width=0)
                self.create_arc(w-r*2, 0, w, r*2, start=0, extent=90, fill=self.bg_color, outline=self.bg_color, width=0)
                self.create_arc(w-r*2, h-r*2, w, h, start=270, extent=90, fill=self.bg_color, outline=self.bg_color, width=0)
                self.create_arc(0, h-r*2, r*2, h, start=180, extent=90, fill=self.bg_color, outline=self.bg_color, width=0)
            except Exception as e:
                self.create_rectangle(0, 0, w, h, fill=self.colors[0], outline="", width=0)
        tri_size = int(h * 0.34)
        cx = r
        cy = h / 2
        self.create_polygon(cx - tri_size/2, cy - tri_size/1.2,
                            cx - tri_size/2, cy + tri_size/1.2,
                            cx + tri_size/1.2, cy,
                            fill=self.text_color, outline="")
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
        self.chapter_menu_scroll_position = 0
        if getattr(sys, 'frozen', False):
            exe_dir = os.path.dirname(sys.executable)
            self.save_file = os.path.join(exe_dir, "game_progress.json")
        else:
            self.save_file = "game_progress.json"
        self.music_enabled = True
        self.music_volume = 0.7
        self._load_progress()
        self._start_timer()
        songs_path = os.path.join(BASE_PATH, "songs")
        self.music_manager = MusicManager(songs_folder=songs_path)
        if not self.music_enabled:
            self.music_manager.set_volume(0.0)
        else:
            self.music_manager.set_volume(self.music_volume)
        additional_methods.set_app_reference(self)
        self.back_icon = None
        img_path = os.path.join(BASE_PATH, "imgs", "red-go-back-arrow.png")
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
        self.profile_icon = None
        profile_path = os.path.join(BASE_PATH, "imgs", "profile.png")
        if os.path.exists(profile_path):
            try:
                pimg = tk.PhotoImage(file=profile_path)
                pw = pimg.width()
                ph = pimg.height()
                target = 48
                if pw > target and ph > target:
                    factor_w = max(1, int(pw/target))
                    factor_h = max(1, int(ph/target))
                    factor = max(factor_w, factor_h)
                    pimg = pimg.subsample(factor, factor)
                self.profile_icon = pimg
            except Exception as e:
                print(f"Error cargando profile.png: {e}")
        self.icon_config = None
        self.icon_exit = None
        icon_config_path = os.path.join(BASE_PATH, "imgs", "iconoconfig.png")
        icon_exit_path = os.path.join(BASE_PATH, "imgs", "iconosalir.png")
        try:
            if os.path.exists(icon_config_path):
                ic = tk.PhotoImage(file=icon_config_path)
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
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.show_main_menu()
    def _on_closing(self):
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
    def show_main_menu(self):
        self.clear_screen()
        try:
            if not hasattr(self, 'music_started'):
                if self.music_enabled:
                    self.music_manager.play()
                self.music_started = True
        except Exception as e:
            print(f"Error iniciando música: {e}")
        banner_h = 100
        banner = tk.Canvas(self.current_screen, height=banner_h, bg=COLOR_FONDO, highlightthickness=0)
        banner.pack(fill=tk.X, side=tk.TOP, pady=(20,10))
        def _draw_banner(event=None):
            bw = max(200, banner.winfo_width() - 40)
            bx = 20
            by = 10
            br = 30
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
            banner.create_text(bx + bw/2, by + banner_h/2 - 8, text="MÉTODOS NUMÉRICOS - EL JUEGO", fill="white", font=("Arial", scale_font(22), "bold"))
            banner.create_text(bx + bw/2, by + banner_h/2 + 22, text="¡Aprende, Juega, Domina!", fill="#dfefff", font=("Arial", scale_font(12)))
        banner.bind('<Configure>', _draw_banner)
        banner.after(10, _draw_banner)
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
        btn_area = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        btn_area.pack(expand=True)
        play = GradientRoundedButton(btn_area, text="JUGAR", width=570, height=105,
                                     colors=("#20E0D0", "#FF8C5A"), text_color="#00303a",
                                     command=self.show_chapter_menu)
        play.pack(pady=(30, 22))
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
        header_frame = tk.Frame(self.current_screen, bg="#0052CC", height=HEADER_HEIGHT)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        tk.Label(header_frame, text="MENÚ DE USUARIO", font=("Arial", scale_font(20), "bold"),
                 bg="#0052CC", fg="white").pack(side=tk.LEFT, padx=20, pady=15)
        btn_back = self.create_back_button(header_frame, self.show_main_menu, "#0052CC")
        btn_back.pack(side=tk.RIGHT, anchor="center", padx=10)
        content = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        row_frame = tk.Frame(content, bg=COLOR_FONDO)
        row_frame.pack(fill=tk.BOTH, expand=False, pady=10)
        row_frame.columnconfigure(0, weight=1)
        row_frame.columnconfigure(1, weight=1)
        time_canvas = tk.Canvas(row_frame, width=550, height=180, bg=COLOR_FONDO, highlightthickness=0)
        time_canvas.grid(row=0, column=0, padx=10, sticky="ew")
        def _draw_time_card(event=None):
            time_canvas.delete("all")
            w = max(200, time_canvas.winfo_width())
            h = 180
            if PIL_AVAILABLE:
                img_time = create_rounded_rect_image(w, h, 20, "#20D0C0", "#00A8CC")
                try:
                    tkimg_time = ImageTk.PhotoImage(img_time)
                    time_canvas._img_time = tkimg_time
                    time_canvas.create_image(0, 0, anchor="nw", image=tkimg_time)
                except:
                    time_canvas.create_rectangle(0, 0, w, h, fill="#20D0C0", outline="")
            else:
                time_canvas.create_rectangle(0, 0, w, h, fill="#20D0C0", outline="")
            time_canvas.create_text(30, 50, text="⏱", font=("Arial", scale_font(32)), anchor="w", fill="white")
            time_canvas.create_text(100, 40, text="TIEMPO TRANSCURRIDO", fill="white", font=("Arial", scale_font(14), "bold"), anchor="w")
            time_canvas.time_text_id = time_canvas.create_text(100, 90, text=self._format_time(), fill="white", font=("Arial", scale_font(24), "bold"), anchor="w")
        time_canvas.bind('<Configure>', _draw_time_card)
        time_canvas.after(10, _draw_time_card)
        def _update_time_display():
            try:
                if hasattr(time_canvas, 'time_text_id'):
                    time_canvas.itemconfig(time_canvas.time_text_id, text=self._format_time())
                if self.time_elapsed_seconds % 5 == 0:
                    self._save_progress()
                self.root.after(1000, _update_time_display)
            except:
                pass  # Canvas destruido, detener actualizaciones
        _update_time_display()
        error_canvas = tk.Canvas(row_frame, width=550, height=180, bg=COLOR_FONDO, highlightthickness=0)
        error_canvas.grid(row=0, column=1, padx=10, sticky="ew")
        def _draw_error_card(event=None):
            error_canvas.delete("all")
            w = max(200, error_canvas.winfo_width())
            h = 180
            if PIL_AVAILABLE:
                img_err = create_rounded_rect_image(w, h, 20, "#FF8C42", "#E63946")
                try:
                    tkimg_err = ImageTk.PhotoImage(img_err)
                    error_canvas._img_err = tkimg_err
                    error_canvas.create_image(0, 0, anchor="nw", image=tkimg_err)
                except:
                    error_canvas.create_rectangle(0, 0, w, h, fill="#FF8C42", outline="")
            else:
                error_canvas.create_rectangle(0, 0, w, h, fill="#FF8C42", outline="")
            error_canvas.create_text(30, 50, text="✕", font=("Arial", scale_font(32)), anchor="w", fill="white")
            error_canvas.create_text(100, 40, text="ERRORES COMETIDOS", fill="white", font=("Arial", scale_font(14), "bold"), anchor="w")
            error_canvas.create_text(100, 90, text=str(self.errors_committed), fill="white", font=("Arial", scale_font(24), "bold"), anchor="w")
        error_canvas.bind('<Configure>', _draw_error_card)
        error_canvas.after(10, _draw_error_card)
        medals_label = tk.Label(content, text="MEDALLAS:", font=("Arial", scale_font(16), "bold"), bg=COLOR_FONDO, fg="white")
        medals_label.pack(pady=(20, 10), anchor="w")
        medals_frame = tk.Frame(content, bg=COLOR_FONDO)
        medals_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        if self.medals:
            filtered_medals = [m for m in self.medals if not m.startswith("FAILED_")]
            if filtered_medals:
                medals_text = "\n".join([f"🏅 {m}" for m in filtered_medals])
            else:
                medals_text = "Sin medallas aún"
        else:
            medals_text = "Sin medallas aún"
        tk.Label(medals_frame, text=medals_text, font=("Arial", scale_font(12)), bg=COLOR_FONDO, fg="white", justify=tk.LEFT).pack(anchor="w", padx=10)
    def show_config_menu(self):
        self.clear_screen()
        header_frame = tk.Frame(self.current_screen, bg="#003366", height=HEADER_HEIGHT)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        tk.Label(header_frame, text="CONFIGURACIÓN", font=("Arial", scale_font(20), "bold"),
                 bg="#003366", fg="white").pack(side=tk.LEFT, padx=20, pady=15)
        btn_back = self.create_back_button(header_frame, self.show_main_menu, "#003366")
        btn_back.pack(side=tk.RIGHT, anchor="center", padx=10)
        scroll_container = ScrollableFrame(self.current_screen, bg_color=COLOR_FONDO)
        scroll_container.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        buttons_container = tk.Frame(scroll_container.scrollable_frame, bg=COLOR_FONDO)
        buttons_container.pack(expand=True, anchor="center", pady=20)
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
        RoundedButton(buttons_container, text="🌐  IDIOMA", width=570, height=105,
                  color="#20D0C0", text_color="#ffffff",
                  command=lambda: messagebox.showinfo("Idioma", "Funcionalidad próximamente")).pack(pady=22)
        credits_text = "EQUIPO 1 - MÉTODOS NUMÉRICOS\n\nEstudiantes:\nJorge Aaron Cuellar Fuentes\n2007916\n\nGerardo Ulloa Loredo\n2001913\n\nCatedrático: ORALIA ZAMORA PEQUEÑO\nPeríodo: A2025\nGrupo: 005\nHorario: LMV, V6"
        RoundedButton(buttons_container, text="ℹ️  CRÉDITOS", width=570, height=105,
                  color="#20D0C0", text_color="#ffffff",
                  command=lambda: messagebox.showinfo("Créditos", credits_text)).pack(pady=22)
        bibliography_text = "1. Zamora Pequeño, O., Zamora Pequeño, R. S., & Del Ángel Ramírez, A. (2020). Métodos numéricos aplicados con software (2.ª ed.). Universidad Autónoma de Nuevo León.\n\n2. Python Software Foundation. (s.f.). tkinter — Python interface to Tcl/Tk. Python 3.12 Documentation.\n\n3. Python Software Foundation. (s.f.). json — JSON encoder and decoder. Python 3.12 Documentation.\n\n4. The NumPy Developers. (s.f.). NumPy documentation. NumPy."
        RoundedButton(buttons_container, text="📚  BIBLIOGRAFÍA", width=570, height=105,
                  color="#20D0C0", text_color="#ffffff",
                  command=lambda: messagebox.showinfo("Bibliografía", bibliography_text)).pack(pady=22)
        def _on_reset_click():
            response = messagebox.askyesno("Reiniciar Progreso",
                                          "¿Estás seguro de que deseas reiniciar tu progreso?\nEsta acción no se puede deshacer.")
            if response:
                self._reset_progress()
        RoundedButton(buttons_container, text="⚠️  REINICIAR PROGRESO", width=570, height=105,
                  color="#FF3333", text_color="#ffffff",
                  command=_on_reset_click).pack(pady=22)
    def show_chapter_menu(self):
        self.clear_screen()
        self.add_header_with_back("LECCIONES", self.show_main_menu)
        scroll_container = ScrollableFrame(self.current_screen, bg_color=COLOR_FONDO)
        scroll_container.pack(fill="both", expand=True, pady=20, padx=15)
        for chapter_name in GAME_STRUCTURE.keys():
            chapter_frame = tk.Frame(scroll_container.scrollable_frame, bg=COLOR_FONDO)
            chapter_frame.pack(fill=tk.X, pady=15)
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
            levels = GAME_STRUCTURE[chapter_name]['levels']
            for level_name in levels.keys():
                level_frame = tk.Frame(chapter_frame, bg="#1a3a52", highlightthickness=0)
                level_frame.pack(fill=tk.X, pady=8, padx=10)
                level_label = tk.Label(level_frame, text=level_name,
                                      font=("Arial", scale_font(13), "bold"),
                                      bg="#1a3a52", fg="white",
                                      padx=15, pady=12, anchor="w")
                level_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
                def _on_level_click(event, c=chapter_name, l=level_name):
                    self.chapter_menu_scroll_position = scroll_container.canvas.yview()[0]
                    self.show_difficulty_menu(c, l)
                try:
                    if PIL_AVAILABLE:
                        from PIL import Image as PILImage, ImageTk as PILImageTk
                        btn_img_pil = PILImage.open(os.path.join(BASE_PATH, 'imgs', 'botonnivel.png'))
                        btn_img_pil.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
                        btn_img_tk = PILImageTk.PhotoImage(btn_img_pil)
                    else:
                        btn_img_tk = tk.PhotoImage(file=os.path.join(BASE_PATH, 'imgs', 'botonnivel.png'))
                        if btn_img_tk.width() > 40:
                            factor = max(1, int(btn_img_tk.width() / 40))
                            btn_img_tk = btn_img_tk.subsample(factor)
                    level_btn = tk.Label(level_frame, image=btn_img_tk,
                                        bg="#1a3a52", padx=15, pady=12, cursor="hand2")
                    level_btn.image = btn_img_tk  # Keep reference
                    level_btn.pack(side=tk.RIGHT)
                    level_btn.bind("<Button-1>", _on_level_click)
                except Exception:
                    level_btn = tk.Label(level_frame, text="➤",
                                        font=("Arial", scale_font(18), "bold"),
                                        bg="#1a3a52", fg="white",
                                        padx=15, pady=12, cursor="hand2")
                    level_btn.pack(side=tk.RIGHT)
                    level_btn.bind("<Button-1>", _on_level_click)
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
        self.root.after(100, lambda: self._restore_scroll_position(scroll_container))
    def show_level_menu(self, chapter_name):
        pass
    def _restore_scroll_position(self, scroll_container):
        try:
            if self.chapter_menu_scroll_position > 0:
                scroll_container.canvas.yview_moveto(self.chapter_menu_scroll_position)
        except Exception as e:
            print(f"Error al restaurar posición del scroll: {e}")
    def show_difficulty_menu(self, chapter, level):
        self.clear_screen()
        try:
            if self.music_enabled:
                self.music_manager.fade_in(duration=3.0, target_volume=self.music_volume)
        except Exception as e:
            print(f"Error en fade in de música: {e}")
        self.add_header_with_back(level, self.show_chapter_menu)
        container = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        container.pack(expand=True)
        RoundedButton(container, text="Fácil   ★", width=300, height=60,
                      color=BTN_EASY_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Fácil", 0)).pack(pady=15)
        RoundedButton(container, text="Intermedio   ★★", width=300, height=60,
                      color=BTN_INTER_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Intermedio", 0)).pack(pady=15)
        RoundedButton(container, text="Avanzado   ★★★", width=300, height=60,
                      color=BTN_ADV_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Avanzado", 0)).pack(pady=15)
        RoundedButton(container, text="Prueba Final   🏆", width=300, height=60,
                      color=BTN_FINAL_COLOR, text_color="white",
                      command=lambda: self.start_lesson(chapter, level, "Prueba Final", 0)).pack(pady=15)
    def start_lesson(self, chapter, level, difficulty, lesson_index):
        try:
            if self.music_enabled:
                self.music_manager.fade_out(duration=5.0)
        except Exception as e:
            print(f"Error en fade out de música: {e}")
        self.clear_screen()
        method_info = get_method_info(chapter, level, difficulty)
        if method_info and 'function' in method_info:
            func_name = method_info['function']
            if hasattr(additional_methods, func_name):
                func = getattr(additional_methods, func_name)
                func(chapter, level, difficulty, lesson_index)
                return
            elif hasattr(self, func_name):
                func = getattr(self, func_name)
                func(chapter, level, difficulty, lesson_index)
                return
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
            medal_name = f"{level} ({difficulty})"
            if medal_name not in self.medals:
                self.medals.append(medal_name)
            self.show_difficulty_menu(chapter, level)
            return
        current_lesson = lessons[lesson_index]
        lesson_type = current_lesson['type']
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
    
    def _show_generic_problem(self, problem_id, chapter, level, difficulty, lesson_index):
        import random
        problem_data = PROBLEM_DATA.get(problem_id, {})
        if not problem_data:
            messagebox.showerror("Error", f"No se encontraron datos para el problema: {problem_id}")
            self.show_difficulty_menu(chapter, level)
            return
        medal_str = f"{level} ({difficulty})"
        is_final = difficulty.lower() == 'prueba final'
        if is_final:
            failed_key = f"FAILED_{medal_str}"
            if failed_key in self.medals:
                messagebox.showwarning("Prueba Bloqueada",
                    "⛔ Esta Prueba Final está BLOQUEADA.\n\n" +
                    "Has fallado previamente esta prueba.\n" +
                    "No puedes volver a intentarla.")
                self.show_difficulty_menu(chapter, level)
                return
            if medal_str in self.medals:
                messagebox.showinfo("Prueba Completada",
                    "✅ Ya has completado esta Prueba Final exitosamente.\n\n" +
                    "No puedes volver a realizarla.")
                self.show_difficulty_menu(chapter, level)
                return
        style = DIFFICULTY_STYLES.get(difficulty.lower(), DIFFICULTY_STYLES['intermedio'])
        banner_color = style['banner_color']
        banner_frame = tk.Frame(self.current_screen, bg=banner_color, height=style['banner_height'])
        banner_frame.pack(fill=tk.X, side=tk.TOP)
        banner_frame.pack_propagate(False)
        chapter_num = chapter.split(':')[0].replace('Capítulo', '').strip()
        banner_text = f"{chapter.split(':')[1].strip() if ':' in chapter else chapter} - {level.split(':')[1].strip() if ':' in level else level} - {difficulty}"
        tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"),
                bg=banner_color, fg=style['banner_text_color']).pack(side=tk.LEFT, padx=20, pady=15)
        try:
            if PIL_AVAILABLE:
                from PIL import Image as PILImage, ImageTk as PILImageTk
                pil_img = PILImage.open(os.path.join(BASE_PATH, 'imgs', 'red-go-back-arrow.png'))
                pil_img.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
                back_arrow_img = PILImageTk.PhotoImage(pil_img)
            else:
                back_arrow_img = tk.PhotoImage(file=os.path.join(BASE_PATH, 'imgs', 'red-go-back-arrow.png'))
                if back_arrow_img.width() > 40:
                    factor = max(1, int(back_arrow_img.width() / 40))
                    back_arrow_img = back_arrow_img.subsample(factor)
            back_btn = tk.Label(banner_frame, image=back_arrow_img, bg=banner_color, cursor="hand2")
            back_btn.image = back_arrow_img
            back_btn.pack(side=tk.RIGHT, padx=15, pady=10)
            if is_final:
                back_btn.bind("<Button-1>", lambda e: self._confirm_exit_final(chapter, level))
            else:
                back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        except Exception:
            back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"),
                               bg=banner_color, fg="#FF5733", cursor="hand2")
            back_btn.pack(side=tk.RIGHT, padx=20, pady=10)
            if is_final:
                back_btn.bind("<Button-1>", lambda e: self._confirm_exit_final(chapter, level))
            else:
                back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        main_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        tk.Label(main_frame, text=problem_data.get('title', "Problema"), font=("Arial", scale_font(18), "bold"),
                bg=COLOR_FONDO, fg=style['title_color']).pack(pady=10)
        top_content_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        top_content_frame.pack(pady=15, fill=tk.X)
        x_val = problem_data.get('x_value')
        if x_val is not None:
            tk.Label(top_content_frame, text=f"x = {x_val}", font=("Arial", scale_font(16), "bold"),
                    bg=COLOR_FONDO, fg="white").pack(side=tk.LEFT, padx=20)
        table_data = problem_data.get('table', [])
        if table_data:
            table_frame = tk.Frame(top_content_frame, bg=COLOR_FONDO)
            table_frame.pack(side=tk.LEFT, padx=20)
            for row_data in table_data:
                if isinstance(row_data, tuple):
                    if len(row_data) == 1:
                        tk.Label(table_frame, text=str(row_data[0]), font=("Arial", scale_font(13), "bold"),
                                bg=COLOR_FONDO, fg=style['title_color'], padx=5, pady=3).pack(pady=2)
                    elif len(row_data) == 2:
                        if isinstance(row_data[0], (int, float)) and isinstance(row_data[1], (int, float)):
                            row_frame = tk.Frame(table_frame, bg=style['table_header_bg'], bd=1, relief=tk.SOLID)
                            row_frame.pack(pady=2)
                            tk.Label(row_frame, text=f"{row_data[0]}", font=("Arial", scale_font(12), "bold"),
                                    bg=style['table_header_bg'], fg=style['table_header_fg'], width=8).pack(side=tk.LEFT, padx=4, pady=4)
                            tk.Label(row_frame, text=f"{row_data[1]}", font=("Arial", scale_font(12), "bold"),
                                    bg=style['table_header_bg'], fg=style['table_header_fg'], width=8).pack(side=tk.LEFT, padx=4, pady=4)
                        else:
                            tk.Label(table_frame, text=f"{row_data[0]} → {row_data[1]}", 
                                    font=("Arial", scale_font(11)), bg=COLOR_FONDO, fg="white").pack(pady=2)
                    else:
                        for item in row_data:
                            tk.Label(table_frame, text=str(item), font=("Arial", scale_font(12), "italic"),
                                    bg="#34495e", fg="#ecf0f1", padx=10, pady=5, relief=tk.RAISED).pack(pady=3)
        timer_container = tk.Frame(top_content_frame, bg=COLOR_FONDO)
        time_min = problem_data.get('time_minutes')
        
        # Los problemas Fácil no tienen temporizador
        if time_min is None or difficulty.lower() == 'fácil':
            timer_container.pack_forget()  # No mostrar timer para Fácil
            timer_state = {'seconds': 0, 'timer_id': None}
            timer_label = None
        else:
            timer_container.pack(side=tk.RIGHT, padx=20)
            tk.Label(timer_container, text="⏱", font=("Arial", scale_font(24)),
                    bg=COLOR_FONDO, fg="white").pack(pady=5)
            tk.Label(timer_container, text="Tiempo restante", font=("Arial", scale_font(12), "bold"),
                    bg=COLOR_FONDO, fg="white").pack()
            timer_label = tk.Label(timer_container, text=f"{time_min}:00", font=("Arial", scale_font(20), "bold"),
                                  bg=COLOR_FONDO, fg=style['timer_color'])
            timer_label.pack(pady=5)
            timer_state = {'seconds': time_min * 60, 'timer_id': None}
        def _update_timer():
            if timer_label is None:  # No hay timer para Fácil
                return
            timer_state['seconds'] -= 1
            minutes = timer_state['seconds'] // 60
            seconds = timer_state['seconds'] % 60
            time_str = f"{minutes}:{seconds:02d}"
            timer_label.config(text=time_str)
            if timer_state['seconds'] > 0:
                timer_state['timer_id'] = self.root.after(1000, _update_timer)
            else:
                messagebox.showinfo("Tiempo agotado", "Se acabó el tiempo para resolver el problema.")
                if is_final:
                    self.errors_committed += 1
                self._save_progress()
                self.show_difficulty_menu(chapter, level)
        _update_timer()
        options_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
        options_frame.pack(pady=30, fill=tk.BOTH, expand=True)
        tk.Label(options_frame, text="Selecciona la respuesta:", font=("Arial", scale_font(16), "bold"),
                bg=COLOR_FONDO, fg="white").pack(pady=15)
        btn_frame = tk.Frame(options_frame, bg=COLOR_FONDO)
        btn_frame.pack(pady=20)
        options_values = problem_data.get('options', [])
        correct_answer = problem_data.get('correct', '')
        random.shuffle(options_values)
        def _make_handler(option_text):
            def _handler():
                if timer_state['timer_id']:
                    self.root.after_cancel(timer_state['timer_id'])
                if option_text == correct_answer:
                    if is_final:
                        if medal_str not in self.medals:
                            self.medals.append(medal_str)
                        self._save_progress()
                        messagebox.showinfo("¡Correcto!", f"¡Excelente! ¡Prueba Final completada!")
                        self.show_difficulty_menu(chapter, level)
                    else:
                        messagebox.showinfo("¡Correcto!", f"¡Excelente!")
                        self._save_progress()
                        self.start_lesson(chapter, level, difficulty, lesson_index + 1)
                else:
                    self.errors_committed += 1
                    if is_final:
                        failed_key = f"FAILED_{medal_str}"
                        if failed_key not in self.medals:
                            self.medals.append(failed_key)
                        self._save_progress()
                        messagebox.showerror("Prueba Final Fallida",
                            "❌ Respuesta incorrecta.\n\n" +
                            "Has fallado la Prueba Final.\n" +
                            "Esta prueba quedará BLOQUEADA permanentemente.\n" +
                            "No se otorga medalla.")
                        self.show_difficulty_menu(chapter, level)
                    else:
                        messagebox.showinfo("Incorrecto", "Lo siento, esa respuesta no es correcta.")
                        self._save_progress()
                        self.show_difficulty_menu(chapter, level)
            return _handler
        for opt_text in options_values:
            btn = RoundedButton(btn_frame, text=opt_text, width=180, height=90,
                              color=style['button_color'], text_color=style['button_text_color'],
                              command=_make_handler(opt_text))
            btn.pack(side=tk.LEFT, padx=12)
    
    def _show_lagrange_intermedio(self, chapter, level, difficulty, lesson_index):
        return self._show_generic_problem('lagrange_intermedio', chapter, level, difficulty, lesson_index)
    
    def _show_lagrange_avanzado(self, chapter, level, difficulty, lesson_index):
        return self._show_generic_problem('lagrange_avanzado', chapter, level, difficulty, lesson_index)
    
    def _show_lagrange_final(self, chapter, level, difficulty, lesson_index):
        return self._show_generic_problem('lagrange_final', chapter, level, difficulty, lesson_index)
    
    def _show_standard_question(self, lesson, chapter, level, difficulty, lesson_index):
        style = DIFFICULTY_STYLES.get(difficulty.lower(), DIFFICULTY_STYLES['intermedio'])
        banner_frame = tk.Frame(self.current_screen, bg=style['banner_color'], height=style['banner_height'])
        banner_frame.pack(fill=tk.X, side=tk.TOP)
        banner_frame.pack_propagate(False)
        chapter_num = chapter.split(':')[0].replace('Capítulo', '').strip()
        banner_text = f"Capítulo {chapter_num} - {level.split(':')[1].strip() if ':' in level else level} - {difficulty}"
        tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"),
                bg=style['banner_color'], fg=style['banner_text_color']).pack(side=tk.LEFT, padx=20, pady=15)
        try:
            if PIL_AVAILABLE:
                from PIL import Image as PILImage, ImageTk as PILImageTk
                pil_img = PILImage.open(os.path.join(BASE_PATH, 'imgs', 'red-go-back-arrow.png'))
                pil_img.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
                back_arrow_img = PILImageTk.PhotoImage(pil_img)
            else:
                back_arrow_img = tk.PhotoImage(file=os.path.join(BASE_PATH, 'imgs', 'red-go-back-arrow.png'))
                if back_arrow_img.width() > 40:
                    factor = max(1, int(back_arrow_img.width() / 40))
                    back_arrow_img = back_arrow_img.subsample(factor)
            back_btn = tk.Label(banner_frame, image=back_arrow_img, bg=style['banner_color'], cursor="hand2")
            back_btn.image = back_arrow_img
            back_btn.pack(side=tk.RIGHT, padx=15, pady=10)
            back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        except Exception:
            back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"),
                               bg=style['banner_color'], fg="#FF5733", cursor="hand2")
            back_btn.pack(side=tk.RIGHT, padx=20, pady=10)
            back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
        content_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
        content_frame.pack(fill=tk.BOTH, expand=True, pady=30, padx=20)
        if 'content' in lesson:
            tk.Label(content_frame, text=lesson['content'],
                    wraplength=900, font=("Arial", scale_font(14), "bold"),
                    bg=COLOR_FONDO, fg=style['title_color'], justify=tk.LEFT).pack(pady=20)
        if 'options' in lesson and 'answer' in lesson:
            btns_frame = tk.Frame(content_frame, bg=COLOR_FONDO)
            btns_frame.pack(pady=20)
            for option in lesson['options']:
                btn = RoundedButton(btns_frame, text=option, width=200, height=70,
                                  color=style['button_color'], text_color=style['button_text_color'],
                                  command=lambda o=option: self.check_answer(o, lesson, chapter, level, difficulty, lesson_index))
                btn.pack(side=tk.LEFT, padx=10)
    
    def show_practica(self, lesson, chapter, level, difficulty, lesson_index):
        import random
        if 'problem_id' in lesson:
            return self._show_generic_problem(lesson['problem_id'], chapter, level, difficulty, lesson_index)
        if 'options' in lesson and 'answer' in lesson:
            return self._show_standard_question(lesson, chapter, level, difficulty, lesson_index)
        try:
            is_lagrange_intermedio = 'Lagrange' in level and difficulty.lower() == 'intermedio'
        except Exception:
            is_lagrange_intermedio = False
        if is_lagrange_intermedio:
            return self._show_lagrange_intermedio(chapter, level, difficulty, lesson_index)
        try:
            is_lagrange_avanzado = 'Lagrange' in level and difficulty.lower() == 'avanzado'
        except Exception:
            is_lagrange_avanzado = False
        if is_lagrange_avanzado:
            return self._show_lagrange_avanzado(chapter, level, difficulty, lesson_index)
        try:
            is_lagrange_final = 'Lagrange' in level and difficulty.lower() == 'prueba final'
        except Exception:
            is_lagrange_final = False
        if is_lagrange_final:
            return self._show_lagrange_final(chapter, level, difficulty, lesson_index)
        try:
            is_lagrange = 'Lagrange' in level and difficulty.lower() == 'fácil'
        except Exception:
            is_lagrange = False
        if is_lagrange:
            img_dir = os.path.join(BASE_PATH, 'imgs', 'Lagrange')
            if not os.path.exists(img_dir):
                tk.Label(self.current_screen, text="Carpeta de imágenes de Lagrange no encontrada.", bg=COLOR_FONDO, fg='white').pack(pady=20)
                return
            is_final = False  # Lagrange Fácil nunca es Final
            lagrange_state = {
                'current_question_index': 0,
                'total_correct': 0,
                'formula_seen': False,
                'questions_list': []  # Lista de (imagen_file, answer_text)
            }
            question_images = []
            for f in os.listdir(img_dir):
                name, ext = os.path.splitext(f)
                if name.lower().startswith('formulaoriginal'):
                    continue
                if ext.lower() not in ('.png', '.jpg', '.gif', '.bmp'):
                    continue
                question_images.append(f)
            random.shuffle(question_images)
            lagrange_state['questions_list'] = question_images
            fake_answers = LAGRANGE_FAKE_ANSWERS
            def _show_formula():
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
                for w in self.current_screen.winfo_children():
                    w.destroy()
                if lagrange_state['current_question_index'] >= len(lagrange_state['questions_list']):
                    messagebox.showinfo("¡Completado!", f"¡Felicidades! Has completado el nivel Lagrange Fácil.")
                    medal_str = f"{level} ({difficulty})"
                    if medal_str not in self.medals:
                        self.medals.append(medal_str)
                    self._save_progress()
                    self.start_lesson(chapter, level, difficulty, lesson_index + 1)
                    return
                banner_frame = tk.Frame(self.current_screen, bg="#00e676", height=60)
                banner_frame.pack(fill=tk.X, side=tk.TOP)
                banner_frame.pack_propagate(False)
                banner_text = f"Capítulo 1 Nivel 1. Lagrange. {difficulty}"
                tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"),
                        bg="#00e676", fg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=10)
                try:
                    if PIL_AVAILABLE:
                        from PIL import Image, ImageTk as PILImageTk
                        pil_img = Image.open(os.path.join(BASE_PATH, 'imgs', 'red-go-back-arrow.png'))
                        pil_img.thumbnail((40, 40), Image.Resampling.LANCZOS)
                        back_arrow_img = PILImageTk.PhotoImage(pil_img)
                    else:
                        back_arrow_img = tk.PhotoImage(file=os.path.join(BASE_PATH, 'imgs', 'red-go-back-arrow.png'))
                        if back_arrow_img.width() > 40:
                            factor = max(1, int(back_arrow_img.width() / 40))
                            back_arrow_img = back_arrow_img.subsample(factor)
                    back_btn = tk.Label(banner_frame, image=back_arrow_img, bg="#00e676", cursor="hand2")
                    back_btn.image = back_arrow_img  # Keep reference
                    back_btn.pack(side=tk.RIGHT, padx=15, pady=10)
                    if is_final:
                        back_btn.bind("<Button-1>", lambda e: self._confirm_exit_final(chapter, level))
                    else:
                        back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
                except Exception:
                    back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"),
                                       bg="#00e676", fg="#FF5733", cursor="hand2")
                    back_btn.pack(side=tk.RIGHT, padx=20, pady=10)
                    if is_final:
                        back_btn.bind("<Button-1>", lambda e: self._confirm_exit_final(chapter, level))
                    else:
                        back_btn.bind("<Button-1>", lambda e: self.show_difficulty_menu(chapter, level))
                current_image_file = lagrange_state['questions_list'][lagrange_state['current_question_index']]
                current_image_path = os.path.join(img_dir, current_image_file)
                current_answer = os.path.splitext(current_image_file)[0]
                img_frame = tk.Frame(self.current_screen, bg=COLOR_FONDO)
                img_frame.pack(pady=30)
                if os.path.exists(current_image_path):
                    try:
                        display_img = tk.PhotoImage(file=current_image_path)
                        if display_img.height() > 250:
                            factor = max(1, int(display_img.height() / 250))
                            display_img = display_img.subsample(factor)
                        img_lbl = tk.Label(img_frame, image=display_img, bg=COLOR_FONDO)
                        img_lbl.image = display_img
                        img_lbl.pack()
                    except Exception:
                        tk.Label(img_frame, text=f"No se pudo cargar: {current_image_file}", bg=COLOR_FONDO, fg="white").pack()
                tk.Label(self.current_screen, text="¿Qué falta en esta parte de la fórmula de Lagrange?", font=("Arial", scale_font(14), "bold"),
                        bg=COLOR_FONDO, fg="white").pack(pady=15)
                correct_option = current_answer
                if current_answer in fake_answers:
                    fake_opts = fake_answers[current_answer]
                    wrong_options = random.sample(fake_opts, min(3, len(fake_opts)))
                else:
                    wrong_options = [f"Opción {i}" for i in range(1, 4)]
                all_options = [correct_option] + wrong_options
                random.shuffle(all_options)
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
                for option_text in all_options:
                    btn = RoundedButton(btns_frame, text=option_text, width=120, height=50,
                                      color=BTN_EASY_COLOR, text_color="#000000",
                                      command=_make_answer_handler(option_text))
                    btn.pack(side=tk.LEFT, padx=8)
            _show_formula()
            return
    
    def check_answer(self, user_answer, lesson, chapter, level, difficulty, lesson_index):
        correct_answer = lesson['answer']
        lesson_type = lesson['type']
        if user_answer == correct_answer:
            messagebox.showinfo("¡Correcto!", "¡Muy bien!")
            self.start_lesson(chapter, level, difficulty, lesson_index + 1)
        else:
            self.errors_committed += 1
            self._save_progress()  # Guardar error cometido
            if difficulty.lower() == 'fácil':
                if lesson_type == 'practica':
                    messagebox.showerror("Incorrecto", f"Respuesta correcta: '{correct_answer}'.")
                    self.start_lesson(chapter, level, difficulty, max(0, lesson_index - 1))
                elif lesson_type == 'examen':
                    messagebox.showerror("Incorrecto", "Fallo crítico. Reiniciando sección.")
                    self.start_lesson(chapter, level, difficulty, 0)
            else:
                messagebox.showinfo("Incorrecto", "Lo siento, esa respuesta no es correcta.")
                self.show_difficulty_menu(chapter, level)
    def _start_timer(self):
        def _increment_time():
            self.time_elapsed_seconds += 1
            self.root.after(1000, _increment_time)
        self.root.after(1000, _increment_time)
    def _confirm_exit_final(self, chapter, level):
        """Confirma si el usuario desea salir de una Prueba Final"""
        response = messagebox.askyesno(
            "⚠️  Salir de Prueba Final",
            "¿Estás seguro de que deseas salir?\n\n"
            "Si sales ahora:\n"
            "• La Prueba Final se bloqueará permanentemente\n"
            "• No obtendrás la medalla\n"
            "• No podrás intentarla de nuevo\n\n"
            "¿Confirmas que deseas salir?"
        )
        if response:
            # Marcar como fallida para bloquear la prueba
            medal_str = f"{level} (Prueba Final)"
            failed_key = f"FAILED_{medal_str}"
            if failed_key not in self.medals:
                self.medals.append(failed_key)
            self._save_progress()
            self.show_difficulty_menu(chapter, level)
    def _format_time(self):
        hours = self.time_elapsed_seconds // 3600
        minutes = (self.time_elapsed_seconds % 3600) // 60
        return f"{hours}h {minutes}m"
    def _save_progress(self):
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
        self.time_elapsed_seconds = 0
        self.errors_committed = 0
        self.medals = []
        self.music_enabled = True
        self.music_volume = 0.7
        self._save_progress()
        messagebox.showinfo("Progreso Reiniciado", "Tu progreso ha sido reiniciado. ¡A jugar!")
        self.show_main_menu()