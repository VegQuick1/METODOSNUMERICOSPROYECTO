
import random
import numpy as np
from math import sqrt
from methods_engine import (
    solve_lagrange,
    solve_linear_interpolation,
    solve_newton_divided_differences,
    solve_newton_forward,
    solve_newton_backward,
)

LAGRANGE_FAKE_ANSWERS = {
    'yi': ['y', 'yi+1', 'y(i)', 'yn'],
    'n': ['m', 'k', 'l', 'i'],
    'x-xj': ['x-xi', 'x-x0', 'x-xn', 'xi-x'],
    'xi-xj': ['xi-xk', 'xj-xi', 'xk-xi', 'x-xj'],
    'Σ': ['Σ', 'Π', '∫', 'Δ'],
    'Nada': ['?', '*', '·', '—']
}

GAME_STRUCTURE = {
    "Interpolación": {
        "levels": {
            "Lineal": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'linear_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'linear_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'linear_interp_1'}
                ]
            },
            "Newton Hacia Adelante": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'newton_forward_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'newton_forward_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'newton_forward_1'}
                ]
            },
            "Newton Hacia Atrás": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'newton_backward_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'newton_backward_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'newton_backward_1'}
                ]
            },
            "Newton con Diferencias Divididas": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'newton_div_diff_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'newton_div_diff_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'newton_div_diff_1'}
                ]
            },
            "Lagrange": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'lagrange_intermedio'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'lagrange_avanzado'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'lagrange_final'}
                ]
            },
        }
    },
    "Ecuaciones No Lineales": {
        "levels": {
            "Método Gráfico": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'graphical_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'graphical_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'graphical_1'}
                ]
            },
            "Bisección (Bisectriz)": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'bisection_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'bisection_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'bisection_1'}
                ]
            },
            "Punto Fijo": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'fixed_point_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'fixed_point_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'fixed_point_1'}
                ]
            },
            "Falsa Posición (Regula-Falsi)": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'false_position_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'false_position_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'false_position_1'}
                ]
            },
            "Secante": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'secant_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'secant_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'secant_1'}
                ]
            },
            "Newton-Raphson": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'newton_raphson_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'newton_raphson_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'newton_raphson_1'}
                ]
            },
        }
    },
    "Ecuaciones Lineales": {
        "levels": {
            "Gauss-Seidel": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'gauss_seidel_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'gauss_seidel_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'gauss_seidel_1'}
                ]
            },
            "Jacobi": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'jacobi_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'jacobi_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'jacobi_1'}
                ]
            },
            "Montante": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'montante_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'montante_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'montante_1'}
                ]
            },
            "Gauss-Jordan": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'gauss_jordan_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'gauss_jordan_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'gauss_jordan_1'}
                ]
            },
            "Eliminación Gaussiana": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'gaussian_elim_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'gaussian_elim_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'gaussian_elim_1'}
                ]
            },
        }
    },
    "Mínimos Cuadrados": {
        "levels": {
            "Línea Recta": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'least_sq_linear_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'least_sq_linear_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_linear_1'}
                ]
            },
            "Cuadrática": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'least_sq_quadratic_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'least_sq_quadratic_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_quadratic_1'}
                ]
            },
            "Cúbica": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'least_sq_cubic_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'least_sq_cubic_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_cubic_1'}
                ]
            },
            "Lineal con Función": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'least_sq_linear_func_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'least_sq_linear_func_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_linear_func_1'}
                ]
            },
            "Cuadrática con Función": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'least_sq_quadratic_func_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'least_sq_quadratic_func_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_quadratic_func_1'}
                ]
            },
        }
    },
    "Integración": {
        "levels": {
            "Regla Trapezoidal": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'trapezoidal_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'trapezoidal_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'trapezoidal_1'}
                ]
            },
            "Regla de 1/3 Simpson": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'simpson_1_3_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'simpson_1_3_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'simpson_1_3_1'}
                ]
            },
            "Regla de 3/8 Simpson": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'simpson_3_8_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'simpson_3_8_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'simpson_3_8_1'}
                ]
            },
            "Newton-Cotes Abiertas y Cerradas": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'cotes_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'cotes_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'cotes_1'}
                ]
            },
        }
    },
    "Ecuaciones Diferenciales Ordinarias (EDO)": {
        "levels": {
            "Euler Modificado": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'euler_modified_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'euler_modified_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'euler_modified_1'}
                ]
            },
            "Runge-Kutta 2do Orden": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'rk2_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'rk2_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk2_1'}
                ]
            },
            "Runge-Kutta 3er Orden": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'rk3_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'rk3_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk3_1'}
                ]
            },
            "Runge-Kutta 4to Orden (1/3 Simpson)": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'rk4_simpson13_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'rk4_simpson13_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk4_simpson13_1'}
                ]
            },
            "Runge-Kutta 4to Orden (3/8 Simpson)": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'rk4_simpson38_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'rk4_simpson38_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk4_simpson38_1'}
                ]
            },
            "Runge-Kutta Orden Superior": {
                "Fácil": [
                    {'type': 'practica'}
                ],
                "Intermedio": [
                    {'type': 'practica', 'problem_id': 'rk_higher_order_intermedio_1'}
                ],
                "Avanzado": [
                    {'type': 'practica', 'problem_id': 'rk_higher_order_avanzado_1'}
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk_higher_order_1'}
                ]
            },
        }
    },
}

def _round_str(val, places=5):
    return f"{val:.{places}f}" if isinstance(val, (int, float)) else str(val)

def _round_table(table, decimals=2):
    """Redondea todos los valores en una tabla a 'decimals' decimales"""
    rounded = []
    for row in table:
        if isinstance(row, tuple):
            rounded_row = tuple(round(v, decimals) if isinstance(v, (int, float)) else v for v in row)
            rounded.append(rounded_row)
        else:
            rounded.append(round(row, decimals) if isinstance(row, (int, float)) else row)
    return rounded

# ===================== FACTORÍAS DINÁMICAS: INTERPOLACIÓN (PRUEBA FINAL) =====================

def generate_lagrange_final():
    # Genera 5-6 puntos a partir de un polinomio cúbico aleatorio
    n = random.randint(5, 6)
    x0 = random.randint(1, 3)
    h = random.choice([0.4, 0.5, 0.6])
    xs = [x0 + i * h for i in range(n)]
    # Polinomio cúbico con coeficientes pequeños para evitar explosión
    a0 = random.uniform(1, 4)
    a1 = random.uniform(0.5, 2)
    a2 = random.uniform(-0.5, 0.8)
    a3 = random.uniform(-0.2, 0.2)
    def poly(x):
        return a0 + a1*x + a2*x**2 + a3*x**3
    table = [(round(x, 2), round(poly(x), 2)) for x in xs]
    # Escoger x_to_find entre dos puntos internos para asegurar interpolación real
    k = random.randint(1, n-3)  # evita extremos
    x_to_find = round(xs[k] + (h/2), 2)
    correct_val = solve_lagrange(table, x_to_find)
    # Distractores: variaciones simulando errores humanos
    distractors = set()
    # Error de signo en término cúbico
    wrong1 = a0 + a1*x_to_find + a2*x_to_find**2 - a3*x_to_find**3
    # Omite término de mayor grado
    wrong2 = a0 + a1*x_to_find + a2*x_to_find**2
    # Usa solo primer k+1 puntos
    subset = table[:k+1]
    if len(subset) >= 2:
        wrong3 = solve_lagrange(subset, x_to_find)
    else:
        wrong3 = correct_val * (1 + 0.07)
    # Pequeña perturbación
    wrong4 = correct_val * (1 - 0.05)
    for w in [wrong1, wrong2, wrong3, wrong4]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    # Asegurar al menos 4 distractores; si faltan, generar por perturbación
    while len(distractors) < 4:
        perturb = correct_val * (1 + random.uniform(-0.12, 0.12))
        p_str = _round_str(perturb, 5)
        if p_str != _round_str(correct_val, 5) and p_str not in distractors:
            distractors.append(p_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Lagrange Final -> coef: ({a0:.3f},{a1:.3f},{a2:.3f},{a3:.3f}) x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Obtener g(x) (Lagrange)',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 25
    }

def generate_lagrange_simple():
    """Versión simplificada: solo 3-4 puntos"""
    n = random.randint(3, 4)
    x0 = random.randint(1, 3)
    h = random.choice([0.5, 1])  # Espaciamiento más simple
    xs = [x0 + i * h for i in range(n)]
    # Polinomio cuadrático (no cúbico) para simplificar
    a0 = random.uniform(1, 3)
    a1 = random.uniform(0.5, 1.5)
    a2 = random.uniform(-0.3, 0.3)
    def poly(x):
        return a0 + a1*x + a2*x**2
    table = [(round(x, 2), round(poly(x), 2)) for x in xs]
    # Escoger x_to_find entre dos puntos internos
    k = random.randint(0, n-2)
    x_to_find = round(xs[k] + (h/2), 2)
    correct_val = solve_lagrange(table, x_to_find)
    # Distractores más simples
    distractors = set()
    # Error de signo
    wrong1 = a0 + a1*x_to_find - a2*x_to_find**2
    # Omite término de mayor grado
    wrong2 = a0 + a1*x_to_find
    # Pequeña perturbación
    wrong3 = correct_val * (1 - 0.05)
    wrong4 = correct_val * (1 + 0.05)
    for w in [wrong1, wrong2, wrong3, wrong4]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        perturb = correct_val * (1 + random.uniform(-0.08, 0.08))
        p_str = _round_str(perturb, 5)
        if p_str != _round_str(correct_val, 5) and p_str not in distractors:
            distractors.append(p_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Lagrange Intermedio -> coef: ({a0:.3f},{a1:.3f},{a2:.3f}) x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Obtener g(x) (Lagrange)',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 30
    }

def generate_linear_interp_final():
    # Genera 6 puntos de una función lineal y obliga a elegir intervalo correcto
    n = 6
    x0 = random.randint(1, 4)
    h = random.choice([1, 2])
    m = random.uniform(0.5, 3)
    c = random.uniform(-2, 4)
    xs = [x0 + i*h for i in range(n)]
    def line(x):
        return m*x + c
    table = [(round(x, 2), round(line(x), 2)) for x in xs]
    # Elegir índice interno para interpolar entre xs[k] y xs[k+1]
    k = random.randint(1, n-3)
    x_left, x_right = xs[k], xs[k+1]
    x_to_find = round((x_left + x_right) / 2.0, 2)
    correct_val = solve_linear_interpolation(x_left, line(x_left), x_right, line(x_right), x_to_find)
    # Distractores
    wrong_interval_val = solve_linear_interpolation(xs[k-1], line(xs[k-1]), x_left, line(x_left), x_to_find)
    wrong_interval_val2 = solve_linear_interpolation(x_right, line(x_right), xs[k+2], line(xs[k+2]), x_to_find)
    sign_error = line(x_left) + ((line(x_right)-line(x_left))/(x_left - x_right)) * (x_to_find - x_left)
    offset_error = correct_val * (1 + random.uniform(-0.08, 0.08))
    distractors = set()
    for w in [wrong_interval_val, wrong_interval_val2, sign_error, offset_error]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = correct_val * (1 + random.uniform(-0.15, 0.15))
        e_str = _round_str(extra, 5)
        if e_str != _round_str(correct_val, 5) and e_str not in distractors:
            distractors.append(e_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Lineal Final -> m={m:.3f} c={c:.3f} intervalo=({x_left},{x_right}) x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Interpolación Lineal: Selecciona el intervalo correcto',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 25
    }

def generate_linear_interp_simple():
    """Versión simplificada: solo 4 puntos"""
    n = 4
    x0 = random.randint(1, 3)
    h = random.choice([1, 2])
    m = random.uniform(0.5, 2)
    c = random.uniform(-2, 2)
    xs = [x0 + i*h for i in range(n)]
    def line(x):
        return m*x + c
    table = [(round(x, 2), round(line(x), 2)) for x in xs]
    # Elegir índice interno (más simple con 4 puntos)
    k = random.randint(0, n-2)
    x_left, x_right = xs[k], xs[k+1]
    x_to_find = round((x_left + x_right) / 2.0, 2)
    correct_val = solve_linear_interpolation(x_left, line(x_left), x_right, line(x_right), x_to_find)
    # Distractores más simples
    distractors = set()
    # Error de intervalo (si hay más puntos)
    if k > 0:
        wrong1 = solve_linear_interpolation(xs[k-1], line(xs[k-1]), x_left, line(x_left), x_to_find)
        w_str = _round_str(wrong1, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    # Error de signo
    sign_error = line(x_left) + ((line(x_right)-line(x_left))/(x_left - x_right)) * (x_to_find - x_left)
    w_str = _round_str(sign_error, 5)
    if w_str != _round_str(correct_val, 5):
        distractors.add(w_str)
    # Perturbaciones
    for _ in range(2):
        offset_error = correct_val * (1 + random.uniform(-0.08, 0.08))
        w_str = _round_str(offset_error, 5)
        if w_str != _round_str(correct_val, 5) and w_str not in distractors:
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = correct_val * (1 + random.uniform(-0.12, 0.12))
        e_str = _round_str(extra, 5)
        if e_str != _round_str(correct_val, 5) and e_str not in distractors:
            distractors.append(e_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Lineal Intermedio -> m={m:.3f} c={c:.3f} intervalo=({x_left},{x_right}) x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Interpolación Lineal: Selecciona el intervalo correcto',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 30
    }

def generate_newton_div_diff_simple():
    """Versión simplificada: solo 3-4 puntos"""
    n = random.randint(3, 4)
    xs = []
    current = random.randint(1, 3)
    for _ in range(n):
        current += random.uniform(0.5, 1)
        xs.append(round(current, 3))
    # Polinomio lineal o cuadrático simple
    a0 = random.uniform(-1, 2)
    a1 = random.uniform(0.5, 2)
    a2 = random.uniform(-0.3, 0.3)
    def poly(x):
        return a0 + a1*x + a2*x**2
    table = [(round(x, 2), round(poly(x), 2)) for x in xs]
    # x_to_find interno
    if n > 2:
        k = random.randint(0, n-2)
        x_to_find = round(xs[k] + (xs[k+1]-xs[k]) * random.uniform(0.3, 0.7), 2)
    else:
        x_to_find = xs[0] + 0.2
    correct_val = solve_newton_divided_differences(table, x_to_find)
    # Distractores simples
    omit_second = a0 + a1*x_to_find  # omite x^2
    wrong_sign = a0 + a1*x_to_find - a2*x_to_find**2
    perturb = correct_val * (1 + random.uniform(-0.06, 0.06))
    distractors = set()
    for w in [omit_second, wrong_sign, perturb]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = correct_val + random.uniform(-0.15, 0.15)
        e_str = _round_str(extra, 5)
        if e_str != _round_str(correct_val, 5) and e_str not in distractors:
            distractors.append(e_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Newton DivDif Intermedio -> coef: ({a0:.3f},{a1:.3f},{a2:.3f}) x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Newton Diferencias Divididas',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 30
    }

def generate_newton_forward_simple():
    """Versión simplificada: solo 3-4 puntos"""
    n = random.randint(3, 4)
    x0 = random.randint(1, 3)
    h = 0.5  # Espaciamiento fijo
    xs = [x0 + i*h for i in range(n)]
    # Polinomio cuadrático simple
    a0 = random.uniform(0.5, 2)
    a1 = random.uniform(0.2, 1)
    a2 = random.uniform(-0.2, 0.2)
    def poly(x):
        return a0 + a1*x + a2*x**2
    table = [(round(x, 2), round(poly(x), 2)) for x in xs]
    x_to_find = round(xs[0] + h*random.uniform(0.2, 0.8), 2)
    correct_val = solve_newton_forward(table, x_to_find)
    # Distractores simples
    wrong_omit_term = a0 + a1*x_to_find
    perturb = correct_val * (1 + random.uniform(-0.05, 0.05))
    sign_error = a0 + a1*x_to_find - a2*x_to_find**2
    distractors = set()
    for w in [wrong_omit_term, perturb, sign_error]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = correct_val + random.uniform(-0.12, 0.12)
        e_str = _round_str(extra, 5)
        if e_str != _round_str(correct_val, 5) and e_str not in distractors:
            distractors.append(e_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Newton Forward Intermedio -> coef: ({a0:.3f},{a1:.3f},{a2:.3f}) x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Newton Diferencias Finitas Adelante',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 30
    }

def generate_newton_backward_simple():
    """Versión simplificada: solo 3-4 puntos"""
    n = random.randint(3, 4)
    x0 = random.randint(3, 5)
    h = 0.5  # Espaciamiento fijo
    xs = [x0 - i*h for i in range(n)]
    xs.reverse()
    # Polinomio cuadrático simple
    a0 = random.uniform(0.5, 2)
    a1 = random.uniform(0.2, 1)
    a2 = random.uniform(-0.2, 0.2)
    def poly(x):
        return a0 + a1*x + a2*x**2
    table = [(round(x, 2), round(poly(x), 2)) for x in xs]
    x_to_find = round(xs[-1] + h*random.uniform(0.2, 0.8), 2)
    correct_val = solve_newton_backward(table, x_to_find)
    # Distractores simples
    wrong_omit_term = a0 + a1*x_to_find
    perturb = correct_val * (1 + random.uniform(-0.05, 0.05))
    sign_error = a0 + a1*x_to_find - a2*x_to_find**2
    distractors = set()
    for w in [wrong_omit_term, perturb, sign_error]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = correct_val + random.uniform(-0.12, 0.12)
        e_str = _round_str(extra, 5)
        if e_str != _round_str(correct_val, 5) and e_str not in distractors:
            distractors.append(e_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Newton Backward Intermedio -> coef: ({a0:.3f},{a1:.3f},{a2:.3f}) x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Newton Diferencias Finitas Atrás',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 30
    }

def generate_newton_div_diff_final():
    # Genera puntos NO uniformes para diferencias divididas (5-6 puntos)
    n = random.randint(5, 6)
    xs = []
    current = random.randint(2, 5)
    for _ in range(n):
        current += random.uniform(0.5, 1.5)
        xs.append(round(current, 3))
    # Polinomio cuadrático aleatorio
    a0 = random.uniform(-2, 3)
    a1 = random.uniform(0.5, 2.5)
    a2 = random.uniform(-0.5, 0.8)
    def poly(x):
        return a0 + a1*x + a2*x**2
    table = [(round(x, 2), round(poly(x), 2)) for x in xs]
    # x_to_find interno
    k = random.randint(1, n-3)
    x_to_find = round(xs[k] + (xs[k+1]-xs[k]) * random.uniform(0.3, 0.7), 2)
    correct_val = solve_newton_divided_differences(table, x_to_find)
    # Distractores
    wrong_subset = solve_newton_divided_differences(table[:k+2], x_to_find)
    omit_second = a0 + a1*x_to_find  # omite x^2
    perturb = correct_val * (1 + random.uniform(-0.06, 0.06))
    wrong_sign = a0 + a1*x_to_find - a2*x_to_find**2
    distractors = set()
    for w in [wrong_subset, omit_second, perturb, wrong_sign]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = correct_val + random.uniform(-0.2, 0.2)
        e_str = _round_str(extra, 5)
        if e_str != _round_str(correct_val, 5) and e_str not in distractors:
            distractors.append(e_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Newton DivDif Final -> coef: ({a0:.3f},{a1:.3f},{a2:.3f}) x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Newton Diferencias Divididas',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 25
    }

def generate_newton_forward_final():
    # Datos uniformes
    n = random.randint(5, 6)
    x0 = random.randint(1, 3)
    h = random.choice([0.5, 0.7, 0.8])
    xs = [x0 + i*h for i in range(n)]
    # Polinomio cúbico suave
    a0 = random.uniform(0.5, 3)
    a1 = random.uniform(0.2, 1.5)
    a2 = random.uniform(-0.3, 0.6)
    a3 = random.uniform(-0.1, 0.15)
    def poly(x):
        return a0 + a1*x + a2*x**2 + a3*x**3
    table = [(round(x, 2), round(poly(x), 2)) for x in xs]
    x_to_find = round(xs[random.randint(1, n-3)] + h*random.uniform(0.2, 0.9), 2)
    correct_val = solve_newton_forward(table[:4], x_to_find) if len(table) >= 4 else solve_newton_forward(table, x_to_find)
    wrong_s_sign = correct_val * (1 - 0.04)
    wrong_omit_term = a0 + a1*x_to_find + a2*x_to_find**2
    perturb = correct_val * (1 + random.uniform(-0.07, 0.07))
    subset_val = solve_newton_forward(table[:3], x_to_find)
    distractors = set()
    for w in [wrong_s_sign, wrong_omit_term, perturb, subset_val]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = correct_val + random.uniform(-0.15, 0.15)
        e_str = _round_str(extra, 5)
        if e_str != _round_str(correct_val, 5):
            distractors.append(e_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Newton Forward Final -> h={h} x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Newton Adelante',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 25
    }

def generate_newton_backward_final():
    # Datos uniformes
    n = random.randint(5, 6)
    x0 = random.randint(2, 4)
    h = random.choice([0.5, 0.6, 0.7])
    xs = [x0 + i*h for i in range(n)]
    a0 = random.uniform(0.5, 3)
    a1 = random.uniform(0.2, 1.5)
    a2 = random.uniform(-0.3, 0.6)
    a3 = random.uniform(-0.1, 0.15)
    def poly(x):
        return a0 + a1*x + a2*x**2 + a3*x**3
    table = [(round(x, 2), round(poly(x), 2)) for x in xs]
    x_to_find = round(xs[random.randint(2, n-2)] - h*random.uniform(0.2, 0.9), 2)
    correct_val = solve_newton_backward(table[-4:], x_to_find) if len(table) >= 4 else solve_newton_backward(table, x_to_find)
    wrong_s_sign = correct_val * (1 + 0.05)
    wrong_omit = a0 + a1*x_to_find + a2*x_to_find**2
    subset_val = solve_newton_backward(table[-3:], x_to_find)
    perturb = correct_val * (1 + random.uniform(-0.08, 0.08))
    distractors = set()
    for w in [wrong_s_sign, wrong_omit, subset_val, perturb]:
        w_str = _round_str(w, 5)
        if w_str != _round_str(correct_val, 5):
            distractors.add(w_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = correct_val + random.uniform(-0.14, 0.14)
        e_str = _round_str(extra, 5)
        if e_str != _round_str(correct_val, 5):
            distractors.append(e_str)
    options = distractors[:4] + [_round_str(correct_val, 5)]
    random.shuffle(options)
    print(f"DEBUG: Newton Backward Final -> h={h} x*={x_to_find:.3f} g(x)={correct_val:.6f}")
    return {
        'title': 'Newton Atrás',
        'x_value': x_to_find,
        'table': table,
        'options': options,
        'correct': _round_str(correct_val, 5),
        'time_minutes': 25
    }

# ===================== FACTORÍAS DINÁMICAS: ECUACIONES LINEALES (PRUEBA FINAL) =====================

def _is_diagonally_dominant(A):
    """Verifica si matriz es diagonalmente dominante"""
    n = len(A)
    for i in range(n):
        if abs(A[i, i]) <= sum(abs(A[i, j]) for j in range(n) if j != i):
            return False
    return True

def generate_linear_system_final(system_size=3):
    # Genera un sistema aleatorio que cumple dominancia diagonal para Gauss-Seidel/Jacobi
    while True:
        A = np.random.uniform(-5, 5, (system_size, system_size))
        b = np.random.uniform(-20, 20, system_size)
        # Hacer diagonal dominante
        for i in range(system_size):
            A[i, i] = sum(abs(A[i, j]) for j in range(system_size) if j != i) + random.uniform(2, 5)
        if _is_diagonally_dominant(A):
            break
    # Solución de referencia
    try:
        x_true = np.linalg.solve(A, b)
    except:
        x_true = np.ones(system_size)
    sol_str = ', '.join([f"x{i+1}={x_true[i]:.3f}" for i in range(system_size)])
    # Tabla de ecuaciones
    table_rows = []
    for i in range(system_size):
        eq_str = ' + '.join([f"{A[i,j]:.2f}*x{j+1}" for j in range(system_size)])
        eq_str += f" = {b[i]:.2f}"
        table_rows.append((eq_str,))
    # Distractores
    wrong_sols = []
    for k in range(4):
        x_wrong = x_true * (1 + np.random.uniform(-0.15, 0.15, system_size))
        wrong_str = ', '.join([f"x{i+1}={x_wrong[i]:.3f}" for i in range(system_size)])
        if wrong_str != sol_str:
            wrong_sols.append(wrong_str)
    options = (wrong_sols[:4] if len(wrong_sols) >= 4 else wrong_sols + [sol_str]*(4-len(wrong_sols))) + [sol_str]
    options = list(set(options))[:5]  # Eliminar duplicados
    random.shuffle(options)
    print(f"DEBUG: Linear System ({system_size}x{system_size}) Final -> sol: {sol_str}")
    return {
        'title': f'Sistema {system_size}x{system_size} (Dominante Diagonal)',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': sol_str,
        'time_minutes': 25
    }

def generate_linear_system_simple(system_size=2):
    """Genera un sistema lineal simplificado para Intermedio (2x2 o 3x3)"""
    # Genera un sistema aleatorio que cumple dominancia diagonal para Gauss-Seidel/Jacobi
    while True:
        A = np.random.uniform(-5, 5, (system_size, system_size))
        b = np.random.uniform(-20, 20, system_size)
        # Hacer diagonal dominante
        for i in range(system_size):
            A[i, i] = sum(abs(A[i, j]) for j in range(system_size) if j != i) + random.uniform(2, 5)
        if _is_diagonally_dominant(A):
            break
    # Solución de referencia
    try:
        x_true = np.linalg.solve(A, b)
    except:
        x_true = np.ones(system_size)
    sol_str = ', '.join([f"x{i+1}={x_true[i]:.3f}" for i in range(system_size)])
    # Tabla de ecuaciones
    table_rows = []
    for i in range(system_size):
        eq_str = ' + '.join([f"{A[i,j]:.2f}*x{j+1}" for j in range(system_size)])
        eq_str += f" = {b[i]:.2f}"
        table_rows.append((eq_str,))
    # Distractores
    wrong_sols = []
    for k in range(4):
        x_wrong = x_true * (1 + np.random.uniform(-0.15, 0.15, system_size))
        wrong_str = ', '.join([f"x{i+1}={x_wrong[i]:.3f}" for i in range(system_size)])
        if wrong_str != sol_str:
            wrong_sols.append(wrong_str)
    options = (wrong_sols[:4] if len(wrong_sols) >= 4 else wrong_sols + [sol_str]*(4-len(wrong_sols))) + [sol_str]
    options = list(set(options))[:5]  # Eliminar duplicados
    random.shuffle(options)
    print(f"DEBUG: Linear System ({system_size}x{system_size}) Intermedio -> sol: {sol_str}")
    return {
        'title': f'Sistema {system_size}x{system_size} (Dominante Diagonal)',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': sol_str,
        'time_minutes': 30
    }

def generate_gauss_seidel_final():
    return generate_linear_system_final(3)

def generate_jacobi_final():
    return generate_linear_system_final(3)

def generate_montante_final():
    return generate_linear_system_final(3)

def generate_gauss_jordan_final():
    return generate_linear_system_final(4)

def generate_gaussian_elim_final():
    return generate_linear_system_final(3)

# ===================== FACTORÍAS DINÁMICAS: ECUACIONES NO LINEALES (PRUEBA FINAL) =====================

def generate_polynomial_root(degree=3):
    """Genera polinomio grado >= 3 con raíz verificable"""
    # Coeficientes aleatorios
    coeffs = [random.uniform(-3, 3) for _ in range(degree)]
    coeffs.append(random.uniform(-5, 5))  # término independiente
    
    def poly(x):
        result = 0
        for i, c in enumerate(coeffs):
            result += c * (x ** (degree - i))
        return result
    
    # Encontrar raíz aproximada con bisección
    a, b = random.uniform(-2, 0), random.uniform(0, 2)
    if poly(a) * poly(b) < 0:
        # Bisección simple
        for _ in range(20):
            c = (a + b) / 2
            if poly(a) * poly(c) < 0:
                b = c
            else:
                a = c
        root = (a + b) / 2
    else:
        root = random.uniform(-2, 2)
    
    return poly, root, coeffs, degree

def generate_nonlinear_final():
    """Genera problema de ecuación no lineal dinámico"""
    poly, true_root, coeffs, degree = generate_polynomial_root(degree=random.randint(3, 4))
    
    # Intervalo que contiene la raíz
    interval_width = random.uniform(0.5, 2)
    a = true_root - interval_width/2
    b = true_root + interval_width/2
    
    # Construir descripción
    poly_str = f"f(x) = "
    degree_list = []
    for i, c in enumerate(coeffs):
        power = degree - i
        if power == 0:
            degree_list.append(f"{c:.2f}")
        elif power == 1:
            degree_list.append(f"{c:.2f}*x")
        else:
            degree_list.append(f"{c:.2f}*x^{power}")
    poly_str += " + ".join(degree_list)
    
    table_rows = [
        (f"Polinomio: {poly_str}",),
        (f"Intervalo: [{a:.2f}, {b:.2f}]",),
        ("Encuentra la raíz",)
    ]
    
    # Opciones
    correct_str = _round_str(true_root, 4)
    distractors = set()
    for k in range(4):
        perturb = true_root + random.uniform(-interval_width*0.3, interval_width*0.3)
        p_str = _round_str(perturb, 4)
        if p_str != correct_str:
            distractors.add(p_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = true_root + random.uniform(-1, 1)
        e_str = _round_str(extra, 4)
        if e_str != correct_str and e_str not in distractors:
            distractors.append(e_str)
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: Non-linear ({degree}°) Final -> root: {true_root:.6f} interval: [{a:.3f}, {b:.3f}]")
    return {
        'title': f'Ecuación No Lineal (Grado {degree})',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 25
    }

def generate_nonlinear_simple():
    """Genera problema de ecuación no lineal simplificado para Intermedio"""
    poly, true_root, coeffs, degree = generate_polynomial_root(degree=2)  # Solo grado 2
    
    # Intervalo más pequeño que contiene la raíz
    interval_width = random.uniform(0.3, 1)
    a = true_root - interval_width/2
    b = true_root + interval_width/2
    
    # Construir descripción
    poly_str = f"f(x) = "
    degree_list = []
    for i, c in enumerate(coeffs):
        power = degree - i
        if power == 0:
            degree_list.append(f"{c:.2f}")
        elif power == 1:
            degree_list.append(f"{c:.2f}*x")
        else:
            degree_list.append(f"{c:.2f}*x^{power}")
    poly_str += " + ".join(degree_list)
    
    table_rows = [
        (f"Polinomio: {poly_str}",),
        (f"Intervalo: [{a:.2f}, {b:.2f}]",),
        ("Encuentra la raíz",)
    ]
    
    # Opciones
    correct_str = _round_str(true_root, 4)
    distractors = set()
    for k in range(4):
        perturb = true_root + random.uniform(-interval_width*0.3, interval_width*0.3)
        p_str = _round_str(perturb, 4)
        if p_str != correct_str:
            distractors.add(p_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = true_root + random.uniform(-1, 1)
        e_str = _round_str(extra, 4)
        if e_str != correct_str and e_str not in distractors:
            distractors.append(e_str)
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: Non-linear (2°) Intermedio -> root: {true_root:.6f} interval: [{a:.3f}, {b:.3f}]")
    return {
        'title': f'Ecuación No Lineal (Grado 2)',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 30
    }

def generate_bisection_final():
    return generate_nonlinear_final()

def generate_false_position_final():
    return generate_nonlinear_final()

def generate_newton_raphson_final():
    return generate_nonlinear_final()

def generate_fixed_point_final():
    return generate_nonlinear_final()

def generate_secant_final():
    return generate_nonlinear_final()

def generate_graphical_final():
    return generate_nonlinear_final()

# ===================== FACTORÍAS DINÁMICAS: INTEGRACIÓN NUMÉRICA (PRUEBA FINAL) =====================

def generate_integration_function():
    """Crea función e integral bajo curva para integración
    Genera casos realistas con a=0, b=1 y funciones como (1-x²), polinomios, etc.
    """
    func_type = random.choice(['polynomial', 'one_minus_x2', 'exponential', 'sine'])
    a = 0
    b = 1
    
    if func_type == 'one_minus_x2':
        # Función clásica: (1 - x²)
        def f(x):
            return 1 - x**2
        # Integral: ∫(1-x²)dx = x - x³/3
        integral_exact = b - (b**3)/3 - (a - (a**3)/3)
        func_name = "(1 - x²)"
    elif func_type == 'polynomial':
        # Polinomios más complejos: coeficientes aleatorios
        degree = random.randint(2, 3)
        coeffs = [random.uniform(0.5, 2) for _ in range(degree + 1)]
        
        def f(x):
            return sum(c * x**i for i, c in enumerate(coeffs))
        
        # Integral analítica: ∑ c_i * x^(i+1)/(i+1)
        integral_exact = sum(coeffs[i] * (b**(i+1) - a**(i+1)) / (i + 1) for i in range(len(coeffs)))
        
        # Crear nombre legible
        terms = []
        for i, c in enumerate(coeffs):
            if abs(c) > 0.01:
                if i == 0:
                    terms.append(f"{c:.2f}")
                elif i == 1:
                    terms.append(f"{c:.2f}x")
                else:
                    terms.append(f"{c:.2f}x^{i}")
        func_name = " + ".join(terms).replace("+ -", "- ")[:30]
    elif func_type == 'exponential':
        # e^x o múltiplos
        coeff = random.choice([0.5, 1, 1.5, 2])
        
        def f(x):
            return coeff * np.exp(x)
        
        integral_exact = coeff * (np.exp(b) - np.exp(a))
        func_name = f"{coeff}·e^x" if coeff != 1 else "e^x"
    else:  # sine
        # sin(x), cos(x) o múltiplos
        coeff = random.uniform(0.5, 2)
        trig_func = random.choice(['sin', 'cos'])
        
        if trig_func == 'sin':
            def f(x):
                return coeff * np.sin(x)
            integral_exact = coeff * (-np.cos(b) + np.cos(a))
            func_name = f"{coeff:.1f}·sen(x)" if coeff != 1 else "sen(x)"
        else:
            def f(x):
                return coeff * np.cos(x)
            integral_exact = coeff * (np.sin(b) - np.sin(a))
            func_name = f"{coeff:.1f}·cos(x)" if coeff != 1 else "cos(x)"
    
    return f, a, b, integral_exact, func_type, func_name

def generate_integration_final():
    """Problema de integración con n > 4"""
    f, a, b, integral_exact, func_type, func_name = generate_integration_function()
    n = random.randint(6, 10)
    
    # Calcular con Simpson 1/3 (requiere n par)
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    sum_odd = 0
    for i in range(1, n, 2):
        sum_odd += f(a + i * h)
    sum_even = 0
    for i in range(2, n, 2):
        sum_even += f(a + i * h)
    integral_computed = (h / 3) * (f(a) + 4*sum_odd + 2*sum_even + f(b))
    
    table_rows = [
        (f"Integrar: ∫ f(x) dx desde {round(a, 2)} hasta {round(b, 2)}",),
        (f"Función: {func_name}",),
        (f"n = {n} intervalos",)
    ]
    
    correct_str = _round_str(integral_computed, 4)
    distractors = set()
    # Error de cálculo: omitir un término
    integral_wrong1 = integral_computed * 1.08
    # Usar trapecio en lugar de Simpson
    trap_result = (h/2) * (f(a) + f(b) + 2*sum(f(a+i*h) for i in range(1, n)))
    distractors.add(_round_str(integral_wrong1, 4))
    distractors.add(_round_str(trap_result, 4))
    # Perturbaciones
    for _ in range(3):
        perturb = integral_computed * (1 + random.uniform(-0.1, 0.1))
        distractors.add(_round_str(perturb, 4))
    
    distractors = list(distractors)[:4]
    while len(distractors) < 4:
        extra = integral_computed + random.uniform(-2, 2)
        e_str = _round_str(extra, 4)
        if e_str not in distractors and e_str != correct_str:
            distractors.append(e_str)
    
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: Integration ({func_type}, n={n}) Final -> integral: {integral_computed:.6f}")
    return {
        'title': f'Integración ({func_name}, n={n})',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 25
    }

def generate_integration_simple():
    """Problema de integración más simple (n ≤ 4) para Intermedio"""
    f, a, b, integral_exact, func_type, func_name = generate_integration_function()
    n = random.randint(2, 4)
    
    # Calcular con Simpson 1/3 (requiere n par)
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    sum_odd = 0
    for i in range(1, n, 2):
        sum_odd += f(a + i * h)
    sum_even = 0
    for i in range(2, n, 2):
        sum_even += f(a + i * h)
    integral_computed = (h / 3) * (f(a) + 4*sum_odd + 2*sum_even + f(b))
    
    table_rows = [
        (f"Integrar: ∫ f(x) dx desde {round(a, 2)} hasta {round(b, 2)}",),
        (f"Función: {func_name}",),
        (f"n = {n} intervalos",)
    ]
    
    correct_str = _round_str(integral_computed, 4)
    distractors = set()
    # Error de cálculo: omitir un término
    integral_wrong1 = integral_computed * 1.08
    # Usar trapecio en lugar de Simpson
    trap_result = (h/2) * (f(a) + f(b) + 2*sum(f(a+i*h) for i in range(1, n)))
    distractors.add(_round_str(integral_wrong1, 4))
    distractors.add(_round_str(trap_result, 4))
    # Perturbaciones
    for _ in range(3):
        perturb = integral_computed * (1 + random.uniform(-0.1, 0.1))
        distractors.add(_round_str(perturb, 4))
    
    distractors = list(distractors)[:4]
    while len(distractors) < 4:
        extra = integral_computed + random.uniform(-2, 2)
        e_str = _round_str(extra, 4)
        if e_str not in distractors and e_str != correct_str:
            distractors.append(e_str)
    
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: Integration ({func_type}, n={n}) Intermedio -> integral: {integral_computed:.6f}")
    return {
        'title': f'Integración ({func_name}, n={n})',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 30
    }

def generate_trapezoidal_final():
    return generate_integration_final()

def generate_trapezoidal_intermedio():
    return generate_integration_simple()

def generate_simpson_1_3_final():
    return generate_integration_final()

def generate_simpson_1_3_intermedio():
    return generate_integration_simple()

def generate_simpson_3_8_final():
    return generate_integration_final()

def generate_simpson_3_8_intermedio():
    return generate_integration_simple()

def generate_integration_for_cotes(max_n=10):
    """Problema de integración con N limitado para Newton-Cotes"""
    f, a, b, integral_exact, func_type, func_name = generate_integration_function()
    n = random.randint(4, max_n)
    
    # Calcular con Simpson 1/3 (requiere n par)
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    sum_odd = 0
    for i in range(1, n, 2):
        sum_odd += f(a + i * h)
    sum_even = 0
    for i in range(2, n, 2):
        sum_even += f(a + i * h)
    integral_computed = (h / 3) * (f(a) + 4*sum_odd + 2*sum_even + f(b))
    
    table_rows = [
        (f"Integrar: ∫ f(x) dx desde {round(a, 2)} hasta {round(b, 2)}",),
        (f"Función: {func_name}",),
        (f"n = {n} intervalos",)
    ]
    
    correct_str = _round_str(integral_computed, 4)
    distractors = set()
    # Error de cálculo: omitir un término
    integral_wrong1 = integral_computed * 1.08
    # Usar trapecio en lugar de Simpson
    trap_result = (h/2) * (f(a) + f(b) + 2*sum(f(a+i*h) for i in range(1, n)))
    distractors.add(_round_str(integral_wrong1, 4))
    distractors.add(_round_str(trap_result, 4))
    # Perturbaciones
    for _ in range(3):
        perturb = integral_computed * (1 + random.uniform(-0.1, 0.1))
        distractors.add(_round_str(perturb, 4))
    
    distractors = list(distractors)[:4]
    while len(distractors) < 4:
        extra = integral_computed + random.uniform(-2, 2)
        e_str = _round_str(extra, 4)
        if e_str not in distractors and e_str != correct_str:
            distractors.append(e_str)
    
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: Integration ({func_type}, n={n}) Final -> integral: {integral_computed:.6f}")
    return {
        'title': f'Integración ({func_name}, n={n})',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 25
    }

def generate_cotes_final():
    """Newton-Cotes: elige aleatoriamente entre Abiertas (n≤6) y Cerradas (n≤10)"""
    method = random.choice(['Abiertas', 'Cerradas'])
    max_n = 6 if method == 'Abiertas' else 10
    result = generate_integration_for_cotes(max_n=max_n)
    # Modificar el título para incluir el método seleccionado
    result['title'] = f'Resuelve según el método Newton-Cotes {method}'
    # Agregar la imagen de la tabla correspondiente (TNCA = Tabla Newton Cotes Abiertas, TNCC = Tabla Newton Cotes Cerradas)
    image_abbr = 'TNCA' if method == 'Abiertas' else 'TNCC'
    result['image'] = image_abbr
    return result

def generate_cotes_intermedio():
    """Newton-Cotes Intermedio: elige aleatoriamente entre Abiertas (n≤4) y Cerradas (n≤6)"""
    method = random.choice(['Abiertas', 'Cerradas'])
    max_n = 4 if method == 'Abiertas' else 6
    result = generate_integration_for_cotes(max_n=max_n)
    # Modificar el título para incluir el método seleccionado
    result['title'] = f'Resuelve según el método Newton-Cotes {method}'
    # Agregar la imagen de la tabla correspondiente
    image_abbr = 'TNCA' if method == 'Abiertas' else 'TNCC'
    result['image'] = image_abbr
    result['time_minutes'] = 30
    return result

def generate_cotes_closed_final():
    """Newton-Cotes Cerradas: n ≤ 10"""
    result = generate_integration_for_cotes(max_n=10)
    result['title'] = f'Newton-Cotes Cerradas: {result["title"]}'
    result['image'] = 'TNCC'
    return result

def generate_cotes_open_final():
    """Newton-Cotes Abiertas: n ≤ 6"""
    result = generate_integration_for_cotes(max_n=6)
    result['title'] = f'Newton-Cotes Abiertas: {result["title"]}'
    result['image'] = 'TNCA'
    return result

# ===================== FACTORÍAS DINÁMICAS: MÍNIMOS CUADRADOS (PRUEBA FINAL) =====================

def generate_least_squares_final():
    """Generador para mínimos cuadrados dinámico"""
    method = random.choice(['lineal', 'cuadrática', 'cúbica'])
    n_points = random.randint(5, 8)
    
    # Generar datos
    xs = sorted([random.uniform(0, 10) for _ in range(n_points)])
    
    if method == 'lineal':
        # y = a + bx
        a0, a1 = random.uniform(1, 5), random.uniform(0.5, 2)
        points = [(x, a0 + a1*x + random.uniform(-0.5, 0.5)) for x in xs]
        x_eval = round(random.uniform(min(xs), max(xs)), 2)
        y_pred = a0 + a1*x_eval
    elif method == 'cuadrática':
        a0, a1, a2 = random.uniform(1, 4), random.uniform(-0.5, 1), random.uniform(-0.3, 0.3)
        points = [(x, a0 + a1*x + a2*x**2 + random.uniform(-0.8, 0.8)) for x in xs]
        x_eval = round(random.uniform(min(xs), max(xs)), 2)
        y_pred = a0 + a1*x_eval + a2*x_eval**2
    else:  # cúbica
        a0, a1, a2, a3 = random.uniform(1, 3), random.uniform(-0.3, 0.8), random.uniform(-0.2, 0.2), random.uniform(-0.05, 0.05)
        points = [(x, a0 + a1*x + a2*x**2 + a3*x**3 + random.uniform(-1, 1)) for x in xs]
        x_eval = round(random.uniform(min(xs), max(xs)), 2)
        y_pred = a0 + a1*x_eval + a2*x_eval**2 + a3*x_eval**3
    
    table_rows = [("Ajustar mínimos cuadrados",), ("Datos:",)]
    for x, y in points[:6]:
        table_rows.append((round(x, 2), round(y, 2)))
    
    # Opciones
    correct_str = _round_str(y_pred, 4)
    distractors = set()
    for k in range(4):
        perturb = y_pred * (1 + random.uniform(-0.12, 0.12))
        p_str = _round_str(perturb, 4)
        if p_str != correct_str:
            distractors.add(p_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = y_pred + random.uniform(-3, 3)
        e_str = _round_str(extra, 4)
        if e_str != correct_str and e_str not in distractors:
            distractors.append(e_str)
    
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: Least Squares ({method}) Final -> y_pred({x_eval:.2f}): {y_pred:.6f}")
    return {
        'title': 'Resuelve según el método',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 25
    }

def generate_least_squares_simple():
    """Generador para mínimos cuadrados simplificado - solo 4-5 puntos"""
    method = random.choice(['lineal', 'cuadrática'])  # Sin cúbica
    n_points = random.randint(4, 5)  # Menos puntos
    
    # Generar datos
    xs = sorted([random.uniform(0, 8) for _ in range(n_points)])
    
    if method == 'lineal':
        # y = a + bx
        a0, a1 = random.uniform(1, 3), random.uniform(0.5, 1.5)
        points = [(x, a0 + a1*x + random.uniform(-0.3, 0.3)) for x in xs]
        x_eval = round(random.uniform(min(xs), max(xs)), 2)
        y_pred = a0 + a1*x_eval
    else:  # cuadrática (no cúbica)
        a0, a1, a2 = random.uniform(1, 3), random.uniform(-0.3, 0.8), random.uniform(-0.2, 0.2)
        points = [(x, a0 + a1*x + a2*x**2 + random.uniform(-0.5, 0.5)) for x in xs]
        x_eval = round(random.uniform(min(xs), max(xs)), 2)
        y_pred = a0 + a1*x_eval + a2*x_eval**2
    
    table_rows = [("Ajustar mínimos cuadrados",), ("Datos:",)]
    for x, y in points:  # Mostrar todos los puntos (solo 4-5)
        table_rows.append((round(x, 2), round(y, 2)))
    
    # Opciones
    correct_str = _round_str(y_pred, 4)
    distractors = set()
    for k in range(4):
        perturb = y_pred * (1 + random.uniform(-0.12, 0.12))
        p_str = _round_str(perturb, 4)
        if p_str != correct_str:
            distractors.add(p_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = y_pred + random.uniform(-2, 2)
        e_str = _round_str(extra, 4)
        if e_str != correct_str and e_str not in distractors:
            distractors.append(e_str)
    
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: Least Squares ({method}) Intermedio -> y_pred({x_eval:.2f}): {y_pred:.6f}")
    return {
        'title': 'Resuelve según el método',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 30
    }

def generate_least_sq_linear_final():
    return generate_least_squares_final()

def generate_least_sq_quadratic_final():
    return generate_least_squares_final()

def generate_least_sq_cubic_final():
    return generate_least_squares_final()

def generate_least_sq_linear_func_final():
    return generate_least_squares_final()

def generate_least_sq_quadratic_func_final():
    return generate_least_squares_final()

# ===================== FACTORÍAS DINÁMICAS: EDO (PRUEBA FINAL) =====================

def generate_ode_final():
    """Generador para ecuaciones diferenciales ordinarias"""
    method = random.choice(['euler', 'rk2', 'rk4'])
    # EDO simple: dy/dx = ay + b
    a = random.uniform(-1, 0.5)
    b = random.uniform(-2, 2)
    y0 = random.uniform(0.5, 2)
    h = random.choice([0.05, 0.1])
    steps = random.randint(2, 4)
    
    # Solución analítica aproximada
    def ode_func(y, x):
        return a*y + b
    
    y_current = y0
    x_current = 0
    for _ in range(steps):
        # Euler simple para valor de referencia
        y_current = y_current + h * ode_func(y_current, x_current)
        x_current += h
    
    x_eval = round(x_current, 2)
    y_true = y_current
    
    table_rows = [
        (f"EDO: dy/dx = {a:.2f}*y + {b:.2f}",),
        (f"y(0) = {y0:.2f}",),
        (f"h = {h}, calcular y({x_eval})",)
    ]
    
    correct_str = _round_str(y_true, 4)
    distractors = set()
    for k in range(4):
        perturb = y_true * (1 + random.uniform(-0.15, 0.15))
        p_str = _round_str(perturb, 4)
        if p_str != correct_str:
            distractors.add(p_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = y_true + random.uniform(-0.5, 0.5)
        e_str = _round_str(extra, 4)
        if e_str != correct_str and e_str not in distractors:
            distractors.append(e_str)
    
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: ODE ({method}) Final -> y({x_eval}): {y_true:.6f}")
    return {
        'title': 'Resuelve según el método',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 25
    }

def generate_ode_simple():
    """Generador para ecuaciones diferenciales ordinarias - versión más simple para Intermedio"""
    method = random.choice(['euler', 'rk2', 'rk4'])
    # EDO simple: dy/dx = ay + b
    a = random.uniform(-0.8, -0.2)  # Valores más simples
    b = random.uniform(-1, 1)
    y0 = random.uniform(1, 2)
    h = 0.1  # Valor fijo para simplificar
    steps = random.randint(1, 2)  # Menos pasos
    
    # Solución analítica aproximada
    def ode_func(y, x):
        return a*y + b
    
    y_current = y0
    x_current = 0
    for _ in range(steps):
        # Euler simple para valor de referencia
        y_current = y_current + h * ode_func(y_current, x_current)
        x_current += h
    
    x_eval = round(x_current, 2)
    y_true = y_current
    
    table_rows = [
        (f"EDO: dy/dx = {a:.2f}*y + {b:.2f}",),
        (f"y(0) = {y0:.2f}",),
        (f"h = {h}, calcular y({x_eval})",)
    ]
    
    correct_str = _round_str(y_true, 4)
    distractors = set()
    for k in range(4):
        perturb = y_true * (1 + random.uniform(-0.15, 0.15))
        p_str = _round_str(perturb, 4)
        if p_str != correct_str:
            distractors.add(p_str)
    distractors = list(distractors)
    while len(distractors) < 4:
        extra = y_true + random.uniform(-0.5, 0.5)
        e_str = _round_str(extra, 4)
        if e_str != correct_str and e_str not in distractors:
            distractors.append(e_str)
    
    options = distractors[:4] + [correct_str]
    random.shuffle(options)
    
    print(f"DEBUG: ODE ({method}) Intermedio -> y({x_eval}): {y_true:.6f}")
    return {
        'title': 'Resuelve según el método',
        'x_value': None,
        'table': table_rows,
        'options': options,
        'correct': correct_str,
        'time_minutes': 30
    }

def generate_euler_modified_final():
    return generate_ode_final()

def generate_rk2_final():
    return generate_ode_final()

def generate_rk3_final():
    return generate_ode_final()

def generate_rk4_simpson13_final():
    return generate_ode_final()

def generate_rk4_simpson38_final():
    return generate_ode_final()

def generate_rk_higher_order_final():
    return generate_ode_final()

# ===================== FACTORÍAS DINÁMICAS: NIVEL AVANZADO =====================
# Los ejercicios Intermedio son versiones simplificadas de Prueba Final con 15 min
# Los ejercicios Avanzado son idénticos a Prueba Final pero con 30 min en lugar de 25
# Todos siguen la misma estructura: mismas opciones de respuesta y dificultad matemática similar,
# solo varía el tiempo para resolver


def generate_lagrange_intermedio():
    return generate_lagrange_simple()

def generate_linear_intermedio_1():
    return generate_linear_interp_simple()

def generate_newton_div_diff_intermedio_1():
    return generate_newton_div_diff_simple()

def generate_newton_forward_intermedio_1():
    return generate_newton_forward_simple()

def generate_newton_backward_intermedio_1():
    return generate_newton_backward_simple()

def generate_graphical_intermedio_1():
    return generate_nonlinear_simple()

def generate_bisection_intermedio_1():
    return generate_nonlinear_simple()

def generate_fixed_point_intermedio_1():
    return generate_nonlinear_simple()

def generate_false_position_intermedio_1():
    return generate_nonlinear_simple()

def generate_secant_intermedio_1():
    return generate_nonlinear_simple()

def generate_newton_raphson_intermedio_1():
    return generate_nonlinear_simple()

def generate_gauss_seidel_intermedio_1():
    return generate_linear_system_simple(2)

def generate_jacobi_intermedio_1():
    return generate_linear_system_simple(2)

def generate_montante_intermedio_1():
    return generate_linear_system_simple(2)

def generate_gauss_jordan_intermedio_1():
    return generate_linear_system_simple(3)

def generate_gaussian_elim_intermedio_1():
    return generate_linear_system_simple(2)

def generate_least_sq_linear_intermedio_1():
    return generate_least_squares_simple()

def generate_least_sq_quadratic_intermedio_1():
    return generate_least_squares_simple()

def generate_least_sq_cubic_intermedio_1():
    return generate_least_squares_simple()

def generate_least_sq_linear_func_intermedio_1():
    return generate_least_squares_simple()

def generate_least_sq_quadratic_func_intermedio_1():
    return generate_least_squares_simple()

def generate_trapezoidal_intermedio_1():
    return generate_integration_simple()

def generate_simpson_1_3_intermedio_1():
    return generate_integration_simple()

def generate_simpson_3_8_intermedio_1():
    return generate_integration_simple()

def generate_cotes_intermedio_1():
    """Newton-Cotes Intermedio con N más pequeño"""
    method = random.choice(['Abiertas', 'Cerradas'])
    max_n = 4 if method == 'Abiertas' else 6
    result = generate_integration_for_cotes(max_n=max_n)
    result['title'] = f'Resuelve según el método Newton-Cotes {method}'
    image_abbr = 'TNCA' if method == 'Abiertas' else 'TNCC'
    result['image'] = image_abbr
    result['time_minutes'] = 30
    return result

def generate_euler_modified_intermedio_1():
    return generate_ode_simple()

def generate_rk2_intermedio_1():
    return generate_ode_simple()

def generate_rk3_intermedio_1():
    return generate_ode_simple()

def generate_rk4_simpson13_intermedio_1():
    return generate_ode_simple()

def generate_rk4_simpson38_intermedio_1():
    return generate_ode_simple()

def generate_rk_higher_order_intermedio_1():
    return generate_ode_simple()

def generate_lagrange_avanzado():
    result = generate_lagrange_final()
    result['time_minutes'] = 30
    return result

def generate_linear_avanzado_1():
    result = generate_linear_interp_final()
    result['time_minutes'] = 30
    return result

def generate_newton_div_diff_avanzado_1():
    result = generate_newton_div_diff_final()
    result['time_minutes'] = 30
    return result

def generate_newton_forward_avanzado_1():
    result = generate_newton_forward_final()
    result['time_minutes'] = 30
    return result

def generate_newton_backward_avanzado_1():
    result = generate_newton_backward_final()
    result['time_minutes'] = 30
    return result

def generate_graphical_avanzado_1():
    result = generate_graphical_final()
    result['time_minutes'] = 30
    return result

def generate_bisection_avanzado_1():
    result = generate_bisection_final()
    result['time_minutes'] = 30
    return result

def generate_fixed_point_avanzado_1():
    result = generate_fixed_point_final()
    result['time_minutes'] = 30
    return result

def generate_false_position_avanzado_1():
    result = generate_false_position_final()
    result['time_minutes'] = 30
    return result

def generate_secant_avanzado_1():
    result = generate_secant_final()
    result['time_minutes'] = 30
    return result

def generate_newton_raphson_avanzado_1():
    result = generate_newton_raphson_final()
    result['time_minutes'] = 30
    return result

def generate_gauss_seidel_avanzado_1():
    result = generate_gauss_seidel_final()
    result['time_minutes'] = 30
    return result

def generate_jacobi_avanzado_1():
    result = generate_jacobi_final()
    result['time_minutes'] = 30
    return result

def generate_montante_avanzado_1():
    result = generate_montante_final()
    result['time_minutes'] = 30
    return result

def generate_gauss_jordan_avanzado_1():
    result = generate_gauss_jordan_final()
    result['time_minutes'] = 30
    return result

def generate_gaussian_elim_avanzado_1():
    result = generate_gaussian_elim_final()
    result['time_minutes'] = 30
    return result

def generate_least_sq_linear_avanzado_1():
    result = generate_least_sq_linear_final()
    result['time_minutes'] = 30
    return result

def generate_least_sq_quadratic_avanzado_1():
    result = generate_least_sq_quadratic_final()
    result['time_minutes'] = 30
    return result

def generate_least_sq_cubic_avanzado_1():
    result = generate_least_sq_cubic_final()
    result['time_minutes'] = 30
    return result

def generate_least_sq_linear_func_avanzado_1():
    result = generate_least_sq_linear_func_final()
    result['time_minutes'] = 30
    return result

def generate_least_sq_quadratic_func_avanzado_1():
    result = generate_least_sq_quadratic_func_final()
    result['time_minutes'] = 30
    return result

def generate_trapezoidal_avanzado_1():
    result = generate_trapezoidal_final()
    result['time_minutes'] = 30
    return result

def generate_simpson_1_3_avanzado_1():
    result = generate_simpson_1_3_final()
    result['time_minutes'] = 30
    return result

def generate_simpson_3_8_avanzado_1():
    result = generate_simpson_3_8_final()
    result['time_minutes'] = 30
    return result

def generate_cotes_avanzado_1():
    result = generate_cotes_final()
    result['time_minutes'] = 30
    return result

def generate_cotes_closed_avanzado_1():
    result = generate_cotes_closed_final()
    result['time_minutes'] = 30
    return result

def generate_cotes_open_avanzado_1():
    result = generate_cotes_open_final()
    result['time_minutes'] = 30
    return result

def generate_euler_modified_avanzado_1():
    result = generate_euler_modified_final()
    result['time_minutes'] = 30
    return result

def generate_rk2_avanzado_1():
    result = generate_rk2_final()
    result['time_minutes'] = 30
    return result

def generate_rk3_avanzado_1():
    result = generate_rk3_final()
    result['time_minutes'] = 30
    return result

def generate_rk4_simpson13_avanzado_1():
    result = generate_rk4_simpson13_final()
    result['time_minutes'] = 30
    return result

def generate_rk4_simpson38_avanzado_1():
    result = generate_rk4_simpson38_final()
    result['time_minutes'] = 30
    return result

def generate_rk_higher_order_avanzado_1():
    result = generate_rk_higher_order_final()
    result['time_minutes'] = 30
    return result

# Mapeo de claves de problemas finales a sus factorías
DYNAMIC_PROBLEM_FACTORIES = {
    # Interpolación
    'lagrange_final': generate_lagrange_final,
    'linear_interp_1': generate_linear_interp_final,
    'newton_div_diff_1': generate_newton_div_diff_final,
    'newton_forward_1': generate_newton_forward_final,
    'newton_backward_1': generate_newton_backward_final,
    # Ecuaciones Lineales
    'gauss_seidel_1': generate_gauss_seidel_final,
    'jacobi_1': generate_jacobi_final,
    'montante_1': generate_montante_final,
    'gauss_jordan_1': generate_gauss_jordan_final,
    'gaussian_elim_1': generate_gaussian_elim_final,
    # Ecuaciones No Lineales
    'bisection_1': generate_bisection_final,
    'false_position_1': generate_false_position_final,
    'newton_raphson_1': generate_newton_raphson_final,
    'fixed_point_1': generate_fixed_point_final,
    'secant_1': generate_secant_final,
    'graphical_1': generate_graphical_final,
    # Integración Numérica
    'trapezoidal_1': generate_trapezoidal_final,
    'simpson_1_3_1': generate_simpson_1_3_final,
    'simpson_3_8_1': generate_simpson_3_8_final,
    'cotes_1': generate_cotes_final,
    # Mínimos Cuadrados
    'least_sq_linear_1': generate_least_sq_linear_final,
    'least_sq_quadratic_1': generate_least_sq_quadratic_final,
    'least_sq_cubic_1': generate_least_sq_cubic_final,
    'least_sq_linear_func_1': generate_least_sq_linear_func_final,
    'least_sq_quadratic_func_1': generate_least_sq_quadratic_func_final,
    # EDO
    'euler_modified_1': generate_euler_modified_final,
    'rk2_1': generate_rk2_final,
    'rk3_1': generate_rk3_final,
    'rk4_simpson13_1': generate_rk4_simpson13_final,
    'rk4_simpson38_1': generate_rk4_simpson38_final,
    'rk_higher_order_1': generate_rk_higher_order_final,
}

PROBLEM_DATA = {
    'lagrange_intermedio': generate_lagrange_intermedio,
    'lagrange_avanzado': generate_lagrange_avanzado,
    'lagrange_final': generate_lagrange_final,
    'linear_interp_1': generate_linear_interp_final,
    'newton_div_diff_1': generate_newton_div_diff_final,
    'newton_forward_1': generate_newton_forward_final,
    'newton_backward_1': generate_newton_backward_final,
    'bisection_1': generate_bisection_final,
    'false_position_1': generate_false_position_final,
    'newton_raphson_1': generate_newton_raphson_final,
    'fixed_point_1': generate_fixed_point_final,
    'secant_1': generate_secant_final,
    'graphical_1': generate_graphical_final,
    'gauss_seidel_1': generate_gauss_seidel_final,
    'jacobi_1': generate_jacobi_final,
    'montante_1': generate_montante_final,
    'gauss_jordan_1': generate_gauss_jordan_final,
    'gaussian_elim_1': generate_gaussian_elim_final,
    'trapezoidal_1': generate_trapezoidal_final,
    'simpson_1_3_1': generate_simpson_1_3_final,
    'simpson_3_8_1': generate_simpson_3_8_final,
    'cotes_1': generate_cotes_final,
    'cotes_closed_1': generate_cotes_closed_final,
    'cotes_open_1': generate_cotes_open_final,
    'least_sq_linear_1': generate_least_sq_linear_final,
    'least_sq_quadratic_1': generate_least_sq_quadratic_final,
    'least_sq_cubic_1': generate_least_sq_cubic_final,
    'least_sq_linear_func_1': generate_least_sq_linear_func_final,
    'least_sq_quadratic_func_1': generate_least_sq_quadratic_func_final,
    'euler_modified_1': generate_euler_modified_final,
    'rk2_1': generate_rk2_final,
    'rk3_1': generate_rk3_final,
    'rk4_simpson13_1': generate_rk4_simpson13_final,
    'rk4_simpson38_1': generate_rk4_simpson38_final,
    'rk_higher_order_1': generate_rk_higher_order_final,
    'linear_facil_1': {
        'title': 'La interpolación lineal une dos puntos mediante una...',
        'options': ['Parábola', 'Línea Recta'],
        'correct': 'Línea Recta'
    },
    'linear_intermedio_1': generate_linear_intermedio_1,
    'linear_avanzado_1': generate_linear_avanzado_1,
    'newton_div_diff_facil_1': {
        'title': '¿Qué tipo de intervalos maneja principalmente este método?',
        'options': ['Uniformes', 'No Uniformes'],
        'correct': 'No Uniformes'
    },
    'newton_div_diff_intermedio_1': generate_newton_div_diff_intermedio_1,
    'newton_div_diff_avanzado_1': generate_newton_div_diff_avanzado_1,
    'newton_forward_facil_1': {
        'title': 'En Newton Adelante, el factor "s" se calcula como:',
        'options': ['(x - xi) / h', '(x + xi) / h'],
        'correct': '(x - xi) / h'
    },
    'newton_forward_intermedio_1': generate_newton_forward_intermedio_1,
    'newton_forward_avanzado_1': generate_newton_forward_avanzado_1,
    'newton_backward_facil_1': {
        'title': 'El signo del factor binomial "s" en este método es generalmente:',
        'options': ['Positivo', 'Negativo'],
        'correct': 'Negativo'
    },
    'newton_backward_intermedio_1': generate_newton_backward_intermedio_1,
    'newton_backward_avanzado_1': generate_newton_backward_avanzado_1,
    'bisection_facil_1': {
        'title': 'Si f(a) es positivo y f(b) positivo, ¿hay raíz garantizada?',
        'options': ['Si', 'No'],
        'correct': 'No'
    },
    'bisection_intermedio_1': generate_bisection_intermedio_1,
    'bisection_avanzado_1': generate_bisection_avanzado_1,
    'false_position_facil_1': {
        'title': 'Este método se basa en una visualización:',
        'options': ['Gráfica', 'Aleatoria'],
        'correct': 'Gráfica'
    },
    'false_position_intermedio_1': generate_false_position_intermedio_1,
    'false_position_avanzado_1': generate_false_position_avanzado_1,
    'newton_raphson_facil_1': {
        'title': '¿Qué requiere este método obligatoriamente?',
        'options': ['La derivada f\'(x)', 'Dos puntos iniciales'],
        'correct': 'La derivada f\'(x)'
    },
    'newton_raphson_intermedio_1': generate_newton_raphson_intermedio_1,
    'newton_raphson_avanzado_1': generate_newton_raphson_avanzado_1,
    'fixed_point_facil_1': {
        'title': 'Si $2x^2 - x - 5 = 0$, una posible g(x) es:',
        'options': ['$2x^2 - 5$', '$\\sqrt{(x+5)/2}$'],
        'correct': '$2x^2 - 5$'
    },
    'fixed_point_intermedio_1': generate_fixed_point_intermedio_1,
    'fixed_point_avanzado_1': generate_fixed_point_avanzado_1,
    'secant_facil_1': {
        'title': '¿Cuántos valores iniciales requiere la Secante?',
        'options': ['1', '2'],
        'correct': '2'
    },
    'secant_intermedio_1': generate_secant_intermedio_1,
    'secant_avanzado_1': generate_secant_avanzado_1,
    'graphical_facil_1': {
        'title': 'Una raíz se identifica visualmente cuando la curva cruza el eje:',
        'options': ['X', 'Y'],
        'correct': 'X'
    },
    'graphical_intermedio_1': generate_graphical_intermedio_1,
    'graphical_avanzado_1': generate_graphical_avanzado_1,
    'gauss_seidel_facil_1': {
        'title': '¿Qué valores usa para calcular la variable "b" en la iteración 1?',
        'options': ['Los iniciales (0)', 'El nuevo "a" recién calculado'],
        'correct': 'El nuevo "a" recién calculado'
    },
    'gauss_seidel_intermedio_1': generate_gauss_seidel_intermedio_1,
    'gauss_seidel_avanzado_1': generate_gauss_seidel_avanzado_1,
    'jacobi_facil_1': {
        'title': 'Diferencia clave con Gauss-Seidel:',
        'options': ['Uso de valores anteriores', 'No iterativo'],
        'correct': 'Uso de valores anteriores'
    },
    'jacobi_intermedio_1': generate_jacobi_intermedio_1,
    'jacobi_avanzado_1': generate_jacobi_avanzado_1,
    'montante_facil_1': {
        'title': 'El método Montante utiliza principalmente aritmética de:',
        'options': ['Enteros', 'Fracciones'],
        'correct': 'Enteros'
    },
    'montante_intermedio_1': generate_montante_intermedio_1,
    'montante_avanzado_1': generate_montante_avanzado_1,
    'gauss_jordan_facil_1': {
        'title': 'La matriz final en Gauss-Jordan debe ser:',
        'options': ['Identidad', 'Triangular'],
        'correct': 'Identidad'
    },
    'gauss_jordan_intermedio_1': generate_gauss_jordan_intermedio_1,
    'gauss_jordan_avanzado_1': generate_gauss_jordan_avanzado_1,
    'gaussian_elim_facil_1': {
        'title': 'A diferencia de Gauss-Jordan, aquí solo buscamos una matriz:',
        'options': ['Triangular Superior', 'Identidad'],
        'correct': 'Triangular Superior'
    },
    'gaussian_elim_intermedio_1': generate_gaussian_elim_intermedio_1,
    'gaussian_elim_avanzado_1': generate_gaussian_elim_avanzado_1,
    'trapezoidal_facil_1': {
        'title': '¿A qué grado de polinomio corresponde el trapecio?',
        'options': ['1er Grado', '2do Grado'],
        'correct': '1er Grado'
    },
    'trapezoidal_intermedio_1': generate_trapezoidal_intermedio_1,
    'trapezoidal_avanzado_1': generate_trapezoidal_avanzado_1,
    'simpson_1_3_facil_1': {
        'title': 'Requisito indispensable de "n" para 1/3 Simpson:',
        'options': ['Debe ser Par', 'Debe ser Impar'],
        'correct': 'Debe ser Par'
    },
    'simpson_1_3_intermedio_1': generate_simpson_1_3_intermedio_1,
    'simpson_1_3_avanzado_1': generate_simpson_1_3_avanzado_1,
    'simpson_3_8_facil_1': {
        'title': 'Simpson 3/8 requiere que "n" sea:',
        'options': ['Múltiplo de 3', 'Par'],
        'correct': 'Múltiplo de 3'
    },
    'simpson_3_8_intermedio_1': generate_simpson_3_8_intermedio_1,
    'simpson_3_8_avanzado_1': generate_simpson_3_8_avanzado_1,
    'cotes_closed_facil_1': {
        'title': 'En fórmulas cerradas, ¿se incluyen los límites a y b?',
        'options': ['Si', 'No'],
        'correct': 'Si'
    },
    'cotes_closed_intermedio_1': generate_cotes_intermedio_1,
    'cotes_open_intermedio_1': None,  # No se usa en GAME_STRUCTURE
    'cotes_intermedio_1': generate_cotes_intermedio_1,
    'cotes_avanzado_1': generate_cotes_avanzado_1,
    'cotes_open_facil_1': {
        'title': 'Fórmula para calcular h en Cotes Abiertas:',
        'options': ['(b-a)/(n+2)', '(b-a)/n'],
        'correct': '(b-a)/(n+2)'
    },
    'cotes_open_intermedio_1': generate_cotes_intermedio_1,
    'least_sq_linear_facil_1': {
        'title': 'El objetivo es minimizar:',
        'options': ['La dispersión (error)', 'El valor de x'],
        'correct': 'La dispersión (error)'
    },
    'least_sq_linear_intermedio_1': generate_least_sq_linear_intermedio_1,
    'least_sq_linear_avanzado_1': generate_least_sq_linear_avanzado_1,
    'least_sq_quadratic_facil_1': {
        'title': '¿Cuántas incógnitas (coeficientes) se buscan?',
        'options': ['3 (a0, a1, a2)', '2'],
        'correct': '3 (a0, a1, a2)'
    },
    'least_sq_quadratic_intermedio_1': generate_least_sq_quadratic_intermedio_1,
    'least_sq_quadratic_avanzado_1': generate_least_sq_quadratic_avanzado_1,
    'least_sq_cubic_facil_1': {
        'title': 'El sistema de ecuaciones resultante es de tamaño:',
        'options': ['4x4', '3x3'],
        'correct': '4x4'
    },
    'least_sq_cubic_intermedio_1': generate_least_sq_cubic_intermedio_1,
    'least_sq_cubic_avanzado_1': generate_least_sq_cubic_avanzado_1,
    'least_sq_linear_func_facil_1': {
        'title': 'En lugar de $x^2$, el tercer término depende de:',
        'options': ['f(x)', 'x^3'],
        'correct': 'f(x)'
    },
    'least_sq_linear_func_intermedio_1': generate_least_sq_linear_func_intermedio_1,
    'least_sq_linear_func_avanzado_1': generate_least_sq_linear_func_avanzado_1,
    'least_sq_quadratic_func_facil_1': {
        'title': 'Este modelo tiene 4 coeficientes, incluyendo:',
        'options': ['El término f(x)', 'Término cúbico'],
        'correct': 'El término f(x)'
    },
    'least_sq_quadratic_func_intermedio_1': generate_least_sq_quadratic_func_intermedio_1,
    'least_sq_quadratic_func_avanzado_1': generate_least_sq_quadratic_func_avanzado_1,
    'euler_modified_facil_1': {
        'title': '¿Qué regla de integración usa Euler Modificado?',
        'options': ['Trapezoidal', 'Simpson'],
        'correct': 'Trapezoidal'
    },
    'euler_modified_intermedio_1': generate_euler_modified_intermedio_1,
    'euler_modified_avanzado_1': generate_euler_modified_avanzado_1,
    'rk2_facil_1': {
        'title': '¿Cuántas evaluaciones de la función (k) se hacen?',
        'options': ['2', '4'],
        'correct': '2'
    },
    'rk2_intermedio_1': generate_rk2_intermedio_1,
    'rk2_avanzado_1': generate_rk2_avanzado_1,
    'rk3_facil_1': {
        'title': 'El peso mayor se le da a la pendiente intermedia:',
        'options': ['k2 (x4)', 'k1 (x1)'],
        'correct': 'k2 (x4)'
    },
    'rk3_intermedio_1': generate_rk3_intermedio_1,
    'rk3_avanzado_1': generate_rk3_avanzado_1,
    'rk4_simpson13_facil_1': {
        'title': '¿Cuáles pendientes se multiplican por 2?',
        'options': ['k2 y k3', 'k1 y k4'],
        'correct': 'k2 y k3'
    },
    'rk4_simpson13_intermedio_1': generate_rk4_simpson13_intermedio_1,
    'rk4_simpson13_avanzado_1': generate_rk4_simpson13_avanzado_1,
    'rk4_simpson38_facil_1': {
        'title': 'En esta variante, el divisor de la fórmula es:',
        'options': ['8', '6'],
        'correct': '8'
    },
    'rk4_simpson38_intermedio_1': generate_rk4_simpson38_intermedio_1,
    'rk4_simpson38_avanzado_1': generate_rk4_simpson38_avanzado_1,
    'rk_higher_order_facil_1': {
        'title': 'Para una EDO de 2do orden, necesitamos calcular:',
        'options': ['k y m', 'Solo k'],
        'correct': 'k y m'
    },
    'rk_higher_order_intermedio_1': generate_rk_higher_order_intermedio_1,
    'rk_higher_order_avanzado_1': generate_rk_higher_order_avanzado_1,
}
