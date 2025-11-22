
import numpy as np
def solve_lagrange(points, x_to_find):
    n = len(points)
    g_x = 0
    for i in range(n):
        xi, yi = points[i]
        Li = 1
        for j in range(n):
            if i == j:
                continue
            xj, yj = points[j]
            Li *= (x_to_find - xj) / (xi - xj)
        g_x += yi * Li
    return g_x
def solve_linear_interpolation(a, fa, b, fb, x):
    g_x = fa + ((fb - fa) / (b - a)) * (x - a)
    return g_x
def solve_newton_divided_differences(points, x_to_find):
    n = len(points)
    table = np.zeros((n, n))
    for i in range(n):
        table[i][0] = points[i][1] # yi
    for j in range(1, n): # Columnas
        for i in range(n - j): # Filas
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (points[i+j][0] - points[i][0])
    g_x = table[0][0]
    product_term = 1
    for j in range(1, n):
        product_term *= (x_to_find - points[j-1][0]) # (x-x1), luego (x-x1)(x-x2), ...
        g_x += table[0][j] * product_term
    return g_x
def solve_newton_forward(points, x_to_find):
    n = len(points)
    h = points[1][0] - points[0][0] # Asume uniforme
    s = (x_to_find - points[0][0]) / h
    table = np.zeros((n, n))
    for i in range(n):
        table[i][0] = points[i][1] # yi
    for j in range(1, n): # Columnas
        for i in range(n - j): # Filas
            table[i][j] = table[i+1][j-1] - table[i][j-1]
    g_x = table[0][0] # y1 * [s 0] (donde [s 0] = 1)
    s_term = 1
    factorial = 1
    for j in range(1, n):
        s_term *= (s - (j - 1)) # s, luego s(s-1), luego s(s-1)(s-2)
        factorial *= j # 1!, 2!, 3!
        g_x += (table[0][j] * s_term) / factorial
    return g_x
def solve_newton_backward(points, x_to_find):
    n = len(points)
    h = points[1][0] - points[0][0] # Asume uniforme
    s = (x_to_find - points[n-1][0]) / h # 's' es negativo
    table = np.zeros((n, n))
    for i in range(n):
        table[i][0] = points[i][1] # yi
    for j in range(1, n): # Columnas
        for i in range(j, n): # Filas (diferente al de "hacia adelante")
            table[i][j] = table[i][j-1] - table[i-1][j-1]
    g_x = table[n-1][0] # y3 * [s 0] (donde [s 0] = 1)
    s_term = 1
    factorial = 1
    for j in range(1, n):
        s_term *= (s + (j - 1)) # s, luego s(s+1), luego s(s+1)(s+2)
        factorial *= j # 1!, 2!, 3!
        g_x += (table[n-1][j] * s_term) / factorial
    return g_x
def solve_bisection(func, a, b, tolerance):
    pass # Implementar lógica
def solve_false_position(func, a, b, tolerance):
    pass # Implementar lógica
def solve_newton_raphson(func, func_prime, x0, tolerance):
    pass # Implementar lógica
def solve_fixed_point(g_func, x0, tolerance):
    pass # Implementar lógica
def solve_secant(func, x0, x1, tolerance):
    pass # Implementar lógica
def solve_graphical(func, x_range):
    pass # Implementar lógica de ploteo
def solve_gauss_seidel(A, b, tolerance=0.001):
    n = len(b)
    x = np.zeros(n) # x0 = [0, 0, 0]
    x_new = np.copy(x)
    iterations = 0
    max_iterations = 100 # Prevenir bucle infinito
    while iterations < max_iterations:
        x = np.copy(x_new)
        for i in range(n):
            sum_j = 0
            for j in range(n):
                if i != j:
                    sum_j += A[i, j] * x_new[j]
            x_new[i] = (b[i] - sum_j) / A[i, i]
        errors = np.abs(x_new - x)
        if np.all(errors < tolerance):
            break # Solución encontrada
        iterations += 1
    return x_new # Resultado: [3.0, -2.5, 7.0]
def solve_jacobi(A, b, tolerance=0.001):
    n = len(b)
    x = np.ones(n) # x0 = [1, 1, 1]
    x_new = np.copy(x)
    iterations = 0
    max_iterations = 100
    while iterations < max_iterations:
        x = np.copy(x_new)
        for i in range(n):
            sum_j = 0
            for j in range(n):
                if i != j:
                    sum_j += A[i, j] * x[j]
            x_new[i] = (b[i] - sum_j) / A[i, i]
        errors = np.abs(x_new - x)
        if np.all(errors < tolerance):
            break
        iterations += 1
    return x_new
def solve_montante(A, b):
    pass # Implementar lógica
def solve_gauss_jordan(A, b):
    pass # Implementar lógica
def solve_gaussian_elimination(A, b):
    pass # Implementar lógica
def solve_trapezoidal_rule(func, a, b, n):
    h = (b - a) / n #
    I = func(a) + func(b)
    sum_mid = 0
    for i in range(1, n):
        sum_mid += func(a + i * h)
    I = (h / 2) * (I + 2 * sum_mid) #
    return I
def solve_simpson_1_3(func, a, b, n):
    h = (b - a) / n
    sum_odd = 0
    for i in range(1, n, 2): # i = 1, 3, 5...
        sum_odd += func(a + i * h)
    sum_even = 0
    for i in range(2, n, 2): # i = 2, 4, 6...
        sum_even += func(a + i * h)
    I = (h / 3) * (func(a) + 4 * sum_odd + 2 * sum_even + func(b))
    return I
def solve_simpson_3_8(func, a, b, n):
    h = (b - a) / n
    I = func(a) + func(b)
    sum_3 = 0 # Para i = 3, 6, 9...
    sum_others = 0 # Para i = 1, 2, 4, 5, 7...
    for i in range(1, n):
        if i % 3 == 0:
            sum_3 += func(a + i * h)
        else:
            sum_others += func(a + i * h)
    I = (3 * h / 8) * (I + 2 * sum_3 + 3 * sum_others)
    return I
def solve_newton_cotes_closed(func, a, b, n):
    h = (b - a) / n # [cite: 969]
    constants = {
        1: {'alpha': 1/2, 'w': [1, 1]},
        2: {'alpha': 1/3, 'w': [1, 4, 1]}, # (Simpson 1/3)
        3: {'alpha': 3/8, 'w': [1, 3, 3, 1]}, # (Simpson 3/8)
        4: {'alpha': 2/45, 'w': [7, 32, 12, 32, 7]},
    }
    if n not in constants:
        return None # No implementado
    alpha = constants[n]['alpha']
    w = constants[n]['w']
    sum_w = 0
    for i in range(n + 1):
        sum_w += w[i] * func(a + i * h)
    I = alpha * h * sum_w
    return I
def solve_newton_cotes_open(func, a, b, n):
    h = (b - a) / (n + 2)
    constants = {
        2: {'alpha': 4/3, 'w': [0, 2, -1, 2, 0]},
        4: {'alpha': 6/20, 'w': [0, 11, -14, 26, -14, 11, 0]},
    }
    if n not in constants:
        return None # No implementado
    alpha = constants[n]['alpha']
    w = constants[n]['w']
    sum_w = 0
    for i in range(1, n + 2): # De 1 a n+1 (ej: 1 a 5 para n=4)
        sum_w += w[i] * func(a + i * h)
    I = alpha * h * sum_w
    return I
def solve_least_squares_linear(points):
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)
    A = np.array([
        [n, sum_x],
        [sum_x, sum_x2]
    ])
    b = np.array([sum_y, sum_xy])
    a = np.linalg.solve(A, b) # a[0] es a0, a[1] es a1
    return a # [cite: 1172, 1179]
def solve_least_squares_quadratic(points):
    pass # Implementar lógica
def solve_least_squares_cubic(points):
    pass # Implementar lógica
def solve_least_squares_linear_func(points, func):
    pass # Implementar lógica
def solve_least_squares_quadratic_func(points, func):
    pass # Implementar lógica
def solve_euler_forward(func, y0, t0, h, t_end):
    pass # Implementar lógica
def solve_euler_modified(func, y0, t0, h, t_end):
    pass # Implementar lógica
def solve_euler_backward(func, y0, t0, h, t_end):
    pass # Implementar lógica
def solve_rk2(func, y0, t0, h, t_end):
    pass # Implementar lógica
def solve_rk3(func, y0, t0, h, t_end):
    pass # Implementar lógica
def solve_rk4_simpson13(func, y0, t0, h, t_end):
    pass # Implementar lógica
def solve_rk4_simpson38(func, y0, t0, h, t_end):
    pass # Implementar lógica
def solve_rk_higher_order(func, y0, y_prime0, t0, h, t_end):
    pass # Implementar lógica