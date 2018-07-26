# Implement a class to hold room information. This should have name and
# description attributes.

default_look = 'You don\'t see anything of particular interest'

class Room:
  def __init__(self, name, description, look = default_look, items=[]):
    self.name = name
    self.description = description
    self.look = look
    self.items = items
    self.inspected = False