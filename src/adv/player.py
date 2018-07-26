# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource

class Player:

  def __init__(self,current):
    self.current = current
    self.items = []
    self.score = 0

  def has_light(self):
    for x in self.items:
      if isinstance(x,LightSource):
        return True
    return False 
  
  def add_score(self,value):
    self.score += value

  def sub_score(self,value):
    self.score -= value
