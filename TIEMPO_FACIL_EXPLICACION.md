# Cómo se aplican los tiempos a los ejercicios Fáciles

## 1. OBTENCIÓN DEL TIEMPO (Línea 868)

```python
def _show_generic_problem(self, problem_id, chapter, level, difficulty, lesson_index):
    # ... código anterior ...
    
    # Línea 868: Se obtiene el tiempo_minutes del diccionario PROBLEM_DATA
    time_min = problem_data.get('time_minutes', 30)
    
    # Línea 869-870: Se crea la etiqueta del temporizador con el tiempo
    timer_label = tk.Label(timer_container, text=f"{time_min}:00", 
                          font=("Arial", scale_font(20), "bold"),
                          bg=COLOR_FONDO, fg=style['timer_color'])
```

**Nota:** 
- `problem_data.get('time_minutes', 30)` obtiene el valor de `time_minutes` de los datos del problema
- Si NO existe la clave `time_minutes`, usa el valor por defecto: **30 minutos**
- **Para problemas Fácil:** Como NO tienen `time_minutes` en `game_data.py`, el temporizador mostraría **30 minutos por defecto**

---

## 2. ACTUALIZACIÓN DEL TEMPORIZADOR (Líneas 872-883)

```python
timer_state = {'seconds': time_min * 60, 'timer_id': None}

def _update_timer():
    timer_state['seconds'] -= 1
    minutes = timer_state['seconds'] // 60
    seconds = timer_state['seconds'] % 60
    time_str = f"{minutes}:{seconds:02d}"
    timer_label.config(text=time_str)
    
    if timer_state['seconds'] > 0:
        timer_state['timer_id'] = self.root.after(1000, _update_timer)
    else:
        messagebox.showinfo("Tiempo agotado", "Se acabó el tiempo para resolver el problema.")
        if is_final:
            self.errors_committed += 1
        self._save_progress()
        self.show_difficulty_menu(chapter, level)

_update_timer()
```

**Proceso:**
1. Se convierte `time_min` (en minutos) a segundos: `time_min * 60`
2. Cada segundo se decrementa el contador
3. Se actualiza la etiqueta visual cada segundo
4. Si se acaba el tiempo → muestra mensaje y vuelve al menú

---

## 3. VALOR POR DEFECTO PARA FÁCIL - ⚠️ PROBLEMA

**LÍNEA 868:**
```python
time_min = problem_data.get('time_minutes', 30)
```

- Cuando un problema **NO tiene** `time_minutes` definido
- El valor por defecto es **30 minutos**
- **Los problemas Fácil NO tienen `time_minutes`** → usan 30 min por defecto ❌

---

## 4. SOLUCIÓN RECOMENDADA

Para que los problemas Fácil **NO tengan límite de tiempo**, hay dos opciones:

### Opción A: Cambiar el valor por defecto
```python
# En lugar de:
time_min = problem_data.get('time_minutes', 30)

# Hacer:
time_min = problem_data.get('time_minutes', None)

# Luego validar:
if time_min is None:
    # No mostrar temporizador para Fácil
    # timer_container.pack_forget()  # Ocultar temporizador
else:
    # Mostrar temporizador con el tiempo especificado
    timer_label.config(text=f"{time_min}:00")
```

### Opción B: Agregar `time_minutes: None` a todos los Fácil
En `game_data.py`, agregar explícitamente a cada problema Fácil:
```python
'bisection_facil_1': {
    'title': '...',
    'options': [...],
    'correct': '...',
    'time_minutes': None  # Explícitamente sin límite
}
```

### Opción C: Validar el nivel de dificultad
```python
if difficulty.lower() == 'fácil':
    time_min = None  # Sin límite para Fácil
else:
    time_min = problem_data.get('time_minutes', 30)
```

---

## 5. RESUMEN

- **Línea 868:** Es donde se obtiene el tiempo de cada problema
- **Valor por defecto:** 30 minutos (para problemas sin `time_minutes`)
- **Problemas Fácil:** No tienen `time_minutes` → usan por defecto 30 min
- **Recomendación:** Modificar la lógica para que Fácil no tenga temporizador
