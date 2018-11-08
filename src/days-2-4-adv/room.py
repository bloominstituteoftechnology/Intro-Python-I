# Implement a class to hold room information. This should have name and
# description attributes.

"""Return a room object

Room holds the room name, description and values of the
rooms in their cardinal direction
"""


class Room:
    # Initialize the properties of the class
    def __init__(self, name, description, is_light=True):
        self.name = name
        self.description = description
        # self.n_to = ''
        # self.s_to = ''
        # self.e_to = ''
        # self.w_to = ''
        self.inventory = []
        self.monsters = []
        self.is_light = is_light

    # Return a formatted value of the Room class
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def contains(self, item):
        if item in self.inventory:
            return True
        else:
            return False

    def remove_item(self, item):
        self.inventory.remove(item)

    def add_item(self, item):
        self.inventory.append(item)

    def remove_monster(self, monster):
        self.monsters.remove(monster)
