A, B, C = map(int, input().split())
C += int(input())

B += C//60
C = C % 60
A += B//60
B = B % 60
print(A % 24, B, C)
