# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, room):
    self.nextRoom = None
    self.room = room
    self.items = []
  
  def updateRoom(self, room):
    self.room = room

  def lookNextRoom(self, room):
    self.nextRoom = room
