
def main():

    names = ["amy", "bob", "tom", "jeff"]
        
    
    user_input = input("Enter a name: ").lower()

    for name in names:
        if user_input == name:
            print(f"The name {user_input} you entered exists in the list")
            return
        
    print("The name you entered does not exist")




if __name__ == '__main__':
    main()

