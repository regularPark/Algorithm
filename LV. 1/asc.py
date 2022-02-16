# my code
def solution(n):
    n = str(n)
    answer = []
    for i in n:
        answer.append(int(i))
    answer.reverse()
    return answer


print(solution(12345))


# short code
def digit_reverse(n):
    return list(map(int, reversed(str(n))))


print(digit_reverse(12345))
