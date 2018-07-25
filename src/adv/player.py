# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, playerName, startRoom, bag):
    self.room = startRoom
    self.name = playerName
    self.bag = bag