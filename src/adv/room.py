# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items, enemies, healthPacks, exits)
  self.name = name
  self.description = description
  self.items = items
  self.enemies = enemies
  self.healthPacks = exits
  self.n_to = None
  self.s_to = None
  self.e_to = None
  self.w_to = None

