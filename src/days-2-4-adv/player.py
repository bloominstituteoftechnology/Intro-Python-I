# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name):
    self.name = name
    self.xp = 0
    self.room = "outside"
