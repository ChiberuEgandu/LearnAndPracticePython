#This python program is a simple calculator 

#Step 1 would be to ask the user for an input for the first number , the oparator Aand the second number 

number1 = float(input("Enter your first number: "))
operator = input("Enter an operator. Must be one of (-, + , * , /)")
number2 = float (input("Enter your second number"))

#Write your calculations 

if operator == "-":
    print("Results: ", number1 - number2)
elif operator == "+":
    print("Results: ", number1 + number2)
elif operator == "*":
    print("Results: ", number1 + number2)
elif operator == "/":
    if number2 != 0:
        print("Results: ", number1 / number2)
    else:
        print("Invalid Input. Can not devide by 0.")
else: 
    print("You entered an invalid operator")
   