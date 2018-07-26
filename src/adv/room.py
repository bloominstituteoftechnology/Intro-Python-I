# Implement a class to hold room information. This should have name and
# description attributes.
from item import LightSource


class Room:

  def __init__(self,name,description):
    self.is_light = False
    self.name = name
    self.description = description
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None
    self.items = []

  def is_lit(self):
    if(self.is_light == True):
      return True
    else:
      for x in self.items:
        if isinstance(x,LightSource):
          return True
        else:
          return False
