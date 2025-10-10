"""
Double the Number
Keep asking the user for a number and print double of it until they type 0.

"""


def main():


    while True:

        user_input = int(input("Enter a number to double. Enter 0 to quit: "))

        if user_input == 0:
            break
        else:
            double = user_input * 2
            print(f"The double of {user_input} is {double}")

    print("Thanks for playning!")


if __name__ == '__main__':
    main()