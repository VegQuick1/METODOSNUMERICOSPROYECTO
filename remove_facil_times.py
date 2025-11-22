import re
import json

with open('game_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all facil problems
pattern = r"'([a-z_]*_facil_1)': \{([^}]*)\}"
facil_problems = {}

for match in re.finditer(pattern, content, re.DOTALL):
    prob_id = match.group(1)
    prob_content = match.group(2)
    
    if "'time_minutes':" in prob_content:
        facil_problems[prob_id] = True  # Has time_minutes - BAD
    else:
        facil_problems[prob_id] = False  # No time_minutes - GOOD

# Count
with_time = [k for k, v in facil_problems.items() if v]
without_time = [k for k, v in facil_problems.items() if not v]

print(f"Fácil problems analysis:")
print(f"  Total: {len(facil_problems)}")
print(f"  With time_minutes (BAD): {len(with_time)}")
print(f"  Without time_minutes (GOOD): {len(without_time)}")

if with_time:
    print(f"\nFácil with time_minutes to remove:")
    for p in sorted(with_time):
        print(f"  - {p}")
    
    # Generate replacements to remove time_minutes from facil
    replacements_to_remove = []
    
    for match in re.finditer(pattern, content, re.DOTALL):
        prob_id = match.group(1)
        if prob_id in with_time:
            old_full = match.group(0)
            # Remove the time_minutes line
            new_content = re.sub(r",?\s*'time_minutes':\s*\d+", "", match.group(2))
            new_full = old_full.replace(match.group(2), new_content)
            
            replacements_to_remove.append({
                'prob_id': prob_id,
                'old_string': old_full,
                'new_string': new_full
            })
    
    if replacements_to_remove:
        # Apply replacements
        for r in replacements_to_remove:
            if r['old_string'] in content:
                content = content.replace(r['old_string'], r['new_string'], 1)
                print(f"✓ Removed time_minutes from {r['prob_id']}")
        
        # Write back
        with open('game_data.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n✓ Removed time_minutes from {len(replacements_to_remove)} Fácil problems")
else:
    print("\n✓ All Fácil problems are correct!")
