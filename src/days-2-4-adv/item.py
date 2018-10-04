

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Treasure(Item):
    def __init__(self, name, description, points):
        Item.__init__(self, name, description)
        self.points = points
    def onGet(self):
        return self.points


class Goblet(Treasure):
    def __init__(self):
        self.name = "Goblet"
        self.description = "It is a beautiful golden goblet that makes your liquids taste like rainbows."
        self.points = 10
    def onGet(self):
        return self.points

