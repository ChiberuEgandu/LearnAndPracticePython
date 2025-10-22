"""
Replace the second element in a list of numbers with a new number.
"""

def main():

    list_numbers = [1,2,3,4,5,6]

    
    #Using Index
    list_numbers[2] = 8
    print(list_numbers)

    #Using for loop
    for index in range(len(list_numbers)):
        if list_numbers[index] == 6:
            list_numbers[index] = 80
            index += 1
    print(list_numbers)


    #Using while loop
    i = 0
    while i < len(list_numbers):
        if list_numbers[i] == 1:
            list_numbers[i] = 10
        i += 1
    print(list_numbers)


if __name__ == '__main__':
    main()