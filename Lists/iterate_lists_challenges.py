"""

Question 1:  Write a program that counts how many numbers are in the list: numbers = [4, 7, 2, 9, 1, 5]
"""


def main():

    numbers = [4, 7, 2, 9, 1, 5]

    count_for_loop = 0

    #Using for loop
    for number in numbers:
        print(number,end=' ')
        count_for_loop += 1
    
    print(f"Count using forloop is: {count_for_loop}")
    #How many numbers using a for loop
    

    print("\n")

    #using while loop 
    i = 0 
    count = 0

    while i < len(numbers):
        print(numbers[i], end=' ')
        count += 1
        i += 1
    
    print(f"Count using whileloop is: {count_for_loop}")
    
    print("\n")

if __name__ == '__main__':
    main()