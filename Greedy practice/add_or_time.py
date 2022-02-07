numbers = input()
result = int(numbers[0])
for i in range(1, len(numbers)):
    n = int(numbers[i])
    if n <= 1 or result <= 1:
        result += n
    else:
        result *= n

print(result)
