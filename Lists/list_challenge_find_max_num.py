"""
Exercise 3 Find maximum value manually

Without using max(), use a while loop to find the largest number in:

scores = [12, 45, 7, 32, 19, 50]
"""


def main():

    scores = [12, 45, 7, 90, 32, 19, 50]

    max = scores[0]
    print(scores[0])


    i = 0

    while i < len(scores):
        current_number = scores[i]
        if current_number >= max:
            max = current_number
        i += 1
    
    print(max)


    #using while loop


if __name__ == '__main__':
    main()