"""
Odd Numbers Only
Print all odd numbers between 1 and 50.
"""
def odd_numbers():

    for number in range(1, 51):
        if number % 2 != 0:
            print(number, end=' ')
    


def main():
    odd_numbers()

if __name__ == '__main__':
    main()