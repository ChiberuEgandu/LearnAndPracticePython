
"""
This program must be submitted in a file called passwordify.py in your Lab 4 repository. 

3. Given a list: board = [ 

['x', '-', 'x'],  

['o', '-', '-'], 

['-', '-', '-'] 

] 

Write a function called: nested_loops () to print the matrix in the given format.  
"""

def nested_loops():
    board = [ 

    ['x', '-', 'x'],  

    ['o', '-', '-'], 

    ['-', '-', '-'] 

    ] 
    
    row = 0

    while row < len(board):
        column = 0
        while column < len(board[row]):
            print(board[row][column], end = '')
            column += 1
        print("\n")
        row += 1





def main():

    nested_loops()

if __name__ == '__main__':
    main()