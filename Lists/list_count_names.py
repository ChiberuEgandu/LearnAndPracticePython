"""
Given a list of names, count how many names start with the letter “A”.

"""

def main():

    list_names = ["John", 'Adam', 'Nick', 'Angenla', 'Alex']

    i = 0 
    count = 0

    while i < len(list_names):
        if list_names[i][0] == 'A':
            count += 1
        i += 1
    
    print(f"The count of all names that start with A is {count}")

if __name__ == '__main__':
    main()

