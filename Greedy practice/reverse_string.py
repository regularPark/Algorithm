# 0과 1로만 이뤄진 문자열 s를 전부 같게 만들기 위한 최소 횟수를 구하기
# ex) input : 0001100, output : 2

s = input()

cnt0 = 0
cnt1 = 0

if s[0] == "1":
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == "1":
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))
