# my code
def solution(numbers):
    numbers.sort()
    result = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num not in result:
                result.append(num)
    result.sort()
    return result


print(solution([5, 0, 2, 7]))


def solution(numbers): return sorted(
    {numbers[i]+numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i > j})


print(solution([5, 0, 2, 7]))
