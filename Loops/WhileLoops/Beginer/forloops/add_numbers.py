"""
Sum of Numbers
Add all numbers from 1 to 100 using a for loop.

"""

def add_all_numbers():
    total = 0

    for number in range(1, 101):
        total += number
        
    print(f"The sum of all numbers is 1 - 100 is {total} ")

def main():
    add_all_numbers()

if __name__ == '__main__':
    main()