
def main():

    numbers = [
        [10, 15, 22],
        [3, 8, 12],
        [7, 14, 5]]


    row = 0 
    count = 0

    while row < len(numbers):
        col = 0
        while col < len(numbers[row]):
            if numbers[row][col] % 2 == 0:
                count += 1
            col += 1
        row += 1

    print(f"The total count of even using  is while is {count} ")


    

if __name__ == '__main__':
    main()