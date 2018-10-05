class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        pass
    def on_drop(self):
        pass

class Treasure(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value
    def on_take(self):
        return self.value
    def on_drop(self):
        self.value = 0