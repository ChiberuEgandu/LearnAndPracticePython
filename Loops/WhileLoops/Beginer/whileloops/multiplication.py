"""
Multiplication Practice
Ask the user for a number and print its multiplication table (1–10) using a while loop.

Enter a number: 3
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
"""

def main():

    user_input = int(input("What number should we build a multiplication table for: "))
    limit = int(input("Up to what number should multiply: "))
    
    number = 1
    

    while number <= limit:
        print(f"{user_input} x {number} = {user_input * number} ")
        number += 1
        
    


if __name__ == '__main__':
    main()