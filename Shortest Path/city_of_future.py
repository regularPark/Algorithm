from dis import dis


INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    # 서로에게 가는 비용 1로 고정
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# Floyd-Warshall Algorithm
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[k][b] + graph[a][k])

# k에 갔다가 x로 가는 것
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)


# 시간복잡도 O(N³)
# Floyd Warshall 알고리즘을 사용하여 최단거리를 구해냈다.
# 다익스트라와 다르게 2차원 리스트를 이용해야 한다.
# 점화식은 D_ab = min(D_ab, D_ak + D_kb)로
# 🚨 '3중 반복문'을 이용하는 것이 특징.
