n = int(input())
x, y = 1, 1
plans = input().split()

dir_x = [0, 0, -1, 1]
dir_y = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            new_x = x + dir_x[i]
            new_y = y + dir_y[i]
    if new_x < 1 or new_y < 1 or new_x > n or new_y > n:
        continue

    x, y = new_x, new_y

print(x, y)
