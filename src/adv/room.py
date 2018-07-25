# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, name):

        item = self.findItem(name)
        self.items.remove(item)

    def findItem(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None