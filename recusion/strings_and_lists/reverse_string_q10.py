"""
Reverse a string.
"cat" → "tac"
Last char + reverse(rest).
"""

def reverse(reset):

    if len(reset) < 0:
        return ""
    else:
        return reverse()



def main():

    word = "tac"

    print(reverse(word))


if __name__ == '__main__':
    main()