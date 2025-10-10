"""
Goal:
Given a nested list, use while loops to create a new single list containing all the elements.

Example:
Input:

nested = [[1, 2], [3, 4, 5], [6]]

"""


def main():

    nested_list = [
        [1, 2], 
        [3, 4, 5], 
        [6]
        ]

    new_list = []

    rows = 0 
    
    while rows < len(nested_list):
        column = 0
        while column < len(nested_list[rows]):
            new_list.append(nested_list[rows][column])
            column += 1

        rows += 1
    
    print(f"My new list of numbers is = {new_list}")


if __name__ == '__main__':
    main()