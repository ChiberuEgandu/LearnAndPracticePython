"""
Simple User Input
Keep asking the user for their name until they type "quit".

"""

def user_input():

    name = ""

    while name.lower() != "quit":
        name = input("What is your name. Type \'quit\' to end:")
    
    print("Thanks You For Playing!")



def main():
    
    user_input()

if __name__ == '__main__':
    main()