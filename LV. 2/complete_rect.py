from math import ceil


def solution(w, h):
    answer = 0
    slope = h / w
    if w == 1 or h == 1:
        return 0
    elif w == h:
        return w * h - w
    for i in range(1, w):
        n = ceil((slope) * i)
        answer += h - n
    return answer * 2


print(solution(8, 12))


# short code
def gcd(a, b):
    return b if (a == 0) else gcd(b % a, a)


def solution(w, h):
    return w * h - w - h + gcd(w, h)  # 크기 - 높이 - 너비 + 최대공약수....


print(solution(8, 12))
