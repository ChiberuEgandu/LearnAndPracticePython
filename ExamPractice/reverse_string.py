"""
3. Reverse a string manually

Without using slicing ([::-1]), use a loop to reverse a string and print the result.
"""

def reverse_string(string):

    if len(string) == 0:
        return " "
    else:
        return string[-1] + reverse_string(string[:-1])
    

def main():

    my_string = 'Hello'

    print(reverse_string(my_string))

if __name__ == '__main__':
    main()