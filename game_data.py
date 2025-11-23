
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
        }
    },
    "Ecuaciones No Lineales": {
        "levels": {
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
    "Integración Numérica": {
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

PROBLEM_DATA = {
    'lagrange_intermedio': {
        'title': 'Lagrange: Interpola f(2.5) con puntos (2, 4) y (3, 7)',
        'options': ['5.5', '6.5', '5', '6'],
        'time_minutes': 25,
        'correct': '5.5'
    },
    'lagrange_avanzado': {
        'title': 'Lagrange: Interpola f(2.4) con puntos (2, 2.54), (2.5, 2.82), (3, 3.21)',
        'x_value': 2.4,
        'table': [(2, 2.54), (2.5, 2.82), (3, 3.21)],
        'options': ['2.672', '2.772', '2.572', '2.872'],
        'correct': '2.672',
        'time_minutes': 30
    },
    'lagrange_final': {
        'title': 'Obtener g(x)',
        'x_value': 2.4,
        'table': [(2.2, 2.54), (2.5, 2.82), (2.8, 3.21), (3.1, 3.32), (3.4, 3.41)],
        'options': ['2.67646', '2.77646', '2.57646', '3.67646', '1.67646'],
        'correct': '2.77646',
        'time_minutes': 25
    },
    'linear_interp_1': {
        'title': 'Prueba Final: Interpolación Lineal',
        'x_value': 3,
        'table': [(2, 0.693), (5, 1.609)],
        'options': ['0.998', '1.098', '1.198', '0.898', '1.298'],
        'correct': '0.998',
        'time_minutes': 25
    },
    'newton_div_diff_1': {
        'title': 'Prueba Final: Newton Diferencias Divididas',
        'x_value': 7,
        'table': [(6.5, -1.35), (7.3, -0.28), (8.1, 0.98)],
        'options': ['-0.657', '-0.557', '-0.757', '-0.457', '-0.857'],
        'correct': '-0.657',
        'time_minutes': 25
    },
    'newton_forward_1': {
        'title': 'Prueba Final: Newton Hacia Adelante',
        'x_value': 3,
        'table': [(1.7, 0.53), (2.4, 0.88), (3.1, 1.09)],
        'options': ['1.029', '1.129', '0.929', '1.229', '0.829'],
        'correct': '1.029',
        'time_minutes': 25
    },
    'newton_backward_1': {
        'title': 'Prueba Final: Newton Hacia Atrás',
        'x_value': 3,
        'table': [(1.7, 0.53), (2.4, 0.88), (3.1, 1.09)],
        'options': ['1.029', '1.129', '0.929', '1.229', '0.829'],
        'correct': '1.029',
        'time_minutes': 25
    },
    'bisection_1': {
        'title': 'Prueba Final: Método de Bisección',
        'x_value': None,
        'table': [('Función: f(x) = x² - 2',), ('Intervalo: [1, 2]',), ('Encuentra la raíz con 5 iteraciones',)],
        'options': ['1.5', '1.6', '1.4', '1.7', '1.3'],
        'correct': '1.5',
        'time_minutes': 25
    },
    'false_position_1': {
        'title': 'Prueba Final: Método de Falsa Posición',
        'x_value': None,
        'table': [('Función: f(x) = x² - 2',), ('Intervalo: [1, 2]',), ('Encuentra la raíz',)],
        'options': ['1.52', '1.62', '1.42', '1.72', '1.32'],
        'correct': '1.52',
        'time_minutes': 25
    },
    'newton_raphson_1': {
        'title': 'Prueba Final: Método de Newton-Raphson',
        'x_value': None,
        'table': [('Función: f(x) = x² - 2',), ("f'(x) = 2x",), ('Valor inicial: x₀ = 2',)],
        'options': ['1.414', '1.514', '1.314', '1.614', '1.214'],
        'correct': '1.414',
        'time_minutes': 25
    },
    'fixed_point_1': {
        'title': 'Prueba Final: Método de Punto Fijo',
        'x_value': None,
        'table': [('Función: g(x) = √(x + 1)',), ('Valor inicial: x₀ = 1',), ('Encuentra el punto fijo',)],
        'options': ['1.732', '1.832', '1.632', '1.932', '1.532'],
        'correct': '1.732',
        'time_minutes': 25
    },
    'secant_1': {
        'title': 'Prueba Final: Método de la Secante',
        'x_value': None,
        'table': [('Función: f(x) = x³ - 5',), ('Valores iniciales: x₀ = 1, x₁ = 2',), ('Encuentra la raíz',)],
        'options': ['2.094', '2.194', '1.994', '2.294', '1.894'],
        'correct': '2.094',
        'time_minutes': 25
    },
    'graphical_1': {
        'title': 'Prueba Final: Método Gráfico',
        'x_value': None,
        'table': [('Función: f(x) = x² - 2',), ('Intervalo: [0, 3]',), ('Identifica la raíz visualmente',)],
        'options': ['1.5', '1.6', '1.4', '1.7', '1.3'],
        'correct': '1.5',
        'time_minutes': 25
    },
    'gauss_seidel_1': {
        'title': 'Prueba Final: Gauss-Seidel',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('4x + y = 9',), ('x + 3y = 10',)],
        'options': ['x=2, y=1', 'x=1, y=3', 'x=3, y=2', 'x=2, y=2', 'x=1, y=2'],
        'correct': 'x=2, y=1',
        'time_minutes': 25
    },
    'jacobi_1': {
        'title': 'Prueba Final: Método de Jacobi',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('5x + y = 11',), ('x + 4y = 9',)],
        'options': ['x=2, y=1', 'x=1, y=2', 'x=3, y=1', 'x=2, y=2', 'x=1, y=3'],
        'correct': 'x=2, y=1',
        'time_minutes': 25
    },
    'montante_1': {
        'title': 'Prueba Final: Método de Montante',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('2x + y = 5',), ('x + 3y = 8',)],
        'options': ['x=1, y=3', 'x=2, y=1', 'x=3, y=2', 'x=2, y=2', 'x=1, y=2'],
        'correct': 'x=1, y=3',
        'time_minutes': 25
    },
    'gauss_jordan_1': {
        'title': 'Prueba Final: Gauss-Jordan',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('3x + 2y = 12',), ('x + 4y = 14',)],
        'options': ['x=2, y=3', 'x=3, y=2', 'x=1, y=4', 'x=4, y=1', 'x=2, y=2'],
        'correct': 'x=2, y=3',
        'time_minutes': 25
    },
    'gaussian_elim_1': {
        'title': 'Prueba Final: Eliminación Gaussiana',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('2x + 3y = 13',), ('x + 2y = 8',)],
        'options': ['x=2, y=3', 'x=3, y=2', 'x=1, y=4', 'x=4, y=1', 'x=2, y=2'],
        'correct': 'x=2, y=3',
        'time_minutes': 25
    },
    'trapezoidal_1': {
        'title': 'Prueba Final: Regla del Trapecio',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx desde 0 hasta 2',), ('Datos de la función:',), (0, 1), (1, 2), (2, 5)],
        'options': ['5.5', '6.5', '4.5', '7.5', '3.5'],
        'correct': '5.5',
        'time_minutes': 25
    },
    'simpson_1_3_1': {
        'title': 'Prueba Final: Simpson 1/3',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx desde 0 hasta 2',), ('Datos de la función:',), (0, 1), (1, 2), (2, 5)],
        'options': ['5.333', '6.333', '4.333', '7.333', '3.333'],
        'correct': '5.333',
        'time_minutes': 25
    },
    'simpson_3_8_1': {
        'title': 'Prueba Final: Simpson 3/8',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx desde 0 hasta 3',), ('Datos de la función:',), (0, 1), (1, 2), (2, 5), (3, 10)],
        'options': ['11.25', '12.25', '10.25', '13.25', '9.25'],
        'correct': '11.25',
        'time_minutes': 25
    },
    'cotes_closed_1': {
        'title': 'Prueba Final: Newton-Cotes Cerrado',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx desde 0 hasta 2',), ('Datos de la función:',), (0, 1), (0.5, 1.5), (1, 2.5), (1.5, 4), (2, 6)],
        'options': ['5.208', '6.208', '4.208', '7.208', '3.208'],
        'correct': '5.208',
        'time_minutes': 25
    },
    'cotes_open_1': {
        'title': 'Prueba Final: Newton-Cotes Abierto',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx',), ('Datos de la función:',), (0.5, 1.5), (1, 2.5), (1.5, 4)],
        'options': ['4.5', '5.5', '3.5', '6.5', '2.5'],
        'correct': '4.5',
        'time_minutes': 25
    },
    'least_sq_linear_1': {
        'title': 'Prueba Final: Mínimos Cuadrados Lineal',
        'x_value': 5,
        'table': [('Ajustar: y = a + bx',), ('Datos:',), (1, 2), (2, 4), (3, 5), (4, 7)],
        'options': ['8.5', '9.5', '7.5', '10.5', '6.5'],
        'correct': '8.5',
        'time_minutes': 25
    },
    'least_sq_quadratic_1': {
        'title': 'Prueba Final: Mínimos Cuadrados Cuadrático',
        'x_value': 5,
        'table': [('Ajustar: y = a + bx + cx²',), ('Datos:',), (1, 1), (2, 3), (3, 7), (4, 13)],
        'options': ['21', '22', '20', '23', '19'],
        'correct': '21',
        'time_minutes': 25
    },
    'least_sq_cubic_1': {
        'title': 'Prueba Final: Mínimos Cuadrados Cúbico',
        'x_value': 3,
        'table': [('Ajustar: y = a + bx + cx² + dx³',), ('Datos:',), (0, 1), (1, 2), (2, 5), (3, 10), (4, 20)],
        'options': ['10.2', '11.2', '9.2', '12.2', '8.2'],
        'correct': '10.2',
        'time_minutes': 25
    },
    'least_sq_linear_func_1': {
        'title': 'Prueba Final: Mínimos Cuadrados Linealización',
        'x_value': 4,
        'table': [('Linealizar y ajustar',), ('Datos:',), (1, 2.5), (2, 5.2), (3, 8.8), (4, 13.1)],
        'options': ['13.5', '14.5', '12.5', '15.5', '11.5'],
        'correct': '13.5',
        'time_minutes': 25
    },
    'least_sq_quadratic_func_1': {
        'title': 'Prueba Final: Mínimos Cuadrados Func. Cuadrática',
        'x_value': 3,
        'table': [('Ajustar función cuadrática',), ('Datos:',), (0, 1), (1, 1.5), (2, 3.8), (3, 8.2)],
        'options': ['8.5', '9.5', '7.5', '10.5', '6.5'],
        'correct': '8.5',
        'time_minutes': 25
    },
    'euler_modified_1': {
        'title': 'Prueba Final: Euler Modificado',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y",), ("Condición inicial: y(0) = 1",), ("Paso: h = 0.1",)],
        'options': ['1.221', '1.321', '1.121', '1.421', '1.021'],
        'correct': '1.221',
        'time_minutes': 25
    },
    'rk2_1': {
        'title': 'Prueba Final: Runge-Kutta Orden 2',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y",), ("Condición inicial: y(0) = 1",), ("Paso: h = 0.1",)],
        'options': ['1.242', '1.342', '1.142', '1.442', '1.042'],
        'correct': '1.242',
        'time_minutes': 25
    },
    'rk3_1': {
        'title': 'Prueba Final: Runge-Kutta Orden 3',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y",), ("Condición inicial: y(0) = 1",), ("Paso: h = 0.1",)],
        'options': ['1.246', '1.346', '1.146', '1.446', '1.046'],
        'correct': '1.246',
        'time_minutes': 25
    },
    'rk4_simpson13_1': {
        'title': 'Prueba Final: RK4 Simpson 1/3',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y",), ("Condición inicial: y(0) = 1",), ("Paso: h = 0.1",)],
        'options': ['1.2428', '1.3428', '1.1428', '1.4428', '1.0428'],
        'correct': '1.2428',
        'time_minutes': 25
    },
    'rk4_simpson38_1': {
        'title': 'Prueba Final: RK4 Simpson 3/8',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y",), ("Condición inicial: y(0) = 1",), ("Paso: h = 0.1",)],
        'options': ['1.2431', '1.3431', '1.1431', '1.4431', '1.0431'],
        'correct': '1.2431',
        'time_minutes': 25
    },
    'rk_higher_order_1': {
        'title': 'Prueba Final: RK Orden Superior',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y",), ("Condición inicial: y(0) = 1",), ("Paso: h = 0.05",)],
        'options': ['1.2435', '1.3435', '1.1435', '1.4435', '1.0435'],
        'correct': '1.2435',
        'time_minutes': 25
    },
    'linear_facil_1': {
        'title': 'La interpolación lineal une dos puntos mediante una...',
        'options': ['Parábola', 'Línea Recta'],
        'correct': 'Línea Recta'
    },
    'linear_intermedio_1': {
        'title': 'Interpola f(3) usando los puntos (2, 0.693) y (5, 1.609)',
        'x_value': 3,
        'table': [(2, 0.693), (5, 1.609)],
        'options': ['0.998', '1.098', '0.898', '1.198'],
        'time_minutes': 25,
        'correct': '0.998'
    },
    'linear_avanzado_1': {
        'title': 'Interpolación Lineal: Estima Ln(3) con (2, 0.693) y (5, 1.609)',
        'x_value': 3,
        'table': [(2, 0.693), (5, 1.609)],
        'options': ['0.998', '1.098', '0.898', '1.198'],
        'correct': '0.998',
        'time_minutes': 30
    },
    'newton_div_diff_facil_1': {
        'title': '¿Qué tipo de intervalos maneja principalmente este método?',
        'options': ['Uniformes', 'No Uniformes'],
        'correct': 'No Uniformes'
    },
    'newton_div_diff_intermedio_1': {
        'title': 'Calcula la 1ra diferencia dividida entre (6.5, -1.35) y (7.3, -0.28)',
        'options': ['1.3375', '0.8375', '1.0375', '1.2375'],
        'time_minutes': 25,
        'correct': '1.3375'
    },
    'newton_div_diff_avanzado_1': {
        'title': 'Newton Diferencias Divididas: Interpola x=7 con (6.5, -1.35), (7.3, -0.28), (8.1, 0.98)',
        'x_value': 7,
        'table': [(6.5, -1.35), (7.3, -0.28), (8.1, 0.98)],
        'options': ['-0.657', '-0.557', '-0.757', '-0.457'],
        'correct': '-0.657',
        'time_minutes': 30
    },
    'newton_forward_facil_1': {
        'title': 'En Newton Adelante, el factor "s" se calcula como:',
        'options': ['(x - xi) / h', '(x + xi) / h'],
        'correct': '(x - xi) / h'
    },
    'newton_forward_intermedio_1': {
        'title': 'Con h=0.7 y x=3, x0=1.7, calcula s = (x - x0)/h',
        'options': ['1.857', '1.657', '2.057', '1.457'],
        'time_minutes': 25,
        'correct': '1.857'
    },
    'newton_forward_avanzado_1': {
        'title': 'Newton Adelante: Interpola g(3) con (1.7, 0.53), (2.4, 0.88), (3.1, 1.09)',
        'x_value': 3,
        'table': [(1.7, 0.53), (2.4, 0.88), (3.1, 1.09)],
        'options': ['1.029', '1.129', '0.929', '1.229'],
        'correct': '1.029',
        'time_minutes': 30
    },
    'newton_backward_facil_1': {
        'title': 'El signo del factor binomial "s" en este método es generalmente:',
        'options': ['Positivo', 'Negativo'],
        'correct': 'Negativo'
    },
    'newton_backward_intermedio_1': {
        'title': 'Con x=3, xn=3.1, h=0.7, calcula s = (x - xn)/h',
        'options': ['-0.1428', '0.1428', '-0.2428', '0.2428'],
        'time_minutes': 25,
        'correct': '-0.1428'
    },
    'newton_backward_avanzado_1': {
        'title': 'Newton Atrás: Interpola g(3) con (1.7, 0.53), (2.4, 0.88), (3.1, 1.09)',
        'x_value': 3,
        'table': [(1.7, 0.53), (2.4, 0.88), (3.1, 1.09)],
        'options': ['1.029', '1.129', '0.929', '1.229'],
        'correct': '1.029',
        'time_minutes': 30
    },
    'bisection_facil_1': {
        'title': 'Si f(a) es positivo y f(b) positivo, ¿hay raíz garantizada?',
        'options': ['Si', 'No'],
        'correct': 'No'
    },
    'bisection_intermedio_1': {
        'title': 'Bisección: Primera iteración entre a=1, f(a)=-1 y b=2, f(b)=5. Calcula c',
        'options': ['0.3087', '1.25', '1.75', '1.0'],
        'time_minutes': 25,
        'correct': '0.3087'
    },
    'bisection_avanzado_1': {
        'title': 'Bisección: Encuentra raíz de f(x)=x³-6.5x+2 en [0,1] tras 3 iteraciones',
        'x_value': None,
        'table': [('Función: f(x) = x³ - 6.5x + 2',), ('Intervalo: [0, 1]',), ('Realiza 3 iteraciones',)],
        'options': ['0.3087', '0.5', '0.25', '0.375'],
        'correct': '0.3087',
        'time_minutes': 30
    },
    'false_position_facil_1': {
        'title': 'Este método se basa en una visualización:',
        'options': ['Gráfica', 'Aleatoria'],
        'correct': 'Gráfica'
    },
    'false_position_intermedio_1': {
        'title': 'Falsa Posición: Con a=1, f(a)=-2, b=2, f(b)=17, calcula c',
        'options': ['1.217859143', '1.205', '1.005', '1.305'],
        'time_minutes': 25,
        'correct': '1.217859143'
    },
    'false_position_avanzado_1': {
        'title': 'Falsa Posición: Encuentra raíz de f(x)=3x³-2x-3 tras 2 iteraciones',
        'x_value': None,
        'table': [('Función: f(x) = 3x³ - 2x - 3',), ('f(1) = -2, f(2) = 17',)],
        'options': ['1.217859143', '1.105', '1.232', '1.042'],
        'correct': '1.217859143',
        'time_minutes': 30
    },
    'newton_raphson_facil_1': {
        'title': '¿Qué requiere este método obligatoriamente?',
        'options': ['La derivada f\'(x)', 'Dos puntos iniciales'],
        'correct': 'La derivada f\'(x)'
    },
    'newton_raphson_intermedio_1': {
        'title': 'Newton-Raphson: f(x)=x³+2x²+10x-20, f\'(x)=3x²+4x+10. Con x0=1, calcula x1',
        'options': ['1.368808108', '1.311', '1.511', '1.211'],
        'time_minutes': 25,
        'correct': '1.368808108'
    },
    'newton_raphson_avanzado_1': {
        'title': 'Newton-Raphson: Encuentra raíz de f(x)=x²-2 con x0=2',
        'x_value': None,
        'table': [('Función: f(x) = x² - 2',), ("f'(x) = 2x",), ('Valor inicial: x₀ = 2',)],
        'options': ['1.368808108', '1.514', '1.314', '1.614'],
        'correct': '1.368808108',
        'time_minutes': 30
    },
    'fixed_point_facil_1': {
        'title': 'Si $2x^2 - x - 5 = 0$, una posible g(x) es:',
        'options': ['$2x^2 - 5$', '$\\sqrt{(x+5)/2}$'],
        'correct': '$2x^2 - 5$'
    },
    'fixed_point_intermedio_1': {
        'title': 'Punto Fijo: Para e^(-x) = x, usa g(x)=e^(-x). Con x0=1, calcula x1',
        'options': ['0.5671433', '0.467', '0.267', '0.567'],
        'time_minutes': 25,
        'correct': '0.5671433'
    },
    'fixed_point_avanzado_1': {
        'title': 'Punto Fijo: Encuentra raíz de f(x) = e^(-x) - x con g(x) = e^(-x)',
        'x_value': None,
        'table': [('Función: g(x) = √(x + 1)',), ('Valor inicial: x₀ = 1',), ('Encuentra el punto fijo',)],
        'options': ['0.5671433', '1.832', '1.632', '1.932'],
        'correct': '0.5671433',
        'time_minutes': 30
    },
    'secant_facil_1': {
        'title': '¿Cuántos valores iniciales requiere la Secante?',
        'options': ['1', '2'],
        'correct': '2'
    },
    'secant_intermedio_1': {
        'title': 'Secante: Con x0=0, f(x0)=0, x1=1, f(x1)=-0.63. Calcula x2 para e^(-x)-x=0',
        'options': ['0.5671433', '0.7127', '0.5127', '0.8127'],
        'time_minutes': 25,
        'correct': '0.5671433'
    },
    'secant_avanzado_1': {
        'title': 'Secante: Encuentra raíz de f(x)=x³-5 con x0=1, x1=2',
        'x_value': None,
        'table': [('Función: f(x) = x³ - 5',), ('Valores iniciales: x₀ = 1, x₁ = 2',), ('Encuentra la raíz',)],
        'options': ['0.5671433', '2.194', '1.994', '2.294'],
        'correct': '0.5671433',
        'time_minutes': 30
    },
    'graphical_facil_1': {
        'title': 'Una raíz se identifica visualmente cuando la curva cruza el eje:',
        'options': ['X', 'Y'],
        'correct': 'X'
    },
    'graphical_intermedio_1': {
        'title': 'Gráfico: Evalúa f(x)=x³-6.5x+2 en x=0: f(0)=? ¿Hay raíz entre 0 y 1?',
        'options': ['f(0)=2, sí hay raíz', 'f(0)=0, no hay raíz', 'f(0)=-1, sí hay raíz', 'f(0)=1, no hay raíz'],
        'time_minutes': 25,
        'correct': 'f(0)=2, sí hay raíz'
    },
    'graphical_avanzado_1': {
        'title': 'Gráfico: Localiza raíz de f(x)=x³-6.5x+2 usando cambios de signo',
        'x_value': None,
        'table': [('Función: f(x) = x³ - 6.5x + 2',), ('Intervalo: [0, 3]',), ('Identifica la raíz visualmente',)],
        'options': ['1.5', '1.6', '1.4', '1.7'],
        'correct': '1.5',
        'time_minutes': 30
    },
    'gauss_seidel_facil_1': {
        'title': '¿Qué valores usa para calcular la variable "b" en la iteración 1?',
        'options': ['Los iniciales (0)', 'El nuevo "a" recién calculado'],
        'correct': 'El nuevo "a" recién calculado'
    },
    'gauss_seidel_intermedio_1': {
        'title': 'Gauss-Seidel: Sistema 2x2: 4x+y=9, x+3y=10. Con x0=y0=0, calcula x1',
        'options': ['2.25', '2.0', '2.5', '2.75'],
        'time_minutes': 25,
        'correct': '2.25'
    },
    'gauss_seidel_avanzado_1': {
        'title': 'Gauss-Seidel: Resuelve el sistema 4x+y=9, x+3y=10',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('4x + y = 9',), ('x + 3y = 10',)],
        'options': ['x=2, y=1', 'x=1, y=3', 'x=3, y=2', 'x=2, y=2'],
        'correct': 'x=2, y=1',
        'time_minutes': 30
    },
    'jacobi_facil_1': {
        'title': 'Diferencia clave con Gauss-Seidel:',
        'options': ['Uso de valores anteriores', 'No iterativo'],
        'correct': 'Uso de valores anteriores'
    },
    'jacobi_intermedio_1': {
        'title': 'En Jacobi, para calcular x(k+1) se usan valores:',
        'options': ['Todos de la iteración k', 'Mezclados de k y k+1', 'Solo de la iteración inicial', 'Aleatorios'],
        'time_minutes': 25,
        'correct': 'Todos de la iteración k'
    },
    'jacobi_avanzado_1': {
        'title': 'Calcula el error $\\epsilon_a$ entre la iteración 3 y 4...',
        'options': ['0.00056', '0.001'],
        'time_minutes': 30,
        'correct': '0.00056'
    },
    'montante_facil_1': {
        'title': 'El método Montante utiliza principalmente aritmética de:',
        'options': ['Enteros', 'Fracciones'],
        'correct': 'Enteros'
    },
    'montante_intermedio_1': {
        'title': 'Montante: Sistema 2x2: 2x+y=5, x+3y=8. Paso 1: Calcula nueva posición [2,2]',
        'options': ['5', '4', '6', '3'],
        'time_minutes': 25,
        'correct': '5'
    },
    'montante_avanzado_1': {
        'title': 'Montante: Resuelve el sistema 2x+y=5, x+3y=8',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('2x + y = 5',), ('x + 3y = 8',)],
        'options': ['x=1, y=3', 'x=2, y=1', 'x=3, y=2', 'x=2, y=2'],
        'correct': 'x=1, y=3',
        'time_minutes': 30
    },
    'gauss_jordan_facil_1': {
        'title': 'La matriz final en Gauss-Jordan debe ser:',
        'options': ['Identidad', 'Triangular'],
        'correct': 'Identidad'
    },
    'gauss_jordan_intermedio_1': {
        'title': 'Gauss-Jordan: Sistema 2x2: 3x+2y=12, x+4y=14. Primera fila normalizada por pivote',
        'options': ['1, 2/3, 4', '3, 2, 12', '1, 1, 1', '2, 3, 4'],
        'time_minutes': 25,
        'correct': '1, 2/3, 4'
    },
    'gauss_jordan_avanzado_1': {
        'title': 'Gauss-Jordan: Resuelve el sistema 3x+2y=12, x+4y=14',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('3x + 2y = 12',), ('x + 4y = 14',)],
        'options': ['x=2, y=3', 'x=3, y=2', 'x=1, y=4', 'x=4, y=1'],
        'correct': 'x=2, y=3',
        'time_minutes': 30
    },
    'gaussian_elim_facil_1': {
        'title': 'A diferencia de Gauss-Jordan, aquí solo buscamos una matriz:',
        'options': ['Triangular Superior', 'Identidad'],
        'correct': 'Triangular Superior'
    },
    'gaussian_elim_intermedio_1': {
        'title': 'Eliminación Gaussiana: Matriz 3x3. Después de fila 1, elemento [2,1] es 0: ?',
        'options': ['15.5', '-7.5', '10.5', '5.5'],
        'time_minutes': 25,
        'correct': '-7.5'
    },
    'gaussian_elim_avanzado_1': {
        'title': 'Eliminación Gaussiana: Resuelve el sistema 2x+3y=13, x+2y=8',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('2x + 3y = 13',), ('x + 2y = 8',)],
        'options': ['x=2, y=3', 'x=3, y=2', 'x=1, y=4', 'x=4, y=1'],
        'correct': 'x=2, y=3',
        'time_minutes': 30
    },
    'trapezoidal_facil_1': {
        'title': '¿A qué grado de polinomio corresponde el trapecio?',
        'options': ['1er Grado', '2do Grado'],
        'correct': '1er Grado'
    },
    'trapezoidal_intermedio_1': {
        'title': 'Trapezoidal: ∫[0,1](1-x²)dx con n=4. Calcula I',
        'options': ['0.65625', '0.5', '0.75', '0.666'],
        'time_minutes': 25,
        'correct': '0.65625'
    },
    'trapezoidal_avanzado_1': {
        'title': 'Trapezoidal: Resuelve ∫[0,1](1-x²)dx con n=4',
        'x_value': 1,
        'table': [('Integral de 1-x² de 0 a 1',), ('h=0.25',)],
        'options': ['0.65625', '0.5', '0.75', '0.666'],
        'correct': '0.65625',
        'time_minutes': 30
    },
    'simpson_1_3_facil_1': {
        'title': 'Requisito indispensable de "n" para 1/3 Simpson:',
        'options': ['Debe ser Par', 'Debe ser Impar'],
        'correct': 'Debe ser Par'
    },
    'simpson_1_3_intermedio_1': {
        'title': 'Simpson 1/3: ∫[0,1](1-x²)dx con n=4. Calcula I',
        'options': ['0.666666667', '0.5', '0.75', '0.55'],
        'time_minutes': 25,
        'correct': '0.666666667'
    },
    'simpson_1_3_avanzado_1': {
        'title': 'Simpson 1/3: Resuelve ∫[0,1](1-x²)dx con n=4',
        'x_value': 1,
        'table': [('Integral de 1-x² de 0 a 1',), ('h=0.25',)],
        'options': ['0.666666667', '0.5', '0.75', '0.55'],
        'correct': '0.666666667',
        'time_minutes': 30
    },
    'simpson_3_8_facil_1': {
        'title': 'Simpson 3/8 requiere que "n" sea:',
        'options': ['Múltiplo de 3', 'Par'],
        'correct': 'Múltiplo de 3'
    },
    'simpson_3_8_intermedio_1': {
        'title': 'Simpson 3/8: Con 4 puntos (n=3), calcula el área bajo la curva',
        'options': ['A usar fórmula 3/8', 'Error - n debe ser par', 'Usar Simpson 1/3', 'Usar Trapecio'],
        'time_minutes': 25,
        'correct': 'A usar fórmula 3/8'
    },
    'simpson_3_8_avanzado_1': {
        'title': 'Simpson 3/8: Integra de 0 a 3 con datos (0,1), (1,2), (2,5), (3,10)',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx',), ('Datos de la función:',), (0, 1), (1, 2), (2, 5), (3, 10)],
        'options': ['11.25', '12.25', '10.25', '13.25'],
        'correct': '11.25',
        'time_minutes': 30
    },
    'cotes_closed_facil_1': {
        'title': 'En fórmulas cerradas, ¿se incluyen los límites a y b?',
        'options': ['Si', 'No'],
        'correct': 'Si'
    },
    'cotes_closed_intermedio_1': {
        'title': 'Newton-Cotes Cerrado: Selecciona n=2 (3 puntos). Qué fórmula usar',
        'options': ['Simpson 1/3 (Trapecio mejorado)', 'Trapecio', 'Simpson 3/8', 'Punto Medio'],
        'time_minutes': 25,
        'correct': 'Simpson 1/3 (Trapecio mejorado)'
    },
    'cotes_closed_avanzado_1': {
        'title': 'Newton-Cotes Cerrado: Integra con 5 datos: (0,1), (0.5,1.5), (1,2.5), (1.5,4), (2,6)',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx desde 0 hasta 2',), ('Datos de la función:',), (0, 1), (0.5, 1.5), (1, 2.5), (1.5, 4), (2, 6)],
        'options': ['5.208', '6.208', '4.208', '7.208'],
        'correct': '5.208',
        'time_minutes': 30
    },
    'cotes_open_facil_1': {
        'title': 'Fórmula para calcular h en Cotes Abiertas:',
        'options': ['(b-a)/(n+2)', '(b-a)/n'],
        'correct': '(b-a)/(n+2)'
    },
    'cotes_open_intermedio_1': {
        'title': 'Newton-Cotes Abierto: Con intervalo [0,2], n=4, calcula h = (b-a)/(n+2)',
        'options': ['1/3', '0.5', '1/4', '2/3'],
        'time_minutes': 25,
        'correct': '1/3'
    },
    'cotes_open_avanzado_1': {
        'title': 'Newton-Cotes Abierto: Integra entre puntos internos (0.5,1.5,1,1.5,4)',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx',), ('Datos de la función (sin extremos):',), (0.5, 1.5), (1, 2.5), (1.5, 4)],
        'options': ['4.5', '5.5', '3.5', '6.5'],
        'correct': '4.5',
        'time_minutes': 30
    },
    'least_sq_linear_facil_1': {
        'title': 'El objetivo es minimizar:',
        'options': ['La dispersión (error)', 'El valor de x'],
        'correct': 'La dispersión (error)'
    },
    'least_sq_linear_intermedio_1': {
        'title': 'Calcula $\\sum x^2$ para los datos: 1, 2, 3...',
        'options': ['14', '6'],
        'time_minutes': 25,
        'correct': '14'
    },
    'least_sq_linear_avanzado_1': {
        'title': 'El método de mínimos cuadrados minimiza:',
        'options': ['∑[yi - (a0 + a1xi)]²', '∑(yi - xi)', 'max|yi - ŷi|', '∑|yi - ŷi|'],
        'time_minutes': 30,
        'correct': '∑[yi - (a0 + a1xi)]²'
    },
    'least_sq_quadratic_facil_1': {
        'title': '¿Cuántas incógnitas (coeficientes) se buscan?',
        'options': ['3 (a0, a1, a2)', '2'],
        'correct': '3 (a0, a1, a2)'
    },
    'least_sq_quadratic_intermedio_1': {
        'title': 'Mínimos Cuadrados Cuadrático: Datos (1,1), (2,3), (3,7). Calcula ∑x²',
        'options': ['14', '6', '12', '10'],
        'time_minutes': 25,
        'correct': '14'
    },
    'least_sq_quadratic_avanzado_1': {
        'title': 'Mínimos Cuadrados Cuadrático: Ajusta y=a+bx+cx² con (1,1), (2,3), (3,7), (4,13)',
        'x_value': 5,
        'table': [('Ajustar: y = a + bx + cx²',), ('Datos:',), (1, 1), (2, 3), (3, 7), (4, 13)],
        'options': ['21', '22', '20', '23'],
        'correct': '21',
        'time_minutes': 30
    },
    'least_sq_cubic_facil_1': {
        'title': 'El sistema de ecuaciones resultante es de tamaño:',
        'options': ['4x4', '3x3'],
        'correct': '4x4'
    },
    'least_sq_cubic_intermedio_1': {
        'title': 'Mínimos Cuadrados Cúbico: Datos (0,1), (1,2), (2,5), (3,10). Calcula ∑x³',
        'options': ['36', '20', '14', '30'],
        'time_minutes': 25,
        'correct': '36'
    },
    'least_sq_cubic_avanzado_1': {
        'title': 'Mínimos Cuadrados Cúbico: Ajusta y=a+bx+cx²+dx³ con (0,1), (1,2), (2,5), (3,10), (4,20)',
        'x_value': 3,
        'table': [('Ajustar: y = a + bx + cx² + dx³',), ('Datos:',), (0, 1), (1, 2), (2, 5), (3, 10), (4, 20)],
        'options': ['10.2', '11.2', '9.2', '12.2'],
        'correct': '10.2',
        'time_minutes': 30
    },
    'least_sq_linear_func_facil_1': {
        'title': 'En lugar de $x^2$, el tercer término depende de:',
        'options': ['f(x)', 'x^3'],
        'correct': 'f(x)'
    },
    'least_sq_linear_func_intermedio_1': {
        'title': 'Mínimos Cuadrados Lineal con f(x): y=a+b*ln(x) con datos (1,2), (2,3), (3,4). Σln(x)',
        'options': ['1.791', '1.691', '1.891', '1.591'],
        'time_minutes': 25,
        'correct': '1.791'
    },
    'least_sq_linear_func_avanzado_1': {
        'title': 'Mínimos Cuadrados Lineal con f(x): Ajusta y=a+b*ln(x) con (1,2.5), (2,5.2), (3,8.8), (4,13.1)',
        'x_value': 4,
        'table': [('Ajustar: y = a + b*ln(x)',), ('Datos:',), (1, 2.5), (2, 5.2), (3, 8.8), (4, 13.1)],
        'options': ['13.5', '14.5', '12.5', '15.5'],
        'correct': '13.5',
        'time_minutes': 30
    },
    'least_sq_quadratic_func_facil_1': {
        'title': 'Este modelo tiene 4 coeficientes, incluyendo:',
        'options': ['El término f(x)', 'Término cúbico'],
        'correct': 'El término f(x)'
    },
    'least_sq_quadratic_func_intermedio_1': {
        'title': 'Mínimos Cuadrados Cuadrático con f(x): y=a+bx+c*e^x. Σe^x es el nuevo término',
        'options': ['Si', 'No'],
        'time_minutes': 25,
        'correct': 'Si'
    },
    'least_sq_quadratic_func_avanzado_1': {
        'title': 'Mínimos Cuadrados Cuadrático con f(x): Ajusta y=a+bx+c*e^x con (0,1), (1,1.5), (2,3.8), (3,8.2)',
        'x_value': 3,
        'table': [('Ajustar: y = a + bx + c*e^x',), ('Datos:',), (0, 1), (1, 1.5), (2, 3.8), (3, 8.2)],
        'options': ['8.5', '9.5', '7.5', '10.5'],
        'correct': '8.5',
        'time_minutes': 30
    },
    'euler_modified_facil_1': {
        'title': '¿Qué regla de integración usa Euler Modificado?',
        'options': ['Trapezoidal', 'Simpson'],
        'correct': 'Trapezoidal'
    },
    'euler_modified_intermedio_1': {
        'title': 'Euler Modificado: 3y\' - 5yt + 1 = 0, y(0) = 1.2, h = 0.2',
        'options': ['1.2', '1.3', '1.1', '1.4'],
        'time_minutes': 25,
        'correct': '1.2'
    },
    'euler_modified_avanzado_1': {
        'title': 'Euler Modificado: Resuelve dy/dx = x + y, y(0) = 1 en [0, 0.2]',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y",), ("Condición inicial: y(0) = 1",), ("Paso: h = 0.1",)],
        'options': ['1.221', '1.321', '1.121', '1.421'],
        'correct': '1.221',
        'time_minutes': 30
    },
    'rk2_facil_1': {
        'title': '¿Cuántas evaluaciones de la función (k) se hacen?',
        'options': ['2', '4'],
        'correct': '2'
    },
    'rk2_intermedio_1': {
        'title': 'RK2: dy/dx = x + y, y(0) = 1, h = 0.2. Calcula y1',
        'options': ['1.242', '1.142', '1.342', '1.042'],
        'time_minutes': 25,
        'correct': '1.242'
    },
    'rk2_avanzado_1': {
        'title': 'RK2: Resuelve dy/dx = x + y, y(0) = 1 en [0, 0.2]',
        'x_value': 0.2,
        'table': [('Ecuación: dy/dx = x + y',), ('Condición inicial: y(0) = 1',), ('Paso: h = 0.1',)],
        'options': ['1.242', '1.342', '1.142', '1.442'],
        'correct': '1.242',
        'time_minutes': 30
    },
    'rk3_facil_1': {
        'title': 'El peso mayor se le da a la pendiente intermedia:',
        'options': ['k2 (x4)', 'k1 (x1)'],
        'correct': 'k2 (x4)'
    },
    'rk3_intermedio_1': {
        'title': 'RK3: dy/dx = 2x, y(0) = 0, h = 0.1. Calcula y1',
        'options': ['0.002', '0.001', '0.003', '0.004'],
        'time_minutes': 25,
        'correct': '0.002'
    },
    'rk3_avanzado_1': {
        'title': 'RK3: Resuelve dy/dx = 2x, y(0) = 0 en [0, 0.1]',
        'x_value': 0.1,
        'table': [('Ecuación: dy/dx = 2x',), ('Condición inicial: y(0) = 0',), ('Paso: h = 0.1',)],
        'options': ['0.002', '0.003', '0.001', '0.004'],
        'correct': '0.002',
        'time_minutes': 30
    },
    'rk4_simpson13_facil_1': {
        'title': '¿Cuáles pendientes se multiplican por 2?',
        'options': ['k2 y k3', 'k1 y k4'],
        'correct': 'k2 y k3'
    },
    'rk4_simpson13_intermedio_1': {
        'title': 'RK4 Simpson 1/3: dy/dx = -2y, y(0) = 1, h = 0.1. Calcula y1',
        'options': ['0.818', '0.918', '0.718', '0.618'],
        'time_minutes': 25,
        'correct': '0.818'
    },
    'rk4_simpson13_avanzado_1': {
        'title': 'RK4 Simpson 1/3: Resuelve dy/dx = -2y, y(0) = 1 en [0, 0.1]',
        'x_value': 0.1,
        'table': [('Ecuación: dy/dx = -2y',), ('Condición inicial: y(0) = 1',), ('Paso: h = 0.05',)],
        'options': ['0.818', '0.918', '0.718', '0.618'],
        'correct': '0.818',
        'time_minutes': 30
    },
    'rk4_simpson38_facil_1': {
        'title': 'En esta variante, el divisor de la fórmula es:',
        'options': ['8', '6'],
        'correct': '8'
    },
    'rk4_simpson38_intermedio_1': {
        'title': 'RK4 Simpson 3/8: dy/dx = y, y(0) = 1, h = 0.1. Calcula y1',
        'options': ['1.105', '1.205', '1.005', '1.305'],
        'time_minutes': 25,
        'correct': '1.105'
    },
    'rk4_simpson38_avanzado_1': {
        'title': 'RK4 Simpson 3/8: Resuelve dy/dx = y, y(0) = 1 en [0, 0.1]',
        'x_value': 0.1,
        'table': [('Ecuación: dy/dx = y',), ('Condición inicial: y(0) = 1',), ('Paso: h = 0.05',)],
        'options': ['1.105', '1.205', '1.005', '1.305'],
        'correct': '1.105',
        'time_minutes': 30
    },
    'rk_higher_order_facil_1': {
        'title': 'Para una EDO de 2do orden, necesitamos calcular:',
        'options': ['k y m', 'Solo k'],
        'correct': 'k y m'
    },
    'rk_higher_order_intermedio_1': {
        'title': 'RK4 Orden Superior: y" = x - y\', y(0) = 1, y\'(0) = 0, h = 0.1. Sistema equivalente: dy/dx = z, dz/dx = x - z',
        'options': ['y(0.1) ≈ 1.005', 'y(0.1) ≈ 1.105', 'y(0.1) ≈ 0.905', 'y(0.1) ≈ 1.205'],
        'time_minutes': 25,
        'correct': 'y(0.1) ≈ 1.005'
    },
    'rk_higher_order_avanzado_1': {
        'title': 'RK4 Orden Superior: Resuelve y" = x - y\' en [0, 0.1] con y(0) = 1, y\'(0) = 0',
        'x_value': 0.1,
        'table': [('Sistema: dy/dx = z, dz/dx = x - z',), ('y(0) = 1, z(0) = 0',), ('Paso: h = 0.05',)],
        'options': ['y(0.1) ≈ 1.005', 'y(0.1) ≈ 1.105', 'y(0.1) ≈ 0.905', 'y(0.1) ≈ 1.205'],
        'correct': 'y(0.1) ≈ 1.005',
        'time_minutes': 30
    },
}
