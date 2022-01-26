n, m = map(int, input().split())

result = 0

# # using min function # #
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_val = min(data)

#     result = max(result, min_val)

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001  # 현재 줄에서 가장 작은 수를 찾는 과정
    for j in data:
        min_value = min(j, min_value)

    result = max(result, min_value)

print(result)
