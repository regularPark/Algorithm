# def solution(arr):
#     answer = []
#     j = -1
#     for i in arr:
#         if i != j:
#             j = i
#             answer.append(j)
#     return answer


# print(solution([1, 1, 3, 3, 0, 1, 1]))


def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a


print(no_continuous([1, 1, 3, 3, 0, 1, 1]))
