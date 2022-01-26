def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

# 깊이 우선 탐색, Depth-First Search, 노드 중 가장 깊이 있는 것부터 탐색. 스택, 재귀 함수를 이용.
