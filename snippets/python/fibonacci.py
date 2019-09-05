"""
Lists the first n Fibonacci numbers using two different algorithms
    1) List construction
    2) Generator
"""

from functools import lru_cache

# Solution using a for loop and a list
def fibonacci_list(previous, current, maximum):
    fib_nums = []
    for num in range(maximum):
        fib_nums.append(previous)
        print('Fib', num, '=', previous)
        previous, current = current, previous + current
    return fib_nums

# The function can be called as follows:
if __name__ == '__main__':
    fibonacci_list(previous=0, current=1, maximum=101)


# An alternative solution using a while loop and a generator
def fibonacci_generator(previous, current, maximum):
    count = 0
    while count < maximum:
        previous, current = current, previous + current
        yield previous
        count += 1
        print(f'Fib {count} = {previous}')


# `pass` statement is there only because the function requires it.
if __name__ == '__main__':
    for num in fibonacci_generator(previous=0, current=1, maximum=101):
        pass


"""
An alternative solution using a recursive function and the `lru_cache` function
from the standard `functools` library as a decorator to implement memoization
"""
@lru_cache(maxsize=1000)
def fibonacci_recursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


if __name__ == "__main__":
    for num in range(0, 101):
        print('Fib', num, '=', fibonacci_recursive(num))
