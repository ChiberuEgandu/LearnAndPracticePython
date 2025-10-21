"""
Count digits in a number.
Input: 12345 → Output: 5
Divide by 10 each time until 0.

"""

def count_digits(n):

    if n == 0:
        return 0
    
    else:
        return 1 + count_digits(n // 10)
    


def main():

    numbers = 1234
    print(count_digits(numbers))

if __name__ == '__main__':
    main()
    