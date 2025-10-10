"""
Sum of Numbers
Use a while loop to calculate the sum of numbers from 1 to 100.
"""

def sum_numbers():

    starting_number = 1
    total = 0

    while starting_number <= 100:
        total += starting_number
        starting_number += 1
    return total


def main():

    results = sum_numbers()
    print(results)

if __name__ == "__main__":
    main()