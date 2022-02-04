# 위상 정렬이란 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'

from collections import deque

v, e = map(int, input().split())
# 모든 노드에 대한 진입차수를 0으로 초기화
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    # a에서 b로 이동 가능
    graph[a].append(b)
    # 진입차수를 1 증가
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새로운 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")


topology_sort()
