"""
Sum numbers from 1 to n.
Input: n=5 → Output: 15
Return n + sum(n-1).
"""


def sum_numbers(n):

    if n  == 1:
        return 1 
    else:
        return n + sum_numbers(n - 1 )
    


def main():

    print(sum_numbers(5))

if __name__ == '__main__':
    main()
    