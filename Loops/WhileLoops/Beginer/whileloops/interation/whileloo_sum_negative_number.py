"""
Sum until a negative number

Keep summing elements in a list until you hit a negative number, then stop.
"""

def main():

    numbers = [1, 2, 3, -4, 5, 6, 7]
    index = 0
    sum = 0

    while index < len(numbers):
        if numbers[index] < 0:
            break
        else:
            sum += numbers[index]
        index += 1

    print(f"The sum of all the number until a negative is {sum}")


if __name__ == '__main__':
    main()