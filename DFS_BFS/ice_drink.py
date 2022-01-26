n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):  # DFS로 특정 노드 방문 후 연결된 모든 노드 방문
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 범위 밖이면 탈출
        return False

    if graph[x][y] == 0:    # 방문한 노드가 0이라면 네 방향으로 DFS 실행
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False    # 방문한 노드가 0이 아니라면 탈출


# # 모든 노드 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
