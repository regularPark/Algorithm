def rotate(key):
    n = len(key)
    rot_key = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rot_key[j][n-1-i] = key[i][j]
    return rot_key


def check(n_lock):
    door = len(n_lock) // 3
    for i in range(door, door * 2):
        for j in range(door, door * 2):
            if n_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(key)
    m = len(lock)
    n_lock = [[0] * (m * 3) for _ in range(m * 3)]
    # 자물쇠에 열쇠 세팅
    for i in range(m):
        for j in range(m):
            n_lock[i+m][j+m] = lock[i][j]
    # 열쇠 넣기
    for _ in range(4):
        key = rotate(key)
        for i in range(m * 2):
            for j in range(m * 2):
                for x in range(n):
                    for y in range(n):
                        n_lock[i + x][j + y] += key[x][y]
                if check(n_lock) == True:
                    return True
                for x in range(n):
                    for y in range(n):
                        n_lock[i + x][j + y] -= key[x][y]
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
