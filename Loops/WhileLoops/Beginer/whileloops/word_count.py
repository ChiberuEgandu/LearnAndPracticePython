"""
Count Characters
Ask the user for a word. Use a while loop to count how many characters it has (without using len()).
"""

def word_count():
    
    word = input("Please provide a word")

    count_charactors = 0

    while count_charactors < word: 
        count_charactors += 1

    return count_charactors



def main():

    results = word_count()
    print(results)

if __name__ == '__main__':
    main()