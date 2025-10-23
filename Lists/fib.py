"""
fib using while 
"""

def fib(n):

    if n == 0:
        result == 0
    elif n == 1:
        result == 1
    else:
        i  = 1
        current = 1
        prevous = 0

        while n > i:
            i += 1
            next = prevous + current
            prevous = current
            current = next 
            result = current 
        return result 

    



def main():

    print(fib(5))



if __name__ == '__main__':
    main()