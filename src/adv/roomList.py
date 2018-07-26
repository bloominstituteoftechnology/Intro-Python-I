from room import Room
from item import Item
import itemList
import npclist

# Declare all the rooms
rooms = {
    'castleWall':  Room("The Castle Wall",
                     "You stand before a castle wall.  From here you can go East or West."),

    'plagueTown':    Room("Plague Town", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'bridgeCrossing': Room("Bridge Crossing", "A black knights stands on the bridge.  'NONE shall pass.' he says."),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

rooms['castleWall'].block_w_to = rooms['plagueTown']
rooms['castleWall'].block_e_to = rooms['bridgeCrossing']
# rooms['foyer'].s_to = rooms['castleWall']
# rooms['foyer'].n_to = rooms['overlook']
# rooms['foyer'].e_to = rooms['narrow']
# rooms['overlook'].s_to = rooms['foyer']
# rooms['narrow'].w_to = rooms['foyer']
# rooms['narrow'].n_to = rooms['treasure']
# rooms['treasure'].s_to = rooms['narrow']

# Beginning world items
rooms['castleWall'].roomInv = [itemList.rock, itemList.stick]

# Mobs and NPCs assigned to rooms
rooms['castleWall'].mobs = [npclist.guard1, npclist.guard2]

# Required items assigned to rooms
rooms['castleWall'].itemRequired = [itemList.coconuts]