"""
Tipos de Lecciones:
- 'Explicativa': Muestra texto y fórmulas. 
- 'Practica': Un problema donde se muestra la solución si se falla.
- 'Examen': Un problema donde fallar reinicia la lección.
"""

GAME_STRUCTURE = {
    "Capítulo 1: Interpolación": {
        "levels": {
            "Nivel 1: Lagrange": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Este método se aplica para intervalos tanto uniformes como NO uniformes. Desventaja: Gran cantidad de cálculos. Fórmula: $g(x) = \\sum y_i \\prod \\frac{x - x_j}{x_i - x_j}$'},
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
            "Nivel 2: Lineal": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Consiste en unir dos puntos con una línea recta. Es una aproximación a la primera derivada. Fórmula: $g(x) = f(a) + \\frac{f(b)-f(a)}{b-a}(x-a)$'},
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
            "Nivel 3: Newton con Diferencias Divididas": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Se aplica cuando los intervalos son NO uniformes. Utiliza "D" como operador. Fórmula: $g(x) = D_0 + D_1(x-x_1) + D_2(x-x_1)(x-x_2) + ...$'},
                    {'type': 'practica', 'content': '¿Qué tipo de intervalos maneja principalmente este método?', 'options': ['Uniformes', 'No Uniformes'], 'answer': 'No Uniformes'},
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
            "Nivel 4: Newton Hacia Adelante": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Requiere intervalos UNIFORMES (h constante). Usa el factor binomial "s" positivo (izquierda a derecha). Fórmula: $g(x) = y_1 + \\Delta f(x_i)s + \\Delta^2 f(x_i)\\frac{s(s-1)}{2!}...$'},
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
            "Nivel 5: Newton Hacia Atrás": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Requiere intervalos UNIFORMES. Se usa cuando el valor a interpolar está al final de la tabla. El factor binomial "s" es negativo. Fórmula: $g(x) = y_n + \\nabla f(x_i)s + \\nabla^2 f(x_i)\\frac{s(s+1)}{2!}...$'},
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
    "Capítulo 2: Ecuaciones No Lineales": {
        "levels": {
            "Nivel 1: Bisección (Bisectriz)": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Método cerrado. Es el punto medio entre a y b. Se basa en el cambio de signo. Fórmula: $x = \\frac{a+b}{2}$'},
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
            "Nivel 2: Falsa Posición (Regula-Falsi)": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Une f(b) y f(a) con una recta. Es más rápido que la bisección. Fórmula basada en triángulos semejantes: $x = a - \\frac{f(a)(b-a)}{f(b)-f(a)}$'},
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
            "Nivel 3: Newton-Raphson": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Utiliza rectas tangentes y la derivada de la función. Requiere un valor inicial cercano. Convergencia rápida. Fórmula: $x_{i+1} = x_i - \\frac{f(x_i)}{f\'(x_i)}$'},
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
            "Nivel 4: Punto Fijo": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Transforma $f(x)=0$ a la forma equivalente $x=g(x)$. Se llama sustitución sucesiva. Fórmula iterativa: $x_{i+1} = g(x_i)$'},
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
            "Nivel 5: Secante": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Similar a Newton pero aproxima la derivada usando dos puntos iniciales ($x_{i-1}, x_i$). Fórmula: $x_{i+1} = x_i - \\frac{f(x_i)(x_i - x_{i-1})}{f(x_i) - f(x_{i-1})}$'},
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
            "Nivel 6: Método Gráfico": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Método simple para obtener una aproximación. Consiste en graficar la función y observar dónde cruza el eje X ($f(x)=0$).'},
                    {'type': 'practica', 'content': 'Una raíz se identifica visualmente cuando la curva cruza el eje:', 'options': ['X', 'Y'], 'answer': 'X'},
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
    "Capítulo 3: Ecuaciones Lineales": {
        "levels": {
            "Nivel 1: Gauss-Seidel": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Método iterativo. Requiere que la matriz tenga DIAGONAL DOMINANTE. Utiliza los valores recién calculados en la misma iteración. Fórmula: Despejar variable de la diagonal.'},
                    {'type': 'practica', 'content': '¿Qué valores usa para calcular la variable "b" en la iteración 1?', 'options': ['Los iniciales (0)', 'El nuevo "a" recién calculado'], 'answer': 'El nuevo "a" recién calculado'},
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
            "Nivel 2: Jacobi": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Método iterativo similar a Gauss-Seidel, pero NO usa los valores nuevos en la misma iteración, usa los de la iteración anterior. Requiere diagonal dominante.'},
                    {'type': 'practica', 'content': 'Diferencia clave con Gauss-Seidel:', 'options': ['Uso de valores anteriores', 'No iterativo'], 'answer': 'Uso de valores anteriores'},
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
            "Nivel 3: Montante": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Método directo de determinantes (algoritmo del pivote). Trabaja con enteros. Transforma la matriz en una matriz identidad multiplicada por el determinante.'},
                    {'type': 'practica', 'content': 'El método Montante utiliza principalmente aritmética de:', 'options': ['Enteros', 'Fracciones'], 'answer': 'Enteros'},
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
            "Nivel 4: Gauss-Jordan": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Método de eliminación para resolver sistemas o encontrar la matriz inversa. El objetivo es convertir la matriz principal en una matriz identidad.'},
                    {'type': 'practica', 'content': 'La matriz final en Gauss-Jordan debe ser:', 'options': ['Identidad', 'Triangular'], 'answer': 'Identidad'},
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
            "Nivel 5: Eliminación Gaussiana": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Método que convierte la matriz en TRIANGULAR SUPERIOR. Luego se usa sustitución hacia atrás para encontrar las variables.'},
                    {'type': 'practica', 'content': 'A diferencia de Gauss-Jordan, aquí solo buscamos una matriz:', 'options': ['Triangular Superior', 'Identidad'], 'answer': 'Triangular Superior'},
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
    "Capítulo 4: Integración Numérica": {
        "levels": {
            "Nivel 1: Regla Trapezoidal": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Integra un polinomio de 1er grado (línea recta). Es el área bajo la curva aproximada por trapecios. Fórmula: $I = \\frac{h}{2} [f(a) + 2\\Sigma f(x_i) + f(b)]$'},
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
            "Nivel 2: Regla de 1/3 Simpson": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Integra un polinomio de 2do grado (parábolas). "n" debe ser PAR. Fórmula: $I = \\frac{h}{3} [f(a) + 4\\Sigma_{impar} + 2\\Sigma_{par} + f(b)]$'},
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
            "Nivel 3: Regla de 3/8 Simpson": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Integra un polinomio de 3er grado. "n" debe ser MÚLTIPLO DE 3. Fórmula: $I = \\frac{3h}{8} [f(a) + 3\\Sigma + 3\\Sigma + f(b)]$'},
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
            "Nivel 4: Newton-Cotes Cerradas": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'El dominio de integración está CERRADO por el primer y último dato (a y b). Incluye Trapecio y Simpson. Fórmula: $I = \\alpha h \\sum w_i f(a+ih)$'},
                    {'type': 'practica', 'content': 'En fórmulas cerradas, ¿se incluyen los límites a y b?', 'options': ['Si', 'No'], 'answer': 'Si'},
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
            "Nivel 5: Newton-Cotes Abiertas": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Extienden la integración más allá de los datos (intervalo a la izquierda y derecha). $h = \\frac{b-a}{n+2}$. Útil cuando f(x) tiene singularidades en los extremos.'},
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
    "Capítulo 5: Mínimos Cuadrados": {
        "levels": {
            "Nivel 1: Línea Recta": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Ajusta una recta $g(x) = a_0 + a_1x$ minimizando el error cuadrático. Resuelve el sistema: $\\sum y = n a_0 + a_1 \\sum x$ y $\\sum xy = a_0 \\sum x + a_1 \\sum x^2$.'},
                    {'type': 'practica', 'content': 'El objetivo es minimizar:', 'options': ['La dispersión (error)', 'El valor de x'], 'answer': 'La dispersión (error)'},
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
            "Nivel 2: Cuadrática": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Ajusta una parábola $g(x) = a_0 + a_1x + a_2x^2$. Genera un sistema de 3x3 ecuaciones normales.'},
                    {'type': 'practica', 'content': '¿Cuántas incógnitas (coeficientes) se buscan?', 'options': ['3 (a0, a1, a2)', '2'], 'answer': '3 (a0, a1, a2)'},
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
            "Nivel 3: Cúbica": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Ajusta un polinomio de 3er grado $g(x) = a_0 + a_1x + a_2x^2 + a_3x^3$. Requiere resolver un sistema de 4x4.'},
                    {'type': 'practica', 'content': 'El sistema de ecuaciones resultante es de tamaño:', 'options': ['4x4', '3x3'], 'answer': '4x4'},
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
            "Nivel 4: Lineal con Función": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Ajuste al modelo $g(x) = a_0 + a_1x + a_2 f(x)$. $f(x)$ puede ser $e^x, \\sin(x), \\ln(x)$, etc. Adapta el método de mínimos cuadrados usando $f(x)$ como variable.'},
                    {'type': 'practica', 'content': 'En lugar de $x^2$, el tercer término depende de:', 'options': ['f(x)', 'x^3'], 'answer': 'f(x)'},
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
            "Nivel 5: Cuadrática con Función": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Ajuste al modelo $g(x) = a_0 + a_1x + a_2x^2 + a_3 f(x)$. Combina ajuste parabólico con una función especial.'},
                    {'type': 'practica', 'content': 'Este modelo tiene 4 coeficientes, incluyendo:', 'options': ['El término f(x)', 'Término cúbico'], 'answer': 'El término f(x)'},
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
    "Capítulo 6: Ecuaciones Diferenciales Ordinarias (EDO)": {
        "levels": {
            "Nivel 1: Euler Modificado": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Más exacto que Euler simple. Aplica la regla trapezoidal (predictor-corrector). Fórmula: $y_{n+1} = y_n + \\frac{h}{2}[f(y_n, t_n) + f(y_{n+1}^*, t_{n+1})]$'},
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
            "Nivel 2: Runge-Kutta 2do Orden": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Usa dos pendientes ($k_1, k_2$). $k_1$ es la pendiente al inicio, $k_2$ al final del intervalo estimado. Fórmula: $y_{n+1} = y_n + \\frac{1}{2}(k_1 + k_2)$'},
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
            "Nivel 3: Runge-Kutta 3er Orden": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Utiliza tres pendientes ($k_1, k_2, k_3$). Es más preciso. Fórmula: $y_{n+1} = y_n + \\frac{1}{6}(k_1 + 4k_2 + k_3)$'},
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
            "Nivel 4: Runge-Kutta 4to Orden (1/3 Simpson)": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'El método más común. Usa 4 pendientes. Basado en Simpson 1/3. Fórmula: $y_{n+1} = y_n + \\frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$'},
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
            "Nivel 5: Runge-Kutta 4to Orden (3/8 Simpson)": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Variante de 4to orden basada en Simpson 3/8. Fórmula: $y_{n+1} = y_n + \\frac{1}{8}(k_1 + 3k_2 + 3k_3 + k_4)$'},
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
            "Nivel 6: Runge-Kutta Orden Superior": {
                "Fácil": [
                    {'type': 'explicativa', 'content': 'Para EDOs de orden superior (ej. $y\'\'$). Se reduce a un sistema de EDOs de 1er orden. Usa $k$ para $y$ y $m$ para $y\'$.'},
                    {'type': 'practica', 'content': 'Para una EDO de 2do orden, necesitamos calcular:', 'options': ['k y m', 'Solo k'], 'answer': 'k y m'},
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