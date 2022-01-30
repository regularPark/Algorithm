d = [0] * 100


def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibonacci(x - 1) + fibonacci(x - 2)
    return d[x]


print(fibonacci(10))

# like this way, "using recursion". called Top-down solution.
