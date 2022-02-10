s = input()


def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        s1 = s[0:i]
        s_ = ""
        cnt = 1
        for j in range(i, len(s), i):
            if s1 == s[j:j+i]:
                cnt += 1
            else:
                if cnt >= 2:
                    s_ += str(cnt) + s1
                else:
                    s_ += s1
                s1 = s[j:j+i]
                cnt = 1
        if cnt >= 2:
            s_ += str(cnt) + s1
        else:
            s_ += s1
        answer = min(answer, len(s_))
    return answer


print(solution(s))
