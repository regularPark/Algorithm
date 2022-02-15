# my code

def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for j in range(max(n, m), (n * m) + 1):
        if j % n == 0 and j % m == 0:
            answer.append(j)
            break
    return answer


# short code

def gcdlcm(a, b):
    for i in range(a):
        if a % (a - i) + b % (a - i) == 0:
            return [a - i, a * b / (a - i)]


print(gcdlcm(2, 5))
