# game_data.py
# Define la estructura de todos los capítulos, niveles y lecciones

"""
Tipos de Lecciones:
- 'Explicativa': Muestra texto y fórmulas. 
- 'Practica': Un problema donde se muestra la solución si se falla.
- 'Examen': Un problema donde fallar reinicia la lección.
"""

GAME_STRUCTURE = {
    "Capítulo 1: Interpolación":{
        "levels": {
            "Nivel 1: Lagrange": [
                {'type': 'explicativa', 'content': 'El método de Lagrange se usa para intervalos no uniformes.... La fórmula es: g(x) = Σ yi * Π... '},
                {'type': 'practica', 'content': '¿Qué falta en la fórmula g(x) = Σ [?] * Π...?', 'options': ['yi', 'xi', 'gi'], 'answer': 'yi'}, 
                {'type': 'practica', 'content': '¿Qué falta en la fórmula ... Π (x - [?]) / ...?', 'options': ['x-xj', 'xi', 'xj'], 'answer': 'x-xj'}, 
                {'type': 'examen', 'problem_id': 'lagrange_1'} 
            ],
            "Nivel 2: Lineal": [
                {'type': 'explicativa', 'content': 'Consiste en unir dos puntos con una línea recta. Fórmula: g(x) = ... '},
                {'type': 'examen', 'problem_id': 'linear_interp_1'} 
            ],
            "Nivel 3: Newton con Diferencias Divididas": [
                {'type': 'explicativa', 'content': 'Se aplica cuando los intervalos son no uniformes. Fórmula: g(x) = D0 + D1(x-x1) + ... '},
                {'type': 'examen', 'problem_id': 'newton_div_diff_1'} 
            ],
            "Nivel 4: Newton Hacia Adelante": [
                {'type': 'explicativa', 'content': 'Se usa para intervalos uniformes. Fórmula: g(x) = yi[s 0] + Δf(xi)[s 1]...'},
                {'type': 'examen', 'problem_id': 'newton_forward_1'} 
            ],
            "Nivel 5: Newton Hacia Atrás": [
                {'type': 'explicativa', 'content': "Requiere intervalos uniformes. El factor binomial 's' es siempre negativo. Fórmula: ...[s(s+1)/2!]... "},
                {'type': 'examen', 'problem_id': 'newton_backward_1'}
            ],
        }
    },
    "Capítulo 2: Ecuaciones No Lineales": {
        "levels": {
            "Nivel 1: Bisección (Bisectriz)": [
                {'type': 'explicativa', 'content': 'Es el punto medio entre dos puntos. Fórmula: x = (a+b)/2 '},
                {'type': 'examen', 'problem_id': 'bisection_1'} 
            ],
            "Nivel 2: Falsa Posición (Regula-Falsi)": [
                {'type': 'explicativa', 'content': 'Une f(b) y f(a) con una línea recta. Fórmula: x = a - f(a)(b-a) / (f(b)-f(a))'},
                {'type': 'examen', 'problem_id': 'false_position_1'} 
            ],
            "Nivel 3: Newton-Raphson": [
                {'type': 'explicativa', 'content': 'Utiliza rectas tangentes[cite: 285]. Fórmula: x_i+1 = x_i - (f(x_i) / f\'(x_i))'},
                {'type': 'examen', 'problem_id': 'newton_raphson_1'} 
            ],
            "Nivel 4: Punto Fijo": [
                {'type': 'explicativa', 'content': 'Transforma algebraicamente f(x)=0 a x=g(x). Fórmula: x_i+1 = g(x_i)'},
                {'type': 'examen', 'problem_id': 'fixed_point_1'} 
            ],
            "Nivel 5: Secante": [
                {'type': 'explicativa', 'content': 'Similar a Newton, pero aproxima la derivada. Fórmula: x_i+1 = ... '},
                {'type': 'examen', 'problem_id': 'secant_1'}  
            ],
            "Nivel 6: Método Gráfico": [
                {'type': 'explicativa', 'content': 'Consiste en graficar la función y observar donde cruza el eje x.'},
                {'type': 'examen', 'problem_id': 'graphical_1'} 
            ],
        }
    },
    "Capítulo 3: Ecuaciones Lineales": {
        "levels": {
            "Nivel 1: Gauss-Seidel": [
                {'type': 'explicativa', 'content': 'Método iterativo para resolver sistemas de ecuaciones. Requiere diagonal dominante.'},
                {'type': 'examen', 'problem_id': 'gauss_seidel_1'} 
            ],
            "Nivel 2: Jacobi": [
                {'type': 'explicativa', 'content': 'Método iterativo similar a Gauss-Seidel, pero no usa los valores nuevos en la misma iteración.'},
                {'type': 'examen', 'problem_id': 'jacobi_1'}
            ],
            "Nivel 3: Montante": [
                {'type': 'explicativa', 'content': 'Método de pivoteo para resolver sistemas de ecuaciones. '},
                {'type': 'examen', 'problem_id': 'montante_1'}
            ],
            "Nivel 4: Gauss-Jordan": [
                {'type': 'explicativa', 'content': 'Método de eliminación para encontrar la matriz inversa o resolver sistemas.'},
                {'type': 'examen', 'problem_id': 'gauss_jordan_1'}
            ],
            "Nivel 5: Eliminación Gaussiana": [
                {'type': 'explicativa', 'content': 'Método de eliminación para convertir la matriz en triangular superior. '},
                {'type': 'examen', 'problem_id': 'gaussian_elim_1'}
            ],
        }
    },
    "Capítulo 4: Integración Numérica": {
        "levels": {
            "Nivel 1: Regla Trapezoidal": [
                {'type': 'explicativa', 'content': 'Integra un polinomio de primer grado. Fórmula: I = h/2 * [f(a) + 2Σ... + f(b)]'},
                {'type': 'examen', 'problem_id': 'trapezoidal_1'} 
            ],
            "Nivel 2: Regla de 1/3 Simpson": [
                {'type': 'explicativa', 'content': 'Integra un polinomio de 2do grado. n debe ser par[cite: 928, 933]. Fórmula: I = h/3 * [f(a) + 4Σ(impar) + 2Σ(par) + f(b)]'},
                {'type': 'examen', 'problem_id': 'simpson_1_3_1'} 
            ],
            "Nivel 3: Regla de 3/8 Simpson": [
                {'type': 'explicativa', 'content': 'Integra un polinomio de 3er grado. n debe ser múltiplo de 3. Fórmula: I = 3h/8 * [...]'},
                {'type': 'examen', 'problem_id': 'simpson_3_8_1'} 
            ],
            "Nivel 4: Newton-Cotes Cerradas": [
                {'type': 'explicativa', 'content': 'Fórmulas de integración donde el dominio está cerrado por el primer y último dato[cite: 1006]. Fórmula: I = αh * Σ(wi * f(a+ih)) '},
                {'type': 'examen', 'problem_id': 'cotes_closed_1'} 
            ],
            "Nivel 5: Newton-Cotes Abiertas": [
                {'type': 'explicativa', 'content': 'Fórmulas de integración que extienden el intervalo. h = (b-a)/(n+2)'},
                {'type': 'examen', 'problem_id': 'cotes_open_1'} 
            ],
        }
    },
    "Capítulo 5: Mínimos Cuadrados": {
        "levels": {
            "Nivel 1: Línea Recta": [
                {'type': 'explicativa', 'content': 'Ajuste a la ecuación g(x) = a0 + a1*x. Se resuelve el sistema: n*a0 + Σx*a1 = Σy ... '},
                {'type': 'examen', 'problem_id': 'least_sq_linear_1'} 
            ],
            "Nivel 2: Cuadrática": [
                {'type': 'explicativa', 'content': 'Ajuste a la ecuación g(x) = a0 + a1*x + a2*x^2. Se resuelve el sistema de 3x3... '},
                {'type': 'examen', 'problem_id': 'least_sq_quadratic_1'}
            ],
            "Nivel 3: Cúbica": [
                {'type': 'explicativa', 'content': 'Ajuste a la ecuación g(x) = a0 + a1*x + a2*x^2 + a3*x^3. Se resuelve el sistema de 4x4... '},
                {'type': 'examen', 'problem_id': 'least_sq_cubic_1'}
            ],
            "Nivel 4: Lineal con Función": [
                {'type': 'explicativa', 'content': 'Ajuste a g(x) = a0 + a1*x + a2*f(x). f(x) puede ser e^x, sen(x), etc. Sistema: ...Σx*f(x)...'},
                {'type': 'examen', 'problem_id': 'least_sq_linear_func_1'}
            ],
            "Nivel 5: Cuadrática con Función": [
                {'type': 'explicativa', 'content': 'Ajuste a g(x) = a0 + a1*x + a2*x^2 + a3*f(x). Sistema de 4x4...'},
                {'type': 'examen', 'problem_id': 'least_sq_quadratic_func_1'}
            ],
        }
    },
    "Capítulo 6: Ecuaciones Diferenciales Ordinarias (EDO)": {
        "levels": {
            "Nivel 1: Euler (Adelante)": [
                {'type': 'explicativa', 'content': 'Método de punto pendiente.'},
                {'type': 'examen', 'problem_id': 'euler_forward_1'}
            ],
            "Nivel 2: Euler Modificado": [
                {'type': 'explicativa', 'content': 'Más exacto que Euler Adelante. Fórmula: y_n+1 = y_n + (h/2) * [f(...) + f(...)'},
                {'type': 'examen', 'problem_id': 'euler_modified_1'} 
            ],
            "Nivel 3: Euler (Atrás)": [
                {'type': 'explicativa', 'content': 'Versión del método de Euler.'},
                {'type': 'examen', 'problem_id': 'euler_backward_1'}
            ],
            "Nivel 4: Runge-Kutta 2do Orden": [
                {'type': 'explicativa', 'content': 'Usa dos pasos de iteración. k1 = h*f(...), k2 = h*f(y_n+k1, ...), y_n+1 = y_n + 1/2(k1+k2) '},
                {'type': 'examen', 'problem_id': 'rk2_1'} 
            ],
            "Nivel 5: Runge-Kutta 3er Orden": [
                {'type': 'explicativa', 'content': 'Fórmulas: k1=..., k2=..., k3=... y_n+1 = y_n + 1/6(k1+4k2+k3)'},
                {'type': 'examen', 'problem_id': 'rk3_1'} 
            ],
            "Nivel 6: Runge-Kutta 4to Orden (1/3 Simpson)": [
                {'type': 'explicativa', 'content': 'Basado en 1/3 de Simpson. Fórmulas: k1, k2, k3, k4. y_n+1 = y_n + 1/6(k1+2k2+2k3+k4)'},
                {'type': 'examen', 'problem_id': 'rk4_simpson13_1'} 
            ],
            "Nivel 7: Runge-Kutta 4to Orden (3/8 Simpson)": [
                {'type': 'explicativa', 'content': 'Basado en 3/8 de Simpson. Fórmulas: k1, k2, k3, k4. y_n+1 = y_n + 1/8(k1+3k2+3k3+k4)'},
                {'type': 'examen', 'problem_id': 'rk4_simpson38_1'} 
            ],
            "Nivel 8: Runge-Kutta Orden Superior": [
                {'type': 'explicativa', 'content': 'Se usa para EDOs de orden superior (ej. y\'\'). Fórmulas: k1=h*Vn, m1=h[...], y_n+1 = ... '},
                {'type': 'examen', 'problem_id': 'rk_higher_order_1'} 
            ],
        }
    },
}