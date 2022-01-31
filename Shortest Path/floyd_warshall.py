INF = int(1e9)

n = int(input())    # 노드의 개수
m = int(input())    # 간선의 개수

# 2차원 배열 생성
graph = [[INF] * (n + 1) for i in range(n + 1)]


# 스스로에게 가는 것은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# a에서 b로 가는 비용은 c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 점화식, ex) min(23,  21 + 13)처럼 경로를 더하여 비교함.
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
