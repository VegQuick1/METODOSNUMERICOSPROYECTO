#!/usr/bin/env python3
"""Verify that PDF answers have been correctly updated"""

from game_data import PROBLEM_DATA

# PDF correct values mapping
PDF_ANSWERS = {
    'euler_modified_intermedio_1': '1.2',
    'simpson_1_3_intermedio_1': '0.666666667',
    'simpson_1_3_avanzado_1': '0.666666667',
    'trapezoidal_intermedio_1': '0.65625',
    'trapezoidal_avanzado_1': '0.65625',
    'bisection_intermedio_1': '0.3087',
    'bisection_avanzado_1': '0.3087',
    'false_position_intermedio_1': '1.217859143',
    'false_position_avanzado_1': '1.217859143',
    'newton_raphson_intermedio_1': '1.368808108',
    'newton_raphson_avanzado_1': '1.368808108',
    'fixed_point_intermedio_1': '0.5671433',
    'fixed_point_avanzado_1': '0.5671433',
    'secant_intermedio_1': '0.5671433',
    'secant_avanzado_1': '0.5671433',
}

print("=" * 60)
print("VERIFICATION: PDF ANSWERS")
print("=" * 60)

all_correct = True
for problem_id, expected_answer in PDF_ANSWERS.items():
    if problem_id not in PROBLEM_DATA:
        print(f"✗ {problem_id}: NOT FOUND IN PROBLEM_DATA")
        all_correct = False
        continue
    
    actual_answer = PROBLEM_DATA[problem_id].get('correct', '')
    if actual_answer == expected_answer:
        print(f"✓ {problem_id}: {actual_answer}")
    else:
        print(f"✗ {problem_id}: Expected '{expected_answer}', got '{actual_answer}'")
        all_correct = False

print("=" * 60)
if all_correct:
    print("✓✓✓ ALL PDF ANSWERS ARE CORRECT! ✓✓✓")
else:
    print("✗✗✗ SOME ANSWERS ARE INCORRECT ✗✗✗")
print("=" * 60)
