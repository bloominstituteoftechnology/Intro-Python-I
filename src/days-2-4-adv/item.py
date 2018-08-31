class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"This is a {self.name} and it's {self.description}"

    def __str__(self):
        return f"This is a {self.name} and it's {self.description}"

    def onTake(self):
        pass

    def onDrop(self):
        pass


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
        self.is_taken = False

    def onTake(self):
        pass

    def onDrop(self):
        pass

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def onTake(self):
        pass

    def onDrop(self):
        print("It's not wise do drop your source of light!")
