
import tkinter as tk
from tkinter import messagebox
import random
import os
from numerical_methods_lessons import *
app_ref = None
scale_font = None  # Se asignará en set_app_reference
PIL_AVAILABLE = False  # Se asignará en set_app_reference
COLOR_FONDO = "#001F3F"  # Se asignará en set_app_reference
def set_app_reference(app):
    global app_ref, scale_font, PIL_AVAILABLE, COLOR_FONDO
    app_ref = app
    from game_app import scale_font as sf, PIL_AVAILABLE as pil_avail, COLOR_FONDO as cf
    scale_font = sf
    PIL_AVAILABLE = pil_avail
    COLOR_FONDO = cf
def show_interpolacion_lineal(chapter, level, difficulty, lesson_index):
    difficulty_key = difficulty.lower().replace(' ', '').replace('pruebafinal', 'final')
    data = LINEAL_LESSONS[difficulty_key]
    colors = {'intermedio': '#FFB6C1', 'avanzado': '#FF69B4', 'final': '#FF1493'}
    color = colors.get(difficulty_key, '#FFB6C1')
    _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, "Interpolación Lineal", color)
def show_newton_forward(chapter, level, difficulty, lesson_index):
    difficulty_key = difficulty.lower().replace(' ', '').replace('pruebafinal', 'final')
    data = NEWTON_FORWARD_LESSONS[difficulty_key]
    colors = {'intermedio': '#90EE90', 'avanzado': '#32CD32', 'final': '#228B22'}
    color = colors.get(difficulty_key, '#90EE90')
    _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, "Newton Hacia Adelante", color)
def show_newton_backward(chapter, level, difficulty, lesson_index):
    difficulty_key = difficulty.lower().replace(' ', '').replace('pruebafinal', 'final')
    data = NEWTON_BACKWARD_LESSONS[difficulty_key]
    colors = {'intermedio': '#87CEEB', 'avanzado': '#4169E1', 'final': '#00008B'}
    color = colors.get(difficulty_key, '#87CEEB')
    _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, "Newton Hacia Atrás", color)
def show_newton_divided_diff(chapter, level, difficulty, lesson_index):
    difficulty_key = difficulty.lower().replace(' ', '').replace('pruebafinal', 'final')
    data = NEWTON_DIVIDED_DIFF_LESSONS[difficulty_key]
    colors = {'intermedio': '#DDA0DD', 'avanzado': '#BA55D3', 'final': '#8B008B'}
    color = colors.get(difficulty_key, '#DDA0DD')
    _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, "Newton Diferencias Divididas", color)
def _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, method_name, banner_color):
    if not app_ref:
        return
    is_final = difficulty == "Prueba Final"
    if is_final:
        medal_str = f"{level} ({difficulty})"
        if medal_str in app_ref.medals:
            messagebox.showinfo("Prueba Final", "Ya completaste esta Prueba Final.")
            app_ref.show_difficulty_menu(chapter, level)
            return
    banner_frame = tk.Frame(app_ref.current_screen, bg=banner_color, height=70)
    banner_frame.pack(fill=tk.X, side=tk.TOP)
    banner_frame.pack_propagate(False)
    chapter_num = chapter.split()[1].rstrip(':') if 'Capítulo' in chapter else "1"
    level_num = level.split()[1].rstrip(':') if 'Nivel' in level else level
    banner_text = f"Capítulo {chapter_num} Nivel {level_num}. {method_name}. {difficulty}"
    tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"),
            bg=banner_color, fg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=15)
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
        back_btn = tk.Label(banner_frame, image=back_arrow_img, bg=banner_color, cursor="hand2")
        back_btn.image = back_arrow_img
        back_btn.pack(side=tk.RIGHT, padx=20, pady=15)
        if is_final:
            back_btn.bind("<Button-1>", lambda e: app_ref._confirm_exit_final(chapter, level))
        else:
            back_btn.bind("<Button-1>", lambda e: app_ref.show_difficulty_menu(chapter, level))
    except Exception:
        back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"),
                           bg=banner_color, fg="#FFFFFF", cursor="hand2")
        back_btn.pack(side=tk.RIGHT, padx=20, pady=15)
        if is_final:
            back_btn.bind("<Button-1>", lambda e: app_ref._confirm_exit_final(chapter, level))
        else:
            back_btn.bind("<Button-1>", lambda e: app_ref.show_difficulty_menu(chapter, level))
    main_frame = tk.Frame(app_ref.current_screen, bg=COLOR_FONDO)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    tk.Label(main_frame, text="Obtener g(x)", font=("Arial", scale_font(18), "bold"),
            bg=COLOR_FONDO, fg="#20E0D0").pack(pady=10)
    top_content_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
    top_content_frame.pack(pady=15, fill=tk.X)
    tk.Label(top_content_frame, text=f"x = {data['x_to_find']}", font=("Arial", scale_font(16), "bold"),
            bg=COLOR_FONDO, fg="white").pack(side=tk.LEFT, padx=20)
    table_frame = tk.Frame(top_content_frame, bg="white", highlightthickness=2, highlightbackground="#20E0D0")
    table_frame.pack(side=tk.LEFT, padx=20)
    header_x = tk.Label(table_frame, text="x", font=("Arial", scale_font(12), "bold"),
                       bg="#20E0D0", fg="white", width=10, height=2)
    header_x.grid(row=0, column=0, sticky="nsew")
    header_y = tk.Label(table_frame, text="y", font=("Arial", scale_font(12), "bold"),
                       bg="#20E0D0", fg="white", width=10, height=2)
    header_y.grid(row=0, column=1, sticky="nsew")
    for i, (x_val, y_val) in enumerate(data['data'], 1):
        cell_x = tk.Label(table_frame, text=f"{x_val:.1f}", font=("Arial", scale_font(11)),
                         bg="white", fg="black", width=10, height=2, relief=tk.RIDGE)
        cell_x.grid(row=i, column=0, sticky="nsew")
        cell_y = tk.Label(table_frame, text=f"{y_val:.5f}", font=("Arial", scale_font(11)),
                         bg="white", fg="black", width=10, height=2, relief=tk.RIDGE)
        cell_y.grid(row=i, column=1, sticky="nsew")
    timer_container = tk.Frame(top_content_frame, bg=COLOR_FONDO)
    timer_container.pack(side=tk.RIGHT, padx=20)
    tk.Label(timer_container, text="⏱", font=("Arial", scale_font(24)),
            bg=COLOR_FONDO, fg="white").pack(pady=5)
    tk.Label(timer_container, text="Tiempo restante", font=("Arial", scale_font(12), "bold"),
            bg=COLOR_FONDO, fg="white").pack()
    timer_label = tk.Label(timer_container, text="00:00", font=("Arial", scale_font(20), "bold"),
                          bg=COLOR_FONDO, fg="#20E0D0")
    timer_label.pack(pady=5)
    timer_state = {'seconds': data['time'], 'timer_id': None}
    def _update_timer():
        timer_state['seconds'] -= 1
        minutes = timer_state['seconds'] // 60
        seconds = timer_state['seconds'] % 60
        time_str = f"{minutes}:{seconds:02d}"
        timer_label.config(text=time_str)
        if timer_state['seconds'] > 0:
            timer_state['timer_id'] = app_ref.root.after(1000, _update_timer)
        else:
            messagebox.showinfo("Tiempo agotado", "Se acabó el tiempo para resolver el problema.")
            app_ref.show_difficulty_menu(chapter, level)
    _update_timer()
    options_frame = tk.Frame(main_frame, bg=COLOR_FONDO)
    options_frame.pack(pady=30, fill=tk.BOTH, expand=True)
    tk.Label(options_frame, text="g(x) =", font=("Arial", scale_font(16), "bold"),
            bg=COLOR_FONDO, fg="white").pack(pady=15)
    btn_frame = tk.Frame(options_frame, bg=COLOR_FONDO)
    btn_frame.pack(pady=20)
    options_values = data['options'].copy()
    correct_answer = data['answer']
    random.shuffle(options_values)
    def _make_handler(option_text):
        def _handler():
            if timer_state['timer_id']:
                app_ref.root.after_cancel(timer_state['timer_id'])
            if option_text == correct_answer:
                messagebox.showinfo("¡Correcto!", f"¡Excelente!")
                if is_final:
                    if f"{level} ({difficulty})" not in app_ref.medals:
                        app_ref.medals.append(f"{level} ({difficulty})")
                    app_ref._save_progress()
                app_ref.start_lesson(chapter, level, difficulty, lesson_index + 1)
            else:
                messagebox.showinfo("Incorrecto", "Lo siento, esa respuesta no es correcta.")
                app_ref.errors_committed += 1
                app_ref._save_progress()
                app_ref.show_difficulty_menu(chapter, level)
        return _handler
    for opt_text in options_values:
        btn = app_ref.RoundedButton(btn_frame, text=opt_text, width=140, height=80,
                          color=app_ref.BTN_EASY_COLOR, text_color="#000000",
                          command=_make_handler(opt_text))
        btn.pack(side=tk.LEFT, padx=10)
def show_gauss_seidel(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Gauss-Seidel será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_jacobi(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Jacobi será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_montante(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Montante será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_gauss_jordan(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Gauss-Jordán será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_eliminacion_gaussiana(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Eliminación Gaussiana será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_bisection(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Bisección será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_falsa_posicion(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Falsa Posición será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_newton_raphson(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Newton-Raphson será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_punto_fijo(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Punto Fijo será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_secante(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Secante será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_euler(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Euler será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_euler_modificado(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Euler Modificado será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_rk2(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "RK2 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_rk3(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "RK3 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_rk4(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "RK4 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_trapezoidal(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Trapezoidal será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_simpson_13(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Simpson 1/3 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_simpson_38(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Simpson 3/8 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_newton_cotes_cerradas(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Newton-Cotes Cerradas será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_newton_cotes_abiertas(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Newton-Cotes Abiertas será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_minimos_cuadrados_lineal(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Lineal será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_minimos_cuadrados_cuadratica(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Cuadrática será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_minimos_cuadrados_cubica(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Cúbica será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_minimos_cuadrados_lineal_func(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Lineal con Función será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
def show_minimos_cuadrados_cuadratica_func(chapter, level, difficulty, lesson_index):
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Cuadrática con Función será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
