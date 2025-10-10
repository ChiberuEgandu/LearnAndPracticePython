"""
Goal:
Use a while loop to find and print the largest number in a list.

Example:
Input: [4, 9, 1, 6, 2]
Output: Largest number is 9

Hint:
Start by assuming the first item is the largest and update as you loop.
"""

def main():

    numbers = [4, 9, 1, 6, 2]

    largest_number = numbers[0]
    print(largest_number)

    index = 1

    while index < len(numbers):
        current_number = numbers[index]

        if current_number > largest_number:
            largest_number = current_number
        index += 1
    
    print(f"The largest number in the list {numbers} is {largest_number}")
        


if __name__ == "__main__":
    main()