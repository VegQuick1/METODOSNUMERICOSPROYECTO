import re

with open('game_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by problem ID definition
problems = {}
current_id = None
current_content = ""

for line in content.split('\n'):
    if line.strip().startswith("'") and "': {" in line:
        if current_id:
            problems[current_id] = current_content
        current_id = line.strip().split("'")[1]
        current_content = line + "\n"
    elif current_id:
        current_content += line + "\n"

# Check times
for prob_id, content in sorted(problems.items()):
    if 'time_minutes' in content:
        time_match = re.search(r"'time_minutes':\s*(\d+)", content)
        if time_match:
            time_val = int(time_match.group(1))
            # Determine expected time
            expected = None
            if 'intermedio' in prob_id:
                expected = 25
            elif 'avanzado' in prob_id:
                expected = 30
            elif 'final' in prob_id or 'Prueba' in content:
                expected = 25
            
            if expected and time_val != expected:
                print(f"{prob_id}: {time_val} (expected {expected}) ❌")
    else:
        # Check if it should have time_minutes
        if 'intermedio' in prob_id or 'avanzado' in prob_id or 'final' in prob_id:
            print(f"{prob_id}: NO TIME SET ❌")
