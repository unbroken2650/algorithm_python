a, b, c, d, e, f = map(int, input().split())

found = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y - c == d * x + e * y - f == 0:
            print(x, y)
            found = True
            break
    if found:
        break
