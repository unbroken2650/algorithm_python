import math

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(math.gcd(A, B) * (A // math.gcd(A, B)) * (B // math.gcd(A, B)))
