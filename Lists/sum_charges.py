
def list(charges):

    sum = 0
    for i in range(len(charges)):
        sum += charges[i]
    
    return sum
        




def main():

    my_list = [1,2,3,1]

    print(list(my_list))

if __name__ == '__main__':
    main()