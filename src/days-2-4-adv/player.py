# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name):
    self.name = name
    self.items = []
    self.score = 0
    self.hp = 50
  def __str__(self):
    return str(f"{self.name}")