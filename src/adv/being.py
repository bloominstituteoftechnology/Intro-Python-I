class Being:
  def __init__(self, room, name, kind, hp, inventory = [], boons = {}):
    self.room = room
    self.name = name
    self.kind = kind
    self.hp = hp
    self.hp_max = hp
    self.inventory = inventory
    self.boons = boons
  
  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name
  
  def move_room(self, direction):
    # Account for variation
    abr_directions = { 'n': 'north', 'e': 'east', 's': 'south', 'w': 'west' }

    # Transfer direction to full name if abreviated
    if direction in abr_directions.keys():
      direction = abr_directions[direction]

    # Make string to call room attribute with getattr()
    move_to = f'{direction[0]}_to'
    
    # Check if room has a path to the requested direction
    if hasattr(self.room, move_to):
      # Move rooms and return description
      self.room = getattr(self.room, move_to)

      return 'You move to the ' + self.room.name

    else:
      # Return information as to why move failed
      return f'I\'m sorry, it looks like the {self.room.name} has no path leading {direction}'
    
  def attack(self, target):
    # Make sure that target is in same room
    if self.room == target.room:
      # Account for human or non-human 
      if hasattr(self, equip_slots):
        power = self.equip_slots['weapon'].power

      else:
        power = self.power
      
      if hasattr(self, equip_slots):
        protection = target.equip_slots['armor'].protection

      else:
        protection = target.protection

      # Calculate total damage after boons
      power += self.boons['power']
      protection += target.boons['protection']
      damage = power - protection
    
    if damage > 0:
      target.hp -= damage


class Humanoid(Being):
  def __init__(self, room, name, kind, hp, inventory = []):
    super().__init__(room, name, kind, hp, inventory)
    self.equip_slots = {
      'backpack': None,
      'satchel': None,
      'pouch': None,
      'armor': None,
      'weapon': None,
      'accessory': None,
      'magic item': None
    }

  def inspect(self, item = None):
    return_str = ''

    if self.room.details:
      return_str += self.room.details

    if len(self.room.inventory) is not 0:
      if self.room.details:
        return_str += '\n'

      return_str += "You see the following items:\n"

      for item in self.room.inventory:
        return_str += f"\n{item.name} - {item.description}"

    if return_str is '':
      return_str = 'You don\'t see anything of particular interest'
  
    return return_str
  
  def use(self, item):
    # If item is on person or in room
      # If item can be used(i.e. - item.use in room.use_targets.keys())
        # Use item
      # Otherwise
        # Print error
    pass
  
  def take(self, item):
    if item in self.room.inventory:
      self.room.inventory.remove(item)
      self.inventory.append(item)

      return True

    return False
  
  def drop(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      self.room.inventory.append(item)

      return True
    
    return False
  
  def equip(self, item):
    # Check if item is on person or in room
      # If so then equip it to slot
      # Otherwise print error
    pass
  
  def check_equipped(self):
    for slot, item in self.equip_slots.iteritems():
      print(f'{slot}: {item}\n')
    
  def check_inventory(self):
    if len(self.inventory) is not 0:
      return_str = 'You are carrying the following:\n'

      for item in self.inventory:
        return_str += f"\n{item.name} - {item.description}"

      return return_str

    return "Your inventory is currently empty."
      

class Player(Humanoid):
  def __init__(self, room, name, kind, hp, inventory = []):
    super().__init__(room, name, kind, hp, inventory)


class NPC(Humanoid):
  def __init__(self, room, name, kind, hp, inventory, action_loop = None, aggressive = False, service = None, dialogue = None):
    super().__init__(room, name, kind, hp, inventory)
    self.action_loop = action_loop
    self.aggressive = aggressive
    self.service = service
    self.dialogue = dialogue


class NonHumanoid(Being):
  def __init__(self, room, name, kind, hp, inventory, power, protection, action_loop = None, aggressive = False):
    super().__init__(room, name, kind, hp, inventory, power, protection)
    self.action_loop = action_loop
    self.aggressive = aggressive

class Animal(NonHumanoid):
  def __init__(self, room, name, kind, hp, inventory, power, protection, action_loop = None, aggressive = False):
    super().__init__(room, name, kind, hp, inventory, power, protection, action_loop, aggressive)
  
class Monster(NonHumanoid):
  def __init__(self, room, name, kind, hp, inventory, power, protection, action_loop = None, aggressive = False):
    super().__init__(room, name, kind, hp, inventory, power, protection, action_loop, aggressive)


#   def use(self, item):
#     from adv import room

#     if item.name == 'lever' and self.room.name == 'Foyer' and self.room.inspected == True:
#       print('''You insert the lever into the gap of the wall.
# It slides into the slot with relative ease and the wall opens up,
# revealing a hidden room.''')
#     self.room.w_to = room['workshop']
