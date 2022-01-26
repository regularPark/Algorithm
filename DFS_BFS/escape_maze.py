from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:  # queue가 빌 때까지
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 미로를 벗어난 경우 무시하고 길찾기
                continue
            if graph[nx][ny] == 0:  # 벽인 경우 무시하고 길찾기
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1  # 길을 표시
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
print(graph)

# 결과값이 [[3, 2, 0], [0, 3, 0], [0, 4, 5]] 이렇게 시작위치가 3으로 나오는데
# 이것은 boolean으로 체크해주면 일어나지 않을 것으로 생각된다.
