def solution(priorities, location):
    answer = 1
    idxs = list(range(len(priorities)))
    # for i in range(len(priorities)):
    while priorities:
        num = priorities.pop(0)
        idx = idxs.pop(0)
        if len(priorities) == 0:
            break
        if num < max(priorities):
            priorities.append(num)
            idxs.append(idx)
        elif idx == location:
            break
        else:
            answer += 1

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([2, 1, 3, 2], 2))

# 딕셔너리처럼 원소에 인덱스를 부여한 다음,
# 원소 크기의 내림차순 >
# 크기가 같을 때 인덱스의 내림차순으로 정렬 후 도출
