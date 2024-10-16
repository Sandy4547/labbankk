class Walet:

    def __init__(self, name, money):
        self.name = name
        self.money = money

def check(self):
    print(f"The {self.name}'s wallet has {self.money} bahts.")

def deposit(self, amount):
    self.money += amount

def withdraw(self, amount):
    self.money -= amount

wallet1 = Walet("Sai", 1000)
wallet2 = Walet("Banti", 2000)

check(wallet1)
check(wallet2)

deposit(wallet1, 500)
withdraw(wallet2, 1000)

check(wallet1)
check(wallet2)