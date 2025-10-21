"""
Goal: Ask the user for a string and print it reversed.
Example:
Input → hello
Output → olleh

Hint: Use slicing word[::-1].
"""



def main():

    number = int(input("Please provide a number : "))

    while True:
        if number < 0:
            number = int(input("Try again. Provide a number greater than 1: "))
        else:
            break
    
    if number % 2 == 0:
        print(f"The number {number} you entered is Even")
    else:
        print((f"The number {number} you entered is Odd"))
    
    


        




if __name__ == '__main__':
    main()