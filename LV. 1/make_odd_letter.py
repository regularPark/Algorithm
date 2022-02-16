def solution(s):
    result = []
    result.append(s)
    li = []
    answer = ''
    for i in range(len(result[0])):
        if (i + 1) % 2 == 0:
            li.append(result[0][i].upper())
        else:
            li.append(result[0][i])

    for j in li:
        answer += j
    return answer


print(solution("\"try hello world\""))
