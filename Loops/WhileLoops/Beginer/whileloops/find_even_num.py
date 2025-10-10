"""
Goal:
From a list of numbers, create a new list that only contains the even numbers.
Use a while loop (no for loops, no list comprehensions).

Example:
Input: [3, 8, 5, 12, 7, 6]
Output: [8, 12, 6]
"""

def even_num():

    numbers = [3, 8, 5, 12, 7, 6]

    new_numbers = []

    i = 0

    while i < len(numbers):
        if numbers[i] % 2 == 0:
            new_numbers.append(numbers[i])
        i += 1
    
    print(f"My list of even numbers is {new_numbers}")







def main():

    even_num()

if __name__ == '__main__':
    main()