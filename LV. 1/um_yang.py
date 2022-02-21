# my code
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += int(absolutes[i])
        else:
            answer -= int(absolutes[i])
    return answer


print(solution([4, 7, 12], [True, False, True]))


# short code
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
