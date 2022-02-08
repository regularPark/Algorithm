# 갖고 있는 동전으로 만들 수 없는 최소 금액을 찾기
# ex) input : 3 2 1 1 9, output : 8

n = int(input())

data = list(map(int, input().split()))
data.sort()

# 다시 생각해보기
target = 1
for i in data:
    if target < i:
        break
    target += i

print(target)
