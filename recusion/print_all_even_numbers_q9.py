"""
Print all even numbers up to n.
Input: n=6 → Output: 2 4 6
Skip by +2 each recursion.

"""

def all_even_num(n):

    if n == 0:
        return
    else:
        all_even_num(n - 1)

        if n % 2 == 0:
            print(n, end = ' ')



def main():

    all_even_num(6)
if __name__ == '__main__':
    main()

