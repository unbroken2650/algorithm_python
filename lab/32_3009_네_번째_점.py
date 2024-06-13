points = []
for _ in range(3):
    points.append(list(map(int, input().split())))
points.sort()

answer = []
for i in range(2):
    if points[0][i] == points[1][i]:
        answer.append(points[2][i])
    elif points[0][i] == points[2][i]:
        answer.append(points[1][i])
    else:
        answer.append(points[0][i])
print(*answer)