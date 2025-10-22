"""
Append a new element to a list and print the updated list.
"""

def main():

    list = ['dog', 'cow']

    #Using Append function/method
    list.append("horse")
    print(list)

    #Using extend to add multiple items
    list.extend(["cat", 'sheep'])
    print(list)

    #using for loop 
    new_items = ["goat", "fish", "fly"]
    
    for items in new_items:
        list.append(items)
    
    print(list)

    # using while loop 

    more_items = ["bird", "lion"]
    i = 0 
    
    while i < len(more_items):
        list.append(more_items[i])
        i += 1
    print(list)
    




if __name__ == '__main__':
    main()