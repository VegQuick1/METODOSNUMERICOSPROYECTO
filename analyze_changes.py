import re

with open('game_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Strategy: Process line by line looking for pattern markers

lines = content.split('\n')
changes = []

i = 0
while i < len(lines):
    line = lines[i]
    
    # Find problem IDs
    if "': {" in line and line.strip().startswith("'"):
        prob_id = line.split("'")[1]
        
        # Look ahead to find time_minutes or end of dict
        j = i + 1
        dict_content = [line]
        while j < len(lines) and not lines[j].strip().startswith("}"):
            dict_content.append(lines[j])
            j += 1
        dict_content.append(lines[j])  # add the closing brace
        dict_str = '\n'.join(dict_content)
        
        # Determine what needs to change
        if 'intermedio' in prob_id:
            if "'time_minutes':" not in dict_str:
                # Need to add time_minutes: 25
                changes.append((prob_id, 'ADD', 25))
            elif "'time_minutes': 25" not in dict_str:
                # Need to change to 25
                changes.append((prob_id, 'CHANGE', 25))
        
        elif 'avanzado' in prob_id:
            if "'time_minutes': 20" in dict_str:
                changes.append((prob_id, 'CHANGE', 30))
            elif "'time_minutes':" not in dict_str:
                changes.append((prob_id, 'ADD', 30))
        
        elif '_1' in prob_id and 'final' not in prob_id.lower():
            # Prueba Final problems
            if "'time_minutes':" not in dict_str:
                changes.append((prob_id, 'ADD', 25))
            else:
                time_match = re.search(r"'time_minutes':\s*(\d+)", dict_str)
                if time_match:
                    current_time = int(time_match.group(1))
                    if current_time != 25:
                        changes.append((prob_id, 'CHANGE', 25))
        
        i = j + 1
    else:
        i += 1

print(f"Total changes needed: {len(changes)}\n")
for prob_id, action, time_val in sorted(changes):
    print(f"{prob_id}: {action} {time_val}")
