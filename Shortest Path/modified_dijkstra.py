import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[]for i in range(n + 1)]
distance = [INF] * (n + 1)

# input way info
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        # 파이썬의 기본 heap은 최소 heap. 최소 heap을 사용했으므로 pop해주면 가장 작은 값이 나옴.

        # 현재 노드가 이미 처리된 적이 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 경우가 더 짧을 때,
            if cost < distance[i[0]]:   # 초기값 INF
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# 시간 복잡도 O(Elog₂V)
# 1차원 리스트를 이용하고, 이때문에 heapq를 사용할 시 가장 작은 원소를 구해내는 작업이 필요없어진다.
# 👉heapq, 즉 우선순위 큐를 사용하므로 거리가 짧은 원소가 항상 먼저 나온다는 것이다.
# 따라서 기존 dijkstra와 다르게 get_smallest_node()라는 함수를 작성할 필요가 없다.
# 이것은 곧 시간 복잡도의 감소를 의미한다.
