from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])  # queue 구현하기 위해 deque 사용
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
# BFS, Breadth-First Search. 가까운 노드부터 탐색한다. Queue 자료구조를 이용.
