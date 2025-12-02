def binary_search(arr, target):  #arr is the list and target is the number we are trying to find

    #left and right are our starting and ending points
    left = 0 #start of the arr
    right = len(arr) - 1 #end of the arr

    #find the middle 
    while left <= right:
        mid = (left + right) // 2

        #check if the middle value is the target
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1 
        
        else:
            right = mid - 1
    return -1 

numbers = [1, 3, 5, 7, 9, 11]
result = binary_search(numbers, 7)
print(result)  # Output: 3
        


