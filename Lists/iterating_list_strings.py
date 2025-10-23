"""
1. Print all characters

Write a program that prints every character from each word in the list:

words = ["cat", "dog", "fox"]
"""

def main():
    words = ["cat", "dog", "fox"]


    #using for loop
    for word in words:
        for letter in word:
            print(letter)
    

    print('\n')
    #using while loop

    i = 0
    
    while i < len(words):
        j = 0 
        while j < len(words[i]):
            print(words[i][j])
            j += 1
        i +=1
    

    #using joini to join all list items 
    new_word = ''.join(words)
    print(new_word)

    #converting the joined word to list 
    split_word = list(new_word)
    print(split_word)

    #then using for loop to print the letters
    for letter in split_word:
        print(letter)

    #using while to print the letters
    c = 0
    while c < len(split_word):
        print(split_word[c])
        c += 1


if __name__ == '__main__':
    main()