import collections
# short code


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 최초 작성 효율성 실패 코드

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in completion[:]:
        if i in participant:
            participant.remove(i)
            completion.remove(i)
    return participant[0]


# 딕셔너리 이용

def solution(participant, completion):
    dict = {}
    for i in participant:
        if dict.get(i):
            dict[i] += 1
        else:
            dict[i] = 1

    for i in completion:
        dict[i] -= 1

    for key in dict:
        if dict[key] > 0:
            return key


print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))


# other's codes, 코드 작성 전 내가 생각하던 아이디어와 유사.

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]


print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))
