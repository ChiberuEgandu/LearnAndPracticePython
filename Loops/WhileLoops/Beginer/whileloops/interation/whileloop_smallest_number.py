"""
Find the smallest number

Same as above, but find the smallest value.
"""

def main():

    numbers = [ 23, 45, 20 ,85 ,63, 71, 52]

    smallest_number = numbers[0]

    index = 1

    while index < len(numbers):
        current_number = numbers[index]

        if current_number < smallest_number:
            smallest_number = current_number
        index += 1
    
    print(f"The smallest number in the list is {smallest_number}")


if __name__ == '__main__':
    main()