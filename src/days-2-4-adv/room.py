# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description    
    self.items = [] # --> Create a list of items for a room

  def default_spawn_items(self, item):
    self.items.append(item)

  def look_around(self):
    print(f"\nYou look around the {self.name} and see:\n")
    for item in self.items:
      print(f"\n==== {item.name}: {item.description} ====\n")