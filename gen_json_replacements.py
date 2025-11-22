import re
import json

with open('game_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = []

# Parse content to find all problem definitions
pattern = r"    '([a-z_0-9]+)': \{([^}]*)\},"

for match in re.finditer(pattern, content, re.DOTALL):
    prob_id = match.group(1)
    prob_content = match.group(2)
    old_str = match.group(0)
    
    new_str = old_str
    changed = False
    
    # Logic for what to change
    if 'facil' in prob_id or 'intermedio' in prob_id or 'avanzado' in prob_id or prob_id.endswith('_1'):
        
        # Determine expected time
        expected_time = None
        if 'intermedio' in prob_id:
            expected_time = 25
        elif 'avanzado' in prob_id:
            expected_time = 30
        elif '_1' in prob_id and 'facil' not in prob_id and 'intermedio' not in prob_id and 'avanzado' not in prob_id:
            expected_time = 25
        
        if expected_time is not None:
            # Check if time_minutes exists
            if "'time_minutes':" in prob_content:
                # Change existing time
                time_match = re.search(r"'time_minutes':\s*(\d+)", prob_content)
                if time_match:
                    old_time = int(time_match.group(1))
                    if old_time != expected_time:
                        old_str_part = f"'time_minutes': {old_time}"
                        new_str_part = f"'time_minutes': {expected_time}"
                        new_str = new_str.replace(old_str_part, new_str_part)
                        changed = True
            else:
                # Add time_minutes before 'correct'
                if "'correct':" in prob_content:
                    new_str = new_str.replace(
                        "'correct':",
                        f"'time_minutes': {expected_time},\n        'correct':"
                    )
                    changed = True
    
    if changed:
        # Ensure we have at least 3 lines of context for uniqueness
        # Find the 3 lines before in original content
        lines_before = old_str.split('\n')[-3:]  # Get last 3 lines for uniqueness
        
        replacements.append({
            'old_string': old_str,
            'new_string': new_str,
            'prob_id': prob_id,
            'action': 'ADD' if "'time_minutes':" not in prob_content else 'CHANGE'
        })

print(f"Total replacements to generate: {len(replacements)}")

# Write to JSON for later processing
with open('replacements.json', 'w', encoding='utf-8') as f:
    json.dump(replacements, f, indent=2, ensure_ascii=False)

print("Replacements saved to replacements.json")

# Show summary
add_count = sum(1 for r in replacements if r['action'] == 'ADD')
change_count = sum(1 for r in replacements if r['action'] == 'CHANGE')
print(f"  ADD: {add_count}")
print(f"  CHANGE: {change_count}")
