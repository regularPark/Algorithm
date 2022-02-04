# 신장트리란 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# graph는 노와 노드 사이에 연결된 간선의 정보를 갖고 있는 자료구조

# 인접 행렬 :2차원 배열 사용 / 플로이드 워셜
# 인접 리스트 : 리스트 사용 / 다익스트라

# 서로소 집합 : 공통 원소가 없는 집합

# 특정 원소가 속한 집합 찾기
# def find_parent(parent, x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# # Path Compression & modified disjoint sets algorithm
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

# 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


for i in range(e):
    a, b, cost = map(int, input().split())
    # 사이클이 발생한 경우
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()


# 간선을 하나씩 확인함
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우(루트가 다른 경우)에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
