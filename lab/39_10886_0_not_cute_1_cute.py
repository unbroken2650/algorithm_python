result = 0
N = int(input())
for _ in range(N):
    result += 1 if int(input()) > 0 else 0
print("Junhee is cute!" if result > N/2 else "Junhee is not cute!")
