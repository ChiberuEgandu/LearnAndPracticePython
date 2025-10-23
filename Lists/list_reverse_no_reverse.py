"""
10. Write a program that reverses a list without using reverse().
"""

def main():

    list = [1,2,3,4,5,6,7]
    
    i = len(list) - 1

    while i >= 0:
        print(list[i])
        i -= 1

if __name__ == '__main__':
    main()