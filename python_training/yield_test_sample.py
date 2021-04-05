def square_yield(number):
    yield number * number
    yield number + number


def square_return(number):
    return number * number
    return number + number


for i in square_yield(6):
    print(i)

print(square_return(6))
