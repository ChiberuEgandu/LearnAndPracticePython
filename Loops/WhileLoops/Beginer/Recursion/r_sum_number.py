"""
LEVEL 2 — Return Values Instead of Just Printing

Now your recursive functions will return something.

3. Sum of numbers from 1 to n

"""

def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)


def main():
    
    sum_to_n(5)

if __name__ == '__main__':
    main()

