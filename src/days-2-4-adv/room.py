# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items):
    self.name = name
    self.description = description
    self.items = []
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None

  def goToRoomInEnteredDirection(self, direction):
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

  def __str__(self):
    return f"\n   {self.name}\n  {self.description}\n"

  # Adds an item to a room
  def addItem(self, item):
    self.items.append(item)

  # Removes an item from a room
  def removeItem(self, item):
    if len(self.items) > 0:
      for i in self.items:
        if i.name == item:
          self.items.remove(i)
    else:
      print('There is no item to remove')