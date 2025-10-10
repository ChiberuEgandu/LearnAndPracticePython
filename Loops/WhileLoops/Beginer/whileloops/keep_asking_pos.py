"""
Keep Asking for Positive Numbers
Keep asking for numbers until the user enters a negative one.
"""

def main():
    
    number = int(input("Please provide a negative number: "))

    while number > 0:
        number = int(input("Please enter a negative number: "))

    print(f" Great job. You entered {number}. A negative number")



if __name__ == '__main__':
    main()