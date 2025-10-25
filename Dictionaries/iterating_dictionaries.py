"""
Loop through a dictionary
Create a dictionary called fruits with at least 5 fruit names as keys and their quantities as values. Loop

2. Sum values in a dictionary
Using the fruits dictionary from Exercise 6, calculate and print the total quantity of all fruits.

#3 Remove a key-value pair
Remove a fruit of your choice from the fruits dictionary. Print the updated dictionary.
"""

def main():
    #1
    fruits = {
        "apple": 10,
        "pears": 10,
        "grapes":20,
        "peach":20,
        "banana":40
    }

    print(fruits)

    #2
    values_list = list(fruits.keys())
    print(values_list)

    total = 0

    for key, value in fruits.items():
        total += value
    
    print(f"The total quantity for all fruits is {total}")

    
    #3
    del fruits["grapes"]
    print(fruits)

if __name__ == '__main__':
    main()