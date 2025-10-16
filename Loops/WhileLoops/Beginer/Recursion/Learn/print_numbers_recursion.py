"""
Print Numbers from 1 to n

Goal: Practice a simple base case and recursive call.

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)   # recursive call
    print(n)

"""

def print_numbers(n):
    if n == 0:
        return #base
    else:
        print_numbers(n - 1)  #recursive 
        print(n)





def main():

    print_numbers(5)

if __name__ == '__main__':
    main()