for _ in range(int(input())):
    r, e, c = map(int, input().split())
    if r < e-c:
        print("advertise")
    elif r == e-c:
        print("does not matter")
    else:
        print("do not advertise")
