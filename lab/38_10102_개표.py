N = int(input())
inp = input()
candidates = {'A': 0, 'B': 0}

for c in inp:
    candidates[c] += 1
print('A' if candidates['A'] > candidates['B'] else 'B' if candidates['A'] < candidates['B'] else 'Tie')
