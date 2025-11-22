import json

with open('game_data.py', 'r', encoding='utf-8') as f:
    original_content = f.read()

with open('replacements.json', 'r', encoding='utf-8') as f:
    replacements = json.load(f)

content = original_content

# Apply each replacement
for i, replacement in enumerate(replacements):
    old_str = replacement['old_string']
    new_str = replacement['new_string']
    
    if old_str in content:
        content = content.replace(old_str, new_str, 1)  # Replace only first occurrence
        print(f"✓ {i+1}. {replacement['prob_id']} ({replacement['action']})")
    else:
        print(f"✗ {i+1}. {replacement['prob_id']} - NOT FOUND")

# Write back
with open('game_data.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Updated {len(replacements)} problems in game_data.py")
