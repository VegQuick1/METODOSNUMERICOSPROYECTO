
LINEAL_LESSONS = {
    'intermedio': {
        'title': 'Interpolación Lineal',
        'data': [(2.0, 0.69314718), (5.0, 1.609437912), (3.0, 1.098612289)],
        'x_to_find': 3.0,
        'options': ['0.998577424', '0.900577424', '1.098577424', '0.898577424'],
        'answer': '0.998577424',
        'time': 1200  # 20 minutos
    },
    'avanzado': {
        'title': 'Interpolación Lineal - Avanzado',
        'data': [(1.0, 0.0), (4.0, 1.38629436), (2.5, 0.916291)],
        'x_to_find': 2.5,
        'options': ['0.910', '0.920', '0.916291', '0.930'],
        'answer': '0.916291',
        'time': 1200
    },
    'final': {
        'title': 'Interpolación Lineal - Prueba Final',
        'data': [(1.0, 0.0), (2.0, 0.69314718), (3.0, 1.098612289), (4.0, 1.38629436), (5.0, 1.609437912)],
        'x_to_find': 3.5,
        'options': ['1.242366', '1.350000', '1.200000', '1.242366', '1.150000'],
        'answer': '1.242366',
        'time': 1500  # 25 minutos
    }
}
NEWTON_FORWARD_LESSONS = {
    'intermedio': {
        'title': 'Newton Hacia Adelante',
        'data': [(1.7, 0.35), (2.4, 0.87), (3.1, 1.03)],
        'x_to_find': 3.0,
        'options': ['1.029183673', '0.999183673', '1.059183673', '0.999183673'],
        'answer': '1.029183673',
        'time': 1200
    },
    'avanzado': {
        'title': 'Newton Hacia Adelante - Avanzado',
        'data': [(1.0, 0.35), (1.7, 0.87), (2.4, 1.03), (3.1, 1.50), (3.8, 1.85)],
        'x_to_find': 2.2,
        'options': ['0.970000', '0.980000', '1.001234', '0.950000'],
        'answer': '1.001234',
        'time': 1200
    },
    'final': {
        'title': 'Newton Hacia Adelante - Prueba Final',
        'data': [(1.0, 0.35), (1.7, 0.87), (2.4, 1.03), (3.1, 1.50), (3.8, 1.85)],
        'x_to_find': 2.55,
        'options': ['1.045678', '1.055000', '1.065000', '1.045678', '1.035000'],
        'answer': '1.045678',
        'time': 1500
    }
}
NEWTON_BACKWARD_LESSONS = {
    'intermedio': {
        'title': 'Newton Hacia Atrás',
        'data': [(1.7, 0.35), (2.4, 0.87), (3.1, 1.03)],
        'x_to_find': 3.0,
        'options': ['1.029183673', '0.999183673', '1.059183673', '0.999183673'],
        'answer': '1.029183673',
        'time': 1200
    },
    'avanzado': {
        'title': 'Newton Hacia Atrás - Avanzado',
        'data': [(1.0, 0.35), (1.7, 0.87), (2.4, 1.03), (3.1, 1.50), (3.8, 1.85)],
        'x_to_find': 3.5,
        'options': ['1.670000', '1.680000', '1.670000', '1.660000'],
        'answer': '1.670000',
        'time': 1200
    },
    'final': {
        'title': 'Newton Hacia Atrás - Prueba Final',
        'data': [(1.0, 0.35), (1.7, 0.87), (2.4, 1.03), (3.1, 1.50), (3.8, 1.85)],
        'x_to_find': 3.7,
        'options': ['1.820000', '1.830000', '1.820000', '1.810000', '1.840000'],
        'answer': '1.820000',
        'time': 1500
    }
}
NEWTON_DIVIDED_DIFF_LESSONS = {
    'intermedio': {
        'title': 'Newton Diferencias Divididas',
        'data': [(7.3, -0.28), (6.5, -1.35), (6.1, -1.96)],
        'x_to_find': 7.0,
        'options': ['-0.657813', '-0.757813', '-0.557813', '-0.757813'],
        'answer': '-0.657813',
        'time': 1200
    },
    'avanzado': {
        'title': 'Newton Diferencias Divididas - Avanzado',
        'data': [(1.0, 0.50), (2.0, 0.87), (3.0, 1.03), (4.0, 1.50), (5.0, 1.85)],
        'x_to_find': 2.5,
        'options': ['0.945000', '0.955000', '0.945123', '0.935000'],
        'answer': '0.945123',
        'time': 1200
    },
    'final': {
        'title': 'Newton Diferencias Divididas - Prueba Final',
        'data': [(1.0, 0.50), (2.0, 0.87), (3.0, 1.03), (4.0, 1.50), (5.0, 1.85)],
        'x_to_find': 3.5,
        'options': ['1.265000', '1.275000', '1.265234', '1.255000', '1.285000'],
        'answer': '1.265234',
        'time': 1500
    }
}
GAUSS_SEIDEL_LESSONS = {
    'intermedio': {
        'title': 'Método de Gauss-Seidel',
        'matrix': 'A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]',
        'b_vector': 'b = [7.85, -19.3, 71.4]',
        'tolerance': '€ = 0.001',
        'options': ['a=3.0, b=-2.5, c=7.0', 'a=3.0, b=-2.4, c=7.0', 'a=2.9, b=-2.5, c=7.0', 'a=3.1, b=-2.5, c=7.0'],
        'answer': 'a=3.0, b=-2.5, c=7.0',
        'time': 1500  # 25 minutos
    },
    'avanzado': {
        'title': 'Método de Gauss-Seidel - Avanzado',
        'matrix': 'A = [[4, -1, 0], [1, 4, -1], [0, -1, 4]]',
        'b_vector': 'b = [15, 10, 10]',
        'tolerance': '€ = 0.001',
        'options': ['x=4.1, y=2.8, z=3.2', 'x=4.0, y=2.8, z=3.2', 'x=4.0, y=2.9, z=3.2', 'x=4.0, y=2.8, z=3.3'],
        'answer': 'x=4.0, y=2.8, z=3.2',
        'time': 1500
    },
    'final': {
        'title': 'Método de Gauss-Seidel - Prueba Final',
        'matrix': 'A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]',
        'b_vector': 'b = [6, 25, -11]',
        'tolerance': '€ = 0.001',
        'options': ['x=1.0, y=2.0, z=-1.0', 'x=1.0, y=2.1, z=-1.0', 'x=1.1, y=2.0, z=-1.0', 'x=1.0, y=2.0, z=-0.9', 'x=1.0, y=2.0, z=-1.1'],
        'answer': 'x=1.0, y=2.0, z=-1.0',
        'time': 1800  # 30 minutos
    }
}
JACOBI_LESSONS = {
    'intermedio': {
        'title': 'Método de Jacobi',
        'matrix': 'A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]',
        'b_vector': 'b = [7.85, -19.3, 71.4]',
        'tolerance': '€ = 0.001',
        'options': ['a=3.0, b=-2.5, c=7.0', 'a=3.0, b=-2.4, c=7.0', 'a=2.9, b=-2.5, c=7.0', 'a=3.1, b=-2.5, c=7.0'],
        'answer': 'a=3.0, b=-2.5, c=7.0',
        'time': 1500
    },
    'avanzado': {
        'title': 'Método de Jacobi - Avanzado',
        'matrix': 'A = [[4, -1, 0], [1, 4, -1], [0, -1, 4]]',
        'b_vector': 'b = [15, 10, 10]',
        'tolerance': '€ = 0.001',
        'options': ['x=3.8, y=2.7, z=3.1', 'x=3.8, y=2.8, z=3.1', 'x=3.9, y=2.8, z=3.1', 'x=3.8, y=2.8, z=3.2'],
        'answer': 'x=3.8, y=2.8, z=3.1',
        'time': 1500
    },
    'final': {
        'title': 'Método de Jacobi - Prueba Final',
        'matrix': 'A = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]',
        'b_vector': 'b = [6, 25, -11]',
        'tolerance': '€ = 0.001',
        'options': ['x=1.0, y=2.0, z=-1.0', 'x=1.0, y=2.1, z=-1.0', 'x=1.1, y=2.0, z=-1.0', 'x=1.0, y=2.0, z=-0.9', 'x=1.0, y=2.0, z=-1.1'],
        'answer': 'x=1.0, y=2.0, z=-1.0',
        'time': 1800
    }
}
BISECTION_LESSONS = {
    'intermedio': {
        'title': 'Método de Bisección',
        'function': 'f(x) = x³ - 6.5x + 2',
        'interval': '[a=0, b=1]',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 0.309', 'x ≈ 0.319', 'x ≈ 0.309', 'x ≈ 0.299'],
        'answer': 'x ≈ 0.309',
        'time': 1200
    },
    'avanzado': {
        'title': 'Método de Bisección - Avanzado',
        'function': 'f(x) = x² - 4',
        'interval': '[a=1, b=3]',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 2.0', 'x ≈ 2.1', 'x ≈ 2.0', 'x ≈ 1.9'],
        'answer': 'x ≈ 2.0',
        'time': 1200
    },
    'final': {
        'title': 'Método de Bisección - Prueba Final',
        'function': 'f(x) = eˣ - 3',
        'interval': '[a=0, b=2]',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 1.099', 'x ≈ 1.199', 'x ≈ 1.099', 'x ≈ 0.999', 'x ≈ 1.299'],
        'answer': 'x ≈ 1.099',
        'time': 1500
    }
}
FALSA_POSICION_LESSONS = {
    'intermedio': {
        'title': 'Falsa Posición (Regula-Falsi)',
        'function': 'f(x) = 3x³ - 2x - 3',
        'interval': '[a=-2, b=2]',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 1.217', 'x ≈ 1.317', 'x ≈ 1.217', 'x ≈ 1.117'],
        'answer': 'x ≈ 1.217',
        'time': 1200
    },
    'avanzado': {
        'title': 'Falsa Posición - Avanzado',
        'function': 'f(x) = x³ - x - 1',
        'interval': '[a=1, b=2]',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 1.325', 'x ≈ 1.425', 'x ≈ 1.325', 'x ≈ 1.225'],
        'answer': 'x ≈ 1.325',
        'time': 1200
    },
    'final': {
        'title': 'Falsa Posición - Prueba Final',
        'function': 'f(x) = x³ + x - 1',
        'interval': '[a=0, b=1]',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 0.682', 'x ≈ 0.782', 'x ≈ 0.682', 'x ≈ 0.582', 'x ≈ 0.882'],
        'answer': 'x ≈ 0.682',
        'time': 1500
    }
}
NEWTON_RAPHSON_LESSONS = {
    'intermedio': {
        'title': 'Método Newton-Raphson',
        'function': 'f(x) = x³ + 2x² + 10x - 20',
        'derivative': "f'(x) = 3x² + 4x + 10",
        'initial': 'x₀ = 1',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 1.368808', 'x ≈ 1.468808', 'x ≈ 1.368808', 'x ≈ 1.268808'],
        'answer': 'x ≈ 1.368808',
        'time': 1200
    },
    'avanzado': {
        'title': 'Método Newton-Raphson - Avanzado',
        'function': 'f(x) = eˣ - 3x',
        'derivative': "f'(x) = eˣ - 3",
        'initial': 'x₀ = 1',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 1.512', 'x ≈ 1.612', 'x ≈ 1.512', 'x ≈ 1.412'],
        'answer': 'x ≈ 1.512',
        'time': 1200
    },
    'final': {
        'title': 'Método Newton-Raphson - Prueba Final',
        'function': 'f(x) = x⁴ - 13',
        'derivative': "f'(x) = 4x³",
        'initial': 'x₀ = 2',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 1.898', 'x ≈ 1.998', 'x ≈ 1.898', 'x ≈ 1.798', 'x ≈ 2.098'],
        'answer': 'x ≈ 1.898',
        'time': 1500
    }
}
PUNTO_FIJO_LESSONS = {
    'intermedio': {
        'title': 'Método de Punto Fijo',
        'function': 'f(x) = eˣ - x',
        'iteration': 'xᵢ₊₁ = e⁻ˣ',
        'initial': 'x₀ = 0',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 0.567', 'x ≈ 0.667', 'x ≈ 0.567', 'x ≈ 0.467'],
        'answer': 'x ≈ 0.567',
        'time': 1200
    },
    'avanzado': {
        'title': 'Método de Punto Fijo - Avanzado',
        'function': 'f(x) = cos(x) - x',
        'iteration': 'xᵢ₊₁ = cos(xᵢ)',
        'initial': 'x₀ = 0.5',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 0.739', 'x ≈ 0.839', 'x ≈ 0.739', 'x ≈ 0.639'],
        'answer': 'x ≈ 0.739',
        'time': 1200
    },
    'final': {
        'title': 'Método de Punto Fijo - Prueba Final',
        'function': 'f(x) = ln(x) - 1',
        'iteration': 'xᵢ₊₁ = eˣ',
        'initial': 'x₀ = 2',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 2.718', 'x ≈ 2.818', 'x ≈ 2.718', 'x ≈ 2.618', 'x ≈ 2.918'],
        'answer': 'x ≈ 2.718',
        'time': 1500
    }
}
SECANTE_LESSONS = {
    'intermedio': {
        'title': 'Método de la Secante',
        'function': 'f(x) = eˣ - x',
        'initial': 'x₀ = 0, x₁ = 1',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 0.567', 'x ≈ 0.667', 'x ≈ 0.567', 'x ≈ 0.467'],
        'answer': 'x ≈ 0.567',
        'time': 1200
    },
    'avanzado': {
        'title': 'Método de la Secante - Avanzado',
        'function': 'f(x) = x³ - x - 1',
        'initial': 'x₀ = 1, x₁ = 2',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 1.325', 'x ≈ 1.425', 'x ≈ 1.325', 'x ≈ 1.225'],
        'answer': 'x ≈ 1.325',
        'time': 1200
    },
    'final': {
        'title': 'Método de la Secante - Prueba Final',
        'function': 'f(x) = x⁴ - 13',
        'initial': 'x₀ = 1.5, x₁ = 2.5',
        'tolerance': '€ = 0.001',
        'options': ['x ≈ 1.898', 'x ≈ 1.998', 'x ≈ 1.898', 'x ≈ 1.798', 'x ≈ 2.098'],
        'answer': 'x ≈ 1.898',
        'time': 1500
    }
}
EULER_MODIFICADO_LESSONS = {
    'intermedio': {
        'title': 'Método Euler Modificado',
        'equation': '3y\' - 5yt + 1 = 0',
        'initial': 'y₀ = 1.2, t₀ = 0, h = 0.2',
        'iterations': 'Calcular y₁ y y₂',
        'options': ['y₁ = 1.2, y₂ = 1.3', 'y₁ = 1.2, y₂ = 1.4', 'y₁ = 1.1, y₂ = 1.3', 'y₁ = 1.3, y₂ = 1.4'],
        'answer': 'y₁ = 1.2, y₂ = 1.3',
        'time': 1500
    },
    'avanzado': {
        'title': 'Método Euler Modificado - Avanzado',
        'equation': 'y\' = t + y',
        'initial': 'y₀ = 1, t₀ = 0, h = 0.1',
        'iterations': 'Calcular hasta t = 0.3',
        'options': ['y ≈ 1.465', 'y ≈ 1.565', 'y ≈ 1.465', 'y ≈ 1.365'],
        'answer': 'y ≈ 1.465',
        'time': 1500
    },
    'final': {
        'title': 'Método Euler Modificado - Prueba Final',
        'equation': 'y\' = 2y - 2t',
        'initial': 'y₀ = 1, t₀ = 0, h = 0.1',
        'iterations': 'Calcular hasta t = 0.4',
        'options': ['y ≈ 1.653', 'y ≈ 1.753', 'y ≈ 1.653', 'y ≈ 1.553', 'y ≈ 1.853'],
        'answer': 'y ≈ 1.653',
        'time': 1800
    }
}
RK2_LESSONS = {
    'intermedio': {
        'title': 'Euler Modificado',
        'equation': 'y\' - 5yt + 1 = 0',
        'initial': 'y₀ = 2, t₀ = 0, h = 0.2',
        'iterations': 'Calcular k₁, k₂, y₁',
        'options': ['y₁ = 1.98', 'y₁ = 2.08', 'y₁ = 1.98', 'y₁ = 1.88'],
        'answer': 'y₁ = 1.98',
        'time': 1500
    },
    'avanzado': {
        'title': 'Euler Modificado - Avanzado',
        'equation': 'y\' = t + y',
        'initial': 'y₀ = 0, t₀ = 0, h = 0.1',
        'iterations': 'Calcular hasta t = 0.3',
        'options': ['y ≈ 0.430', 'y ≈ 0.530', 'y ≈ 0.430', 'y ≈ 0.330'],
        'answer': 'y ≈ 0.430',
        'time': 1500
    },
    'final': {
        'title': 'Euler Modificado - Prueba Final',
        'equation': 'y\' = -2y + t',
        'initial': 'y₀ = 1, t₀ = 0, h = 0.1',
        'iterations': 'Calcular hasta t = 0.4',
        'options': ['y ≈ 0.462', 'y ≈ 0.562', 'y ≈ 0.462', 'y ≈ 0.362', 'y ≈ 0.662'],
        'answer': 'y ≈ 0.462',
        'time': 1800
    }
}
RK4_LESSONS = {
    'intermedio': {
        'title': 'Runge-Kutta 4º Orden (Simpson 1/3)',
        'equation': 'y\' - 5yt + 1 = 0',
        'initial': 'y₀ = 2, t₀ = 0, h = 0.2',
        'iterations': 'Calcular y₁ con k₁, k₂, k₃, k₄',
        'options': ['y₁ = 1.996483', 'y₁ = 2.096483', 'y₁ = 1.996483', 'y₁ = 1.896483'],
        'answer': 'y₁ = 1.996483',
        'time': 1500
    },
    'avanzado': {
        'title': 'Runge-Kutta 4º Orden - Avanzado',
        'equation': 'y\' = t + y²',
        'initial': 'y₀ = 0, t₀ = 0, h = 0.1',
        'iterations': 'Calcular hasta t = 0.3',
        'options': ['y ≈ 0.102', 'y ≈ 0.202', 'y ≈ 0.102', 'y ≈ 0.002'],
        'answer': 'y ≈ 0.102',
        'time': 1500
    },
    'final': {
        'title': 'Runge-Kutta 4º Orden - Prueba Final',
        'equation': 'y\' = sin(t) + y',
        'initial': 'y₀ = 0, t₀ = 0, h = 0.1',
        'iterations': 'Calcular hasta t = 0.4',
        'options': ['y ≈ 0.169', 'y ≈ 0.269', 'y ≈ 0.169', 'y ≈ 0.069', 'y ≈ 0.369'],
        'answer': 'y ≈ 0.169',
        'time': 1800
    }
}
TRAPEZOIDAL_LESSONS = {
    'intermedio': {
        'title': 'Regla Trapezoidal',
        'integral': '∫₀¹ √(1-x²) dx',
        'intervals': 'n = 4',
        'options': ['I ≈ 0.65625', 'I ≈ 0.75625', 'I ≈ 0.65625', 'I ≈ 0.55625'],
        'answer': 'I ≈ 0.65625',
        'time': 1200
    },
    'avanzado': {
        'title': 'Regla Trapezoidal - Avanzado',
        'integral': '∫₁³ 1/x dx',
        'intervals': 'n = 4',
        'options': ['I ≈ 1.118', 'I ≈ 1.218', 'I ≈ 1.118', 'I ≈ 1.018'],
        'answer': 'I ≈ 1.118',
        'time': 1200
    },
    'final': {
        'title': 'Regla Trapezoidal - Prueba Final',
        'integral': '∫₀π sin(x) dx',
        'intervals': 'n = 8',
        'options': ['I ≈ 1.974', 'I ≈ 2.074', 'I ≈ 1.974', 'I ≈ 1.874', 'I ≈ 2.174'],
        'answer': 'I ≈ 1.974',
        'time': 1500
    }
}
SIMPSON_13_LESSONS = {
    'intermedio': {
        'title': 'Regla de Simpson 1/3',
        'integral': '∫₀¹ √(1-x²) dx',
        'intervals': 'n = 4',
        'options': ['I ≈ 0.666667', 'I ≈ 0.766667', 'I ≈ 0.666667', 'I ≈ 0.566667'],
        'answer': 'I ≈ 0.666667',
        'time': 1200
    },
    'avanzado': {
        'title': 'Regla de Simpson 1/3 - Avanzado',
        'integral': '∫₁³ 1/x dx',
        'intervals': 'n = 4',
        'options': ['I ≈ 1.100', 'I ≈ 1.200', 'I ≈ 1.100', 'I ≈ 1.000'],
        'answer': 'I ≈ 1.100',
        'time': 1200
    },
    'final': {
        'title': 'Regla de Simpson 1/3 - Prueba Final',
        'integral': '∫₀π sin(x) dx',
        'intervals': 'n = 8',
        'options': ['I ≈ 2.000', 'I ≈ 2.100', 'I ≈ 2.000', 'I ≈ 1.900', 'I ≈ 2.200'],
        'answer': 'I ≈ 2.000',
        'time': 1500
    }
}
SIMPSON_38_LESSONS = {
    'intermedio': {
        'title': 'Regla de Simpson 3/8',
        'integral': '∫₀¹ √(1-x²) dx',
        'intervals': 'n = 6',
        'options': ['I ≈ 0.667', 'I ≈ 0.767', 'I ≈ 0.667', 'I ≈ 0.567'],
        'answer': 'I ≈ 0.667',
        'time': 1200
    },
    'avanzado': {
        'title': 'Regla de Simpson 3/8 - Avanzado',
        'integral': '∫₁³ 1/x dx',
        'intervals': 'n = 6',
        'options': ['I ≈ 1.099', 'I ≈ 1.199', 'I ≈ 1.099', 'I ≈ 0.999'],
        'answer': 'I ≈ 1.099',
        'time': 1200
    },
    'final': {
        'title': 'Regla de Simpson 3/8 - Prueba Final',
        'integral': '∫₀π sin(x) dx',
        'intervals': 'n = 9',
        'options': ['I ≈ 2.001', 'I ≈ 2.101', 'I ≈ 2.001', 'I ≈ 1.901', 'I ≈ 2.201'],
        'answer': 'I ≈ 2.001',
        'time': 1500
    }
}
MINIMOS_CUADRADOS_LINEAL = {
    'intermedio': {
        'title': 'Mínimos Cuadrados - Línea Recta',
        'data': '(1.1, 2.5), (1.9, 2.7), (2.4, 3.7), (4.8, 5.2), (5.1, 6.0), (10.5, 8.3)',
        'equation': 'g(x) = a₀ + a₁x',
        'options': ['a₀ = 2.008, a₁ = 0.634', 'a₀ = 2.108, a₁ = 0.634', 'a₀ = 2.008, a₁ = 0.734', 'a₀ = 1.908, a₁ = 0.634'],
        'answer': 'a₀ = 2.008, a₁ = 0.634',
        'time': 1200
    },
    'avanzado': {
        'title': 'Mínimos Cuadrados - Línea Recta Avanzado',
        'data': '(0, 1), (1, 3), (2, 5), (3, 7), (4, 9)',
        'equation': 'g(x) = a₀ + a₁x',
        'options': ['a₀ = 1.0, a₁ = 2.0', 'a₀ = 1.1, a₁ = 2.0', 'a₀ = 1.0, a₁ = 2.1', 'a₀ = 0.9, a₁ = 2.0'],
        'answer': 'a₀ = 1.0, a₁ = 2.0',
        'time': 1200
    },
    'final': {
        'title': 'Mínimos Cuadrados - Línea Recta Prueba Final',
        'data': '(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)',
        'equation': 'g(x) = a₀ + a₁x',
        'options': ['a₀ = 0.0, a₁ = 2.0', 'a₀ = 0.1, a₁ = 2.0', 'a₀ = 0.0, a₁ = 2.1', 'a₀ = 0.0, a₁ = 2.0', 'a₀ = -0.1, a₁ = 2.0'],
        'answer': 'a₀ = 0.0, a₁ = 2.0',
        'time': 1500
    }
}
MINIMOS_CUADRADOS_CUADRATICA = {
    'intermedio': {
        'title': 'Mínimos Cuadrados - Parábola',
        'data': '(0, 1), (1, 2), (2, 5), (3, 10)',
        'equation': 'g(x) = a₀ + a₁x + a₂x²',
        'options': ['a₀ = 1.0, a₁ = 0.5, a₂ = 0.5', 'a₀ = 1.0, a₁ = 0.5, a₂ = 0.6', 'a₀ = 0.9, a₁ = 0.5, a₂ = 0.5', 'a₀ = 1.1, a₁ = 0.5, a₂ = 0.5'],
        'answer': 'a₀ = 1.0, a₁ = 0.5, a₂ = 0.5',
        'time': 1200
    },
    'avanzado': {
        'title': 'Mínimos Cuadrados - Parábola Avanzado',
        'data': '(1, 2), (2, 5), (3, 10), (4, 17)',
        'equation': 'g(x) = a₀ + a₁x + a₂x²',
        'options': ['a₀ = 0.0, a₁ = 0.0, a₂ = 1.0', 'a₀ = 0.1, a₁ = 0.0, a₂ = 1.0', 'a₀ = 0.0, a₁ = 0.1, a₂ = 1.0', 'a₀ = 0.0, a₁ = 0.0, a₂ = 1.1'],
        'answer': 'a₀ = 0.0, a₁ = 0.0, a₂ = 1.0',
        'time': 1200
    },
    'final': {
        'title': 'Mínimos Cuadrados - Parábola Prueba Final',
        'data': '(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)',
        'equation': 'g(x) = a₀ + a₁x + a₂x²',
        'options': ['a₀ = 0.0, a₁ = 0.0, a₂ = 1.0', 'a₀ = 0.1, a₁ = 0.0, a₂ = 1.0', 'a₀ = 0.0, a₁ = 0.1, a₂ = 1.0', 'a₀ = 0.0, a₁ = 0.0, a₂ = 1.1', 'a₀ = -0.1, a₁ = 0.0, a₂ = 1.0'],
        'answer': 'a₀ = 0.0, a₁ = 0.0, a₂ = 1.0',
        'time': 1500
    }
}
