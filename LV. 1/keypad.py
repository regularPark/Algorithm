from math import abs

def solution(numbers, hand):
    result =""
    for i in numbers:
        if numbers[i] % 3 == 1:
            result += "L"
        elif numbers[i] % 3 == 0 and numbers[i] > 0:
            result += "R"
        else:
            if 

# 각잡고 다시 할 것.