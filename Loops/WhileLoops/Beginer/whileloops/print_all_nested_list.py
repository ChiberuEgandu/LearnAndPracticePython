"""

Goal:
Given a nested list (a list that contains other lists), use nested while loops to print each individual item.

Example:
Input:

numbers = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
"""

def two_d_list():

    numbers = [
        [1, 2, 3], 
        [4, 5],
        [6, 7, 8, 9]]
    
    rows = 0

    while rows < len(numbers):
        column = 0
        while column < len(numbers[rows]):
            print(numbers[rows][column])
            column +=1

        rows += 1


def main():

    two_d_list()

if __name__ == '__main__':
    main()
        

