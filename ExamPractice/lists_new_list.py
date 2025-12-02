"""
4. Reverse a list recursively

Goal: Return a new list with the elements reversed.

Example:

def reverse_list(lst):
    pass

print(reverse_list([1, 2, 3, 4]))  # → [4, 3, 2, 1]


Hint:

Base case → if list is empty, return empty list.

Recursive case → take last element + reverse of the rest.
"""

def reverse_list(lst):

    if lst == []:
        return []
    else:
        return [lst[-1]] + reverse_list(lst[:-1])



def main():

    print(reverse_list([1, 2, 3, 4]))

if __name__ == '__main__':
    main()