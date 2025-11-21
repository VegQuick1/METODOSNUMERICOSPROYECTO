# additional_methods.py
# Módulo con métodos adicionales para todos los capítulos
# Importar al inicio de game_app.py: from additional_methods import *

import tkinter as tk
from tkinter import messagebox
import random
import os
from numerical_methods_lessons import *

# Referencia a la aplicación (será asignada después)
app_ref = None
scale_font = None  # Se asignará en set_app_reference

def set_app_reference(app):
    """Establecer referencia a la aplicación principal"""
    global app_ref, scale_font
    app_ref = app
    # Importar scale_font desde game_app
    from game_app import scale_font as sf
    scale_font = sf

# ============================================================================
# CAPÍTULO 1: INTERPOLACIÓN - MÉTODOS ADICIONALES
# ============================================================================

def show_interpolacion_lineal(chapter, level, difficulty, lesson_index):
    """Mostrar ejercicio de Interpolación Lineal"""
    difficulty_key = difficulty.lower().replace(' ', '').replace('pruebafinal', 'final')
    data = LINEAL_LESSONS[difficulty_key]
    _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, "Interpolación Lineal", "#FFB6C1")

def show_newton_forward(chapter, level, difficulty, lesson_index):
    """Mostrar ejercicio de Newton Hacia Adelante"""
    difficulty_key = difficulty.lower().replace(' ', '').replace('pruebafinal', 'final')
    data = NEWTON_FORWARD_LESSONS[difficulty_key]
    _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, "Newton Hacia Adelante", "#90EE90")

def show_newton_backward(chapter, level, difficulty, lesson_index):
    """Mostrar ejercicio de Newton Hacia Atrás"""
    difficulty_key = difficulty.lower().replace(' ', '').replace('pruebafinal', 'final')
    data = NEWTON_BACKWARD_LESSONS[difficulty_key]
    _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, "Newton Hacia Atrás", "#87CEEB")

def show_newton_divided_diff(chapter, level, difficulty, lesson_index):
    """Mostrar ejercicio de Newton Diferencias Divididas"""
    difficulty_key = difficulty.lower().replace(' ', '').replace('pruebafinal', 'final')
    data = NEWTON_DIVIDED_DIFF_LESSONS[difficulty_key]
    _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, "Newton Diferencias Divididas", "#DDA0DD")

def _show_generic_interpolation_exercise(chapter, level, difficulty, lesson_index, data, method_name, banner_color):
    """Función genérica para mostrar ejercicios de interpolación"""
    if not app_ref:
        return
    
    # Verificar si es prueba final
    is_final = difficulty == "Prueba Final"
    if is_final:
        medal_str = f"{level} ({difficulty})"
        if medal_str in app_ref.medals:
            messagebox.showinfo("Prueba Final", "Ya completaste esta Prueba Final.")
            app_ref.show_difficulty_menu(chapter, level)
            return
    
    # === BANNER SUPERIOR ===
    banner_frame = tk.Frame(app_ref.current_screen, bg=banner_color, height=60)
    banner_frame.pack(fill=tk.X, side=tk.TOP)
    banner_frame.pack_propagate(False)
    
    # Extraer número del capítulo (ej: "Capítulo 1: Interpolación" → "1")
    chapter_num = chapter.split()[1].rstrip(':') if 'Capítulo' in chapter else "1"
    
    # Extraer número del nivel (ej: "Nivel 2: Interpolación Lineal" → "2")
    level_num = level.split()[1].rstrip(':') if 'Nivel' in level else level
    
    banner_text = f"Capítulo {chapter_num} Nivel {level_num}. {method_name}. {difficulty}"
    tk.Label(banner_frame, text=banner_text, font=("Arial", scale_font(16), "bold"), 
            bg=banner_color, fg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=10)
    
    # Botón de retroceso
    try:
        from PIL import Image as PILImage, ImageTk as PILImageTk
        pil_img = PILImage.open(os.path.join('imgs', 'red-go-back-arrow.png'))
        pil_img.thumbnail((40, 40), PILImage.Resampling.LANCZOS)
        back_arrow_img = PILImageTk.PhotoImage(pil_img)
        back_btn = tk.Label(banner_frame, image=back_arrow_img, bg=banner_color, cursor="hand2")
        back_btn.image = back_arrow_img
    except:
        back_btn = tk.Label(banner_frame, text="◀", font=("Arial", scale_font(20), "bold"), 
                           bg=banner_color, fg="#FFFFFF", cursor="hand2")
    
    back_btn.pack(side=tk.RIGHT, padx=20, pady=10)
    back_btn.bind("<Button-1>", lambda e: app_ref.show_difficulty_menu(chapter, level))
    
    # Contenido principal
    main_frame = tk.Frame(app_ref.current_screen, bg=app_ref.COLOR_FONDO)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Título del problema
    tk.Label(main_frame, text="Obtener g(x)", font=("Arial", scale_font(18), "bold"), 
            bg=app_ref.COLOR_FONDO, fg="#20E0D0").pack(pady=10)
    
    # Frame para tabla y x
    top_content_frame = tk.Frame(main_frame, bg=app_ref.COLOR_FONDO)
    top_content_frame.pack(pady=15, fill=tk.X)
    
    # Mostrar x a encontrar
    tk.Label(top_content_frame, text=f"x = {data['x_to_find']}", font=("Arial", scale_font(16), "bold"), 
            bg=app_ref.COLOR_FONDO, fg="white").pack(side=tk.LEFT, padx=20)
    
    # Tabla de datos
    table_frame = tk.Frame(top_content_frame, bg="white", highlightthickness=2, highlightbackground="#20E0D0")
    table_frame.pack(side=tk.LEFT, padx=20)
    
    # Encabezados
    header_x = tk.Label(table_frame, text="x", font=("Arial", scale_font(12), "bold"), 
                       bg="#20E0D0", fg="white", width=10, height=2)
    header_x.grid(row=0, column=0, sticky="nsew")
    
    header_y = tk.Label(table_frame, text="y", font=("Arial", scale_font(12), "bold"), 
                       bg="#20E0D0", fg="white", width=10, height=2)
    header_y.grid(row=0, column=1, sticky="nsew")
    
    # Datos de la tabla
    for i, (x_val, y_val) in enumerate(data['data'], 1):
        cell_x = tk.Label(table_frame, text=f"{x_val:.1f}", font=("Arial", scale_font(11)), 
                         bg="white", fg="black", width=10, height=2, relief=tk.RIDGE)
        cell_x.grid(row=i, column=0, sticky="nsew")
        
        cell_y = tk.Label(table_frame, text=f"{y_val:.5f}", font=("Arial", scale_font(11)), 
                         bg="white", fg="black", width=10, height=2, relief=tk.RIDGE)
        cell_y.grid(row=i, column=1, sticky="nsew")
    
    # Temporizador
    timer_container = tk.Frame(top_content_frame, bg=app_ref.COLOR_FONDO)
    timer_container.pack(side=tk.RIGHT, padx=20)
    
    tk.Label(timer_container, text="⏱", font=("Arial", scale_font(24)), 
            bg=app_ref.COLOR_FONDO, fg="white").pack(pady=5)
    tk.Label(timer_container, text="Tiempo restante", font=("Arial", scale_font(12), "bold"), 
            bg=app_ref.COLOR_FONDO, fg="white").pack()
    
    timer_label = tk.Label(timer_container, text="00:00", font=("Arial", scale_font(20), "bold"), 
                          bg=app_ref.COLOR_FONDO, fg="#20E0D0")
    timer_label.pack(pady=5)
    
    # Temporizador
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
    
    # Marco con opciones
    options_frame = tk.Frame(main_frame, bg=app_ref.COLOR_FONDO)
    options_frame.pack(pady=30, fill=tk.BOTH, expand=True)
    
    tk.Label(options_frame, text="g(x) =", font=("Arial", scale_font(16), "bold"), 
            bg=app_ref.COLOR_FONDO, fg="white").pack(pady=15)
    
    btn_frame = tk.Frame(options_frame, bg=app_ref.COLOR_FONDO)
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

# ============================================================================
# CAPÍTULO 2: ECUACIONES LINEALES - FUNCIONES STUB
# ============================================================================

def show_gauss_seidel(chapter, level, difficulty, lesson_index):
    """Placeholder - Mostrar ejercicio de Gauss-Seidel"""
    messagebox.showinfo("Próximamente", "Gauss-Seidel será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_jacobi(chapter, level, difficulty, lesson_index):
    """Placeholder - Mostrar ejercicio de Jacobi"""
    messagebox.showinfo("Próximamente", "Jacobi será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_montante(chapter, level, difficulty, lesson_index):
    """Placeholder - Mostrar ejercicio de Montante"""
    messagebox.showinfo("Próximamente", "Montante será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_gauss_jordan(chapter, level, difficulty, lesson_index):
    """Placeholder - Mostrar ejercicio de Gauss-Jordán"""
    messagebox.showinfo("Próximamente", "Gauss-Jordán será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_eliminacion_gaussiana(chapter, level, difficulty, lesson_index):
    """Placeholder - Mostrar ejercicio de Eliminación Gaussiana"""
    messagebox.showinfo("Próximamente", "Eliminación Gaussiana será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

# ============================================================================
# CAPÍTULO 3: ECUACIONES NO LINEALES - FUNCIONES STUB
# ============================================================================

def show_bisection(chapter, level, difficulty, lesson_index):
    """Placeholder - Bisección"""
    messagebox.showinfo("Próximamente", "Bisección será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_falsa_posicion(chapter, level, difficulty, lesson_index):
    """Placeholder - Falsa Posición"""
    messagebox.showinfo("Próximamente", "Falsa Posición será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_newton_raphson(chapter, level, difficulty, lesson_index):
    """Placeholder - Newton-Raphson"""
    messagebox.showinfo("Próximamente", "Newton-Raphson será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_punto_fijo(chapter, level, difficulty, lesson_index):
    """Placeholder - Punto Fijo"""
    messagebox.showinfo("Próximamente", "Punto Fijo será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_secante(chapter, level, difficulty, lesson_index):
    """Placeholder - Secante"""
    messagebox.showinfo("Próximamente", "Secante será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

# ============================================================================
# CAPÍTULO 4: ECUACIONES DIFERENCIALES ORDINARIAS - FUNCIONES STUB
# ============================================================================

def show_euler(chapter, level, difficulty, lesson_index):
    """Placeholder - Euler"""
    messagebox.showinfo("Próximamente", "Euler será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_euler_modificado(chapter, level, difficulty, lesson_index):
    """Placeholder - Euler Modificado"""
    messagebox.showinfo("Próximamente", "Euler Modificado será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_rk2(chapter, level, difficulty, lesson_index):
    """Placeholder - Runge-Kutta 2º Orden"""
    messagebox.showinfo("Próximamente", "RK2 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_rk3(chapter, level, difficulty, lesson_index):
    """Placeholder - Runge-Kutta 3er Orden"""
    messagebox.showinfo("Próximamente", "RK3 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_rk4(chapter, level, difficulty, lesson_index):
    """Placeholder - Runge-Kutta 4º Orden"""
    messagebox.showinfo("Próximamente", "RK4 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

# ============================================================================
# CAPÍTULO 5: INTEGRACIÓN NUMÉRICA - FUNCIONES STUB
# ============================================================================

def show_trapezoidal(chapter, level, difficulty, lesson_index):
    """Placeholder - Regla Trapezoidal"""
    messagebox.showinfo("Próximamente", "Trapezoidal será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_simpson_13(chapter, level, difficulty, lesson_index):
    """Placeholder - Simpson 1/3"""
    messagebox.showinfo("Próximamente", "Simpson 1/3 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_simpson_38(chapter, level, difficulty, lesson_index):
    """Placeholder - Simpson 3/8"""
    messagebox.showinfo("Próximamente", "Simpson 3/8 será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_newton_cotes_cerradas(chapter, level, difficulty, lesson_index):
    """Placeholder - Newton-Cotes Cerradas"""
    messagebox.showinfo("Próximamente", "Newton-Cotes Cerradas será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_newton_cotes_abiertas(chapter, level, difficulty, lesson_index):
    """Placeholder - Newton-Cotes Abiertas"""
    messagebox.showinfo("Próximamente", "Newton-Cotes Abiertas será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

# ============================================================================
# CAPÍTULO 6: MÍNIMOS CUADRADOS - FUNCIONES STUB
# ============================================================================

def show_minimos_cuadrados_lineal(chapter, level, difficulty, lesson_index):
    """Placeholder - Mínimos Cuadrados Línea Recta"""
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Lineal será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_minimos_cuadrados_cuadratica(chapter, level, difficulty, lesson_index):
    """Placeholder - Mínimos Cuadrados Parábola"""
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Cuadrática será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_minimos_cuadrados_cubica(chapter, level, difficulty, lesson_index):
    """Placeholder - Mínimos Cuadrados Cúbica"""
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Cúbica será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_minimos_cuadrados_lineal_func(chapter, level, difficulty, lesson_index):
    """Placeholder - Mínimos Cuadrados Lineal con Función"""
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Lineal con Función será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)

def show_minimos_cuadrados_cuadratica_func(chapter, level, difficulty, lesson_index):
    """Placeholder - Mínimos Cuadrados Cuadrática con Función"""
    messagebox.showinfo("Próximamente", "Mínimos Cuadrados Cuadrática con Función será implementado próximamente")
    app_ref.show_difficulty_menu(chapter, level)
