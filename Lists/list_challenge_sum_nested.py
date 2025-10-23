"""

Use a for loop to find the total sum of all numbers inside this nested list:

matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
"""

def main():

    matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
    ]

    #for loop 

    total_inner_for = 0

    for items in matrix:
        for number in items:
            total_inner_for += number

    print(total_inner_for)


    # using while loop

    """
    matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
    ]

    """

    row = 0
    total_while_out = 0
    
    while row < len(matrix):
        column = 0
        total_while_inner = 0
        while column < len(matrix[row]):
            total_while_inner += matrix[row][column]

        row +=1 
    print()

        






if __name__ == '__main__':
    main()