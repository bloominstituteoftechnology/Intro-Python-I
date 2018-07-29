class Room:
  def __init__(self, name, description, details = None, inventory = [], occupants = []):
    self.name = name
    self.description = f'\'{description}\''
    self.details = f'\'{details}\'' if details else details
    self.inventory = inventory
    self.occupants = occupants
  
  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name