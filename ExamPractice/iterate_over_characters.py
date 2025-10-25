"""
1. Iterate over characters
Write a program that asks the user for a word, then prints each character on a new line.
"""

def main():

    while True:
        user_word = input("Please Provide a word: ").lower()

        if user_word.isalpha():
            break
        else:
            print("Invalid Input: Please enter a string!")
    

    print(f"Your word is {user_word}")

    #print using for loop

    for letter in user_word:
        print(letter)

    print("\n")

    #using while loop 

    i = 0
    while i < len(user_word):
        print(user_word[i])
        i += 1



        

if __name__ == '__main__':
    main()
