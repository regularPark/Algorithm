# input : K1KA5CB7, output : ABCKK13 / input : AE245JL , output : AEJL11

s = input()
li = []
num = 0

for i in s:
    if i.isalpha():
        li.append(i)
    else:
        num += int(i)

li.sort()

if num != 0:
    li.append(str(num))

print(li)

print(''.join(li))
