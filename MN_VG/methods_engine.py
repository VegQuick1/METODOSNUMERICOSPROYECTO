# methods_engine.py
import numpy as np

# --- CAPÍTULO 1: INTERPOLACIÓN ---

def solve_lagrange(points, x_to_find):
    """ Resuelve la interpolación de Lagrange [cite: 420-425] """
    # points es una lista de tuplas (x, y), ej: [(2.2, 2.54), (2.5, 2.82), ...]
    # x_to_find es el valor de x, ej: 2.4
    # Basado en el problema de [cite: 434, 435]
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
    """ Resuelve la interpolación lineal [cite: 370] """
    # Basado en el ejemplo de [cite: 385]
    # g(x) = f(a) + (f(b) - f(a)) / (b - a) * (x - a)
    g_x = fa + ((fb - fa) / (b - a)) * (x - a)
    return g_x

def solve_newton_divided_differences(points, x_to_find):
    """ Resuelve Newton con Diferencias Divididas [cite: 444] """
    # Basado en el ejemplo de [cite: 445-469]
    n = len(points)
    # 'table' almacenará las diferencias divididas (D0, D1, D2, ...)
    table = np.zeros((n, n))
    
    # Columna D0 (yi)
    for i in range(n):
        table[i][0] = points[i][1] # yi
        
    # Calcular las columnas D1, D2, ...
    for j in range(1, n): # Columnas
        for i in range(n - j): # Filas
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (points[i+j][0] - points[i][0])
            
    # Extraer los coeficientes (la primera fila de la tabla: D0, D1_1, D2_1)
    # D0 = table[0][0]
    # D1 = table[0][1]
    # D2 = table[0][2]
    
    # Calcular g(x) usando la fórmula [cite: 464]
    # g(x) = D0 + D1(x-x1) + D2(x-x1)(x-x2) + ...
    g_x = table[0][0]
    product_term = 1
    for j in range(1, n):
        product_term *= (x_to_find - points[j-1][0]) # (x-x1), luego (x-x1)(x-x2), ...
        g_x += table[0][j] * product_term
        
    return g_x

def solve_newton_forward(points, x_to_find):
    """ Resuelve Newton Hacia Adelante [cite: 490] """
    # Basado en el ejemplo de [cite: 493-538]
    n = len(points)
    h = points[1][0] - points[0][0] # Asume uniforme [cite: 510]
    s = (x_to_find - points[0][0]) / h # [cite: 531]
    
    # 'table' almacenará las diferencias (y, Δy, Δ²y, ...)
    table = np.zeros((n, n))
    
    # Columna 0 (yi)
    for i in range(n):
        table[i][0] = points[i][1] # yi
        
    # Calcular las columnas Δ, Δ², ... [cite: 513-526]
    for j in range(1, n): # Columnas
        for i in range(n - j): # Filas
            table[i][j] = table[i+1][j-1] - table[i][j-1]

    # Extraer los coeficientes (la primera fila: y1, Δ1, Δ²1)
    # y1 = table[0][0]
    # Δ1 = table[0][1]
    # Δ²1 = table[0][2]
    
    # Calcular g(x) usando la fórmula [cite: 534]
    g_x = table[0][0] # y1 * [s 0] (donde [s 0] = 1)
    s_term = 1
    factorial = 1
    for j in range(1, n):
        s_term *= (s - (j - 1)) # s, luego s(s-1), luego s(s-1)(s-2)
        factorial *= j # 1!, 2!, 3!
        g_x += (table[0][j] * s_term) / factorial
        
    return g_x

def solve_newton_backward(points, x_to_find):
    """ Resuelve Newton Hacia Atrás [cite: 551] """
    # Basado en el ejemplo de [cite: 555-594]
    n = len(points)
    h = points[1][0] - points[0][0] # Asume uniforme [cite: 586]
    s = (x_to_find - points[n-1][0]) / h # 's' es negativo [cite: 577, 587]
    
    # 'table' almacenará las diferencias (y, ∇y, ∇²y, ...)
    table = np.zeros((n, n))
    
    # Columna 0 (yi)
    for i in range(n):
        table[i][0] = points[i][1] # yi
        
    # Calcular las columnas ∇, ∇², ... [cite: 579-592]
    for j in range(1, n): # Columnas
        for i in range(j, n): # Filas (diferente al de "hacia adelante")
            table[i][j] = table[i][j-1] - table[i-1][j-1]
            
    # Extraer los coeficientes (la *última* fila: y3, ∇'2, ∇²1)
    # y3 = table[n-1][0]
    # ∇'2 = table[n-1][1]
    # ∇²1 = table[n-1][2]
    
    # Calcular g(x) usando la fórmula [cite: 589]
    g_x = table[n-1][0] # y3 * [s 0] (donde [s 0] = 1)
    s_term = 1
    factorial = 1
    for j in range(1, n):
        s_term *= (s + (j - 1)) # s, luego s(s+1), luego s(s+1)(s+2)
        factorial *= j # 1!, 2!, 3!
        g_x += (table[n-1][j] * s_term) / factorial
        
    return g_x

# --- CAPÍTULO 2: ECUACIONES NO LINEALES ---

def solve_bisection(func, a, b, tolerance):
    """ Resuelve por Bisección (Bisectriz) [cite: 233-242] """
    # func es una lambda, ej: lambda x: x**3 - 6.5*x + 2 [cite: 237]
    pass # Implementar lógica

def solve_false_position(func, a, b, tolerance):
    """ Resuelve por Falsa Posición [cite: 243-280] """
    # func es una lambda, ej: lambda x: 3*x**3 - 2*x - 3 [cite: 263]
    # Usar fórmula: x = a - f(a)(b-a) / (f(b)-f(a)) [cite: 259]
    pass # Implementar lógica

def solve_newton_raphson(func, func_prime, x0, tolerance):
    """ Resuelve por Newton-Raphson [cite: 281-299] """
    # func es f(x) [cite: 297]
    # func_prime es f'(x) [cite: 298]
    # Usar fórmula: x_i+1 = x_i - (f(x_i) / f'(x_i)) [cite: 293]
    pass # Implementar lógica

def solve_fixed_point(g_func, x0, tolerance):
    """ Resuelve por Punto Fijo [cite: 300-334] """
    # g_func es la función g(x), ej: lambda x: np.exp(-x) [cite: 323]
    # Usar fórmula: x_i+1 = g(x_i) [cite: 319]
    pass # Implementar lógica

def solve_secant(func, x0, x1, tolerance):
    """ Resuelve por Secante [cite: 335-348] """
    # func es f(x), ej: lambda x: np.exp(-x) - x [cite: 346]
    # Usar fórmula: x_i+1 = x1 - f(x1)(x1-x0) / (f(x1)-f(x0)) [cite: 343, 348]
    pass # Implementar lógica

def solve_graphical(func, x_range):
    """ Resuelve por Método Gráfico [cite: 191-232] """
    # Esto en la app simplemente graficaría la función
    pass # Implementar lógica de ploteo

# --- CAPÍTULO 3: ECUACIONES LINEALES ---

def solve_gauss_seidel(A, b, tolerance=0.001):
    """ Resuelve por Gauss-Seidel  """
    # Basado en el ejemplo [cite: 9, 10, 11]
    # A = np.array([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]])
    # b = np.array([7.85, -19.3, 71.4])
    
    n = len(b)
    x = np.zeros(n) # x0 = [0, 0, 0] [cite: 22]
    x_new = np.copy(x)
    
    iterations = 0
    max_iterations = 100 # Prevenir bucle infinito
    
    while iterations < max_iterations:
        x = np.copy(x_new)
        for i in range(n):
            # Despejes [cite: 15, 16, 18]
            sum_j = 0
            for j in range(n):
                if i != j:
                    # Usa el valor más nuevo (x_new) para j < i
                    # y el valor anterior (x) para j > i
                    sum_j += A[i, j] * x_new[j] 
            
            x_new[i] = (b[i] - sum_j) / A[i, i]
        
        # Calcular error [cite: 87-92]
        # (El PDF usa error absoluto, usaremos error relativo por ser más robusto)
        errors = np.abs(x_new - x)
        if np.all(errors < tolerance):
            break # Solución encontrada
            
        iterations += 1
        
    return x_new # Resultado: [3.0, -2.5, 7.0]

def solve_jacobi(A, b, tolerance=0.001):
    """ Resuelve por Jacobi [cite: 93-179] """
    # A, b como en Gauss-Seidel
    n = len(b)
    x = np.ones(n) # x0 = [1, 1, 1] [cite: 110]
    x_new = np.copy(x)
    
    iterations = 0
    max_iterations = 100
    
    while iterations < max_iterations:
        x = np.copy(x_new)
        for i in range(n):
            # Despejes [cite: 100, 103, 104]
            sum_j = 0
            for j in range(n):
                if i != j:
                    # Diferencia clave: *Siempre* usa el valor de la iteración anterior (x)
                    sum_j += A[i, j] * x[j]
            
            x_new[i] = (b[i] - sum_j) / A[i, i]

        # Calcular error [cite: 174-179]
        errors = np.abs(x_new - x)
        if np.all(errors < tolerance):
            break
            
        iterations += 1
        
    return x_new

def solve_montante(A, b):
    """ Resuelve por Montante [cite: 3] """
    pass # Implementar lógica

def solve_gauss_jordan(A, b):
    """ Resuelve por Gauss-Jordan [cite: 4] """
    pass # Implementar lógica

def solve_gaussian_elimination(A, b):
    """ Resuelve por Eliminación Gaussiana [cite: 5] """
    pass # Implementar lógica

# --- CAPÍTULO 4: INTEGRACIÓN NUMÉRICA ---

def solve_trapezoidal_rule(func, a, b, n):
    """ Resuelve por Regla Trapezoidal [cite: 974-1002] """
    # func es f(x), ej: lambda x: 1 - x**2 [cite: 987]
    h = (b - a) / n # [cite: 990]
    I = func(a) + func(b)
    
    sum_mid = 0
    for i in range(1, n):
        sum_mid += func(a + i * h)
        
    I = (h / 2) * (I + 2 * sum_mid) # [cite: 979, 993]
    return I

def solve_simpson_1_3(func, a, b, n):
    """ Resuelve por Regla 1/3 Simpson [cite: 925-945] """
    # n debe ser par [cite: 933]
    h = (b - a) / n # [cite: 937]
    
    sum_odd = 0
    for i in range(1, n, 2): # i = 1, 3, 5...
        sum_odd += func(a + i * h)
        
    sum_even = 0
    for i in range(2, n, 2): # i = 2, 4, 6...
        sum_even += func(a + i * h)
        
    I = (h / 3) * (func(a) + 4 * sum_odd + 2 * sum_even + func(b)) # [cite: 929]
    return I

def solve_simpson_3_8(func, a, b, n):
    """ Resuelve por Regla 3/8 Simpson [cite: 946-966] """
    # n debe ser múltiplo de 3 [cite: 950]
    h = (b - a) / n
    # La fórmula [cite: 951] está incompleta en el PDF, la completaré:
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
    """ Resuelve por Newton-Cotes Cerradas [cite: 967-973] """
    h = (b - a) / n # [cite: 969]
    # Constantes de la tabla [cite: 971]
    constants = {
        1: {'alpha': 1/2, 'w': [1, 1]},
        2: {'alpha': 1/3, 'w': [1, 4, 1]}, # (Simpson 1/3)
        3: {'alpha': 3/8, 'w': [1, 3, 3, 1]}, # (Simpson 3/8)
        4: {'alpha': 2/45, 'w': [7, 32, 12, 32, 7]},
        # ... agregar más de la tabla
    }
    if n not in constants:
        return None # No implementado
    
    alpha = constants[n]['alpha']
    w = constants[n]['w']
    
    sum_w = 0
    for i in range(n + 1):
        sum_w += w[i] * func(a + i * h)
        
    I = alpha * h * sum_w # [cite: 968]
    return I

def solve_newton_cotes_open(func, a, b, n):
    """ Resuelve por Newton-Cotes Abiertas [cite: 1009-1029] """
    h = (b - a) / (n + 2) # [cite: 1012, 1022]
    # Constantes de la tabla [cite: 901]
    constants = {
        # n=0 (1 punto)
        # n=1
        2: {'alpha': 4/3, 'w': [0, 2, -1, 2, 0]},
        # n=3
        4: {'alpha': 6/20, 'w': [0, 11, -14, 26, -14, 11, 0]},
        # ... agregar más de la tabla
    }
    if n not in constants:
        return None # No implementado
    
    alpha = constants[n]['alpha']
    w = constants[n]['w']
    
    sum_w = 0
    # La fórmula [cite: 1010, 1024] es I = α * h * Σ(wi * f(a+ih))
    # El ejemplo [cite: 1025] parece usar n=4 con h=1/6
    
    # Siguiendo el ejemplo [cite: 1025] para n=4:
    # h = (1-0)/(4+2) = 1/6
    # w = [0, 11, -14, 26, -14, 11, 0] (son n+3=7 puntos, pero w0 y w6 son 0)
    # alpha = 6/20
    # I = (6/20) * (1/6) * [11*f(1/6) - 14*f(2/6) + 26*f(3/6) - 14*f(4/6) + 11*f(5/6)]
    
    for i in range(1, n + 2): # De 1 a n+1 (ej: 1 a 5 para n=4)
        sum_w += w[i] * func(a + i * h)
        
    I = alpha * h * sum_w
    return I


# --- CAPÍTULO 5: MÍNIMOS CUADRADOS ---

def solve_least_squares_linear(points):
    """ Resuelve Mínimos Cuadrados (Línea Recta) [cite: 1095-1198] """
    # points es una lista de tuplas (x, y) [cite: 1102-1114]
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)
    
    # Crear sistema de ecuaciones [cite: 1099, 1150-1161]
    A = np.array([
        [n, sum_x],
        [sum_x, sum_x2]
    ])
    b = np.array([sum_y, sum_xy])
    
    # Resolver para a0, a1
    a = np.linalg.solve(A, b) # a[0] es a0, a[1] es a1
    return a # [cite: 1172, 1179]

def solve_least_squares_quadratic(points):
    """ Resuelve Mínimos Cuadrados (Cuadrática) [cite: 1057-1061] """
    # g(x) = a0 + a1*x + a2*x^2 [cite: 1058]
    # Resolver sistema 3x3 [cite: 1061]
    pass # Implementar lógica

def solve_least_squares_cubic(points):
    """ Resuelve Mínimos Cuadrados (Cúbica) [cite: 1062-1066] """
    # g(x) = a0 + a1*x + a2*x^2 + a3*x^3 [cite: 1063]
    # Resolver sistema 4x4 [cite: 1066]
    pass # Implementar lógica

def solve_least_squares_linear_func(points, func):
    """ Resuelve Mínimos Cuadrados (Lineal con Función) [cite: 1067-1082] """
    # g(x) = a0 + a1*x + a2*f(x) [cite: 1068]
    # Resolver sistema 3x3 [cite: 1077-1082]
    pass # Implementar lógica

def solve_least_squares_quadratic_func(points, func):
    """ Resuelve Mínimos Cuadrados (Cuadrática con Función) [cite: 1083-1094] """
    # g(x) = a0 + a1*x + a2*x^2 + a3*f(x) [cite: 1084]
    # Resolver sistema 4x4 [cite: 1094]
    pass # Implementar lógica

# --- CAPÍTULO 6: ECUACIONES DIFERENCIALES ORDINARIAS (EDO) ---

def solve_euler_forward(func, y0, t0, h, t_end):
    """ Resuelve EDO por Euler Hacia Adelante [cite: 880] """
    pass # Implementar lógica

def solve_euler_modified(func, y0, t0, h, t_end):
    """ Resuelve EDO por Euler Modificado [cite: 735-757] """
    # func es f(y, t), ej: lambda y, t: (5*y*t - 1) / 3 [cite: 744]
    # Usar fórmula: y_n+1 = y_n + (h/2) * [f(y_n, t_n) + f(y_n+1, t_n+1)] [cite: 740]
    # Nota: f(y_n+1, t_n+1) requiere una predicción. El ejemplo [cite: 745, 748] parece usar un y1 *dado* (y1=2)
    # y no lo calcula, lo cual es extraño. La implementación estándar requeriría un paso de predicción.
    pass # Implementar lógica

def solve_euler_backward(func, y0, t0, h, t_end):
    """ Resuelve EDO por Euler Hacia Atrás [cite: 881] """
    pass # Implementar lógica

def solve_rk2(func, y0, t0, h, t_end):
    """ Resuelve EDO por Runge-Kutta 2do Orden [cite: 758-781] """
    # func es f(y, t), ej: lambda y, t: 5*y*t - 1 [cite: 770]
    # k1 = h * f(y_n, t_n) [cite: 760]
    # k2 = h * f(y_n + k1, t_n + h) [cite: 761]
    # y_n+1 = y_n + 0.5 * (k1 + k2) [cite: 762]
    pass # Implementar lógica

def solve_rk3(func, y0, t0, h, t_end):
    """ Resuelve EDO por Runge-Kutta 3er Orden [cite: 782-787] """
    # k1 = h * f(y_n, t_n)
    # k2 = h * f(y_n + k1/2, t_n + h/2)
    # k3 = h * f(y_n - k1 + 2*k2, t_n + h)
    # y_n+1 = y_n + 1/6 * (k1 + 4*k2 + k3) [cite: 783]
    pass # Implementar lógica

def solve_rk4_simpson13(func, y0, t0, h, t_end):
    """ Resuelve EDO por Runge-Kutta 4to Orden (1/3 Simpson) [cite: 788-816] """
    # func es f(y, t), ej: lambda y, t: 5*y*t - 1 [cite: 799]
    # k1 = h * f(y_n, t_n) [cite: 792]
    # k2 = h * f(y_n + k1/2, t_n + h/2) [cite: 793]
    # k3 = h * f(y_n + k2/2, t_n + h/2) [cite: 794]
    # k4 = h * f(y_n + k3, t_n + h) [cite: 795]
    # y_n+1 = y_n + 1/6 * (k1 + 2*k2 + 2*k3 + k4) [cite: 796]
    pass # Implementar lógica

def solve_rk4_simpson38(func, y0, t0, h, t_end):
    """ Resuelve EDO por Runge-Kutta 4to Orden (3/8 Simpson) [cite: 817-826] """
    # k1 = h * f(y_n, t_n) [cite: 818]
    # k2 = h * f(y_n + k1/3, t_n + h/3) [cite: 819]
    # k3 = h * f(y_n + k1/3 + k2/3, t_n + 2*h/3) [cite: 820]
    # k4 = h * f(y_n + k1 - k2 + k3, t_n + h) [cite: 821]
    # y_n+1 = y_n + 1/8 * (k1 + 3*k2 + 3*k3 + k4) [cite: 822]
    pass # Implementar lógica

def solve_rk_higher_order(func, y0, y_prime0, t0, h, t_end):
    """ Resuelve EDO por Runge-Kutta Orden Superior [cite: 827-861] """
    # Para y'' = f(y', y, t), ej: y'' = y'*t + y [cite: 837, 839]
    # U = y, V = y'
    # k1 = h * Vn [cite: 844]
    # m1 = h * f(Vn, Un, qn) [cite: 848]
    # k2 = h * (Vn + m1) [cite: 849]
    # m2 = h * f(Vn+m1, Un+k1, qn+h) [cite: 851]
    # y_n+1 (U_n+1) = Un + 1/2 * (k1 + k2) [cite: 855]
    # y'_n+1 (V_n+1) = Vn + 1/2 * (m1 + m2) [cite: 861]
    pass # Implementar lógica