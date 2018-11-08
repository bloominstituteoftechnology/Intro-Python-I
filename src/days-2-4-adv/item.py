class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def on_take(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===You got {self.name}.")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def on_drop(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===You dropped {self.name}.")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class Treasure(Item):
    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value
        self.scored = False
        self.deducted = False

    def on_take(self):
        self.scored = True
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===You got a RARE: {self.name}.")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def on_drop(self):
        self.deducted = True
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===You dropped {self.name}.")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class LightSource(Item):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def on_drop(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\n===It's not wise to drop your source of light!")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
