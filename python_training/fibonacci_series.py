def fibon(a, b, nr):
    if nr == 0:
        return ""
    else:
        print(a)
        c = a + b
        return fibon(b, c, nr-1)


a = int(input("Enter Starting First Number : "))
b = int(input("Enter Starting Second Number : "))
nr = int(input("Enter Number of Rows: "))
    
print(fibon(a,b,nr))

