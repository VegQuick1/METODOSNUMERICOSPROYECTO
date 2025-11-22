import re

with open('game_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Count problems by level
facil = []
intermedio = []
avanzado = []
final = []

# Simple pattern to find all problem definitions
lines = content.split('\n')
for i, line in enumerate(lines):
    if "': {" in line and line.strip().startswith("'"):
        prob_id = line.split("'")[1]
        
        # Look ahead for time_minutes
        time_val = None
        for j in range(i+1, min(i+20, len(lines))):
            if "'time_minutes':" in lines[j]:
                time_match = re.search(r"'time_minutes':\s*(\d+)", lines[j])
                if time_match:
                    time_val = int(time_match.group(1))
                break
            if '},' in lines[j]:
                break
        
        # Categorize
        if 'facil' in prob_id:
            facil.append((prob_id, time_val))
        elif 'intermedio' in prob_id:
            intermedio.append((prob_id, time_val))
        elif 'avanzado' in prob_id:
            avanzado.append((prob_id, time_val))
        else:
            final.append((prob_id, time_val))

print('=' * 60)
print('VERIFICATION SUMMARY - TIME LIMITS')
print('=' * 60)

print(f'\nFácil ({len(facil)} total) - SHOULD HAVE NO TIME LIMIT:')
facil_no_time = sum(1 for _, t in facil if t is None)
facil_with_time = sum(1 for _, t in facil if t is not None)
print(f'  ✓ Without time_minutes: {facil_no_time}')
if facil_with_time > 0:
    print(f'  ❌ WITH time_minutes: {facil_with_time}')
    for p, t in facil:
        if t is not None:
            print(f'     {p}: {t}min')

print(f'\nIntermedio ({len(intermedio)} total) - SHOULD BE 25 MINUTES:')
intermedio_25 = sum(1 for _, t in intermedio if t == 25)
intermedio_wrong = [(p, t) for p, t in intermedio if t != 25]
print(f'  ✓ With 25 minutes: {intermedio_25}')
if intermedio_wrong:
    print(f'  ❌ Wrong time: {len(intermedio_wrong)}')
    for p, t in intermedio_wrong[:5]:
        print(f'     {p}: {t}')

print(f'\nAvanzado ({len(avanzado)} total) - SHOULD BE 30 MINUTES:')
avanzado_30 = sum(1 for _, t in avanzado if t == 30)
avanzado_wrong = [(p, t) for p, t in avanzado if t != 30]
print(f'  ✓ With 30 minutes: {avanzado_30}')
if avanzado_wrong:
    print(f'  ❌ Wrong time: {len(avanzado_wrong)}')
    for p, t in avanzado_wrong[:5]:
        print(f'     {p}: {t}')

print(f'\nPrueba Final ({len(final)} total) - SHOULD BE 25 MINUTES:')
final_25 = sum(1 for _, t in final if t == 25)
final_wrong = [(p, t) for p, t in final if t != 25]
print(f'  ✓ With 25 minutes: {final_25}')
if final_wrong:
    print(f'  ❌ Wrong time: {len(final_wrong)}')
    for p, t in final_wrong[:5]:
        print(f'     {p}: {t}')

print('\n' + '=' * 60)
total_correct = facil_no_time + intermedio_25 + avanzado_30 + final_25
total_problems = len(facil) + len(intermedio) + len(avanzado) + len(final)
print(f'TOTAL: {total_correct}/{total_problems} problems with correct times')
if total_correct == total_problems:
    print('✓✓✓ ALL PROBLEMS HAVE CORRECT TIME LIMITS! ✓✓✓')
print('=' * 60)
