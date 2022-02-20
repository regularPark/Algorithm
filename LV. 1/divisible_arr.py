# my code
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer


print(solution([5, 9, 7, 10], 5))

# short code


def solution(arr, divisor): return sorted(
    [n for n in arr if n % divisor == 0]) or [-1]
