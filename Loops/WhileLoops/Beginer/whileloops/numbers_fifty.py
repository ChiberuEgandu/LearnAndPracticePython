"""
Print Odd Numbers Only
Print all odd numbers from 1 to 50.

"""

def odd_numbers():

    number = 1

    while number <= 50: 
        if number % 2 != 0:
            print(number)
        number += 1


def main():

    odd_numbers()

if __name__ == '__main__':
    main()