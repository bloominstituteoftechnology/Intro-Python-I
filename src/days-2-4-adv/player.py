# Write a class to hold player information, e.g. what room they are in
# currently.

# class Player():
#   def __init__(self,room):
#     self.room = room


class Player:
  def __init__(self, start_room):
    self.room = start_room #instance variable
    self.items = []

  def addItem(self,item):
    self.items.append(item)
    
  def set_room(self, new_room):
    self.room = new_room

  def __repr__(self):
    return "Current Location: {}".format(self.room)
  def __str__(self):
    return "Current Location: {}".format(self.room) 