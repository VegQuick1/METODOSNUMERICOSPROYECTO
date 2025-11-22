import json
import sys

with open('replacements.json', encoding='utf-8') as f:
    replacements = json.load(f)

# Process in batches of 20
batch_size = 20
for batch_idx in range(0, len(replacements), batch_size):
    batch = replacements[batch_idx:batch_idx + batch_size]
    
    print(f"""
# Batch {batch_idx // batch_size + 1}: Items {batch_idx+1}-{min(batch_idx+batch_size, len(replacements))}
replacements = [""")
    
    for r in batch:
        old_str = r['old_string'].replace("'", "\\'").replace("\n", "\\n")
        new_str = r['new_string'].replace("'", "\\'").replace("\n", "\\n")
        
        # Truncate for display
        old_display = old_str[:80].replace('\\n', ' ')
        new_display = new_str[:80].replace('\\n', ' ')
        
        print(f"""    {{
        "filePath": "c:\\\\Users\\\\gokuj\\\\Downloads\\\\MN\\\\METODOSNUMERICOSPROYECTO\\\\game_data.py",
        "oldString": {repr(r['old_string'])},
        "newString": {repr(r['new_string'])},
        "explanation": "Update time_minutes for {r['prob_id']} ({r['action']})"
    }},""")
    
    print("]")
    print("")
