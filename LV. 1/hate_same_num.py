def solution(arr):
    answer = []
    j = -1
    for i in arr:
        if i != j:
            j = i
            answer.append(j)
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
