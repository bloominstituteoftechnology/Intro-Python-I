# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
  def __init__(self, name, location, equipped):
    self.name = name
    self.location = location
    self.equipped = equipped