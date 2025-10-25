"""
2. String methods

Ask the user to enter a sentence. Then:

Print how many times the letter "a" appears

Print the sentence in uppercase

Replace all spaces with "-"

Check if the sentence starts with "Hello"
"""

def main():

    sentence = []

    while True:
        user_sentence = input("Please enter a sentence : ").lower()

        if len(user_sentence) > 1:
            sentence.append(user_sentence)
            break
        else:
            print("Please provide a full sentence")

    print(sentence)

    #How many A's using for loop
    #example - This sentance has how many a's in it amigo.
    count = 0
    for letter in user_sentence:
        if letter == 'a':
            count += 1
    print(f"There are {count} a's in this sentence. #ForLoop")

    print("\n")

    #How many A's using while loop
    #example - This sentance has how many a's in it amigo.

    count_a = 0
    i = 0 

    while i < len(user_sentence):
        if user_sentence[i] == 'a':
            count_a += 1
        i += 1
    print(f"There are {count_a} a's in this sentence. #Whileloop")


    #Print the sentence in uppercase
    print(user_sentence.upper())

    #Replace all spaces with "-"
    sentence_replce_space = user_sentence.replace(' ', '-')
    print(sentence_replce_space)

    #Check if the sentence starts with "Hello"
    user_sentence_split = user_sentence.split()
    print(user_sentence_split)

    i = 0

    while i < len(user_sentence_split):
        if user_sentence_split[0] == "Hello".lower():
            print(f"Yes, sentence starts with Hello")
            break
        else:
            print("No, sentence does not start with Hello")
            break
        i += 1


if __name__ == '__main__':
    main()