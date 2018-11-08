class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
        self.taken = False
    def pickingUp(self):
        self.taken = True

class Torch(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
    def warning(self):
        print("\n\n ==YOU SHOULD PROBABLY KEEP THE TORCH==")
