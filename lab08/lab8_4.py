class person():
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"

person1 = person("Bantita",20,"bantita.su@ksu.ac.th")
person2 = person("Sandy",20,"poomsandyy@gmail.com")

print(person1)
print(person2)