def solution(n):
    count = 0
    while n != 1 or count > 500:
        if n % 2 == 0:
            n /= 2
            count += 1
        elif count > 500:
            count = -1
            return count
        else:
            n = n * 3 + 1
            count += 1
    return count


print(solution(16))
