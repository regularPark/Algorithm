import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

# 노드의 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력 받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 가는 것이 더 비용이 적을 때,
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # 짧은 것이 거리가 되고,
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드를 제외해야 하기 때문에 -1 연산.
print(count - 1, max_distance)
