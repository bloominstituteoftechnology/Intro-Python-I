# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description, vDescription = None, visited = False, roomInv = []):
    self.name = name
    self.description = description
    self.vDescription = vDescription
    self.visited = visited
    self.roomInv = roomInv