# Implement a class to hold room information. This should have name and
# description attributes.
import random


class Room:
  def __init__(self, room_type):
    self.self = self
    self.room_type = room_type
    self.containsItem = self.hasItem()

  def hasItem():
    return bool(random.getrandbits(1))
