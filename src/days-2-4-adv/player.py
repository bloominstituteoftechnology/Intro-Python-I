# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, startLocation):
        self.location = startLocation

    def change_location(self, new_location):
        self.location = new_location

    def __repr__(self):
        return "Current Location: {}".format(self.location)

    def __str__(self):
        return "Current Location: {}".format(self.location.title)

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        item.on_drop()
        self.items.remove(item)

    def removeItem(self, item):
        self.items.remove(item)

    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
