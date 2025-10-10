"""
Keep Asking Until Even
Keep asking the user for a number until they give you an even number.
"""


def main():
    
    even_number = int(input("Please provide and even number"))

    while even_number % 2 != 0:
        even_number = int(input("Please keep providing numbers until its even:"))
    
    print(f"Good job the number {even_number} is even")


if __name__ == '__main__':
    main()