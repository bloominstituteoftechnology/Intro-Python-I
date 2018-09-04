from item import Item

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.has_been_taken = False
    def on_take(self):
        if self.has_been_taken == True:
            print(f"You take the {self.name}.")
            return None
        else:
            print(f"You take the {self.name} and earn {self.value} points.")
            self.has_been_taken = True
            return self.value