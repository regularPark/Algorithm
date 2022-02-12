# # my code
a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a, end='')
    print()

# other way
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')
    print()


a, b = map(int, input().strip().split(' '))
answer = ('*' * a + '\n') * b
print(answer)
