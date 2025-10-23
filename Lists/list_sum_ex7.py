"""
Create a list of 5 numbers and print the sum of all numbers.
"""

def main():

    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]

    #using sum function
    print(f"The sum of numbers using sum() is {sum(list_numbers)}")

    #using for loop
    sum_numbers = 0
    for num in list_numbers:
        sum_numbers += num
    print(f"The sum using for loop is {sum_numbers}")

    #using while loop 
    i = 0
    sum_num = 0

    while i < len(list_numbers):
        sum_num += list_numbers[i]
        i += 1
    print(f"The sum of all numbers using while loop is {sum_num}")



if __name__ == '__main__':
    main()