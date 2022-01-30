n = int(input())

# initializing DP table
d = [0] * 30001

# DP, Bottom-up
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)  # 약수?에 연산을 한번 더 해줬기 때문에 횟수를 더해준다.
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    # 예를 들어 6의 배수 같은 경우, 2 or 3의 나누기 연산에서 누가 더 횟수가 적은지 확인하기 위해
    # elif를 사용하지 않고 if를 사용하여 또 다시 검증한다.

print(d[n])

# using previous result
