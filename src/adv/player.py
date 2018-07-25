# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, room):
    self.name = name
    self.location = room
    self.health = 100
    self.strength = 1
    self.capacity = 25
    self.inventory = [
      {'item': 'knife', 'weight': 1}
    ]