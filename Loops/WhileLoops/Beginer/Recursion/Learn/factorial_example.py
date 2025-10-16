"""

Factorial (Classic Example)

Goal: See how recursion multiplies values.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
"""
def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():

    print(factorial(5))


if __name__ == "__main__":
    main()