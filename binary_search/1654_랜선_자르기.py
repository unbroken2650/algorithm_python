K, N = map(int, input().split())

lines = []

for _ in range(K):
  lines.append(int(input()))

low, high = 1, max(lines)
mid = 0
while True:
  if low > high:
    break
  total = 0
  mid = (low + high) // 2
  for i in lines:
    total += i // mid
  if total >= N:
    low = mid + 1
  else:
    high = mid - 1

print(high)
