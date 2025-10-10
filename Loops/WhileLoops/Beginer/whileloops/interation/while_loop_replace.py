"""
Replace negatives

Replace every negative number in a list with 0.

"""

def replace_negatives():

    numbers = [10 , 8 , -5, 29, -34, 30, -2]

    index = 0 
    count = 0

    while index < len(numbers):
        if numbers[index] < 0:
            numbers[index] = 0
            count +=1
        index +=1
    
    print(numbers)
    print(f"There were {count} negative values replaced")



def main():

    replace_negatives()


if __name__ == '__main__':
    main()