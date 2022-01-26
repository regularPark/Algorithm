n, m = map(int, input().split())

# 맵 초기화(이동 추적)
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

# 맵 정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction    # 변수 밖에서 선언된 전역변수이기 때문에 global 사용
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1  # 방향 찾기 위해 회전했으나 막혔을 때

    # # 네 방향 모두 갈 수 없을 때
    if turn_time == 4:  # 방향은 유지한 채 한 칸 뒤로 이동하는데
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny]:   # 뒤로 갈 수 있다면 뒤로
            x = nx
            y = ny
        else:
            break   # 갈 곳이 없다면 탈출
        turn_time = 0

print(count)
