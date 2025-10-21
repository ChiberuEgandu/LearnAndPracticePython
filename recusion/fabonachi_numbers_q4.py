"""
Fibonacci number.
Input: fib(5) → Output: 5
fib(n) = fib(n-1) + fib(n-2). Two base cases.
"""

def fib(n):

    if n  == 0: #base case
        return 0
    elif n == 1: 
        return 1
    else:
        return fib( n - 1) + fib(n - 2) #recursive case


def mystery(num):
    if num < 0:
        return 2 * num
    else:
        return mystery(num - 1) + num

def thing(num2):
    if num2 == 1 or num2 == 2:
        return 2 * num2
    else:
        return thing(num2 - 1) - thing(num2 - 2)
    

def main():

    print(fib(5))

    print("\n")

    print(mystery(-3))
    print(mystery(3))

    print("\n")
    print(thing(5))
    print(thing(6))

if __name__ == '__main__':
    main()