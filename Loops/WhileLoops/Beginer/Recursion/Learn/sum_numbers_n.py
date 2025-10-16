"""
Sum of Numbers up to n

Goal: Learn how recursion can return a value instead of just printing.

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)
"""

def sum_numbers(n):

    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)
        


def main():

    print(sum_numbers(4))

if __name__ == '__main__':
    main()