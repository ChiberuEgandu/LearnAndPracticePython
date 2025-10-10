"""
Given a list of numbers, calculate the total sum using a while loop.

Example:
Input: [2, 5, 7, 1]
Output: Total = 15

Hint:
"""

def sum_list():

    numbers = [2, 5, 7, 1]

    index = 0
    sum = 0

    while index < len(numbers):
        sum+= numbers[index]
        index += 1
    

    print(f"The sum of the {numbers} list is {sum}")



def main():
    
    sum_list()

if __name__ == '__main__':
    main()