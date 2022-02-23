def solution(numbers):
    com_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = sum(set(com_num) - set(numbers))
    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))


# short code
def solution(numbers):
    return 45 - sum(numbers)
