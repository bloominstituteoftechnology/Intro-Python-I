# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description, roomInv = [], nextDesc = '', itemRequired = None, itemUsed = False):
    self.name = name
    self.description = description
    self.roomInv = roomInv
    self.nextDesc = nextDesc
    self.itemRequired = itemRequired
    self.itemUsed = itemUsed