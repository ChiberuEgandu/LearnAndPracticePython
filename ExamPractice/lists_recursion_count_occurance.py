"""
2. Count occurrences of an element in a list

Goal: Count how many times a specific element appears in a list using recursion.

Example:

def count_occurrences(lst, target):
    pass

print(count_occurrences([1, 2, 3, 2, 4, 2], 2))  # → 3
"""

def count_occurances(list, target):

    if list == []:
        return 0
    else:
        if list[0] == target:
            return 1 + count_occurances(list[1:], target)
        else:
            return count_occurances(list[1:], target)
        





def main():

    my_list = [1, 2, 3, 2, 4, 2]
    
    print(count_occurances(my_list, 2))

if __name__ == '__main__':
    main()

