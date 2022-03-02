from itertools import permutations
from math import sqrt


# my code
def solution(numbers):
    res = []
    res2 = []
    pn = []
    answer = 0
    for i in numbers:
        res.append(i)  # 문자열 분해
    for j in range(1, len(res) + 1):
        res2.append(list(map("".join, permutations(res, j))))  # 문자열 조합
    for rs2 in res2:
        set(rs2)
        for _ in range(len(rs2)):
            pn.append(int(rs2[_]))
    pn = set(pn)  # 정수화 && 중복 원소 제거
    for x in pn:
        if x == 2 or x == 3:
            answer += 1
        if x >= 4:
            for i in range(2, int(sqrt(x)+1), 1):
                if x % i == 0:
                    break
                if i == int(sqrt(x)):
                    answer += 1
                    break

    return answer


# short code
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))   # 0~1 원소를 삭제함
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))   # i * 2의 배수들을 삭제하는 과정
    return len(a)


print(solution("011"))


# recursion
