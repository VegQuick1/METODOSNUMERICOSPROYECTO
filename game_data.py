# game_data.py
# Define la estructura de todos los capítulos, niveles y lecciones
# basado en tu boceto [cite: 672, 686, 705-722]

"""
Tipos de Lecciones (definidos en tu boceto [cite: 714-718]):
- 'explicativa': Muestra texto y fórmulas. [cite: 715]
- 'practica': Un problema donde se muestra la solución si se falla. [cite: 716]
- 'examen': Un problema donde fallar reinicia la lección. [cite: 718, 721]
"""

GAME_STRUCTURE = {
    "Capítulo 1: Interpolación":{
        "levels": {
            "Nivel 1: Lagrange": [
                {'type': 'explicativa', 'content': 'El método de Lagrange se usa para intervalos no uniformes...[cite: 419]. La fórmula es: g(x) = Σ yi * Π... [cite: 420]'},
                {'type': 'practica', 'content': '¿Qué falta en la fórmula g(x) = Σ [?] * Π...?', 'options': ['yi', 'xi', 'gi'], 'answer': 'yi'}, # [cite: 627, 628]
                {'type': 'practica', 'content': '¿Qué falta en la fórmula ... Π (x - [?]) / ...?', 'options': ['x-xj', 'xi', 'xj'], 'answer': 'x-xj'}, # [cite: 634, 635]
                {'type': 'examen', 'problem_id': 'lagrange_1'} # Coincide con el problema en [cite: 644]
            ],
            "Nivel 2: Lineal": [
                {'type': 'explicativa', 'content': 'Consiste en unir dos puntos con una línea recta[cite: 367]. Fórmula: g(x) = ... [cite: 370]'},
                {'type': 'examen', 'problem_id': 'linear_interp_1'} # Coincide con el problema en [cite: 385]
            ],
            "Nivel 3: Newton con Diferencias Divididas": [
                {'type': 'explicativa', 'content': 'Se aplica cuando los intervalos son no uniformes[cite: 439]. Fórmula: g(x) = D0 + D1(x-x1) + ... [cite: 444]'},
                {'type': 'examen', 'problem_id': 'newton_div_diff_1'} # Coincide con el problema en [cite: 445]
            ],
            "Nivel 4: Newton Hacia Adelante": [
                {'type': 'explicativa', 'content': 'Se usa para intervalos uniformes[cite: 475, 479]. Fórmula: g(x) = yi[s 0] + Δf(xi)[s 1]... [cite: 490]'},
                {'type': 'examen', 'problem_id': 'newton_forward_1'} # Coincide con el problema en [cite: 493, 637]
            ],
            "Nivel 5: Newton Hacia Atrás": [
                {'type': 'explicativa', 'content': "Requiere intervalos uniformes[cite: 540]. El factor binomial 's' es siempre negativo[cite: 547]. Fórmula: ...[s(s+1)/2!]... [cite: 551]"},
                {'type': 'examen', 'problem_id': 'newton_backward_1'} # Coincide con el problema en [cite: 555]
            ],
        }
    },
    "Capítulo 2: Ecuaciones No Lineales": {
        "levels": {
            "Nivel 1: Bisección (Bisectriz)": [
                {'type': 'explicativa', 'content': 'Es el punto medio entre dos puntos[cite: 234]. Fórmula: x = (a+b)/2 [cite: 236]'},
                {'type': 'examen', 'problem_id': 'bisection_1'} # Coincide con el problema en [cite: 237]
            ],
            "Nivel 2: Falsa Posición (Regula-Falsi)": [
                {'type': 'explicativa', 'content': 'Une f(b) y f(a) con una línea recta[cite: 245]. Fórmula: x = a - f(a)(b-a) / (f(b)-f(a)) [cite: 259]'},
                {'type': 'examen', 'problem_id': 'false_position_1'} # Coincide con el problema en [cite: 263]
            ],
            "Nivel 3: Newton-Raphson": [
                {'type': 'explicativa', 'content': 'Utiliza rectas tangentes[cite: 285]. Fórmula: x_i+1 = x_i - (f(x_i) / f\'(x_i)) [cite: 293]'},
                {'type': 'examen', 'problem_id': 'newton_raphson_1'} # Coincide con el problema en [cite: 297]
            ],
            "Nivel 4: Punto Fijo": [
                {'type': 'explicativa', 'content': 'Transforma algebraicamente f(x)=0 a x=g(x)[cite: 304]. Fórmula: x_i+1 = g(x_i) [cite: 319]'},
                {'type': 'examen', 'problem_id': 'fixed_point_1'} # Coincide con el problema en [cite: 322]
            ],
            "Nivel 5: Secante": [
                {'type': 'explicativa', 'content': 'Similar a Newton, pero aproxima la derivada[cite: 336]. Fórmula: x_i+1 = ... [cite: 343]'},
                {'type': 'examen', 'problem_id': 'secant_1'} # Coincide con el problema en [cite: 346]
            ],
            "Nivel 6: Método Gráfico": [
                {'type': 'explicativa', 'content': 'Consiste en graficar la función y observar donde cruza el eje x[cite: 192].'},
                {'type': 'examen', 'problem_id': 'graphical_1'} # Coincide con el problema en [cite: 194]
            ],
        }
    },
    "Capítulo 3: Ecuaciones Lineales": {
        "levels": {
            "Nivel 1: Gauss-Seidel": [
                {'type': 'explicativa', 'content': 'Método iterativo para resolver sistemas de ecuaciones[cite: 6]. Requiere diagonal dominante[cite: 12].'},
                {'type': 'examen', 'problem_id': 'gauss_seidel_1'} # Coincide con el problema en [cite: 9, 10, 11]
            ],
            "Nivel 2: Jacobi": [
                {'type': 'explicativa', 'content': 'Método iterativo similar a Gauss-Seidel, pero no usa los valores nuevos en la misma iteración[cite: 7].'},
                {'type': 'examen', 'problem_id': 'jacobi_1'} # Coincide con el problema en [cite: 94, 95, 96]
            ],
            "Nivel 3: Montante": [
                {'type': 'explicativa', 'content': 'Método de pivoteo para resolver sistemas de ecuaciones[cite: 3]. (Teoría no incluida en PDF).'},
                {'type': 'examen', 'problem_id': 'montante_1'}
            ],
            "Nivel 4: Gauss-Jordan": [
                {'type': 'explicativa', 'content': 'Método de eliminación para encontrar la matriz inversa o resolver sistemas[cite: 4]. (Teoría no incluida en PDF).'},
                {'type': 'examen', 'problem_id': 'gauss_jordan_1'}
            ],
            "Nivel 5: Eliminación Gaussiana": [
                {'type': 'explicativa', 'content': 'Método de eliminación para convertir la matriz en triangular superior[cite: 5]. (Teoría no incluida en PDF).'},
                {'type': 'examen', 'problem_id': 'gaussian_elim_1'}
            ],
        }
    },
    "Capítulo 4: Integración Numérica": {
        "levels": {
            "Nivel 1: Regla Trapezoidal": [
                {'type': 'explicativa', 'content': 'Integra un polinomio de primer grado[cite: 976]. Fórmula: I = h/2 * [f(a) + 2Σ... + f(b)] [cite: 979]'},
                {'type': 'examen', 'problem_id': 'trapezoidal_1'} # Coincide con el problema en [cite: 987]
            ],
            "Nivel 2: Regla de 1/3 Simpson": [
                {'type': 'explicativa', 'content': 'Integra un polinomio de 2do grado [cite: 926]. n debe ser par[cite: 928, 933]. Fórmula: I = h/3 * [f(a) + 4Σ(impar) + 2Σ(par) + f(b)] [cite: 929]'},
                {'type': 'examen', 'problem_id': 'simpson_1_3_1'} # Coincide con el problema en [cite: 934]
            ],
            "Nivel 3: Regla de 3/8 Simpson": [
                {'type': 'explicativa', 'content': 'Integra un polinomio de 3er grado [cite: 947]. n debe ser múltiplo de 3[cite: 950]. Fórmula: I = 3h/8 * [...] [cite: 951]'},
                {'type': 'examen', 'problem_id': 'simpson_3_8_1'} # Coincide con el problema en [cite: 958]
            ],
            "Nivel 4: Newton-Cotes Cerradas": [
                {'type': 'explicativa', 'content': 'Fórmulas de integración donde el dominio está cerrado por el primer y último dato[cite: 1006]. Fórmula: I = αh * Σ(wi * f(a+ih)) [cite: 968]'},
                {'type': 'examen', 'problem_id': 'cotes_closed_1'} # Coincide con el problema en [cite: 972]
            ],
            "Nivel 5: Newton-Cotes Abiertas": [
                {'type': 'explicativa', 'content': 'Fórmulas de integración que extienden el intervalo [cite: 1009]. h = (b-a)/(n+2) [cite: 1012]'},
                {'type': 'examen', 'problem_id': 'cotes_open_1'} # Coincide con el problema en [cite: 1019]
            ],
        }
    },
    "Capítulo 5: Mínimos Cuadrados": {
        "levels": {
            "Nivel 1: Línea Recta": [
                {'type': 'explicativa', 'content': 'Ajuste a la ecuación g(x) = a0 + a1*x[cite: 1097]. Se resuelve el sistema: n*a0 + Σx*a1 = Σy ... [cite: 1099]'},
                {'type': 'examen', 'problem_id': 'least_sq_linear_1'} # Coincide con el problema en [cite: 1102-1114]
            ],
            "Nivel 2: Cuadrática": [
                {'type': 'explicativa', 'content': 'Ajuste a la ecuación g(x) = a0 + a1*x + a2*x^2[cite: 1058]. Se resuelve el sistema de 3x3... [cite: 1061]'},
                {'type': 'examen', 'problem_id': 'least_sq_quadratic_1'}
            ],
            "Nivel 3: Cúbica": [
                {'type': 'explicativa', 'content': 'Ajuste a la ecuación g(x) = a0 + a1*x + a2*x^2 + a3*x^3[cite: 1063]. Se resuelve el sistema de 4x4... [cite: 1066]'},
                {'type': 'examen', 'problem_id': 'least_sq_cubic_1'}
            ],
            "Nivel 4: Lineal con Función": [
                {'type': 'explicativa', 'content': 'Ajuste a g(x) = a0 + a1*x + a2*f(x) [cite: 1068]. f(x) puede ser e^x, sen(x), etc.[cite: 1069, 1071]. Sistema: ...Σx*f(x)... [cite: 1077-1082]'},
                {'type': 'examen', 'problem_id': 'least_sq_linear_func_1'}
            ],
            "Nivel 5: Cuadrática con Función": [
                {'type': 'explicativa', 'content': 'Ajuste a g(x) = a0 + a1*x + a2*x^2 + a3*f(x)[cite: 1084]. Sistema de 4x4... [cite: 1094]'},
                {'type': 'examen', 'problem_id': 'least_sq_quadratic_func_1'}
            ],
        }
    },
    "Capítulo 6: Ecuaciones Diferenciales Ordinarias (EDO)": {
        "levels": {
            "Nivel 1: Euler (Adelante)": [
                {'type': 'explicativa', 'content': 'Método de punto pendiente[cite: 877]. (Fórmula no provista en PDF).'},
                {'type': 'examen', 'problem_id': 'euler_forward_1'}
            ],
            "Nivel 2: Euler Modificado": [
                {'type': 'explicativa', 'content': 'Más exacto que Euler Adelante[cite: 737]. Fórmula: y_n+1 = y_n + (h/2) * [f(...) + f(...)] [cite: 740]'},
                {'type': 'examen', 'problem_id': 'euler_modified_1'} # Coincide con el problema en [cite: 742]
            ],
            "Nivel 3: Euler (Atrás)": [
                {'type': 'explicativa', 'content': 'Versión del método de Euler[cite: 881]. (Fórmula no provista en PDF).'},
                {'type': 'examen', 'problem_id': 'euler_backward_1'}
            ],
            "Nivel 4: Runge-Kutta 2do Orden": [
                {'type': 'explicativa', 'content': 'Usa dos pasos de iteración [cite: 759]. k1 = h*f(...), k2 = h*f(y_n+k1, ...), y_n+1 = y_n + 1/2(k1+k2) [cite: 760, 761, 762]'},
                {'type': 'examen', 'problem_id': 'rk2_1'} # Coincide con el problema en [cite: 768]
            ],
            "Nivel 5: Runge-Kutta 3er Orden": [
                {'type': 'explicativa', 'content': 'Fórmulas: k1=..., k2=..., k3=... y_n+1 = y_n + 1/6(k1+4k2+k3) [cite: 783]'},
                {'type': 'examen', 'problem_id': 'rk3_1'} # Coincide con el problema en [cite: 785]
            ],
            "Nivel 6: Runge-Kutta 4to Orden (1/3 Simpson)": [
                {'type': 'explicativa', 'content': 'Basado en 1/3 de Simpson[cite: 791]. Fórmulas: k1, k2, k3, k4. y_n+1 = y_n + 1/6(k1+2k2+2k3+k4) [cite: 792-796]'},
                {'type': 'examen', 'problem_id': 'rk4_simpson13_1'} # Coincide con el problema en [cite: 797]
            ],
            "Nivel 7: Runge-Kutta 4to Orden (3/8 Simpson)": [
                {'type': 'explicativa', 'content': 'Basado en 3/8 de Simpson[cite: 817]. Fórmulas: k1, k2, k3, k4. y_n+1 = y_n + 1/8(k1+3k2+3k3+k4) [cite: 818-822]'},
                {'type': 'examen', 'problem_id': 'rk4_simpson38_1'} # Coincide con el problema en [cite: 824]
            ],
            "Nivel 8: Runge-Kutta Orden Superior": [
                {'type': 'explicativa', 'content': 'Se usa para EDOs de orden superior (ej. y\'\')[cite: 827, 874]. Fórmulas: k1=h*Vn, m1=h[...], y_n+1 = ... [cite: 829-834]'},
                {'type': 'examen', 'problem_id': 'rk_higher_order_1'} # Coincide con el problema en [cite: 837]
            ],
        }
    },
}