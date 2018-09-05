# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, start_room):
    self.name = name
    self.location = start_room
    self.inventory = []
  def changeLocation(self, new_room):
    self.location = new_room
  def __repr__(self):
    return "Current Location: {}\n".format(self.location.name)
  def __str__(self):
    return "Current Location: {}\n".format(self.location.name)
  def addItem(self, item):
    self.inventory.append(item)
  def removeItem(self, item):
    if len(self.inventory) > 0:
      for i in self.inventory:
        if i == item:
          self.inventory.remove(i)
    else:
      print('that item is not in your inventory')




    # def change_location(self, new_location):
    #     self.location = new_location
    # def __repr__(self):
    #     return "Current Location: {}".format(self.location)
    # def __str__(self):
    #     return "Current Location: {}".format(self.location)