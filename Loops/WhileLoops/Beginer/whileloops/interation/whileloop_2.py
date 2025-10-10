"""
Print with index

Print both the index and the item (e.g. “Index 0: apple”).
"""

def main():

    fruits = ["bananas", "apples", "peach", "orange", "grapes"]

    index = 0

    while index < len(fruits):
        print(f"Index {index} : {fruits[index]}")
        index += 1




if __name__ == '__main__':
    main()