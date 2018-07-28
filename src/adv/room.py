import textwrap
import sys
from item import item


# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, inventory=[], details = None):
    self.name = name
    self.description = description
    self.inventory = inventory
    self.details = details
  
  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name

  def inspect(self):
    return_str = ''

    if self.details:
      return_str += self.details

    if len(self.inventory) is not 0:
      if self.details:
        return_str += '\n'

      return_str += "You see the following items:\n"

      for item in self.inventory:
        return_str += f"\n{item.name} - {textwrap.fill(item.description, 50)}\n"

    if return_str is '':
      return_str = 'You don\'t see anything of particular interest'
  
    return return_str


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty 
passages run north and east.""", [], """You see a wall to the west that seems to 
have very uniform gaps in the shape of a doorway. Upon further inspection there
appears to be a gab in the wall with a slot inside. It must be a mehcanism of some sort"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['lever']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'workshop': Room("Smith's Workshop", """This hidden room has scraps strewn out
across the floor and containers along portions of the walls.""", [], """Around the corner seems
to be a functional workbench. Maybe we could use this to craft something useful"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']