import json

# Datos del PDF que deberían estar en los problemas
pdf_data = {
    'euler_modified': {
        'intermedio': {
            'title': 'Euler Modificado: 3y\' - 5yt + 1 = 0, y(0) = 1.2, h = 0.2',
            'correct': '1.2'
        },
        'avanzado': {
            'title': 'Euler Modificado: Resuelve 3y\' - 5yt + 1 = 0, y(0) = 1.2 en [0, 0.2]',
            'correct': '1.2',
            'time_minutes': 30
        }
    },
    'rk2': {
        'intermedio': {
            'title': 'RK2: dy/dx = x + y, y(0) = 1, h = 0.2. Calcula y1',
            'correct': '1.242'
        },
        'avanzado': {
            'title': 'RK2: Resuelve dy/dx = x + y, y(0) = 1 en [0, 0.2]',
            'correct': '1.242',
            'time_minutes': 30
        }
    },
    'rk4_simpson13': {
        'intermedio': {
            'title': 'RK4 Simpson 1/3: dy/dx = -2y, y(0) = 1, h = 0.1. Calcula y1',
            'correct': '0.818'
        },
        'avanzado': {
            'title': 'RK4 Simpson 1/3: Resuelve dy/dx = -2y, y(0) = 1 en [0, 0.1]',
            'correct': '0.818',
            'time_minutes': 30
        }
    },
    'simpson_1_3': {
        'intermedio': {
            'title': 'Simpson 1/3: ∫[0,1](1-x²)dx, n=4. Calcula I',
            'correct': '0.666666667'
        },
        'avanzado': {
            'title': 'Simpson 1/3: ∫[0,1](1-x²)dx con n=4',
            'correct': '0.666666667',
            'time_minutes': 30
        }
    },
    'trapezoidal': {
        'intermedio': {
            'title': 'Trapezoidal: ∫[0,1](1-x²)dx, n=4. Calcula I',
            'correct': '0.65625'
        },
        'avanzado': {
            'title': 'Trapezoidal: ∫[0,1](1-x²)dx con n=4',
            'correct': '0.65625',
            'time_minutes': 30
        }
    },
    'gauss_seidel': {
        'intermedio': {
            'title': 'Gauss-Seidel: 3a - 0.1b - 0.2c = 7.85; 0.1a + 7b - 0.3c = -19.3; 0.3a - 0.2b + 10c = 71.4',
            'correct': 'a≈3, b≈-2.5, c≈7'
        },
        'avanzado': {
            'title': 'Gauss-Seidel: Resuelve el sistema de 3 ecuaciones',
            'correct': 'a≈3, b≈-2.5, c≈7',
            'time_minutes': 30
        }
    },
    'jacobi': {
        'intermedio': {
            'title': 'Jacobi: 3a - 0.1b - 0.2c = 7.85; 0.1a + 7b - 0.3c = -19.3; 0.3a - 0.2b + 10c = 71.4',
            'correct': 'a≈3, b≈-2.5, c≈7'
        },
        'avanzado': {
            'title': 'Jacobi: Resuelve el sistema de 3 ecuaciones',
            'correct': 'a≈3, b≈-2.5, c≈7',
            'time_minutes': 30
        }
    },
    'bisection': {
        'intermedio': {
            'title': 'Bisección: f(x) = x³ - 6.5x + 2, intervalo [0,1]. Calcula x',
            'correct': '0.3087'
        },
        'avanzado': {
            'title': 'Bisección: f(x) = x³ - 6.5x + 2, intervalo [0,1]',
            'correct': '0.3087',
            'time_minutes': 30
        }
    },
    'false_position': {
        'intermedio': {
            'title': 'Falsa Posición: f(x) = 3x³ - 2x - 3. Calcula x',
            'correct': '1.217859143'
        },
        'avanzado': {
            'title': 'Falsa Posición: f(x) = 3x³ - 2x - 3',
            'correct': '1.217859143',
            'time_minutes': 30
        }
    },
    'newton_raphson': {
        'intermedio': {
            'title': 'Newton-Raphson: f(x) = x³ + 2x² + 10x - 20, x₀=1. Calcula x',
            'correct': '1.368808108'
        },
        'avanzado': {
            'title': 'Newton-Raphson: f(x) = x³ + 2x² + 10x - 20, x₀=1',
            'correct': '1.368808108',
            'time_minutes': 30
        }
    },
    'fixed_point': {
        'intermedio': {
            'title': 'Punto Fijo: f(x) = e⁻ˣ - x → x = e⁻ˣ, x₀=0',
            'correct': '0.5671433'
        },
        'avanzado': {
            'title': 'Punto Fijo: f(x) = e⁻ˣ - x, x₀=0',
            'correct': '0.5671433',
            'time_minutes': 30
        }
    },
    'secant': {
        'intermedio': {
            'title': 'Secante: f(x) = e⁻ˣ - x, x₀=0, x₁=1',
            'correct': '0.5671433'
        },
        'avanzado': {
            'title': 'Secante: f(x) = e⁻ˣ - x, x₀=0, x₁=1',
            'correct': '0.5671433',
            'time_minutes': 30
        }
    }
}

print("Información del PDF para validar:")
print(json.dumps(pdf_data, indent=2, ensure_ascii=False))
