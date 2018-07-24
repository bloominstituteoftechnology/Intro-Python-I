# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, location, hp, playerInv = []):
    self.location = location
    self.hp = hp
    self.playerInv = playerInv
