import textwrap

# Implement a class to hold room information. This should have name and
# description attributes.

default_look = 'You don\'t see anything of particular interest'

class Room:
  def __init__(self, name, description, look_description = default_look, items=[]):
    self.name = name
    self.description = description
    self.look_description = look_description
    self.items = items
    self.inspected = False

  def list_items(self):
    return_str = '\nYou see the following items in the room:\n'

    for item in self.items:
      return_str += f'\n{item.name}:\n{textwrap.fill(item.description, 50)}\n'
    
    return return_str


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty 
passages run north and east.""", """You see a wall to the west that seems to 
have very uniform gaps in the shape of a doorway. Upon further inspection there
appears to be a gab in the wall with a slot inside. It must be a mehcanism of some sort"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", """As you inspect the area, you see a strange
metal object near the edge of the cliff.
It appears to be a lever.""",[item['lever']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'workshop': Room("Smith's Workshop", """This hidden room has scraps strewn out
across the floor and containers along portions of the walls.""", """Around the corner seems
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