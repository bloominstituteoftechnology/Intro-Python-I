# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        inventoryItem = inventory.split(" ")
        self.inventory = [*inventoryItem]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def roomDirection(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None

    def __str__(self):
        return f'{self.name}, {self.description}. You see, tucked away in a dusty corner, {self.inventory}'

    def removeItem(self, item):
        self.inventory.remove(item)

    def addItem(self, item):
        self.inventory.append(item)

    



