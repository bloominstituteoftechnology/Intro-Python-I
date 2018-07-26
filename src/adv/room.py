# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, descript, itemList, is_light):
    self.name = name
    self.descript = descript
    self.itemList = itemList
    self.newRoom = True
    self.is_light = is_light
