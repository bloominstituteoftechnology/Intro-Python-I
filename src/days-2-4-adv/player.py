# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory

    def gainItem(self, item):
        self.inventory.append(item)
