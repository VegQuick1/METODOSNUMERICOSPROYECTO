import re
with open('game_app.py', 'r', encoding='utf-8') as f:
    content = f.read()
replacements = [
    ('tk.Canvas(', 'tk.Canvas('),
    ('time_canvas = tk.Canvas(row_frame, height=120', 'time_canvas = tk.Canvas(row_frame, height=scale_value(120)'),
    ('error_canvas = tk.Canvas(row_frame, height=120', 'error_canvas = tk.Canvas(row_frame, height=scale_value(120)'),
    ('create_rounded_rect_image(time_canvas.winfo_width() or 150, 120', 'create_rounded_rect_image(time_canvas.winfo_width() or 150, scale_value(120)'),
    ('create_rounded_rect_image(error_canvas.winfo_width() or 150, 120', 'create_rounded_rect_image(error_canvas.winfo_width() or 150, scale_value(120)'),
    ('banner_h = 120', 'banner_h = scale_value(120)'),
    ('banner_h = 80', 'banner_h = scale_value(80)'),
]
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
with open('game_app.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Tamaños escalados exitosamente')
