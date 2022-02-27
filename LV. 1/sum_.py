def solution(a, b):
    if a <= b:
        return sum(i for i in range(a, b + 1))
    else:
        return sum(i for i in range(b, a + 1))


print(solution(5, 3))

# short code
def adder(a, b):
    return sum(range(min(a, b), max(a, b) + 1))
