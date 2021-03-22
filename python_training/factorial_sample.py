def fact(num):
    fact_sum = 1
    for nu in range(1,num + 1):
        fact_sum = fact_sum * nu
    return fact_sum


for i in range(1,11):
    print(f'{i} Factorial is {fact(i)}')
