

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Treasure(Item):
    def __init__(self, name, description, points):
        Item.__init__(self, name, description)
        self.points = points

class goblet(Treasure):
    def __init__(self):
        self.name: "Golden_Goblet"
        self.description: "It is a beautiful golden goblet that makes your liquids taste like rainbows."
        self.points: 10
