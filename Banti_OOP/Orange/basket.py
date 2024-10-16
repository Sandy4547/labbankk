class Basket:
    def __init__(self, location):
        self.location = location
        self.oranges = []

    def add_orange(self, orange):
        self.oranges.append(orange)