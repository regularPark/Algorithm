def solution(array, commands):
    res = []
    ans = []
    for x in range(len(commands)):
        i = commands[x][0]
        j = commands[x][1]
        k = commands[x][2]
        for _ in range(i - 1, j):
            res.append(array[_])
        res.sort()
        ans.append(res[k - 1])
        res = []
    return ans


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


# others code
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer


# short code
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
