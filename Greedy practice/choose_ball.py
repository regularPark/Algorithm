# A와 B는 서로 무게가 다른 볼링공을 고르려 함.

n, m = map(int, input().split())

k = list(map(int, input().split()))

arr = [0] * 11
for i in k:
    arr[i] += 1

result = 0
for i in range(1, m + 1):
    n -= arr[i]  # 무게 i일 때 고를 수 있는 공 개수
    result += arr[i] * n  # 무게 i인 공의 개수와 n을 곱하면 A가 i를 고를 때 조합의 수가 나옴.


print(result)
