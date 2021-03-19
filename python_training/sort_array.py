num = [5, 3, 2, -4, 1, -1, 6, 8, 10, -21, 25, -56, 0]
print(f'Normal Array : {num}')

num1 = []
for i in num:
    if i > 0:
        num1.append(i)
    else:
        num1.append(i * -1)
num1 = sorted(num1)
print(f'Sorted Array : {num1}')

for j in num:
    if num1.count(j) > 0:
        pass
    else:
        num1[num1.index(j * -1)]=j
print(f'Final Array : {num1}')
