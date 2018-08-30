# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.contents = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return "You see: {}".format(self.title) 
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
    def findItemByName(self, name):
      for item in self.contents:
        if item.name.lower() == name.lower():
          return item
      return None
    def removeItem(self, item):
      self.contents.remove(item)
    def addItem(self, item):
      self.contents.append(item)