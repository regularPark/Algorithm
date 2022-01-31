import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    # 'a' to 'b', price 'c'


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            index = i
    return index


def dijkstra(start):
    # initialize start point
    dist[start] = 0
    visited[start] = True
    for j in graph[start]:
        dist[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = dist[now] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if dist[i] == INF:
        print("INFINITY")
    else:
        print(dist[i])

# 시간 복잡도 Ο(V²)
