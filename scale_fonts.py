import re
with open('game_app.py', 'r', encoding='utf-8') as f:
    content = f.read()
pattern = r'font=\("Arial",\s*(\d+)'
def replace_func(match):
    size = match.group(1)
    start = max(0, match.start() - 50)
    context = content[start:match.end() + 50]
    if 'scale_font' in context:
        return match.group(0)
    return f'font=("Arial", scale_font({size})'
content = re.sub(pattern, replace_func, content)
with open('game_app.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fuentes escaladas exitosamente')
