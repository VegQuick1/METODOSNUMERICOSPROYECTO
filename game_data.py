
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
                    {'type': 'practica', 'content': '¿El método de Lagrange requiere intervalos uniformes obligatoriamente?', 'options': ['Si', 'No'], 'answer': 'No'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Dados los puntos (2, 2.54) y (2.5, 2.82), configura el primer término de Lagrange para x=2.4...', 'options': ['A', 'B'], 'answer': 'A'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula g(2.4) usando Lagrange con 3 puntos...', 'options': ['3.32', '3.15'], 'answer': '3.15'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'lagrange_final'}
                ]
            },
            "Lineal": {
                "Fácil": [
                    {'type': 'practica', 'content': 'La interpolación lineal une dos puntos mediante una...', 'options': ['Parábola', 'Línea Recta'], 'answer': 'Línea Recta'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula la pendiente (m) entre Ln(2) y Ln(5)...', 'options': ['0.305', '0.609'], 'answer': '0.305'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Estimar Ln(3) usando interpolación lineal entre Ln(2) y Ln(5)...', 'options': ['1.098', '0.998'], 'answer': '0.998'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'linear_interp_1'}
                ]
            },
            "Newton con Diferencias Divididas": {
                "Fácil": [                    {'type': 'practica', 'content': '¿Qué tipo de intervalos maneja principalmente este método?', 'options': ['Uniformes', 'No Uniformes'], 'answer': 'No Uniformes'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula la primera diferencia dividida $D_1$ entre (7.3, -0.28) y (6.5, -1.35)...', 'options': ['1.3375', '-1.22'], 'answer': '1.3375'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Construye el polinomio completo para interpolar x=7...', 'options': ['-0.657', '-0.28'], 'answer': '-0.657'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'newton_div_diff_1'}
                ]
            },
            "Newton Hacia Adelante": {
                "Fácil": [
                    {'type': 'practica', 'content': 'En Newton Adelante, el factor "s" se calcula como:', 'options': ['(x - xi) / h', '(x + xi) / h'], 'answer': '(x - xi) / h'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Dada una h=0.7 y x=3 con xi=1.7, calcula s...', 'options': ['1.857', '0.5'], 'answer': '1.857'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Resuelve g(3) usando la tabla de diferencias finitas...', 'options': ['1.029', '0.87'], 'answer': '1.029'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'newton_forward_1'}
                ]
            },
            "Newton Hacia Atrás": {
                "Fácil": [
                    {'type': 'practica', 'content': 'El signo del factor binomial "s" en este método es generalmente:', 'options': ['Positivo', 'Negativo'], 'answer': 'Negativo'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula s para x=3, x_final=3.1, h=0.7...', 'options': ['-0.1428', '0.1428'], 'answer': '-0.1428'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula g(3) usando diferencias hacia atrás...', 'options': ['1.029', '1.05'], 'answer': '1.029'},
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
                    {'type': 'practica', 'content': 'Si f(a) es positivo y f(b) positivo, ¿hay raíz garantizada?', 'options': ['Si', 'No'], 'answer': 'No'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula la primera iteración entre a=0 y b=1...', 'options': ['0.5', '0.25'], 'answer': '0.5'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Realiza 3 iteraciones para $x^3 - 6.5x + 2 = 0$...', 'options': ['0.3125', '0.5'], 'answer': '0.3125'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'bisection_1'}
                ]
            },
            "Falsa Posición (Regula-Falsi)": {
                "Fácil": [
                    {'type': 'practica', 'content': 'Este método se basa en una visualización:', 'options': ['Gráfica', 'Aleatoria'], 'answer': 'Gráfica'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Sustituye valores: a=1, f(a)=-2, b=2, f(b)=17...', 'options': ['1.105', '1.5'], 'answer': '1.105'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Encuentra la raíz de $3x^3 - 2x - 3$ tras 2 iteraciones...', 'options': ['1.162', '1.105'], 'answer': '1.162'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'false_position_1'}
                ]
            },
            "Newton-Raphson": {
                "Fácil": [
                    {'type': 'practica', 'content': '¿Qué requiere este método obligatoriamente?', 'options': ['La derivada f\'(x)', 'Dos puntos iniciales'], 'answer': 'La derivada f\'(x)'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula f\'(x) para $x^3 + 2x^2 + 10x - 20$...', 'options': ['$3x^2 + 4x + 10$', '$3x^2 + 2x$'], 'answer': '$3x^2 + 4x + 10$'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Itera una vez desde x0=1 para la función anterior...', 'options': ['1.411', '1.2'], 'answer': '1.411'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'newton_raphson_1'}
                ]
            },
            "Punto Fijo": {
                "Fácil": [
                    {'type': 'practica', 'content': 'Si $2x^2 - x - 5 = 0$, una posible g(x) es:', 'options': ['$2x^2 - 5$', '$\\sqrt{(x+5)/2}$'], 'answer': '$2x^2 - 5$'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Despeja x de $e^{-x} - x = 0$...', 'options': ['$x = e^{-x}$', '$x = e^x$'], 'answer': '$x = e^{-x}$'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula x2 iterando $x = e^{-x}$ iniciando en x0=0...', 'options': ['0.367', '0.567'], 'answer': '0.367'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'fixed_point_1'}
                ]
            },
            "Secante": {
                "Fácil": [
                    {'type': 'practica', 'content': '¿Cuántos valores iniciales requiere la Secante?', 'options': ['1', '2'], 'answer': '2'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula el denominador de la fórmula con f(x1)=-0.63 y f(x0)=1...', 'options': ['-1.63', '0.37'], 'answer': '-1.63'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula la primera iteración para $e^{-x} - x$ con x0=0, x1=1...', 'options': ['0.6127', '0.5'], 'answer': '0.6127'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'secant_1'}
                ]
            },
            "Método Gráfico": {
                "Fácil": [                    {'type': 'practica', 'content': 'Una raíz se identifica visualmente cuando la curva cruza el eje:', 'options': ['X', 'Y'], 'answer': 'X'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Si f(-2)=7 y f(-1)=7.5, ¿hay raíz segura entre -2 y -1?', 'options': ['No', 'Si'], 'answer': 'No'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Identifica el intervalo de la raíz para $x^3 - 6.5x + 2$ observando cambio de signo...', 'options': ['Entre 0 y 1', 'Entre 1 y 2'], 'answer': 'Entre 0 y 1'},
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
                "Fácil": [                    {'type': 'practica', 'content': '¿Qué valores usa para calcular la variable "b" en la iteración 1?', 'options': ['Los iniciales (0)', 'El nuevo "a" recién calculado'], 'answer': 'El nuevo "a" recién calculado'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Despeja "a" de la ecuación $3a - 0.1b - 0.2c = 7.85$...', 'options': ['$(7.85 + 0.1b + 0.2c)/3$', '$(7.85 - 0.1b)/3$'], 'answer': '$(7.85 + 0.1b + 0.2c)/3$'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Realiza la 1ra iteración completa del sistema 3x3 de ejemplo...', 'options': ['a=2.61, b=-2.79, c=7.00', 'a=2, b=2, c=2'], 'answer': 'a=2.61, b=-2.79, c=7.00'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'gauss_seidel_1'}
                ]
            },
            "Jacobi": {
                "Fácil": [                    {'type': 'practica', 'content': 'Diferencia clave con Gauss-Seidel:', 'options': ['Uso de valores anteriores', 'No iterativo'], 'answer': 'Uso de valores anteriores'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Con a0=1, b0=1, c0=1, calcula a1 para $3a - 0.1b - 0.2c = 7.85$...', 'options': ['2.716', '2.616'], 'answer': '2.716'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula el error $\\epsilon_a$ entre la iteración 3 y 4...', 'options': ['0.00056', '0.001'], 'answer': '0.00056'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'jacobi_1'}
                ]
            },
            "Montante": {
                "Fácil": [                    {'type': 'practica', 'content': 'El método Montante utiliza principalmente aritmética de:', 'options': ['Enteros', 'Fracciones'], 'answer': 'Enteros'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula el nuevo elemento usando la fórmula del pivote: (Piv*Act - Ant*Corr)/PivAnt...', 'options': ['1', '2'], 'answer': '1'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Resuelve un sistema 2x2 usando Montante...', 'options': ['x=1, y=2', 'x=0, y=0'], 'answer': 'x=1, y=2'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'montante_1'}
                ]
            },
            "Gauss-Jordan": {
                "Fácil": [                    {'type': 'practica', 'content': 'La matriz final en Gauss-Jordan debe ser:', 'options': ['Identidad', 'Triangular'], 'answer': 'Identidad'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Operación para hacer cero un elemento debajo del pivote...', 'options': ['Fila - k*FilaPivote', 'Fila + FilaPivote'], 'answer': 'Fila - k*FilaPivote'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Obtén la solución final de un sistema 3x3 tras reducirlo...', 'options': ['Vector columna final', 'Fila final'], 'answer': 'Vector columna final'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'gauss_jordan_1'}
                ]
            },
            "Eliminación Gaussiana": {
                "Fácil": [                    {'type': 'practica', 'content': 'A diferencia de Gauss-Jordan, aquí solo buscamos una matriz:', 'options': ['Triangular Superior', 'Identidad'], 'answer': 'Triangular Superior'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Realiza la sustitución hacia atrás para $10c = 70$...', 'options': ['c=7', 'c=10'], 'answer': 'c=7'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Resuelve el sistema completo tras triangular la matriz...', 'options': ['x=1, y=1, z=1', 'x=3, y=2, z=1'], 'answer': 'x=3, y=2, z=1'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'gaussian_elim_1'}
                ]
            },
        }
    },
    "Integración Numérica": {
        "levels": {
            "Regla Trapezoidal": {
                "Fácil": [
                    {'type': 'practica', 'content': '¿A qué grado de polinomio corresponde el trapecio?', 'options': ['1er Grado', '2do Grado'], 'answer': '1er Grado'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Para $\\int_0^1 (1-x^2)dx$ con n=4, calcula h...', 'options': ['0.25', '1'], 'answer': '0.25'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula la integral completa por trapecio (resultado: 0.656)...', 'options': ['0.65625', '0.666'], 'answer': '0.65625'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'trapezoidal_1'}
                ]
            },
            "Regla de 1/3 Simpson": {
                "Fácil": [
                    {'type': 'practica', 'content': 'Requisito indispensable de "n" para 1/3 Simpson:', 'options': ['Debe ser Par', 'Debe ser Impar'], 'answer': 'Debe ser Par'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Coeficiente que multiplica a la sumatoria de índices impares:', 'options': ['4', '2'], 'answer': '4'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula la integral de $1-x^2$ con n=4 usando Simpson 1/3...', 'options': ['0.6666', '0.5'], 'answer': '0.6666'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'simpson_1_3_1'}
                ]
            },
            "Regla de 3/8 Simpson": {
                "Fácil": [
                    {'type': 'practica', 'content': 'Simpson 3/8 requiere que "n" sea:', 'options': ['Múltiplo de 3', 'Par'], 'answer': 'Múltiplo de 3'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': '¿Qué fracción multiplica a h en esta fórmula?', 'options': ['3/8', '1/3'], 'answer': '3/8'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Aplica Simpson 3/8 si los datos son 4 puntos (n=3)...', 'options': ['Resultado de fórmula', 'Error'], 'answer': 'Resultado de fórmula'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'simpson_3_8_1'}
                ]
            },
            "Newton-Cotes Cerradas": {
                "Fácil": [                    {'type': 'practica', 'content': 'En fórmulas cerradas, ¿se incluyen los límites a y b?', 'options': ['Si', 'No'], 'answer': 'Si'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Identifica el coeficiente $\\alpha$ para n=1 (Trapecio)...', 'options': ['1/2', '1/3'], 'answer': '1/2'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula usando coeficientes para n=4 (Cotes cerrada)...', 'options': ['X', 'Y'], 'answer': 'X'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'cotes_closed_1'}
                ]
            },
            "Newton-Cotes Abiertas": {
                "Fácil": [
                    {'type': 'practica', 'content': 'Fórmula para calcular h en Cotes Abiertas:', 'options': ['(b-a)/(n+2)', '(b-a)/n'], 'answer': '(b-a)/(n+2)'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Para n=4 (abierta), ¿cuántos intervalos h hay en total?', 'options': ['6', '4'], 'answer': '6'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula la integral usando Cotes Abierta n=4 (res: 0.666)...', 'options': ['0.666', '0.555'], 'answer': '0.666'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'cotes_open_1'}
                ]
            },
        }
    },
    "Mínimos Cuadrados": {
        "levels": {
            "Línea Recta": {
                "Fácil": [                    {'type': 'practica', 'content': 'El objetivo es minimizar:', 'options': ['La dispersión (error)', 'El valor de x'], 'answer': 'La dispersión (error)'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula $\\sum x^2$ para los datos: 1, 2, 3...', 'options': ['14', '6'], 'answer': '14'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Resuelve a0 y a1 para el sistema de ejemplo...', 'options': ['a0=2.0, a1=0.63', 'a0=0, a1=1'], 'answer': 'a0=2.0, a1=0.63'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_linear_1'}
                ]
            },
            "Cuadrática": {
                "Fácil": [                    {'type': 'practica', 'content': '¿Cuántas incógnitas (coeficientes) se buscan?', 'options': ['3 (a0, a1, a2)', '2'], 'answer': '3 (a0, a1, a2)'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'El término nuevo en el sistema es la suma de potencias a la...', 'options': ['4ta', '3ra'], 'answer': '4ta'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Plantea la matriz para el ajuste cuadrático...', 'options': ['Matriz 3x3', 'Matriz 2x2'], 'answer': 'Matriz 3x3'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_quadratic_1'}
                ]
            },
            "Cúbica": {
                "Fácil": [                    {'type': 'practica', 'content': 'El sistema de ecuaciones resultante es de tamaño:', 'options': ['4x4', '3x3'], 'answer': '4x4'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': '¿Hasta qué potencia de x necesitamos sumar ($\sum x^?$)?', 'options': ['6', '5'], 'answer': '6'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Resuelve para los coeficientes del polinomio cúbico...', 'options': ['a0..a3', 'a0..a2'], 'answer': 'a0..a3'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_cubic_1'}
                ]
            },
            "Lineal con Función": {
                "Fácil": [                    {'type': 'practica', 'content': 'En lugar de $x^2$, el tercer término depende de:', 'options': ['f(x)', 'x^3'], 'answer': 'f(x)'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula $\\sum x \\cdot f(x)$ si f(x)=ln(x)...', 'options': ['Suma de productos', 'Suma simple'], 'answer': 'Suma de productos'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Encuentra los coeficientes para un ajuste con $e^x$...', 'options': ['X', 'Y'], 'answer': 'X'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_linear_func_1'}
                ]
            },
            "Cuadrática con Función": {
                "Fácil": [                    {'type': 'practica', 'content': 'Este modelo tiene 4 coeficientes, incluyendo:', 'options': ['El término f(x)', 'Término cúbico'], 'answer': 'El término f(x)'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Forma la última columna de la matriz extendida: $\\sum y \\cdot f(x)$...', 'options': ['Correcto', 'Incorrecto'], 'answer': 'Correcto'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Resuelve el sistema 4x4 híbrido...', 'options': ['X', 'Y'], 'answer': 'X'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'least_sq_quadratic_func_1'}
                ]
            },
        }
    },
    "Ecuaciones Diferenciales Ordinarias (EDO)": {
        "levels": {
            "Euler Modificado": {
                "Fácil": [
                    {'type': 'practica', 'content': '¿Qué regla de integración usa Euler Modificado?', 'options': ['Trapezoidal', 'Simpson'], 'answer': 'Trapezoidal'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula el predictor (Euler simple) para la primera iteración...', 'options': ['Valor inicial estimado', 'Valor final'], 'answer': 'Valor inicial estimado'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Realiza una iteración completa de Euler Modificado...', 'options': ['1.99', '2.0'], 'answer': '1.99'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'euler_modified_1'}
                ]
            },
            "Runge-Kutta 2do Orden": {
                "Fácil": [
                    {'type': 'practica', 'content': '¿Cuántas evaluaciones de la función (k) se hacen?', 'options': ['2', '4'], 'answer': '2'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula $k_1 = h \\cdot f(y_n, t_n)$ con h=0.2...', 'options': ['-0.2', '0.5'], 'answer': '-0.2'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Obtén y1 usando RK 2do orden...', 'options': ['1.98', '2.0'], 'answer': '1.98'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk2_1'}
                ]
            },
            "Runge-Kutta 3er Orden": {
                "Fácil": [
                    {'type': 'practica', 'content': 'El peso mayor se le da a la pendiente intermedia:', 'options': ['k2 (x4)', 'k1 (x1)'], 'answer': 'k2 (x4)'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula k2 evaluando en $t_n + h/2$...', 'options': ['X', 'Y'], 'answer': 'X'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Resuelve para y1 con RK 3er orden...', 'options': ['X', 'Y'], 'answer': 'X'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk3_1'}
                ]
            },
            "Runge-Kutta 4to Orden (1/3 Simpson)": {
                "Fácil": [
                    {'type': 'practica', 'content': '¿Cuáles pendientes se multiplican por 2?', 'options': ['k2 y k3', 'k1 y k4'], 'answer': 'k2 y k3'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Calcula k3 usando el resultado de k2...', 'options': ['-0.0005', '-0.01'], 'answer': '-0.0005'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Calcula el valor final y1 tras sumar las k...', 'options': ['1.996', '2.0'], 'answer': '1.996'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk4_simpson13_1'}
                ]
            },
            "Runge-Kutta 4to Orden (3/8 Simpson)": {
                "Fácil": [
                    {'type': 'practica', 'content': 'En esta variante, el divisor de la fórmula es:', 'options': ['8', '6'], 'answer': '8'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Evalúa k2 y k3 en pasos de h/3...', 'options': ['Si', 'No'], 'answer': 'Si'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Compara el resultado con RK 1/3 Simpson...', 'options': ['Similar', 'Muy diferente'], 'answer': 'Similar'},
                ],
                "Prueba Final": [
                    {'type': 'examen', 'problem_id': 'rk4_simpson38_1'}
                ]
            },
            "Runge-Kutta Orden Superior": {
                "Fácil": [                    {'type': 'practica', 'content': 'Para una EDO de 2do orden, necesitamos calcular:', 'options': ['k y m', 'Solo k'], 'answer': 'k y m'},
                ],
                "Intermedio": [
                    {'type': 'practica', 'content': 'Define $V_n = y\'$ y $U_n = y$...', 'options': ['Si', 'No'], 'answer': 'Si'},
                ],
                "Avanzado": [
                    {'type': 'practica', 'content': 'Resuelve para $y_1$ y $y\'_1$ simultáneamente...', 'options': ['y=2.125, y\'=3.06', 'y=2, y\'=2'], 'answer': 'y=2.125, y\'=3.06'},
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
        'title': 'Interpolar g(2.4) usando Lagrange',
        'x_value': 2.4,
        'table': [(2.2, 2.54), (2.5, 2.82)],
        'options': ['2.6680', '2.7680', '2.5680', '2.8680', '2.4680'],
        'correct': '2.6680',
        'time_minutes': 15
    },
    'lagrange_avanzado': {
        'title': 'Obtener g(x)',
        'x_value': 2.4,
        'table': [(2.2, 2.54), (2.5, 2.82), (2.8, 3.21)],
        'options': ['2.67646', '2.77646', '2.57646', '2.87646', '2.47646'],
        'correct': '2.67646',
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
        'time_minutes': 20
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
        'time_minutes': 30
    },
    'false_position_1': {
        'title': 'Prueba Final: Método de Falsa Posición',
        'x_value': None,
        'table': [('Función: f(x) = x² - 2',), ('Intervalo: [1, 2]',), ('Encuentra la raíz',)],
        'options': ['1.52', '1.62', '1.42', '1.72', '1.32'],
        'correct': '1.52',
        'time_minutes': 30
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
        'time_minutes': 20
    },
    'gauss_seidel_1': {
        'title': 'Prueba Final: Gauss-Seidel',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('4x + y = 9',), ('x + 3y = 10',)],
        'options': ['x=2, y=1', 'x=1, y=3', 'x=3, y=2', 'x=2, y=2', 'x=1, y=2'],
        'correct': 'x=2, y=1',
        'time_minutes': 30
    },
    'jacobi_1': {
        'title': 'Prueba Final: Método de Jacobi',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('5x + y = 11',), ('x + 4y = 9',)],
        'options': ['x=2, y=1', 'x=1, y=2', 'x=3, y=1', 'x=2, y=2', 'x=1, y=3'],
        'correct': 'x=2, y=1',
        'time_minutes': 30
    },
    'montante_1': {
        'title': 'Prueba Final: Método de Montante',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('2x + y = 5',), ('x + 3y = 8',)],
        'options': ['x=1, y=3', 'x=2, y=1', 'x=3, y=2', 'x=2, y=2', 'x=1, y=2'],
        'correct': 'x=1, y=3',
        'time_minutes': 30
    },
    'gauss_jordan_1': {
        'title': 'Prueba Final: Gauss-Jordan',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('3x + 2y = 12',), ('x + 4y = 14',)],
        'options': ['x=2, y=3', 'x=3, y=2', 'x=1, y=4', 'x=4, y=1', 'x=2, y=2'],
        'correct': 'x=2, y=3',
        'time_minutes': 30
    },
    'gaussian_elim_1': {
        'title': 'Prueba Final: Eliminación Gaussiana',
        'x_value': None,
        'table': [('Sistema de ecuaciones:',), ('2x + 3y = 13',), ('x + 2y = 8',)],
        'options': ['x=2, y=3', 'x=3, y=2', 'x=1, y=4', 'x=4, y=1', 'x=2, y=2'],
        'correct': 'x=2, y=3',
        'time_minutes': 30
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
        'time_minutes': 30
    },
    'cotes_open_1': {
        'title': 'Prueba Final: Newton-Cotes Abierto',
        'x_value': None,
        'table': [('Integrar: ∫ f(x) dx',), ('Datos de la función:',), (0.5, 1.5), (1, 2.5), (1.5, 4)],
        'options': ['4.5', '5.5', '3.5', '6.5', '2.5'],
        'correct': '4.5',
        'time_minutes': 30
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
        'time_minutes': 30
    },
    'least_sq_cubic_1': {
        'title': 'Prueba Final: Mínimos Cuadrados Cúbico',
        'x_value': 3,
        'table': [('Ajustar: y = a + bx + cx² + dx³',), ('Datos:',), (0, 1), (1, 2), (2, 5), (3, 10), (4, 20)],
        'options': ['10.2', '11.2', '9.2', '12.2', '8.2'],
        'correct': '10.2',
        'time_minutes': 30
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
        'time_minutes': 30
    },
    'euler_modified_1': {
        'title': 'Prueba Final: Euler Modificado',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y", "Condición inicial: y(0) = 1", "Paso: h = 0.1")],
        'options': ['1.221', '1.321', '1.121', '1.421', '1.021'],
        'correct': '1.221',
        'time_minutes': 25
    },
    'rk2_1': {
        'title': 'Prueba Final: Runge-Kutta Orden 2',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y", "Condición inicial: y(0) = 1", "Paso: h = 0.1")],
        'options': ['1.242', '1.342', '1.142', '1.442', '1.042'],
        'correct': '1.242',
        'time_minutes': 25
    },
    'rk3_1': {
        'title': 'Prueba Final: Runge-Kutta Orden 3',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y", "Condición inicial: y(0) = 1", "Paso: h = 0.1")],
        'options': ['1.246', '1.346', '1.146', '1.446', '1.046'],
        'correct': '1.246',
        'time_minutes': 30
    },
    'rk4_simpson13_1': {
        'title': 'Prueba Final: RK4 Simpson 1/3',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y", "Condición inicial: y(0) = 1", "Paso: h = 0.1")],
        'options': ['1.2428', '1.3428', '1.1428', '1.4428', '1.0428'],
        'correct': '1.2428',
        'time_minutes': 30
    },
    'rk4_simpson38_1': {
        'title': 'Prueba Final: RK4 Simpson 3/8',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y", "Condición inicial: y(0) = 1", "Paso: h = 0.1")],
        'options': ['1.2431', '1.3431', '1.1431', '1.4431', '1.0431'],
        'correct': '1.2431',
        'time_minutes': 30
    },
    'rk_higher_order_1': {
        'title': 'Prueba Final: RK Orden Superior',
        'x_value': 0.2,
        'table': [("Ecuación: dy/dx = x + y", "Condición inicial: y(0) = 1", "Paso: h = 0.05")],
        'options': ['1.2435', '1.3435', '1.1435', '1.4435', '1.0435'],
        'correct': '1.2435',
        'time_minutes': 35
    },
}
