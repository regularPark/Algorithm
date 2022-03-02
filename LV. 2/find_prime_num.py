from itertools import permutations


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
        if x > 1:
            for i in range(2, x):
                if x % i == 0:
                    continue

    return answer


print(solution("011"))
