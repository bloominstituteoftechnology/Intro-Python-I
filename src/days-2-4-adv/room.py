# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.items = []

  def removeItem(self, item):
    if len(self.items) > 0:
      self.items.remove(item)

  def addItem(self, item):
    self.items.append(item)

  def findItemByName(self, name):
    for item in self.items:
      if item.name.lower() == name.lower():
        return item
      return None

def __repr__(self):
    return f"{self.name} - {self.description}"