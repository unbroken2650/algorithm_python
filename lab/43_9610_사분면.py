counts = {
    'Q1': 0,
    'Q2': 0,
    'Q3': 0,
    'Q4': 0,
    'AXIS': 0
}
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a*b == 0:
        counts['AXIS'] += 1
    elif a > 0 and b > 0:
        counts['Q1'] += 1
    elif a < 0 and b > 0:
        counts['Q2'] += 1
    elif a < 0 and b < 0:
        counts['Q3'] += 1
    else:
        counts['Q4'] += 1

for i in counts.keys():
    print(f"{i}: {counts[i]}")
