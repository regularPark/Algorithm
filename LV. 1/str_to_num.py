import math

# my code
def solution(s):
    return int(s)


# my code
def solution(n):
    answer = [True] * (n + 1)
    result = []
    answer[0], answer[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if answer[i]:
            result.append(i)
            j = 2
            while i * j <= n:
                answer[i * j] = False
                j += 1
    result = [x for x in range(n + 1) if answer[x]]
    return len(result)


print(solution(10))
