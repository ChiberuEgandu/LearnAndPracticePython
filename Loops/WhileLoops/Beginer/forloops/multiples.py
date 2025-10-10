"""
Multiplication Table (Fixed)
Print the multiplication table for 5:
"""

def multiples():

    multiple = 5

    for number in range(1, 11):
        print(f"{multiple} x {number} = {multiple * number}")

    
def main():
    multiples()

if __name__ == '__main__':
    main()