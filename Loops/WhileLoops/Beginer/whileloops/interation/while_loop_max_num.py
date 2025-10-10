"""
Exercise 2: Find the maximum number
Write a program that uses nested while loops to find and print the largest number from the given list of lists.
Input: data = [[10, 2, 8], [4, 15], [3, 9, 21, 6]]
Desired output: 21

"""

def main():

    data = [
        [10, 2, 8], 
        [4, 15], 
        [3, 9, 21, 6]]
    
    index_rows = 0
    largest_number_rows = data[0]
    largest_number = data[index_rows][0]

    while index_rows < len(data):
        index_column = 1
        

        while index_column < len(data[index_rows]):
            current_number = data[index_rows][index_column]

            if current_number > largest_number:
                largest_number = current_number
                print(largest_number)
            index_column += 1
            


if __name__ == '__main__':
    main()