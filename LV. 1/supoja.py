def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]   # 8
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if s1[i % 5] == answers[i]:
            cnt[0] += 1
        if s2[i % 8] == answers[i]:
            cnt[1] += 1
        if s3[i % 10] == answers[i]:
            cnt[2] += 1

    for j in range(len(cnt)):
        if cnt[j] == max(cnt):
            answer.append(j+1)
    return answer


print(solution([1, 3, 2, 4, 2]))


# using enumerate

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
