"""
Keep Asking for Password
Keep asking for a password until the user types "letmein".
"""

def main():

    password = "letmein"

    guess = input("Please enter the password: ")

    while guess != password:
        guess = input("Ops. Wrong password. Guess again: ")
    
    print(f"Good job!. You guessed the correct password {password}")

if __name__ == '__main__':
    main()