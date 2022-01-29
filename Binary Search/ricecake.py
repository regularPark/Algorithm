

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    rice_len = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            rice_len += i - mid
    if rice_len < m:  # 잘린 떡이 부족할 때 왼쪽 부분 탐색
        end = mid - 1
    else:   # 잘린 떡이 더 많을 때 오른쪽 부분 탐색
        result = mid    # 최대한 덜 자른 것이 정답이므로 result에 기록해 둠.
        start = mid + 1

print(result)
