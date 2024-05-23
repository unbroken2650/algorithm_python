A, B = map(int, input().split())
B += int(input())

while B >= 60:
    A += 1
    B -= 60
print(A if A < 24 else A-24, B)
