#Create a class called Car with two attributes: make and model.
#Then create two different car objects and print their attributes.

class Car:

    #Add a Default Attribute Add a third attribute (like color) with a default value.
    # Create one object that uses the default and one that overrides it.
    color = "Red"

    ##Then create two different car objects and print their attributes.

    def __init__(self, make, model):
        
        self.make = make
        self.model = model

    #Add a method to your Car class called start_engine() that prints a message showing the car’s make and model.

    def start_engine(self):
        print(f"Your car is a {self.make} {self.model}")
    
    


car1 = Car("Toyota", "Camery")
car2 = Car("Lexus", "RC350")
car1.start_engine()
car2.start_engine()

car3 = Car("Honda", "Civic") #uses default attribute color
car4 = Car("Subaru", "Oubback")
car4.color = "Blue" #overides default attribute color


print(car3.make, car3.model, car3.color)
print(car4.make , car4.model, car4.color)
