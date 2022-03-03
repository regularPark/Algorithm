# my code
def solution(progresses, speeds):
    result = []
    answer = []
    for i in range(len(progresses)):
        result.append(0)
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            result[i] += 1
    cnt = 0
    len_res = len(result)
    for i in range(0, len_res):
        if len(result) == 0:
            break
        tmp = result.pop(0)
        cnt += 1
        for j in range(i + 1, len_res):
            if len(result) == 0:
                break
            if tmp >= result[0]:
                result.pop(0)
                cnt += 1
            else:
                break
        answer.append(cnt)
        cnt = 0
    return answer


# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


# short code
def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
