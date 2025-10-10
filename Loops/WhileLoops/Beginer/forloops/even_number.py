"""
Even Numbers Only
Print all even numbers between 1 and 50.

"""

def even_numbers():

    for number in range(1, 51):
        if number % 2 == 0:
            print(number, end=' ')

def main():
    even_numbers()

if __name__ == '__main__':
    main()