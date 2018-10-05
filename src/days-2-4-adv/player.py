# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, room):
    self.nextRoom = None
    self.name = 'Stranger'
    self.room = room
    self.items = []
    self.health = 100
