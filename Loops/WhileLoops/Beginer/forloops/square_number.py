"""
Squares of Numbers
Print the squares of numbers from 1 to 10.
"""


def square_number():
    
    for number in range(1, 11):
        square = number  ** 2
        print(square)



def main():
        square_number()

if __name__ == '__main__':
    main()