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


# using zip in zip
def sumMatrix(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer
# iteration #1-1. A.a = [1, 2] B.b = [3, 4]  >> a.c = 1, b.d = 3 >> c+d = 4
# iteration #1-2. a.c = 2, b.d = 4 >> c+d = 6
# ...


print(sumMatrix([[1, 2], [2, 3]],
                [[3, 4], [5, 6]]))
