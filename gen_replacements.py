import re

with open('game_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = []

# 1. Cambiar todos los avanzado_1 de 20 a 30
avanzado_pattern = r"('([a-z_]*_avanzado_1': \{[^}]*)'time_minutes': 20"
matches = re.finditer(avanzado_pattern, content, re.DOTALL)

for match in matches:
    old = match.group(0)
    new = match.group(1) + "'time_minutes': 30"
    replacements.append({
        'old': old,
        'new': new,
        'type': 'avanzado_change_30'
    })

# 2. Cambiar Prueba Final (pattern like "problem_1" pero no "intermedio_1" ni "avanzado_1")
# Buscar problemas que terminen en "_1" sin intermedio ni avanzado
final_pattern = r"('([a-z_]+?)_1': \{[^}]*)'time_minutes': (?:20|30|35)"
for match in re.finditer(final_pattern, content, re.DOTALL):
    prob_name = match.group(2)
    # Skip if it's intermedio or avanzado
    if 'intermedio' not in prob_name and 'avanzado' not in prob_name:
        old = match.group(0)
        time_val = old.split("'time_minutes': ")[1]
        if time_val != '25':
            new = old.replace(f"'time_minutes': {time_val}", "'time_minutes': 25")
            replacements.append({
                'old': old,
                'new': new,
                'type': 'final_change_25'
            })

# 3. Agregar 'time_minutes': 25 a intermedio sin tiempo
intermedio_no_time_pattern = r"('([a-z_]*?)_intermedio_1': \{[^}]*)'correct':"

for match in re.finditer(intermedio_no_time_pattern, content, re.DOTALL):
    # Check if there's already a time_minutes
    snippet = match.group(0)
    if "'time_minutes':" not in snippet:
        old = match.group(0)
        # Insert before 'correct'
        new = old.replace("'correct':", "'time_minutes': 25,\n        'correct':")
        replacements.append({
            'old': old,
            'new': new,
            'type': 'intermedio_add_25'
        })

print(f"Total replacements needed: {len(replacements)}")
print("\nGrouped by type:")
from collections import Counter
types = Counter([r['type'] for r in replacements])
for t, count in types.items():
    print(f"  {t}: {count}")

# Show a few examples
print("\n=== EXAMPLES ===")
for i, r in enumerate(replacements[:3]):
    print(f"\nReplacement {i+1} ({r['type']}):")
    print(f"OLD: {r['old'][:100]}...")
    print(f"NEW: {r['new'][:100]}...")
