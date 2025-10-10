"""
Guess the Number
The program picks a secret number (e.g. 7). Keep asking the user until they guess correctly.

"""
import random

def random_number():

    #generate random number 
    secrete_number = random.randint(1, 10)
    print(secrete_number)

    #ask user to guess 
    guess = int(input("Please gusess the random number between 1 and 10 : "))

    too_low_guesses = 0
    too_high_guess = 0

    while True:
        
        if guess < secrete_number:
            int(input("Too Small. Guess again: "))
            too_low_guesses += 1
        elif guess > secrete_number:
            int(input("Too Big. Try again"))
            too_high_guess += 1
        else:
            total_guesses = too_low_guesses + too_high_guess
            print(f"Good job you guess the secrete number {secrete_number}. You guessed {too_high_guess} times too high and {too_low_guesses} time too low. A total of {total_guesses} times.")
            break





def main():
    random_number()

if __name__ == '__main__':
    main()