import textwrap

# Implement a class to hold room information. This should have name and
# description attributes.

default_look = 'You don\'t see anything of particular interest'

class Room:
  def __init__(self, name, description, look_description = default_look, items=[]):
    self.name = name
    self.description = description
    self.look_description = look_description
    self.items = items
    self.inspected = False

  def list_items(self):
    return_str = '\nYou see the following items in the room:\n'

    for item in self.items:
      return_str += f'\n{item.name}:\n{textwrap.fill(item.description, 50)}\n'
    
    return return_str