inp = input()
prev = ""
result = 0
for i in inp:
    if prev != "" and i == prev:
        result += 5
    else:
        result += 10
        prev = i

print(result)
