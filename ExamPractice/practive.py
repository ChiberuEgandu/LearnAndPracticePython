"""
Print the numbers from 1 to 10 using a for loop.



"""


def main():

    my_string = "a dog is using and eating"
    vowels = ["a", "e", "i", "o", "u"]

    my_vowel_list = []

    count = 0

    for vowel in range(len(my_string)):
        if my_string[vowel] in vowels :
            count +=1
            my_vowel_list.append(my_string[vowel])
    
    print(f"There are {count} vowels and they are {my_vowel_list}")



if __name__ == '__main__':
    main()