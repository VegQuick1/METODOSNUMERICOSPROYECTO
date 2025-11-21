"""
GUÍA DE IMPLEMENTACIÓN - Todos los Métodos Numéricos

Este archivo contiene las instrucciones paso a paso para implementar todos los métodos
en el proyecto. El código es modular y puede integrarse incrementalmente.

PASOS:

1. Ya has creado: numerical_methods_lessons.py, methods_mapping.py y additional_methods.py

2. Modificar game_app.py - Agregar al inicio (después de otros imports):

    from numerical_methods_lessons import *
    from methods_mapping import METHODS_MAPPING, get_method_info
    import additional_methods
    
3. En __init__ de NumericalMethodsGame, agregar:
    
    additional_methods.set_app_reference(self)
    # Esto permite que los métodos adicionales accedan a la instancia de la app

4. Modificar start_lesson() para detectar y llamar métodos especiales:

    Reemplazar la sección de "Caso especial: Lagrange" con:
    
    # Caso especial: Métodos con interfaz personalizada
    method_info = get_method_info(chapter, level, difficulty)
    
    if method_info and 'function' in method_info:
        func_name = method_info['function']
        # Para métodos en additional_methods
        if hasattr(additional_methods, func_name):
            func = getattr(additional_methods, func_name)
            func(chapter, level, difficulty, lesson_index)
            return
        # Para métodos en self (como _show_lagrange_*)
        elif hasattr(self, func_name):
            func = getattr(self, func_name)
            func(chapter, level, difficulty, lesson_index)
            return

5. Completar additional_methods.py:
   
   El archivo necesita más funciones. Las incluidas son:
   - show_interpolacion_lineal ✓
   - show_newton_forward ✓
   - show_newton_backward ✓
   - show_newton_divided_diff ✓
   
   Falta agregar (están en MÉTODOS_MAPPING pero no implementadas):
   - show_montante, show_gauss_jordan, show_eliminacion_gaussiana (Ecuaciones Lineales)
   - show_gauss_seidel ✓, show_jacobi ✓ (Ecuaciones Lineales - falta completar)
   - show_bisection ✓, show_falsa_posicion ✓, show_newton_raphson ✓, 
     show_punto_fijo ✓, show_secante ✓ (Ecuaciones No Lineales - stubs creados)
   - show_euler, show_euler_modificado ✓, show_rk2 ✓, show_rk3, show_rk4 ✓ 
     (Ecuaciones Diferenciales - parcialmente)
   - show_trapezoidal ✓, show_simpson_13 ✓, show_simpson_38 ✓,
     show_newton_cotes_cerradas, show_newton_cotes_abiertas (Integración - parcialmente)
   - show_minimos_cuadrados_lineal ✓, show_minimos_cuadrados_cuadratica ✓,
     show_minimos_cuadrados_cubica, show_minimos_cuadrados_lineal_func, 
     show_minimos_cuadrados_cuadratica_func (Mínimos Cuadrados - parcialmente)

DISEÑO DE REFERENCIA - Cada función debe:

1. Recibir: chapter, level, difficulty, lesson_index
2. Verificar si es prueba final y si ya fue completada (usando app_ref.medals)
3. Crear banner_frame con color específico, titulo y botón de retroceso
4. Crear main_frame con problema/tabla/ecuación
5. Agregar temporizador que cuenta hacia atrás
6. Mostrar opciones de respuesta con botones RoundedButton
7. Manejar respuesta correcta/incorrecta
8. Si es final, agregar medalla y guardar progreso

ESTRUCTURA GENERIC PARA CADA MÉTODO:

def show_metodo_nombre(chapter, level, difficulty, lesson_index):
    \"\"\"Descripción del método\"\"\"
    data = METODO_LESSONS[difficulty]  # Obtener datos del diccionario
    _show_generic_exercise(...)         # Llamar función genérica personalizada

NOTAS IMPORTANTES:

- Los temporizadores varían por dificultad:
  * Intermedio: Generalmente 1200s (20 min) o 1500s (25 min)
  * Avanzado: 1200s (20 min) o 1500s (25 min)
  * Prueba Final: 1500s (25 min) o 1800s (30 min)

- Los colores de banner deben ser consistentes y visualmente distintos
- Cada método necesita entre 3-4 opciones de respuesta para Intermedio/Avanzado
- Prueba Final necesita 5 opciones
- Las respuestas correctas están en los diccionarios de numerical_methods_lessons.py

EJECUCIÓN:

1. Ejecutar: python main.py
2. Navegar a un nivel (ej: Capítulo 1 > Nivel 2 Lineal > Intermedio)
3. El sistema debería mostrar el ejercicio personalizado

"""

# RESUMEN DE ARCHIVOS CREADOS:

# 1. numerical_methods_lessons.py - Datos de todos los métodos y ejercicios
# 2. methods_mapping.py - Mapeo de qué función llama cada método
# 3. additional_methods.py - Implementación de funciones de visualización
# 4. Este archivo - Guía de integración

# PRÓXIMOS PASOS:

# 1. Completar additional_methods.py con todas las funciones faltantes
# 2. Modificar game_app.py para importar y usar estos módulos
# 3. Probar cada método individualmente
# 4. Ajustar colores, tiempos y contenido según sea necesario

print(__doc__)
