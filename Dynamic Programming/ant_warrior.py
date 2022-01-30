n = int(input())

array = list(map(int, input().split()))
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])
    # d[i]까지 연산의 최댓값을 d[]에 저장하는 형태인 것이다.


print(d[n - 1])
