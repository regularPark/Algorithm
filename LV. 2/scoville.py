import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)

    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        min_scv = heapq.heappop(scoville)
        sec_scv = heapq.heappop(scoville)
        heapq.heappush(scoville, min_scv + (sec_scv * 2))
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
