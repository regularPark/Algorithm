def solution(n):
    a = n
    b = n
    while a > 1:
        a //= 3
        b %= 3
        print(a, b)


print(solution(18))
