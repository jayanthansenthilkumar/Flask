from data import COLLEGES
from collections import Counter

print(f"✓ Total colleges in database: {len(COLLEGES)}")
print("\n" + "="*60)
print("TOP 20 STATES BY NUMBER OF COLLEGES:")
print("="*60)

state_counts = Counter([c['state'] for c in COLLEGES])
for i, (state, count) in enumerate(sorted(state_counts.items(), key=lambda x: x[1], reverse=True)[:20], 1):
    print(f"{i:2}. {state:35} : {count:4} colleges")

print("\n" + "="*60)
print("COLLEGE TYPE DISTRIBUTION:")
print("="*60)
type_counts = Counter([c['type'] for c in COLLEGES])
for ctype, count in type_counts.items():
    print(f"{ctype:15} : {count:4} colleges")

print("\n" + "="*60)
print("SAMPLE COLLEGES FROM TAMIL NADU:")
print("="*60)
tamil_nadu_colleges = [c for c in COLLEGES if c['state'] == 'Tamil Nadu']
for i, college in enumerate(tamil_nadu_colleges[:20], 1):
    print(f"{i}. {college['name']} - {college['city']}")

print(f"\n✓ Total Tamil Nadu colleges: {len(tamil_nadu_colleges)}")
