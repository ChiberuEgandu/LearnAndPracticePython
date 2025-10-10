"""
Sum of numbers

Given a list of integers, calculate the sum manually using a while loop.
"""

def main():

    numbers = [1, 2, 3, 4, 5]

    index = 0
    sum = 0

    while index < len(numbers):
        sum += numbers[index]
        index += 1
    print(f"The sum of {numbers} list is {sum}")


if __name__ == '__main__':
    main()
