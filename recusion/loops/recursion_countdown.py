

##Count down 


def recursive_countdown(n):

    if n == 0:
        print("Blast Off!")
    else:
        print(n)
        recursive_countdown(n - 1)
    

recursive_countdown(9)
