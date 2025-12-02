"""

"""
#Write a recursive function sum_list(lst) that returns the sum of all elements in a list.
def  sum_list(num_list):
    if num_list == []:
        return 0
    else:
        return num_list[0] + sum_list(num_list[1:])
    

def count_o(list_num, target):
    if list_num == []:
        return 0
    elif list_num[0] == target:
        return 1 + count_o(list_num[1:0], target)
    else:
        return count_o(list_num[1:0], target)



def main():

    print(sum_list([1,2,3]))
    print(count_o([1,2,3,2,4,2], 2))

if __name__ == '__main__':
    main()