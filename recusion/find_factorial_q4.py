"""
Find factorial.
Input: 5 → Output: 120
Multiply n * factorial(n-1).
"""

def factorial(n):

    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial( n - 1)


def main():

    print(factorial(5))

if __name__ == '__main__':
    main()