class Shoes:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Shoes: -- size {self.size}"

class Leg:
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"Leg: -- length {self.length}"

class Man:
    def __init__(self, shoes):
        self.shoes = shoes
        self.leg = Leg(120)

    def __str__(self):
        return f"Man with {self.shoes} and {self.leg}"

shoes = Shoes(9)
man = Man(shoes)
print(man.leg)    # Outputs: Leg: -- length 120
print(man.shoes)  # Outputs: Shoes: -- size 9
print(man)        # Outputs: Man with Shoes: -- size 9 and Leg: -- length 120
del man

# After deleting `man`, trying to access `man.leg` or `man.shoes` will cause an error.
print(shoes)      # Outputs: Shoes: -- size 9
# print(man.leg)  # This will raise an error since `man` is deleted.
