"""
2. Count up to a number

Do the opposite — print from 1 up to n.

Hint: You can first go “down” recursively, then print on the way “back up”.
"""

def count_up(n):
    if n == 0:
        return
    count_up(n - 1)
    print(n)

def main():

    count_up(5)
if __name__ == '__main__':
    main()
