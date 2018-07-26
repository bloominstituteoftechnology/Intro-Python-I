class Item:
    def __init__(self, name):
        self.name = name    

    def on_take(self):
        pass

class Treasure(Item):
    def __init__(self, name, value):
        self.value = value
        super().__init__(name)

    def on_take(self):
        return self.value


# test = Treasure("Sword", "500 physical damage and 200 magicka", 500)

# print(test.on_take())
