"""
Lists

Iterate over a list
Given numbers = [2, 4, 6, 8], write a program that prints each number squared.

Append to a list
Create an empty list and ask the user to enter 5 numbers. Append each number to the list and then print the list.

Combined exercise
Given words = ["cat", "dog", "bird"], append "fish" and print all words in uppercase using a loop.
"""

def main():

    numbers = [2, 4, 6, 8]

    #forloop 
    for num in numbers:
        print(num)
    print("\n")
    #while loop
    i = 0 
    while i < len(numbers):
        print(numbers[i])
        i += 1

    #Given numbers = [2, 4, 6, 8], write a program that prints each number squared.
    nums = 0

    for number in numbers:
        print(f"The number {number} squared is {number * 2}")



    #Append new values to a list   

    new_numbers = []

    while True:

        user_input = int(input("Please provide 5 numbers:  "))

        if user_input == 0:
            break
        else:
            new_numbers.append(user_input)
    
    print(f"My new list is {new_numbers}")



    #Given words = ["cat", "dog", "bird"], append "fish" and print all words in uppercase using a loop.

    words = ["cat", "dog", "bird"]
    words.append("fish")
    print(words)




if __name__ == '__main__':
    main()
