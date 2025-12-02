#Start with the second element (index 1).
#Compare it to the elements before it.
#Move the bigger elements to the right.
#Place the current element in the correct position.
#repeat for all elements.

def insertion_sort(arr):

    #start indexing at 1 because the first element is already sorted
    for i in range(1, len(arr)):
        key = arr[i] # This is the element we would like to insert
        j = i - 1 #comparing with the element before it

        #move the elements that are greater than the key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] == arr[j]
            j -= 1
        

        #place the key in it's correct possition 
        arr[j + 1] = key

    
    return arr


def main():

    print(insertion_sort([9, 3, 1, 7]))
    
if __name__ == '__main__':
    main()