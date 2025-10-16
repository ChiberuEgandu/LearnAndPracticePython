"""

Write a function that returns the sum of all numbers in a list recursively.
"""

def sum_of_list(list):

    if len(list) == 0:   
        return 0 #Base case: list is empty
    else:
        #Recursive case: first element + sum of the rest of the list
        return list[0] + sum_of_list(list[1:])


def main():

    print(sum_of_list([2, 4, 6]))

if __name__ == '__main__':
    main()