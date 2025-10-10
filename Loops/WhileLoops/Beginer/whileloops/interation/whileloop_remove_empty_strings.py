"""
Remove empty strings
Given a list that contains some empty strings, remove them using a while loop.
"""

def main():

    list_of_string = ["apples", " ", "tomatoes", " ", " ", "grabes"]
    print(list_of_string)
    print(len(list_of_string))

    index = 0

    while index < len(list_of_string):
        if list_of_string[index] == " ":
            list_of_string.remove(list_of_string[index])
        else:
            index += 1
    
    print(list_of_string)


if __name__ == '__main__':
    main()