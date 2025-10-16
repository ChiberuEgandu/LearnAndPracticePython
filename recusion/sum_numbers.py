"""
Exercise 3 - Sum of Natural Numbers

Goal: Write a recursive function sum_n(n) that returns the sum of numbers from 1 to n.

Example:

"""

def sum_numbers(n):

    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)
    

def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    


def main():

    print(sum_numbers(3))
    print(factorial(5))

if __name__ == '__main__':
    main()