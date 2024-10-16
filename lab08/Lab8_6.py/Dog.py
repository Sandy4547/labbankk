# Dog.py
from Pet import Pet

class Dog(Pet):
    def __init__(self, name, breed, age):
        super().__init__(name, age)
        self.breed = breed
    
    def display_info(self):
        return f"{super().display_info()}, Breed: {self.breed}"
    
    def makeSound(self):
        return "Woof!"
