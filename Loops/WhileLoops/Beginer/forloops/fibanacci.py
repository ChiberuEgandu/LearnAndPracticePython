def fib(n):

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        i = 1
        current = 1
        previous = 0

        while n > i:
            next = previous + current
            previous = current
            current = next
            i +=1
        result = current
    return result




def main():

    number = 4
    fib_seq = fib(number)
    print(fib_seq)


        


if __name__ == '__main__':
    main()
