# Implement a class to hold room information. This should have name and description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.w_to = None
    self.e_to = None
    self.items = []

  def addItem(self, item):
    self.items.append(item)

  def removeItem(self, item):
    self.items.remove(item)
    return item

  def getItems(self):
    return self.items

  def itemAvailability(self, itemName):
    for item in self.items:
      if item.name.lower() == itemName.lower():
        return item
    return None