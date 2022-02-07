# n명의 모험가에게는 공포도가 존재함. 그룹 인원 중 최대 공포도의 크기만큼 그룹의 인원이 필요하고,
# ex) 공포도 3인 팀원이 있다면 3명 이상의 팀원이 필요.

n = int(input())
data = list(map(int, input().split()))

data.sort()

count = 0
result = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
