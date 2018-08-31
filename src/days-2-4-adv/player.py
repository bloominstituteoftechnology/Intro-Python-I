# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, startLocation, starterItems):
        self.location = startLocation
        self.name = name
        self.items = []
        self.items = starterItems
        self.score = 0
    def change_location(self, new_location):
        self.location = new_location
    def __repr__(self):
        return "Current Location: {}".format(self.location)
    def __str__(self):
        return "Current Location: {}".format(self.location.title)

    def addItem(self, item):
        self.items.append(item)
        if hasattr(item, "value") and item.score_counter > 0:
            scoreGain = int(item.on_take())
            self.score += scoreGain
            print (f"\nPicking up this treasure has added {item} {item.on_take()} to your score!\n")

    def removeItem(self, item):
        self.items.remove(item)
    
    def findItemByName(self, item):
        if len(self.items) > 0:
            for i in self.items:
                if i.name == item:
                    return i

    def listOfItems(self):
        if len(self.items) < 1:
            return ' '
        for i in self.items:
            return f'{i.name}'
    
    def getInventoryString(self):
        return ", ".join([item.name for item in self.items])
