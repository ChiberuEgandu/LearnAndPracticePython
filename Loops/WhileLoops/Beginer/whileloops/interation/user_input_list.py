"""

Ask user for numbers until 0

Keep asking the user for a number and store it in a list until they type 0. Then print all numbers.
"""



def main():

    my_numbers = []

    while True:
        numbers = int(input("please provide a list of numbers. Enter 0 to stop: "))

        if numbers == 0:
            break

        my_numbers.append(numbers)
    
    print(my_numbers)


if __name__ == '__main__':
    main()