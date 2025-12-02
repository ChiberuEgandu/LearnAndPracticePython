"""
Classes 
"""

#Attributes we want for the car
#wheels
#runs
#top_speed
#current_speed
#type

class Car:
    def __init__(self, type_of_car, runs, top_speed, current_speed, wheels):
        self.type_of_car = type_of_car
        self.runs = runs
        self.top_seed = top_speed
        self.current_speed = current_speed
        self.wheels = wheels

    def __str__(self):
        return f"This is a {self.type_of_car}"


tesla = Car('Tesla', True, 120, 0, 4)
bmw = Car('bmw', True, 120, 0, 4)

print(isinstance(bmw, Car))
print(bmw)
print(bmw.wheels)


