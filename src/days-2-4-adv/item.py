class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
class Treasure(Item):
    def __init__(self, name, description, worth):
        Item.__init__(self, name, description)
        self.worth = worth
    def onTake(self):
        value = self.worth
        self.worth = 0
        return value
class Light(Item):
    def __init__(self, name, description, brightness):
        Item.__init__(self, name, description)
        self.brightness = brightness
    def onDrop(self):
        return False