"""
1. Sum all elements in a list (classic recursion)

Goal: Write a recursive function that returns the sum of all numbers in a list.

Example:
"""

def my_list(numbers):
    if numbers == []:
        return 0
    else:
        return numbers[0] + my_list(numbers[1:])


def main():

    my_numbers = [2, 4, 6]
    print(my_list(my_numbers))

if __name__ == '__main__':
    main()