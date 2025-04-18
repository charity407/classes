#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours
#methods
    def make_call(self, contact):
        return f"Calling {contact} from {self.brand} {self.model}."

    def take_photo(self):
        return f"Taking a photo with {self.brand} {self.model}."

    def __str__(self):
        return f"{self.brand} {self.model} - {self.storage}GB, {self.battery_life}h battery life."
    
    
    #Activity 2: Polymorphism Challenge! 🎭

#Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
class Animal:
    def move(self):
        return "The animal moves."
    class Dog(Animal):
        def move(self):
            return "The dog runs."
    class Bird(Animal):
        def move(self):
            return "The bird flies."
        class Fish(Animal):
            def move(self):
                return("The fish swims")
            
