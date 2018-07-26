class LivingBeing:
  def __init__(self, room, name, kind, hp, inventory):
    self.room = room
    self.name = name
    self.kind = kind
    self.hp = hp
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
    
  def attack(self, target):
    pass


class Humanoid(LivingBeing):
  def __init__(self, room, name, kind, hp, inventory):
    super().__init__(room, name, kind, hp, inventory)
    self.equip_slots = {
      'backpack': None,
      'satchel': None,
      'armor': None,
      'weapon': None, # Natural weapon if none equipped
      'accessory': None,
      'magic item': None
    }

  def examine(self, target):
    # If no target given
      # Print details of current room
    # Otherwise
      # Check if item is on person or in room
    pass
  
  def use(self, item):
    # If item is on person or in room
      # If item can be used(i.e. - item.use in room.use_targets.keys())
        # Use item
      # Otherwise
        # Print error
    pass
  
  def pickup(self, item):
    if item in self.room.items:
      self.room.items.remove(item)
      self.inventory.append(item)
    else:
      print('\nItem invalid\n')
  
  def drop(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      self.room.items.append(item)
    else:
      print('\nItem invalid\n')
  
  def equip(self, item):
    # Check if item is on person or in room
      # If so then equip it to slot
      # Otherwise print error
    pass
  
  def check_equipped(self, item):
    for slot, item in self.equip_slots.iteritems():
      print(f'{slot}: {item}\n')


class Player(Humanoid):
  def __init__(self, room, name, kind, hp, inventory):
    super().__init__(room, name, kind, hp, inventory)


class NPC(Humanoid):
  def __init__(self, room, name, kind, hp, inventory, action_loop, aggressive, service, dialogue):
    super().__init__(room, name, kind, hp, inventory)
    self.action_loop = action_loop
    self.aggressive = aggressive
    self.service = service
    self.dialogue = dialogue


class NonHumanoid(LivingBeing):
  def __init__(self, room, name, kind, hp, inventory, action_loop, aggressive):
    super().__init__(room, name, kind, hp, inventory)
    self.action_loop = action_loop
    self.aggressive = aggressive

class Animal(NonHumanoid):
  def __init__(self, room, name, kind, hp, inventory, action_loop, aggressive):
    super().__init__(room, name, kind, hp, inventory, action_loop, aggressive)
  
class Monster(NonHumanoid):
  def __init__(self, room, name, kind, hp, inventory, action_loop, aggressive):
    super().__init__(room, name, kind, hp, inventory, action_loop, aggressive)


#   def use(self, item):
#     from adv import room

#     if item.name == 'lever' and self.room.name == 'Foyer' and self.room.inspected == True:
#       print('''You insert the lever into the gap of the wall.
# It slides into the slot with relative ease and the wall opens up,
# revealing a hidden room.''')
#     self.room.w_to = room['workshop']


# Make a new player that is currently in the 'outside' room.

# player = Player('Devon', room['overlook'])
    
    
