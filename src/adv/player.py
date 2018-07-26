# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
  def __init__(self, name, currentRoom, health, items): 
    self.name = name
    self.currentRoom = currentRoom
    self.health = health
    self.items = items
    
    def updateName(name):
      self.name = name