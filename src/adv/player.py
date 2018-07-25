# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, loc, playerInv = []):
    self.loc = loc
    self.playerInv = playerInv