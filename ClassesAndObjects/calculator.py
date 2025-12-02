#Create a class Calculator with methods:
# add(a, b)
#subtract(a, b)
#multiply(a, b)
#divide(a, b) (handle division by zero)

class Calculator:

    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):

        if b <= 0:
            return f"Error: You can not divide by 0"
        else:
            return a / b

print(Calculator.add(2, 2))
print(Calculator.subtract(2, 2))
print(Calculator.multiply(2, 2))
print(Calculator.divide(2, 0))