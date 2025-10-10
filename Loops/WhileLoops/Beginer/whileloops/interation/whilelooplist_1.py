"""
Print all elements

Given a list of fruits, print each fruit using a while loop.
"""

def main():
    fruits = ["bananas", "apples", "peach", "orange", "grapes"]
    index = 0 

    while index < len(fruits):
        print(f"Index {index}  =",fruits[index])
        index += 1


if __name__ == '__main__':
    main()