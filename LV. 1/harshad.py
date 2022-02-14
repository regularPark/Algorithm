# my code

def solution(x):
    x_ = str(x)
    div = 0
    for i in x_:
        div += int(i)
    if x % div == 0:
        return True
    else:
        return False

# short code


def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0


print(Harshad(18))
