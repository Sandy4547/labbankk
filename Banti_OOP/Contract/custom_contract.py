class Friend(Contract):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"
    
class Supplier(Contract):
    def order(self, order):
        print(f"{self.name} is placing order for: {order}")