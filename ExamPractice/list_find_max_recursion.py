"""
3. Find the maximum number in a list recursively

Goal: Return the largest number in a list using recursion.

Example:

def find_max(lst):
    pass

print(find_max([3, 7, 1, 9, 2]))  # → 9
"""

def find_max(nums):

    if len(nums) == 1:
        return nums[0]
    else:
        # Recursive case: compare first element with max of the rest
        rest_max = find_max(nums[1:])

        if nums[0] > rest_max:
            return nums[0]
        else:
            return rest_max




def main():

    print(find_max([3, 7, 1, 9, 2]))
    
if __name__ == '__main__':
    main()