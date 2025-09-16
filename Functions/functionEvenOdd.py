#Exercise 5: Even or Odd
#Write a function is_even(n) that returns True if n is even, otherwise False.
#Test with 3, 4, 7.

def is_even(n):
    if (n % 2) == 0:
        print(True)
    else:
        print(False)

def main():
    is_even(3)
    is_even(4)
    is_even(7)
main()