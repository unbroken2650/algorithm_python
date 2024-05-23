T = int(input())


def calculate(eq):
    num = float(eq[0])
    for i in eq[1:]:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        else:
            num -= 7
    print(f'{num:.2f}')


for _ in range(T):
    calculate(list(map(str, input().split())))
