"""
Use a nested loop to count how many vowels (a, e, i, o, u) appear in:

names = ["Alice", "Bob", "Eve"]
    count = 0

    for name in names:
        for letter in name:
            if letter in vowels:
                count += 1
    
    print(count)
"""

def main():

    names = ["Alice", "Bob", "Eve"]

    vowels = ["a", "e", "i", "o", "u"]



    i = 0 
    count_w = 0

    while i < len(names):
        j = 0 
        while j < len(names[i]):
            if names[i][j].lower() in vowels:
                count_w += 1
            j += 1
        i += 1
    
    print(count_w)

if __name__ == '__main__':
    main()