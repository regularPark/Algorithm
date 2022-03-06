# # 1~11번 시간 초과
# import itertools


# def solution(numbers):
#     numbers = list(map(str, numbers))
#     combination = list(itertools.permutations(numbers, len(numbers)))
#     result = []
#     for num in combination:
#         result.append("".join(num))
#     result = list(map(int, result))
#     return str(max(result))


# print(solution([6, 10, 2]))

# 도저히 못 풀겠어서 검색...


def solution(numbers):
    num_str = list(map(str, numbers))
    num_str.sort(key=lambda num: num*3, reverse=True)
    return str(int("".join(num_str)))   # 000인 부분 없애기 위함


print(solution([3, 30, 34, 5, 9]))


# 원소의 크기 제한 1000, 때문에 str화한 원소에 *3 연산을 하여
# 333
# 303...
# 343...
# 555
# 999
# 로 바꾸면 문자열인 상태에서 sort를 하게 됨.
# 이때 문자열 첫번째부터 인덱스 값의 ASCII 값으로 비교하기 때문에
# 9 5 34 3 30 순으로 정렬됨


# # using functools
# import functools


# def comparator(a, b):
#     t1 = a+b
#     t2 = b+a
#     # t1이 크면 1  t2가 크면 -1  같으면 0
#     return (int(t1) > int(t2)) - (int(t1) < int(t2))


# def solution(numbers):
#     n = [str(x) for x in numbers]
#     n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
#     answer = str(int(''.join(n)))
#     return answer
