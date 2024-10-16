# Cat.py
from Pet import Pet

class Cat(Pet):
    def __init__(self, name, breed, age):
        super().__init__(name, age)
        self.breed = breed
    
    def display_info(self):
        return f"{super().display_info()}, Breed: {self.breed}"
    
    def makeSound(self):
        return "เมี๊ยว!"
