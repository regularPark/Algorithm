# my code

def solution(phone_number):
    answer = ''
    for i in phone_number[:-4]:
        answer += '*'
    for i in phone_number[-4:]:
        answer += i
    return answer


# short code

def hide(s):
    return '*'*(len(s) - 4) + s[-4:]
