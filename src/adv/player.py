# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, currentRoom, inventory):
    self.currentRoom = currentRoom
    self.inventory = inventory
    self.score = 0
