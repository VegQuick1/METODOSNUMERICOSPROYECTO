# GUÍA DE PRUEBA - Métodos Numéricos Implementados

## Estado Actual de Implementación

### ✅ COMPLETAMENTE IMPLEMENTADOS

**Capítulo 1: Interpolación**
- Nivel 1: Lagrange (Intermedio, Avanzado, Prueba Final) ✓
- Nivel 2: Interpolación Lineal (Intermedio, Avanzado, Prueba Final) ✓
- Nivel 3: Newton Diferencias Divididas (Intermedio, Avanzado, Prueba Final) ✓
- Nivel 4: Newton Hacia Adelante (Intermedio, Avanzado, Prueba Final) ✓
- Nivel 5: Newton Hacia Atrás (Intermedio, Avanzado, Prueba Final) ✓

### 🔷 COMO PLACEHOLDERS (Muestran mensajes "Próximamente")

**Capítulo 2: Ecuaciones Lineales**
- Montante
- Gauss-Jordán
- Eliminación Gaussiana
- Gauss-Seidel
- Jacobi

**Capítulo 3: Ecuaciones No Lineales**
- Bisección
- Falsa Posición
- Newton-Raphson
- Punto Fijo
- Secante

**Capítulo 4: Ecuaciones Diferenciales Ordinarias**
- Euler
- Euler Modificado
- Runge-Kutta 2º Orden
- Runge-Kutta 3er Orden
- Runge-Kutta 4º Orden

**Capítulo 5: Integración Numérica**
- Regla Trapezoidal
- Simpson 1/3
- Simpson 3/8
- Newton-Cotes Cerradas
- Newton-Cotes Abiertas

**Capítulo 6: Mínimos Cuadrados**
- Línea Recta
- Parábola (Cuadrática)
- Cúbica
- Lineal con Función
- Cuadrática con Función

## INSTRUCCIONES DE PRUEBA

### 1. Iniciar la Aplicación

```bash
cd d:\DESCARGAS\MN\METODOSNUMERICOSPROYECTO
python main.py
```

### 2. Probar Métodos de Interpolación Completamente Implementados

1. Click en "Continuar como Jugador 1"
2. Click en un capítulo (ej: "Capítulo 1: Interpolación")
3. Click en "Nivel 2: Lineal" (nuevo método)
4. Seleccionar dificultad: "Intermedio"
5. Debería aparecer:
   - Barra superior rosa (#FFB6C1) con "Interpolación Lineal. Intermedio"
   - Tabla de datos x, y
   - Valor x a encontrar
   - Temporizador
   - 4 opciones de respuesta

**Pruebas Recomendadas:**
- Nivel 2: Lineal (todos los niveles de dificultad)
- Nivel 3: Newton Diferencias Divididas (todos)
- Nivel 4: Newton Hacia Adelante (todos)
- Nivel 5: Newton Hacia Atrás (todos)
- Nivel 1: Lagrange (verificar que sigue funcionando)

### 3. Probar Otros Métodos (Placeholders)

Cuando selecciones cualquier otro método (Capítulos 2-6):
- Mostrará un diálogo: "Próximamente - [Método] será implementado próximamente"
- Al cerrar el diálogo, regresa al menú de dificultad
- **Esto es correcto para esta versión**

### 4. Verificar Funcionalidades

**Correcta respuesta:**
- Diálogo: "¡Correcto! ¡Excelente!"
- Avanza a siguiente problema
- Si es Prueba Final, obtiene medalla

**Respuesta incorrecta:**
- Diálogo: "Incorrecto - Lo siento, esa respuesta no es correcta."
- Incrementa contador de errores
- Regresa al menú de dificultad
- Si es Prueba Final, no permite reintentar

**Tiempo agotado:**
- Diálogo: "Tiempo agotado - Se acabó el tiempo para resolver el problema."
- Regresa al menú de dificultad

### 5. Verificar Otros Elementos

**Botón de Retroceso:**
- Click en flecha "◀" en barra superior
- Debe regresar a menú de dificultad
- Si no hay imagen, mostrará "◀" texto

**Temporizadores:**
- Intermedio: 20 minutos (1200 segundos)
- Avanzado: 20 minutos (1200 segundos)
- Prueba Final: 25-30 minutos según el método

**Medallas (Prueba Final):**
- Completar exitosamente una Prueba Final
- Verificar en "Mi Perfil" - Debería mostrarse la medalla
- Intentar entrar nuevamente a la misma Prueba Final
- Debe mostrar: "Ya completaste esta Prueba Final."

## DATOS DE PRUEBA - RESPUESTAS CORRECTAS

### Interpolación Lineal (Nivel 2)
- **Intermedio:** g(x) = 0.998577424
- **Avanzado:** g(x) = 0.916291
- **Final:** g(x) = 1.242366

### Newton Hacia Adelante (Nivel 4)
- **Intermedio:** g(x) = 1.029183673
- **Avanzado:** g(x) = 1.001234
- **Final:** g(x) = 1.045678

### Newton Hacia Atrás (Nivel 5)
- **Intermedio:** g(x) = 1.029183673
- **Avanzado:** g(x) = 1.670000
- **Final:** g(x) = 1.820000

### Newton Diferencias Divididas (Nivel 3)
- **Intermedio:** g(x) = -0.657813
- **Avanzado:** g(x) = 0.945123
- **Final:** g(x) = 1.265234

## ARCHIVOS CREADOS

```
d:\DESCARGAS\MN\METODOSNUMERICOSPROYECTO\
├── numerical_methods_lessons.py    [Datos de todos los métodos]
├── methods_mapping.py              [Mapeo de métodos a funciones]
├── additional_methods.py            [Implementación de visualización]
├── IMPLEMENTATION_GUIDE.md         [Guía de integración]
└── TEST_GUIDE.md                   [Este archivo]
```

## PRÓXIMOS PASOS PARA COMPLETAR

Para implementar completamente los métodos faltantes, seguir el patrón:

1. Copiar la estructura de `_show_generic_interpolation_exercise()` 
2. Crear funciones específicas para cada capítulo
3. Actualizar `numerical_methods_lessons.py` con datos correctos
4. Probar cada método individualmente

Ejemplo para Gauss-Seidel:

```python
def show_gauss_seidel(chapter, level, difficulty, lesson_index):
    data = GAUSS_SEIDEL_LESSONS[difficulty]
    _show_linear_system_exercise(chapter, level, difficulty, lesson_index, 
                                  data, "Gauss-Seidel", "#FF6B6B")
```

## NOTAS TÉCNICAS

- Todos los archivos nuevos ya están creados y compilados
- game_app.py ha sido modificado para importar y usar los nuevos módulos
- El sistema detecta automáticamente qué función llamar según el capítulo/nivel
- Los métodos placeholder muestran diálogos informativos

## SOPORTE

Si encuentras errores:
1. Verifica que todos los archivos .py estén en la carpeta correcta
2. Ejecuta: `python -m py_compile archivo.py` para validar sintaxis
3. Revisa la consola (Python Debug Console en VSCode) para mensajes de error
4. Los logs incluyen información de errores en `_load_progress()` y módulo de música

