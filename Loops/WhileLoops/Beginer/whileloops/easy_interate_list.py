"""
Given a list of fruits, print each item using a while loop.

Example:
Input list: ["apple", "banana", "cherry"]

"""

def fruits():

    list =["apple", "banana", "cherry"]

    index = 0

    while index < len(list):
        print(list[index], end= ' ')
        index += 1



def main():

    fruits()

if __name__ == '__main__':
    main()