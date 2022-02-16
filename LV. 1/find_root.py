# my code
from math import sqrt


def solution(n):
    if int(sqrt(n)) == sqrt(n):
        return (sqrt(n) + 1) ** 2
    else:
        return -1


print(solution(121))


# short code

def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'
