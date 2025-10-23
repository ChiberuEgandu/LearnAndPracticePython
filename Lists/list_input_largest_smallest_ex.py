"""
Ask the user to enter 5 numbers, store them in a list, then print the largest and smallest.
"""

def user_input():

    number_list = []

    while True:
        number = int(input("Please provide 5 numbers, enter 0 to stop:"))

        if number == 0:
            break
        else:
            number_list.append(number)
    
    return number_list
    




def main():

    my_num_list = user_input()

    print(f"Here is the list of numbers you provided {my_num_list}")
    
    #using for loop
    for num in reversed(my_num_list):
        print(num)



    #using while loop
    i = len(my_num_list) - 1
    while i > 0:
        print(my_num_list[i], end='')
        i -= 1
    

if __name__ == '__main__':
    main()