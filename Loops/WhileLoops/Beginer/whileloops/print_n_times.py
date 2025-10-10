"""
Print a Word N Times
Ask the user for a word and a number. Print that word N times
"""


def main():

    word = input("Please provide a word: \n")
    number = int(input("How many times do you want to print the word: \n"))

    count = 1


    while count <= number:
        print(word)
        count += 1


if __name__ == '__main__':
    main()