# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.room = current_room
    self.inventory = []

  def move(self, direction):
    # Account for variation
    valid_directions = [ 'north', 'east', 'south', 'west' ]
    abr_directions = { 'n': 'north', 'e': 'east', 's': 'south', 'w': 'west' }

    # Transfer direction to full name if abreviated
    if direction in abr_directions.keys():
      direction = abr_directions[direction]

    # Check if direction is valid
    if direction in valid_directions:
      # Make string to call room attribute with getattr()
      move_to = f'{direction[0]}_to'
      
      # Check if room has a path to the requested direction
      if hasattr(self.room, move_to):
        # Move rooms and print description
        self.room = getattr(self.room, move_to)
      else:
        print(f'I\'m sorry, it looks like the {self.room.name} has no path leading {direction}\n')
    else:
      print('\nInvalid direction.\n')

    
    
