"""
Countdown with “Blastoff”.
Input: n=3 → Output: 3 2 1 Blastoff!
Stop when you hit 0
"""


def blast_off(n):

    if n < 1:
        print("Blast Off")
    else:
        print(n)
        blast_off(n - 1)



def main():

    blast_off(3)
if __name__ == '__main__':
    main()