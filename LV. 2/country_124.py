def solution(n):
    answer = ""
    con_124 = ["1", "2", "4"]

    [n // 3]

    if n % 3 == 1:
        answer += con_124[0]
    elif n % 3 == 2:
        answer += con_124[1]
    elif n % 3 == 0:
        answer += con_124[2]

    return answer


print(solution(13))
