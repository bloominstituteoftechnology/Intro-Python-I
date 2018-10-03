# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

  items = []

  def __init__(self, place, description):
    self.place = place
    self.description = description
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None

  def __str__(self):
    return f'{self.place}'

