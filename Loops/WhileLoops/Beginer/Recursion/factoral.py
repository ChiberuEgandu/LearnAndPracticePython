"""
Solve for 5 factoral

"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    


def main():

    factorial(5)

if __name__ == "__main__":
    main()