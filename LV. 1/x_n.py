# my code

x, n = map(int, input().split())
li = []
if x > 0:
    for i in range(x, x * n + 1, x):
        li.append(i)
elif x == 0:
    for k in range(n):
        li.append(x)
else:
    for j in range(x, x * n - 1, x):
        li.append(j)
print(li)


# just need ONE line....
x, n = map(int, input().split())

print([x*i for i in range(1, n + 1)])
