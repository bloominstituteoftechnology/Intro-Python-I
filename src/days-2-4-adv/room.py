# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, isLight=False):
        self.name = name
        self.description = description
        self.items = []
        self.isLight = isLight

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)

    def showItmes(self):
        print('This room contains the following items: ')
        for item in self.items:
            print(item.name)
