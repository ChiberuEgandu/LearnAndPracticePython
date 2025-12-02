
def square(my_array):
    squared_array = []
    for i in range(len(my_array)):
        squared_value = my_array[i] ** 2

        squared_array.append(squared_value)
    return squared_array

def main():
    
    og_array = [1,2,4,6,10]
    
    print("Squared Array:", square(og_array))


if __name__ == '__main__':
    main()