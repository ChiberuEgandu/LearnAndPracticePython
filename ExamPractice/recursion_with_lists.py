

#def sum_list(lst):
    # base case: empty list
    # recursive case: first + sum of the rest
    # Example: [2, 4, 6] → 12

def sum_list(my_list1):
    if my_list1 == []:
        return 0
    else:
        return my_list1[0] + sum_list(my_list1[1:])


#2. Count occurrences of a target
    # base case: empty list → return 0
    # if first matches target → 1 + recursion on rest
    # else → recursion on rest
    # Example: [1, 2, 2, 3], target=2 → 2
def count_occurrences(my_list2, target):
    if my_list2 == []:
        return 0
    if my_list2[0] == target:
        return 1 + count_occurrences(my_list2[1:], target)
    else: 
        return count_occurrences(my_list2[1:], target)

#Find the maximum number
    # base case: one element → return it
    # recursive case: compare first with max of rest
    # Example: [3, 7, 1, 9, 2] → 9

def find_max(my_list3):
    if len(my_list3) == 1:
        return my_list3[0]
    else:
        # Get the biggest number in the rest of the list
        max_rest = find_max(my_list3[1:])
        
        # Compare the first number with the biggest of the rest
        if my_list3[0] > max_rest:
            return my_list3[0]
        else:
            return max_rest
        


def countDownAndUp(number):
    print(number)
    if number == 0:
    # BASE CASE
        print('Reached the base case.')
        return
    else:
    # RECURSIVE CASE
        countDownAndUp(number - 1)
        print(number)



    


def main():

    print(sum_list( [2, 4, 6]))

    print(count_occurrences([1, 2, 2, 3], 2))

    print("\n")
    countDownAndUp(3)

if __name__ == '__main__': 
    main()