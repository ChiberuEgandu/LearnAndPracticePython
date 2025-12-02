def main():
    #Create a list of numbers [1, 2, 3, 4, 5] and: 
    list_nums = [1, 2, 3, 4, 5]
    # Print the first and last element
    print(list_nums[0])
    # Append a number to the end
    list_nums.append(6)
    print(list_nums)
    # Remove the number 3
    list_nums.remove(3)
    print(list_nums)
    # Replace the 2nd element with 99
    list_nums[1] = 99
    print(list_nums)

    #print list in reverse using splicing
    print(list_nums[::-1])

if __name__ == '__main__':
    main()
