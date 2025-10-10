"""
Count elements

Without using len(), count how many elements are in a list using a while loop.

"""

def main():

    fruits = ["bananas", "apples", "peach", "orange", "grapes"]

    index = 0
    count = 0

    while index < len(fruits):
        count += 1
        index += 1
    
    print(f" There are {count} elements in the list")


if __name__ == '__main__':
    main()