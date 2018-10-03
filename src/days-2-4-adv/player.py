# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

  nextRoom = None

  def __init__(self, room):
    self.room = room
  
  def updateRoom(self, room):
    self.room = room

  def lookNextRoom(self, room):
    self.nextRoom = room
