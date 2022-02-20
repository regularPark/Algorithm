# # 바로 앞 뒤 번호만 대여 가능
# my code
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 여벌 갖고 있는데 도난 당함
    for i in lost[:]:  # remove() 과정에서 원본 리스트 데이터를 해쳐서 [:]를 적용하여 순서대로 돌게 만듦.
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    # 여벌 있는 학생의 앞뒤
    for i in reserve[:]:
        for j in lost:
            if i - 1 == j or i + 1 == j:
                lost.remove(j)
    answer = n - len(lost)

    return answer


# other's code

def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost:
            answer += 1
        else:
            if i in reserve:    # 잃어버렸지만 여분이 있는 경우
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost:  # 빌려야하는 학생
        if i - 1 in reserve:
            answer += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            answer += 1
            reserve.remove(i + 1)

    return answer


print(solution(9, [5, 6, 8, 1, 2], [2, 3, 1, 4, 8, 9]))
