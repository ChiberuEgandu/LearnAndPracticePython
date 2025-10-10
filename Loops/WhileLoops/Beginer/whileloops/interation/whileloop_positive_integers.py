"""
Filter positive numbers

Given a list of integers, print only the positive ones.
"""

def positive_int():

    values = [ 23, -45, 20 ,-85 ,63, -71, 52, 88]

    index = 0

    while index < len(values):
        if values[index] > 0:
            print(values[index])
        index +=1
    



def main():

    positive_int()

if __name__ == '__main__':
    main()
