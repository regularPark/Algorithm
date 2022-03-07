def fibonacci(n):
    fib = [1, 1]
    if n == 1 or n == 2:
        return 1
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n - 1]


def solution(n):
    return fibonacci(n) % 1234567


print(solution(5))
