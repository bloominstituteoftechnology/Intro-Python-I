# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
  def __init__(self, name, description, items):
    self.name = name
    self.description = description
    self.n_to = None
    self.s_to = None
    self.w_to = None
    self.e_to = None
    self.items = items

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

  def connectRooms(self,destination_room, direction):
    if direction == "n":
      self.n_to = destination_room
      destination_room.s_to = self
    elif direction == "s":
      self.s_to = destination_room
      destination_room.n_to = self  
    elif direction == "e":
      self.e_to = destination_room
      destination_room.w_to = self  
    elif direction == "w":
      self.w_to = destination_room
      destination_room.e_to = self
    else:
      pring("Invalid Direction")

  def addItem(self,item):
    self.items.append(item)

  def removeItem(self, item):
    if len(self.items) > 0:
      for i in self.items:
        if i.name == item:
          self.items.remove(i)
    else:
      print('Item not available to remove!')

  def displayItems(self):
    if (self.items):
      for i in self.items:
        print('\x1b[1;33;40m' + i.name + '\x1b[0m')
    else:
      print('No items available')