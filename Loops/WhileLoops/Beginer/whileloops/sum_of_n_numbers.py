"""
Sum of First N Numbers
Ask the user for a number n and calculate the sum from 1 to n.
"""

def calculate_sum():

    number = int(input("Enter a number"))
    total = 0
    first_value = 1

    while first_value <= number:
        total += first_value
        first_value += 1
    return total


def main():


    result = calculate_sum()
    print(result)

if __name__ == '__main__':
    main()