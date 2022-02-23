def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))


def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
