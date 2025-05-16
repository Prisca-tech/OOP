# Base class for animals
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}!")

# Subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def fetch(self):
        print(f"{self.name} the {self.breed} is fetching the ball!")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog1.speak()
dog1.fetch()



class Animal:
    def move(self):
        print("The animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("Dog runs 🐕")

class Bird(Animal):
    def move(self):
        print("Bird flies 🐦")

class Fish(Animal):
    def move(self):
        print("Fish swims 🐟")

# Function to demonstrate polymorphism
def move_animal(animal):
    animal.move()

# Example usage
animals = [Dog(), Bird(), Fish()]
for a in animals:
    move_animal(a)


# polymorphism with vehicles
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Function to test polymorphism
def test_movement(vehicle):
    vehicle.move()

# Example usage
vehicles = [Boat()]
for v in vehicles:
    test_movement(v)
