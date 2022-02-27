def solution(s):
    answer = ""
    res = []
    for i in range(len(s)):
        res.append(s[i])
    res.sort(reverse=True)
    for j in res:
        answer += j
    return answer


print(solution("Zbcdefg"))


# short code
def solution(s):
    return "".join(sorted(s, reverse=True))
