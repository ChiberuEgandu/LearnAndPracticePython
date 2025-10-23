"""
6. Write a program that prints each item in a list of animals, one per line.
"""

def main():

    list_animals = ['dog', 'cow', 'horse', 'cat', 'sheep', 'goat', 'fish', 'fly', 'bird', 'lion']

    #using for loop 
    for animal in list_animals:
        print(animal)

    #using while loop
    i = 0
    while i < len(list_animals):
        print(list_animals[i])
        i += 1

if __name__ == '__main__':
    main()