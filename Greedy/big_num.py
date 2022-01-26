n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# # It is too repetitive to compute large number. # #
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

count = int(m / (k + 1)) * k
count += m % (k + 1)  # the number of times add the biggest number.

result = 0
result += (count) * first
result += (m - count) * second
print(result)
