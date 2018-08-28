# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def getItems(self):
        return ', '.join([i.name for i in self.items])