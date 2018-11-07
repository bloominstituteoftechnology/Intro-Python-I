# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, start_location):
    self.location = start_location
    self.items = []

  def change_location(self, new_location):
    self.location = new_location

  def __repr__(self):
    return f"Current Location: {self.location}"

  def __str__(self):
    return f"Current Location: {self.location}"

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    if len(self.items) > 0:
      for i in self.items:
        if i.name == item:
          self.items.remove(i)
        else:
          print('There is no item to remove at this time')