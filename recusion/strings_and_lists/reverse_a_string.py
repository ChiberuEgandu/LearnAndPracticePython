"""

Reverse a string.
"cat" → "tac"
Last char + reverse(rest).
"""

def reversed_string(s):

    if len(s) == 0:
        return  ""
    else:
        return s[-1] + reversed_string(s[:-1])




def main():

    string = 'cat'

    print(reversed_string(string))


if __name__ == '__main__':
    main()