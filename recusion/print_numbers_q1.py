"""
Print numbers from 1 to n.
Input: n=5 → Output: 1 2 3 4 5
Print smaller numbers first, then the current one.
"""

def print_numbers(n):

    if n < 1:
        return
    else:
        print_numbers(n - 1)
        print(n)
    


def main():

    print_numbers(5)
    
if __name__ == '__main__':
    main()