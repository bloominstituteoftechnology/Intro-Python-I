# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, startLocation):
        self.location = startLocation
        self.name = name
        self.items = []
    def change_location(self, new_location):
        self.location = new_location
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location.title)

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        if len(self.items) > 0:
            for i in self.items:
                if i.name == item:
                    self.items.remove(i)

    
