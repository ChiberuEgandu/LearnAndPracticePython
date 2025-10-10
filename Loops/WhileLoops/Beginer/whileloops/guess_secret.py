"""
Guess the Secret Word
Set a secret word (e.g., "python"). Keep asking the user to guess it until they're correct.
"""

def main():

    secret = "food"

    while True:
        guess_word = input("Guess the secrete word: ").lower()

        if guess_word == secret:
            print(f"Good job you guessed the secrete word {secret}")
            break
        else:
            continue

if __name__ == '__main__':
    main()