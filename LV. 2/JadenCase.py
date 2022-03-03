def solution(s):
    s = s.lower()
    answer = ""
    tmp = []
    for i in range(len(s)):
        tmp.append(s[i])
    for j in range(len(tmp)):
        if tmp[0] and tmp[0].isalpha():
            tmp[0] = tmp[0].upper()
        if tmp[j] == " " and tmp[j + 1].isalpha():
            tmp[j + 1] = tmp[j + 1].upper()
        if tmp[-1] == " ":
            break
    for k in tmp:
        answer += k
    return answer


print(sol2("  3for the    last wEek    "))


# def sol2(s):
#     return " ".join(i.title() for i in s.split(" "))


# print(sol2("  3for the    last wEek    "))
