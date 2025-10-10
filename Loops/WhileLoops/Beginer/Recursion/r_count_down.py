"""
These help you understand how recursion flows.

1. Count down from a number

Write a function that prints numbers from n down to 1.

def count_down(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        count_down(n - 1)


Try calling count_down(5) and see the order it prints.

"""

def count_down(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        count_down(n - 1)


def main():

    count_down(5)
if __name__ == '__main__':
    main()