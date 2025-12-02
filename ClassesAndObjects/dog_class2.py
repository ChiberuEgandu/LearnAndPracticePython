
class Dog: #initilizing the class 
    species = "Canine" #attribule of dog class that all instances will have

    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age  #instance attribute 
    
    def bark(self): #method
        print(f"{self.name} is barking")
    
dog1 = Dog('Bob', 5)

print(dog1.name, dog1.age, dog1.species)
dog1.bark()