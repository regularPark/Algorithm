# 입력된 수를 반으로 나눠 각각 더함. 같으면 LUCKY, 다르면 READY

n = input()

data1 = list(n[:len(n)//2])
data2 = list(n[len(n)//2:])

result1 = 0
result2 = 0

for i in data1:
    result1 += int(i)

for j in data2:
    result2 += int(j)

if result1 == result2:
    print("LUCKY")
else:
    print("READY")
