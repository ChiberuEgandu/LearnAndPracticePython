"""
Print the numbers from 1 to 10 using a for loop.
"""


def main():
    #Print the numbers from 1 to 10 using a for loop.
    for num in range(1, 11):
        print(num)
    
    #Print each character in the string "Python Rocks".

    my_string = "Python Rock"

    for letter in my_string:
        print(letter)

    #Given a list nums = [3, 5, 7, 9], print each number multiplied by 2.

    print("\n")

    numbers = [3, 5, 7, 9]

    for number in numbers:
        print(number * 2)
    
    print("\n")
    

    #Use a for loop to compute the sum of all numbers in [1, 2, 3, 4, 5].

    number_list = [1, 2, 3, 4, 5]

    total_sum = 0

    for my_number in number_list:
        total_sum += my_number
    
    print(f"The sum of the {number_list} is {total_sum}")

    print("\n")


    #Given fruits = ["apple", "banana", "cherry"], print "I like apple", "I like banana", etc.

    fruits = ["apple", "banana", "cherry"]

    for fruit in fruits:
        print(f"I like {fruit}")
    
    print("\n")

    #Write a for loop that counts how many numbers are even in [2, 5, 8, 11, 14, 17].

    list_nums =[2, 5, 8, 11, 14, 17]
    count_even = 0

    for list_num in list_nums:
        if list_num % 2 == 0:
            count_even += 1
    
    print(f"There are {count_even} even numbers in the {list_nums} list")

    print("\n")
    
    #Write a for loop that finds the largest number in [10, 22, 5, 75, 65] without using max().

    largest_num_list = [10, 22, 5, 75, 65]

    largest_num = largest_num_list[0]

    for large_num in largest_num_list:
        if large_num > largest_num:
            largest_num = large_num
    
    print(f"The largest number in the {largest_num_list} is {largest_num} ")


    #Use a for loop to create a new list that contains the squares of numbers from [1, 2, 3, 4, 5].

    original_numbers = [1, 2, 3, 4, 5]

    new_square_list_numbers = []

    for s_nums in original_numbers:
        new_square_list_numbers.append(s_nums ** 2)
    
    print(f"My new list of numbers square is {new_square_list_numbers}")

        


if __name__ == '__main__':
    main()