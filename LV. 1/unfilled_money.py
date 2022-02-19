# my code
def solution(price, money, count):
    result = 0
    for i in range(1, count + 1):
        result += price * i
    if result - money <= 0:
        return 0
    return result - money


print(solution(3, 20, 4))


# short code
def solution(price, money, count):
    return max(0, price * (count + 1) * count // 2 - money)
