# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items):
    self.name = name
    self.description = description
    self.items = items
  def room_direction(self, direction):
    if direction == "n":
      return self.n_to
    elif direction == "s":
      return self.s_to
    elif direction == "e":
      return self.e_to
    elif direction == "w":
      return self.w_to
    else:
      return None
  def __str__(self):
    return str(f"\n{self.name}, {self.description}")