T = int(input())

for _ in range(T):
    num, sent = input().split()
    print(''.join([i*int(num) for i in sent]))
