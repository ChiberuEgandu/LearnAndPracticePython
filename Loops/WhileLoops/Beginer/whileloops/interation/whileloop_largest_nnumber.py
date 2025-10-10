"""
Find the largest number

Loop through the list to find and print the largest number.
"""

def main():

    numbers = [ 23, 45, 20 ,85 ,63, 71, 52]

    #inituialize the largest number at index [0]
    largest_number = numbers[0]
    print(largest_number)

    #initialize the index to start at 1
    index = 1

    while index < len(numbers):
        current_number = numbers[index]

        if current_number > largest_number:
            largest_number = current_number
        index += 1
    

    print(f"The largest number in the list is {largest_number}")






if __name__ == '__main__':
    main()
