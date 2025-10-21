"""
Sum digits.
Input: 1234 → Output: 10
"""
def sum_digits(numbers):

    if numbers == 0:
        return 0 
    else:
        return numbers + sum_digits(numbers // 10)



def main():

    values = 1234

    print(sum_digits(values))


if __name__ == '__main__':
    main()