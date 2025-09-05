#This python file includes notes about inputs - which porompts users for an imput

#input to ask user to imput or enter a name and  value
name = input("Enter your name: ")

while True:
    user_input = input("Enter a value: ") # Ask the user to input a value
    try:
        value = int(user_input) ##The number they enter must be and integer
        break ## If the conditions are met, kill/break out of the loop
    except ValueError: ## If not throw this error that asked the user to try to enter another value
        print("Error: You entered an incorrect value. Please try Again")

print("Your name is ", name,  "and you entered the number:", value) ## Once they provide a name and value print this

