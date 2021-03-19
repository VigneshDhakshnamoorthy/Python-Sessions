number = int(input("Enter Number :"))

for i in range(number):
    print(" " * (number - 1 - i), end=" ")
    print("*" * int(i + i + 1))

for i in reversed(range(number)):
    print(" " * (number - 1 - i), end=" ")
    print("*" * int(i + i + 1))