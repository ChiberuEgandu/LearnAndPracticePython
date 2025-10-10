"""
Exercise 3: Create a flattened list
Write a program that uses nested while loops to create a new, "flattened" list that contains all the elements from the nested list in a single, one-dimensional list. 
Input: nested_list = [[10, 20], [30, 40], [50, 60]]
Desired output: [10, 20, 30, 40, 50, 60] 

"""

def main():

    nested_list = [
        [10, 20], 
        [30, 40], 
        [50, 60]]
    
    flat = []

    index_rows = 0

    while index_rows < len(nested_list):
        index_columns = 0

        while index_columns < len(nested_list[index_rows]):
            flat.append(nested_list[index_rows][index_columns])
            index_columns +=1
        
        index_rows += 1

    print(flat)



if __name__ == '__main__':
    main()