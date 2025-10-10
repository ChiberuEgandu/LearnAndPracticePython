"""
Goal:
Use a while loop to create a new list that has the elements of the original list in reverse order.

Example:
Input: [10, 20, 30, 40]
Output: [40, 30, 20, 10]

Hint:
Start from the last index (len(list) - 1) and move backwards.
"""

def main():

    numbers = [10, 20, 30, 40]
    
    new_list_numbers = []

    i = len(numbers) - 1

    print(i)

    while i >= 0:
        new_list_numbers.append(numbers[i])
        i-= 1
    

    print(f" My reverse list of numbers is = {new_list_numbers}")


if __name__ == '__main__':
    main()