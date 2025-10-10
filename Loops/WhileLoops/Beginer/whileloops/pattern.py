"""
Print a Pattern
Print:

*
**
***
****
*****


using a while loop.
"""

def main():
    char = " * "
    count = 1

    while count <= 5: 
        print(f"{char * count}")
        count += 1



if __name__ == '__main__':
    main()