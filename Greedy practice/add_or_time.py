# 연속된 숫자열을 순차적으로 돌면서 덧셈, 혹은 곱셈을 통해 가장 큰 수를 만들어 내는 프로그램을 만들라.
# ex) input: 567, output : 210
# ex) input: 02984, output : 576

numbers = input()
result = int(numbers[0])
for i in range(1, len(numbers)):
    n = int(numbers[i])
    if n <= 1 or result <= 1:
        result += n
    else:
        result *= n

print(result)
