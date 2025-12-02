#Create a class called Dog that keeps track of how many Dog objects have been created using a class variable.
#Print the total number of dogs after creating a few instances.

class Dog:

    num_dogs = 0

    def __init__(self, name):
        
        self.name = name 
        Dog.num_dogs += 1


dog1 = Dog("Tom")
dog2 = Dog("Jimmy")
dog3 = Dog("Balto")

print(Dog.num_dogs)