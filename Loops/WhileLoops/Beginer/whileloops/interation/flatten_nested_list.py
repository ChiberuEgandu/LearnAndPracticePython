"""
Flatten a nested list (one level deep)

Example: [[1, 2], [3, 4], [5]] → [1, 2, 3, 4, 5] using only while loops.
"""


def main():

    list = [
        [1, 2], 
        [3, 4], 
        [5]]
    
    new_list = []
    #len of list is 3
    index_rows = 0

    while index_rows < len(list):
        index_column = 0
        while index_column < len(list[index_rows]):
            print(list[index_rows][index_column], end= ' ')
            new_list.append(list[index_rows][index_column])
            index_column += 1
        print()
        index_rows +=1

    print(new_list)

    


if __name__ == '__main__':
    main()