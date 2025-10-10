"""
Modify list elements

Given a list of numbers, multiply each number by 2 using a while loop (change the list directly).

"""

def main():

    list_numbers = [2, 5, 8, 10]
    
    index = 0


    while index < len(list_numbers):
        list_numbers[index] *= 2
        index +=1
    
    print(list_numbers)



if __name__ == '__main__':
    main()