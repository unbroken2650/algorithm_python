while True:
    A, B = map(int, input().split())
    if A + B == 0:
        break
    print("Yes" if A > B else "No")
