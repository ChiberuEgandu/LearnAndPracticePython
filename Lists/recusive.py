



def mystry(n):
    
    if n < 0:
        return 2 * n 
    else:
        return mystry(n - 1) + n 

def main():
    print(mystry(3))

if __name__ == '__main__':
    main()