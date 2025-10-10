"""
Exercise 1: Summing all elements
Write a program that uses nested while loops to find the sum of all the numbers in the following list of lists.
Input: numbers = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
Desired output: 45
"""

def main():

    numbers = [
        [1, 2, 3], 
        [4, 5], 
        [6, 7, 8, 9]
        ]
    
    index_rows = 0 
    sum_rows = 0 

    while index_rows < len(numbers): #index_rows = 0 and the len of numbers is 3. This evaluates to True
        index_columns = 0
        sum_columns = 0
        while index_columns < len(numbers[index_rows]): #index column is 0 and 0 is less than the len of  3 
            sum_columns += numbers[index_rows][index_columns]
            index_columns += 1
            
        print(sum_columns)

        sum_rows += sum_columns
        index_rows += 1

    print(sum_rows)



if __name__ == '__main__':
    main()