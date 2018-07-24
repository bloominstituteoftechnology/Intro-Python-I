# Write a class to hold player information, e.g. what room they are in currently.

class Player:
  def __init__(self, playerName, currentRoom):
    self.playerName = playerName
    self.currentRoom = currentRoom
    self.description = currentRoom.description

  def setCurrentRoom(self, newRoom):
    self.currentRoom = newRoom
    self.description = newRoom.description