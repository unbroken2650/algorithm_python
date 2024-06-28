results = []
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    if A == B == C:
        results.append(10000+A*1000)
    elif A == B or A == C:
        results.append(1000+A*100)
    elif B == C:
        results.append(1000+B*100)
    else:
        results.append(max(A, B, C)*100)

print(max(results))
