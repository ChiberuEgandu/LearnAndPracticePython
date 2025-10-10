#This is a calculator with a loop
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

while True:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")

    if operator.lower() == "q":
        print("Calculator closed.")
        break

    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", add(num1, num2))
    elif operator == "-":
        print("Result:", subtract(num1, num2))
    elif operator == "*":
        print("Result:", multiply(num1, num2))
    elif operator == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operator!")