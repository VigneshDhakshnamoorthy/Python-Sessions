def square_yield(number):
    yield number * number
    add = yield number + number


def square_return(number):
    return number * number


for i in square_yield(6):
    print(i)
