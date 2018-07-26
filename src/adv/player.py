# Write a class to hold player information, e.g. what room they are in currently.

class Player:
  def __init__(self, playerName, currentRoom):
    self.playerName = playerName
    self.currentRoom = currentRoom
    self.inventory = []

  def setCurrentRoom(self, newRoom):
    self.currentRoom = newRoom

  def getItem(self, item):
    print("\nYou picked up ", item.name)
    self.currentRoom.removeItem(item)
    self.inventory.append(item)

  def dropItem(self, item):
    print("\nYou removed %s from your inventory." % (item.name))
    self.inventory.remove(item)
    self.currentRoom.addItem(item)

  def locateInventory(self, itemName):
    for item in self.inventory:
      if item.name.lower() == itemName.lower():
        return item
    return None