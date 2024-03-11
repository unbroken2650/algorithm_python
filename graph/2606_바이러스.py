from collections import deque

INF = int(1e9)

N = int(input())  # 컴퓨터의 수
M = int(input())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

network = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)  # 방향성 없는 연결로 처리

visited = [False] * (N + 1)
visited[1] = True  # 1번 컴퓨터는 이미 웜 바이러스에 걸렸다고 가정

queue = deque([1])
cnt = 0

while queue:
    current = queue.pop()  # 오른쪽에서 요소를 빼오는 것을 유지하면서 웜 바이러스 전파
    for neighbor in network[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
            cnt += 1

print(cnt)  # 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력
