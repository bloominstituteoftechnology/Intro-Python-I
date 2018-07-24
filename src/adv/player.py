# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def move(direction):
    if direction == 'north' or direction == 'n':
      if hasattr(self.current_room, 'n_to'):
        self.current_room = self.current_room.n_to

    elif direction == 'east' or direction == 'e':
      if hasattr(self.current_room, 'e_to'):
        self.current_room = self.current_room.e_to

    elif direction == 'south' or direction == 's':
      if hasattr(self.current_room, 's_to'):
        self.current_room = self.current_room.s_to
      
    elif direction == 'west' or direction == 'w':
      if hasattr(self.current_room, 'w_to'):
        self.current_room = self.current_room.w_to

    else:
      print('I\'m sorry, it looks like there is no path in that direction.')
    
    print(self.current_room.description)
    
