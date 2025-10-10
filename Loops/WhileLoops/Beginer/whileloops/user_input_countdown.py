"""
Countdown Timer
Ask the user for a number and count down to 0 using a while loop.

Enter a number: 5
5
4
3
2
1
Blast off!

"""

def user_input_countdown():

    
    user_input = int(input("Enter a number: "))

    while user_input > 0:
        print(user_input)
        user_input -= 1

        
    print("Blast Off")
    







def main():

    user_input_countdown()

if __name__ == '__main__':
    main()