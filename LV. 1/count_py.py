# my code
def solution(s):
    np = 0
    ny = 0
    for i in s:
        if i == 'p' or i == 'P':
            np += 1
        elif i == 'y' or i == 'Y':
            ny += 1
    if np == ny:
        return True
    else:
        return False


print(solution("Pyy"))


# short code
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
