import numpy as np


# my code
def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append([x + y for x, y in zip(arr1[i], arr2[i])])
    return result


print(solution([[1], [2]], [[3], [4]]))


# using numpy
def sum(arr1, arr2):
    A = np.array(arr1)
    B = np.array(arr2)
    answer = (A+B)

    return answer.tolist()


print(sum([[1], [2]], [[3], [4]]))
