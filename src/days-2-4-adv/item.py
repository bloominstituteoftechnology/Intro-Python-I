class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def on_take(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===You got {self.name}.")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class Treasure(Item):
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value
        self.scored = False

    def on_take(self, item):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===You got a RARE: {self.name}.")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
