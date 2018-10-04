# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light, inventory):
        self.name = name
        self.description = description
        self.is_light = is_light
        inv = inventory.split(" ")
        self.inventory = [*inv]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"~~ {self.name} ~~\n\n   {self.description}\n\n   Visible items: {self.inventory}"

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def removeItem(self, item):
                self.inventory.remove(item)

    def addItem(self, item):
                self.inventory.append(item)