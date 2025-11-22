import re

with open('game_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Strategy: Use regex to find and replace patterns
# This is safer than trying to parse complex nested dicts

# 1. Change all avanzado_1 with time_minutes: 20 to 30
content = re.sub(
    r"('([a-z_]*_avanzado_1': \{[^}]*)'time_minutes': 20)",
    lambda m: m.group(1).replace("'time_minutes': 20", "'time_minutes': 30"),
    content,
    flags=re.DOTALL
)

# 2. Change all _1 (Prueba Final) with wrong time to 25
# This is tricky - we need to match _1 but not _intermedio_1 or _avanzado_1
def fix_final_times(match):
    content = match.group(1)
    # Replace time_minutes with 25
    content = re.sub(r"'time_minutes':\s*\d+", "'time_minutes': 25", content)
    return "    '" + match.group(2) + "': {" + content + "},"

pattern = r"    '([a-z_]*?)_1': \{((?(?!intermedio|avanzado)[^}])*)\},"
content = re.sub(
    pattern,
    fix_final_times,
    content,
    flags=re.DOTALL
)

# 3. Add time_minutes: 25 to all intermedio without time
content = re.sub(
    r"('([a-z_]*_intermedio_1': \{[^}]*)'correct':)",
    lambda m: m.group(1).replace("'correct':", "'time_minutes': 25,\n        'correct':"),
    content,
    flags=re.DOTALL
)

# Write back
with open('game_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ File updated successfully")

# Verify
import json
with open('replacements.json') as f:
    expected = json.load(f)
    
print(f"Applied changes for {len(expected)} problems")
