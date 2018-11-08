# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room 
    self.inventory = []

  def try_move(self, direction):
    key = direction + '_to'

    if not hasattr(self.room, key):
      print("No path lies in this direction. Pick another")      
    else:
      return getattr(self.room, key)
