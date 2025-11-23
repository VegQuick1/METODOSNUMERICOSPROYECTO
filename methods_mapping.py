
METHODS_MAPPING = {
    "Capítulo 1: Interpolación": {
        "Nivel 1: Lagrange": {
            "Intermedio": {"function": "_show_lagrange_intermedio", "banner_color": "#f8cf39"},
            "Avanzado": {"function": "_show_lagrange_avanzado", "banner_color": "#f94255"},
            "Prueba Final": {"function": "_show_lagrange_final", "banner_color": "#ac35e4"},
        },
        "Nivel 2: Lineal": {
            "Intermedio": {"function": "show_interpolacion_lineal", "banner_color": "#FFB6C1"},
            "Avanzado": {"function": "show_interpolacion_lineal", "banner_color": "#FFB6C1"},
            "Prueba Final": {"function": "show_interpolacion_lineal", "banner_color": "#FFB6C1"},
        },
        "Nivel 3: Newton con Diferencias Divididas": {
            "Intermedio": {"function": "show_newton_divided_diff", "banner_color": "#DDA0DD"},
            "Avanzado": {"function": "show_newton_divided_diff", "banner_color": "#DDA0DD"},
            "Prueba Final": {"function": "show_newton_divided_diff", "banner_color": "#DDA0DD"},
        },
        "Nivel 4: Newton Hacia Adelante": {
            "Intermedio": {"function": "show_newton_forward", "banner_color": "#90EE90"},
            "Avanzado": {"function": "show_newton_forward", "banner_color": "#90EE90"},
            "Prueba Final": {"function": "show_newton_forward", "banner_color": "#90EE90"},
        },
        "Nivel 5: Newton Hacia Atrás": {
            "Intermedio": {"function": "show_newton_backward", "banner_color": "#87CEEB"},
            "Avanzado": {"function": "show_newton_backward", "banner_color": "#87CEEB"},
            "Prueba Final": {"function": "show_newton_backward", "banner_color": "#87CEEB"},
        },
    },
    "Capítulo 2: Ecuaciones Lineales": {
        "Nivel 1: Montante": {
            "Intermedio": {"function": "show_montante", "banner_color": "#FFD700"},
            "Avanzado": {"function": "show_montante", "banner_color": "#FFD700"},
            "Prueba Final": {"function": "show_montante", "banner_color": "#FFD700"},
        },
        "Nivel 2: Gauss-Jordán": {
            "Intermedio": {"function": "show_gauss_jordan", "banner_color": "#FF8C00"},
            "Avanzado": {"function": "show_gauss_jordan", "banner_color": "#FF8C00"},
            "Prueba Final": {"function": "show_gauss_jordan", "banner_color": "#FF8C00"},
        },
        "Nivel 3: Eliminación Gaussiana": {
            "Intermedio": {"function": "show_eliminacion_gaussiana", "banner_color": "#FF7F50"},
            "Avanzado": {"function": "show_eliminacion_gaussiana", "banner_color": "#FF7F50"},
            "Prueba Final": {"function": "show_eliminacion_gaussiana", "banner_color": "#FF7F50"},
        },
        "Nivel 4: Gauss-Seidel": {
            "Intermedio": {"function": "show_gauss_seidel", "banner_color": "#FF6B6B"},
            "Avanzado": {"function": "show_gauss_seidel", "banner_color": "#FF6B6B"},
            "Prueba Final": {"function": "show_gauss_seidel", "banner_color": "#FF6B6B"},
        },
        "Nivel 5: Jacobi": {
            "Intermedio": {"function": "show_jacobi", "banner_color": "#4ECDC4"},
            "Avanzado": {"function": "show_jacobi", "banner_color": "#4ECDC4"},
            "Prueba Final": {"function": "show_jacobi", "banner_color": "#4ECDC4"},
        },
    },
    "Capítulo 3: Ecuaciones No Lineales": {
        "Nivel 1: Bisección (Bisectriz)": {
            "Intermedio": {"function": "show_bisection", "banner_color": "#FF7F50"},
            "Avanzado": {"function": "show_bisection", "banner_color": "#FF7F50"},
            "Prueba Final": {"function": "show_bisection", "banner_color": "#FF7F50"},
        },
        "Nivel 2: Falsa Posición (Regula-Falsi)": {
            "Intermedio": {"function": "show_falsa_posicion", "banner_color": "#20B2AA"},
            "Avanzado": {"function": "show_falsa_posicion", "banner_color": "#20B2AA"},
            "Prueba Final": {"function": "show_falsa_posicion", "banner_color": "#20B2AA"},
        },
        "Nivel 3: Newton-Raphson": {
            "Intermedio": {"function": "show_newton_raphson", "banner_color": "#9370DB"},
            "Avanzado": {"function": "show_newton_raphson", "banner_color": "#9370DB"},
            "Prueba Final": {"function": "show_newton_raphson", "banner_color": "#9370DB"},
        },
        "Nivel 4: Punto Fijo": {
            "Intermedio": {"function": "show_punto_fijo", "banner_color": "#3CB371"},
            "Avanzado": {"function": "show_punto_fijo", "banner_color": "#3CB371"},
            "Prueba Final": {"function": "show_punto_fijo", "banner_color": "#3CB371"},
        },
        "Nivel 5: Secante": {
            "Intermedio": {"function": "show_secante", "banner_color": "#FF69B4"},
            "Avanzado": {"function": "show_secante", "banner_color": "#FF69B4"},
            "Prueba Final": {"function": "show_secante", "banner_color": "#FF69B4"},
        },
    },
    "Capítulo 4: Ecuaciones Diferenciales Ordinarias": {
        "Nivel 1: Euler": {
            "Intermedio": {"function": "show_euler", "banner_color": "#FFD700"},
            "Avanzado": {"function": "show_euler", "banner_color": "#FFD700"},
            "Prueba Final": {"function": "show_euler", "banner_color": "#FFD700"},
        },
        "Nivel 2: Euler Modificado": {
            "Intermedio": {"function": "show_euler_modificado", "banner_color": "#FFA500"},
            "Avanzado": {"function": "show_euler_modificado", "banner_color": "#FFA500"},
            "Prueba Final": {"function": "show_euler_modificado", "banner_color": "#FFA500"},
        },
        "Nivel 3: Runge-Kutta 2º Orden": {
            "Intermedio": {"function": "show_rk2", "banner_color": "#FF8C00"},
            "Avanzado": {"function": "show_rk2", "banner_color": "#FF8C00"},
            "Prueba Final": {"function": "show_rk2", "banner_color": "#FF8C00"},
        },
        "Nivel 4: Runge-Kutta 3er Orden": {
            "Intermedio": {"function": "show_rk3", "banner_color": "#FF7F50"},
            "Avanzado": {"function": "show_rk3", "banner_color": "#FF7F50"},
            "Prueba Final": {"function": "show_rk3", "banner_color": "#FF7F50"},
        },
        "Nivel 5: Runge-Kutta 4º Orden": {
            "Intermedio": {"function": "show_rk4", "banner_color": "#FF6347"},
            "Avanzado": {"function": "show_rk4", "banner_color": "#FF6347"},
            "Prueba Final": {"function": "show_rk4", "banner_color": "#FF6347"},
        },
    },
    "Capítulo 5: Integración Numérica": {
        "Nivel 1: Regla Trapezoidal": {
            "Intermedio": {"function": "show_trapezoidal", "banner_color": "#9932CC"},
            "Avanzado": {"function": "show_trapezoidal", "banner_color": "#9932CC"},
            "Prueba Final": {"function": "show_trapezoidal", "banner_color": "#9932CC"},
        },
        "Nivel 2: Regla de 1/3 Simpson": {
            "Intermedio": {"function": "show_simpson_13", "banner_color": "#8B008B"},
            "Avanzado": {"function": "show_simpson_13", "banner_color": "#8B008B"},
            "Prueba Final": {"function": "show_simpson_13", "banner_color": "#8B008B"},
        },
        "Nivel 3: Regla de 3/8 Simpson": {
            "Intermedio": {"function": "show_simpson_38", "banner_color": "#4B0082"},
            "Avanzado": {"function": "show_simpson_38", "banner_color": "#4B0082"},
            "Prueba Final": {"function": "show_simpson_38", "banner_color": "#4B0082"},
        },
        "Nivel 4: Newton-Cotes Abiertas y Cerradas": {
            "Intermedio": {"function": "show_newton_cotes", "banner_color": "#483D8B"},
            "Avanzado": {"function": "show_newton_cotes", "banner_color": "#483D8B"},
            "Prueba Final": {"function": "show_newton_cotes", "banner_color": "#483D8B"},
        },
    },
    "Capítulo 6: Mínimos Cuadrados": {
        "Nivel 1: Línea Recta": {
            "Intermedio": {"function": "show_minimos_cuadrados_lineal", "banner_color": "#EE82EE"},
            "Avanzado": {"function": "show_minimos_cuadrados_lineal", "banner_color": "#EE82EE"},
            "Prueba Final": {"function": "show_minimos_cuadrados_lineal", "banner_color": "#EE82EE"},
        },
        "Nivel 2: Parábola (Cuadrática)": {
            "Intermedio": {"function": "show_minimos_cuadrados_cuadratica", "banner_color": "#DDA0DD"},
            "Avanzado": {"function": "show_minimos_cuadrados_cuadratica", "banner_color": "#DDA0DD"},
            "Prueba Final": {"function": "show_minimos_cuadrados_cuadratica", "banner_color": "#DDA0DD"},
        },
        "Nivel 3: Cúbica": {
            "Intermedio": {"function": "show_minimos_cuadrados_cubica", "banner_color": "#DDA0DD"},
            "Avanzado": {"function": "show_minimos_cuadrados_cubica", "banner_color": "#DDA0DD"},
            "Prueba Final": {"function": "show_minimos_cuadrados_cubica", "banner_color": "#DDA0DD"},
        },
        "Nivel 4: Lineal con Función": {
            "Intermedio": {"function": "show_minimos_cuadrados_lineal_func", "banner_color": "#DA70D6"},
            "Avanzado": {"function": "show_minimos_cuadrados_lineal_func", "banner_color": "#DA70D6"},
            "Prueba Final": {"function": "show_minimos_cuadrados_lineal_func", "banner_color": "#DA70D6"},
        },
        "Nivel 5: Cuadrática con Función": {
            "Intermedio": {"function": "show_minimos_cuadrados_cuadratica_func", "banner_color": "#BA55D3"},
            "Avanzado": {"function": "show_minimos_cuadrados_cuadratica_func", "banner_color": "#BA55D3"},
            "Prueba Final": {"function": "show_minimos_cuadrados_cuadratica_func", "banner_color": "#BA55D3"},
        },
    },
}
def get_method_info(chapter, level, difficulty):
    try:
        return METHODS_MAPPING[chapter][level][difficulty]
    except KeyError:
        return None
