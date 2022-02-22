# my code
def solution(sizes):
    width = 0
    height = 0
    for i in range(len(sizes)):
        sizes[i].sort()
        if sizes[i][0] >= width:
            width = sizes[i][0]
        if sizes[i][1] >= height:
            height = sizes[i][1]
    answer = width * height
    return answer


print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))


# short code
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


# other's code
def solution(sizes):
    answer = 0
    weight, length = 0, 0

    for w, l in sizes:
        weight = max(weight, max(w, l))
        length = max(length, min(w, l))

    answer = weight * length

    return answer
