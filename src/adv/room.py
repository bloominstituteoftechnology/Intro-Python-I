class Room:
  def __init__(self, name, description, details = None, inventory = []):
    self.name = name
    self.description = f'\'{description}\''
    self.inventory = inventory
    self.details = f'\'{details}\'' if details else details
  
  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name