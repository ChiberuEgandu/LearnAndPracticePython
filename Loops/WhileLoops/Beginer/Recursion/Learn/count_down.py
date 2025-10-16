"""
Countdown

Goal: See the “top-down” order (opposite of exercise 1).

def countdown(n):
    if n == 0:
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)

"""
def count_down(n):
    if n == 0:
        print("Blask Off!")
        return
    else:
        print(n)
        count_down(n - 1)





def main():

    count_down(5)

if __name__ == '__main__':
    main()