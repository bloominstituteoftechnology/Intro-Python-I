# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, is_lit, inventory):
        self.name = name
        self.description = description
        self.is_lit = is_lit
        inven = inventory.split(" ")
        self.inventory = [*inven]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
#THIS MAKES THE ROOM CLASS THAT DEFINES THE ATTRIBUTES OF A ROOM

    def __str__(self):
        return f"\n -{self.name}\n\n    {self.description}\n"
#THIS CREATES A STRING THAT PRINTS IN EACH ROOM

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        elif direction == "e":
            return self.e_to
        else:
            return None

    def removeItem(self, item):
        self.inventory.remove(item)

    def addItem(self, item):
        self.inventory.append(item)
