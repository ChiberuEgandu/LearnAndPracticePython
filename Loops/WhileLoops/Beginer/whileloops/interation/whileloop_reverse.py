"""
Print in reverse order

Use a while loop to print the list elements starting from the end.

"""

def main():

    fruits = ["bananas", "apples", "peach", "orange", "grapes"]

    index = len(fruits) - 1

    while index >= 0:
        print(f"index: {index}: {fruits[index]}")
        index -= 1


if __name__ == '__main__':
    main()