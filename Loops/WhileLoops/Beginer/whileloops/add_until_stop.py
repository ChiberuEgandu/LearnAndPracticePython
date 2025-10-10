"""
Sum Until “stop”
Keep asking the user for numbers until they type "stop", then print the total.

"""


def sum_until_stop():
    total = 0 

    while True:

        user_input = input("Please Enter a number: ")

        if user_input.lower() == 'stop':
            break

        total += int(user_input)
    
    return total
    
    


def main():

    results = sum_until_stop()
    print(f"The sum of all your numbers is = {results}")
if __name__ == '__main__':
    main()