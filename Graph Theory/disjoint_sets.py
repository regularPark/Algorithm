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

# 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합 :", end=" ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모 테이블 출력
print("부모 테이블 :", end=" ")
for i in range(1, v + 1):
    print(parent[i], end=" ")
