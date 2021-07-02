from typing import no_type_check


def fact(n):
    if n == 1:
        return 1
    else:
        return (n*fact(n-1))


print(f'factorial of 5 is {fact(5)}')


def reverse_string(string: str) -> str:
    if string == "":
        return ""
    else:
        return string[-1] + reverse_string(string[:-1])


print(f'reverse_string of stressed = {reverse_string("stressed")}')