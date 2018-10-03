class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        print("You have taken the %s." % self.name)

class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.takenAlready = False
    def on_take(self):
        print("You have taken the %s." % self.name)
        self.takenAlready = True