#Chiberu
class Person:
			def __init__(self, name, age):
				self.name = name
				self.age = age
				
			def greet(self):
					print(f"Hello my name is {self.name}")
			
			def is_adult(self):
				if self.age >= 18:
					return True
				else:
					return False
					
			def __str__(self):
				return f"{self.name} and I am {self.age}"
			
			
person1 = Person("Bob", 25)
person1.greet()  # Should print: "Hello, my name is Bob"
person1.is_adult()  # Should return True