grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

gro_dic = {}

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
print('\n')

for item in enumerate(grocery):
    print(item)

print('\n')
for count, item in enumerate(grocery):
    print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 0):
    print(count, item)
    gro_dic[count] = item

print('\n')
for key, value in gro_dic.items():
    print(key, value)
