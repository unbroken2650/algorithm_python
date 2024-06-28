H, M = map(int, input().split())
total = H * 60 + M
total -= 45
print(total // 60 % 24, total % 60)
