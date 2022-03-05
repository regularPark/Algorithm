# my code
import heapq


def solution(scoville, K):
    answer = 0
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


# other's code
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
