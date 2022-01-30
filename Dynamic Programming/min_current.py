n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):  # number of current
    for j in range(array[i], m + 1):    # Bottom up
        if d[j - array[i]] != 10001:
            # ex) cur = (2,5) => d7 = min(d7, d2 + 1)
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
