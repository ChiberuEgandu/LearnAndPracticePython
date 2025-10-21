"""
Check even or odd (no %).
Input: 4 → “Even”
Subtract 2 until 0 or 1.

"""

def even_number(n):

    if n == 0:
        return "Even"
    elif n == 1:
        return "Odd"
    else:
        return even_number(n - 2)




def main():

    print(even_number(5))

if __name__ == '__main__':
    main()