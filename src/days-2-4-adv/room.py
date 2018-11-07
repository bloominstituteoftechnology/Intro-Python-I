# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items_in_room=[]):
    self.name = name
    self.description = description
    self.items_in_room = items_in_room