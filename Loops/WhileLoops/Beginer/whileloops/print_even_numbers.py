"""
Even Numbers Only
Print all even numbers from 2 to 50.

"""

def even_numbers():

    numbers = 2

    while numbers <= 50: 
        if numbers % 2 == 0:
            print(numbers)
        numbers += 1
            

def main():

    even_numbers()


if __name__ == '__main__':
    main()