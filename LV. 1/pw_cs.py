# my code
def solution(s, n):
    answer = ""
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90 and ord(i) + n > 90:
            answer += chr(ord(i) - 26 + n)
        elif ord(i) >= 65 and ord(i) + n <= 90:
            answer += chr(ord(i) + n)
        elif ord(i) >= 97 and ord(i) + n > 122:
            answer += chr(ord(i) - 26 + n)
        elif ord(i) >= 97 and ord(i) + n <= 122:
            answer += chr(ord(i) + n)
        else:
            answer += i
    return answer


print(solution("a B z", 4))


# clean
def ceasar(s, n):
    answer = ""
    for i in s:
        if i.isupper():
            answer += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
        elif i.islower():
            answer += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
        else:
            answer += i
    return answer


print(solution("a B z", 4))
