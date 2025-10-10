"""
Count Down by Twos
Start from 100 and count down by 2s until you reach 0.

"""

def count_down_twos():

    number = 100

    while number >= 0:
        print(number)
        number -= 2
    

def main():

    count_down_twos()

if __name__ == '__main__':
    main()