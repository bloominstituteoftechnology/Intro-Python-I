# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def _init_(self, name, description):
    self.name = name
    self.description = description
    self.paths = []
    self.creatures = None
    self.contents = None
    self.n_to: None
    self.s_to: None
    self.e_to: None
    self.w_to: None