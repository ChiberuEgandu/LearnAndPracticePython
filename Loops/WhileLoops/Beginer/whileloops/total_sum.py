"""
Sum Until Zero
Keep asking the user for numbers and add them together. Stop when the user enters 0. Print the total sum.
"""

def sum_total():

    total = 0

    while True: 
        input_number = int(input("Enter numbers to add together. Enter 0 to stop: "))

        if input_number != 0:
            total += input_number
        else:
            break
    return total



def main():
    
    results = sum_total()

    print(f"The sum of your numbers is {results}")
    
if __name__ == '__main__':
    main()