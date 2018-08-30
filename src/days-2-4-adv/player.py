# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, start_room):
    self.room = start_room #instance variable
    self.items = []
    self.score = 0
  
  def __repr__(self):
    return "Current Location: {}".format(self.room)
  def __str__(self):
    return "Current Location: {}".format(self.room) 

  def set_room(self, new_room):
    self.room = new_room

  def setScore(self, score):
    self.score = score

  def addItem(self,item):
    self.items.append(item)
  
  def removeItem(self, item):
    if len(self.items) > 0:
      for i in self.items:
        if i.name == item:
          self.items.remove(i)
    else:
      print('Item not available to remove!')

  def getItemsList(self):
    if (self.items):
      return [i.name for i in self.items]
    else:
      return []

  def displayItems(self):
    if (self.items):
      for i in self.items:
        print('\x1b[1;35;40m' + i.name + '\x1b[0m')
    else:
      print('\x1b[1;35;40m' + "You don't have any items!" + '\x1b[0m')