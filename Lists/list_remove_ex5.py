"""
Remove one element from a list using remove() or pop() and print it.
"""

def main():

    list = ['dog', 'cow', 'horse', 'cat', 'sheep', 'goat', 'fish', 'fly', 'bird', 'lion']

    #Using  remove()
    list.remove("fly")
    print(list)

    #Using remove with for loop

    to_remove = ["bird", "sheep"]
    for item in list:
        if item in to_remove:
            list.remove(item)

    print(list)


    #using a while loop

    i = 0

    while i < len(list):
        if list[i] == 'horse' or list[i] == 'cow' or list[i] == 'fish':
            list.remove(list[i])
        else:
            i +=1

    print(list)

if __name__ == '__main__':
    main()