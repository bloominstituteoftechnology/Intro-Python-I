# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, score = 0):
        self.location = location
        self.inventory = []
        self.score = score
    def change_location(self, new_location):
        self.location = new_location
    # def __repr__(self):
    #     return "Current Location: {}".format(self.location)
    def __str__(self):
        return f'Current Location: {self.location.title}'
    def addItem(self, item):
      self.inventory.append(item)
    def dropItem(self, item):
      item.on_drop()
      self.inventory.remove(item)
    def removeItem(self, item):
      self.inventory.remove(item)
    def findItemByName(self, name):
      for item in self.inventory:
        if item.name.lower() == name.lower():
          return item
      return None
    def getInventoryString(self):
      return ", ".join([item.name for item in self.inventory])
    def addToScore(self, value):
      self.score += value
      print(f'You get {value} points!')
