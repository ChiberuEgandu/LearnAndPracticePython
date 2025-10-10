"""
Count even numbers

Count how many even numbers are in a list using a while loop.
"""

def main():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    index  = 0 
    count_of_even_numbers = 0 

    while index < len(numbers):
        if numbers[index] % 2 == 0:
            print(numbers[index])
            count_of_even_numbers += 1
        index += 1
    
    print(f"There are {count_of_even_numbers} in the {numbers} list")

            


if __name__ == '__main__':
    main()