a = int(input("Enter Starting First Number : "))
b = int(input("Enter Starting Second Number : "))
Number_Row = int(input("Enter Number of Rows: "))

print(a)
print(b)
for i in range(2, Number_Row):
    c = a + b
    a = b
    b = c
    print(c)
