# Pet.py
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def makeSound(self):
        raise NotImplementedError("Subclasses must implement this method")
