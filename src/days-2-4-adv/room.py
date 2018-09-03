# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name 
    self.description = description
    self.n_to = None
    self.s_to = None
    self.e_to = None
    self.w_to = None
  def getRoomInDirection(self, direction):
    if direction == 'n':
      return self.n_to
    elif direction == 's':
      return self.s_to
    elif direction == 'e':
      return self.e_to
    elif direction == 'w':
      return self.w_to
    else:
      return None
  def connectRooms(self, destinationRoom, direction):
    if direction == 'n':
      self.n_to = destinationRoom
      destinationRoom.s_to = self
    elif direction == 's':
      self.s_to = destinationRoom
      destinationRoom.n_to = self
    elif direction == 'e':
      self.e_to = destinationRoom
      destinationRoom.w_to = self
    elif direction == 'w':
      self.w_to = destinationRoom
      destinationRoom.e_to = self
    else:
      print("invalid direction")
      
    
    
    


