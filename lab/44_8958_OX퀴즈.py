for _ in range(int(input())):
    result = 0
    inp = input().split('X')
    print(sum([len(i)*(len(i)+1)//2 for i in inp]))
