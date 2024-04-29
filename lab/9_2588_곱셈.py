a = int(input())
b = input()
for i in b[-1::-1]:
    print(a*int(i))
print(a*int(b))