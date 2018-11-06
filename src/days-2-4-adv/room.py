# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None

  def to_room(self, direction):
    if direction == "n":
      if self.n_to:
        return self.n_to
    else:
      print("You can't go that way.")