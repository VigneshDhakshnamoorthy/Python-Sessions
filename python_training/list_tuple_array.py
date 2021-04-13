
import array as arr

print("----- List -----")
list = ["mango", "strawberry", "orange",
        "apple"]

print(list)
list.append("Banana")
print(list)
list.remove("apple")
print(list)
list.insert(1,"gowa")
print(list)
list.sort()
print(list)

a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]

replacements = {
    1: 10,
    2: 20,
    3: 30,
}
print(replacements.get(4,400))

a = [replacements.get(x, x) for x in a]

print(a)



# print(list[2:4])
# list[1] = "grapes"
# print(list[1])

# print("----- Tuple -----")
# tuple = ("orange", "apple", "banana")
# print(tuple)

# print(tuple[2])

# print(tuple[0:2])

# print("----- Array -----")

# a = arr.array('i', [1, 2, 3])
# print("The new created array is : ", end=" ")
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()


# b = arr.array('d', [2.5, 3.2, 3.3])
# print("The new created array is : ", end=" ")
# for i in range(0, 3):
#     print (b[i], end=" ")

