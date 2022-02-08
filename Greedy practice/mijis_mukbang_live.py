# 다시 보기... 이해가 될듯 말듯 함.
# while문 내용 제대로 이해 못함.

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_ = 0  # 먹는 데 걸린 시간
    pre = 0  # 직전 음식 먹는 데 걸린 시간
    rest = len(food_times)  # 남은 음식 개수

    # 음식을 먹는 데 가장 적은 시간이 걸리는 원소를 맨 앞에 두기 위해 힙 정렬 쓴 것이다.
    # (음식의 가짓수 * 먹는 데 걸리는 시간) = (가장 적게 걸리는 음식을 다 먹는 데 걸리는 총 시간).
    #

    while sum_ + ((q[0][0] - pre) * rest) <= k:
        now = heapq.heappop(q)[0]
        sum_ += (now - pre) * rest  # 먹기 위해 사용한 시간
        rest -= 1  # 남은 음식 수
        pre = now

    answer = sorted(q, key=lambda x: x[1])  # 남은 음식을 번호순으로 정렬
    print(answer)
    print(answer[(k - sum_) % rest][1])  #


solution([3, 1, 2], 4)
