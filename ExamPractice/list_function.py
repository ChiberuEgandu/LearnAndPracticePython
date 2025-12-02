

#Write a function that takes a list and returns a new list with each number doubled.
# Example: [1, 2, 3] → [2, 4, 6]

def doubled_list(my_list):
    new_list = []

    for num in my_list:
        num *= 2
        new_list.append(num)
    return new_list


#Write a function that counts how many even numbers are in a list.
# Example: [1, 2, 3, 4] → 2

def even_numbers(my_even_list):
    count = 0
    for numbers in my_even_list:
        if numbers % 2 == 0:
            count += 1
    return count

#Write a function that sums all numbers in a list without using sum().(Just use a for loop.)
def sum_numbers(my_sum_list):

    sum = 0
    for i in range(len(my_sum_list)):
        sum += my_sum_list[i] 
    
    return sum

#Write a function that removes all negative numbers from a list.
# Example: [3, -1, 0, -2, 5] → [3, 0, 5]

def remove_negative(my_list_negative):

    for item_num in my_list_negative:
        if item_num < 0:
            my_list_negative.remove(item_num)
    
    return my_list_negative



def main():

    print(doubled_list([1,2,3]))

    results = even_numbers([1, 2, 3, 4])
    print(f"There are {results}")

    print(sum_numbers([1,2,3]))

    print(remove_negative([3, -1, 0, -2, 5]))



if __name__ == '__main__':
    main()