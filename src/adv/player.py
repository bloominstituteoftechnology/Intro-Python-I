# Write a class to hold player information, e.g. what room they are in currently.

class Player:
  def __init__(self, playerName, currentRoom):
    self.playerName = playerName
    self.currentRoom = currentRoom
    self.inventory = []

  def setCurrentRoom(self, newRoom):
    self.currentRoom = newRoom

  def getItem(self, item):
    newItem = self.currentRoom.removeItem(item)
    self.inventory.append(newItem)

  def dropItem(self, item):
    pass
