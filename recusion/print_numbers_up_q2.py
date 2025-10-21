"""
Print numbers from n to 1.
Input: n=4 → Output: 4 3 2 1
Print the current number first, then recurse.
"""

def print_numbers_down(n):

    if n == 0:
        return
    else:
        print(n)
        print_numbers_down(n - 1)



def main():

    print_numbers_down(5)

if __name__ == '__main__':
    main()
