# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.inventory = {}

  def move(self, direction):
    room = self.current_room

    # Account for variation
    valid_directions = [ 'north', 'east', 'south', 'west' ]
    abr_directions = { 'n': 'north', 'e': 'east', 's': 'south', 'w': 'west' }

    # Transfer direction to full name if abreviated
    if direction in abr_directions.keys():
      direction = abr_directions[direction]

    # Check if direction is valid
    if direction in valid_directions:
      # Make string to call room attribute with getattr()
      move_to = '{}_to'.format(direction[0])
      
      # Check if room has a path to the requested direction
      if hasattr(room, move_to):
        # Move rooms and print description
        self.current_room = getattr(room, move_to)
      else:
        print('I\'m sorry, it looks like the {} has no path leading {}\n'.format(room.name, direction))
    else:
      print('\nInvalid direction.\n')

    
    
