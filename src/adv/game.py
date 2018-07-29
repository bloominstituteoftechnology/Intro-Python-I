from room import Room
from item import Item, Consumable, Equippable, Armor, Weapon, Accessory, MagicItem
from being import Player, NPC, Animal, Monster

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages 
run north and east.""", """You see a wall to the west that seems to have very uniform 
gaps in the shape of a doorway. Upon further inspection there appears to be a gab in 
the wall with a slot inside. It must be a mehcanism of some sort."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'workshop': Room("Smith's Workshop", """This hidden room has scraps strewn out
across the floor and containers along portions of the walls.""", """Around the corner 
seems to be a functional workbench. Maybe we could use this to craft something 
useful."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers. The 
only exit is to the south."""),

    'arena': Room("Arena", """This is the place where champions are made. Best of luck!""")
}

# Create all the items
item = {
  'lever': Item('lever', """It looks as though it was broken off at the base.
Possibly part of a larger contraption."""),
  'small potion': Consumable('small potion', 'Heals user for 1-3 hp.', 'potion', 5), 
  'medium potion': Consumable('medium potion', 'Heals user for 2-6 hp.', 'potion', 5),
  'large potion': Consumable('large potion', 'Heals user for 2-6 hp.', 'potion', 5)
}

weapon = {
  # 'medium humanoid natural': Weapon('natural weapons', 'Flying fists and feet of fury!', 1),
  'steel sword': Weapon('steel sword', 'Tried and true with a keen edge.', 2),
  'iron hammer': Weapon('iron hammer', 'You could not ask for a more sturdy companion.', 3)
}

# Create all the beings
npc = {
  'Orc:Vesh': NPC(room['arena'], 'Vesh', 'Orc', 40, [item['small potion']])
}

player = Player(room['arena'], 'Devon', 'Human', 20, [weapon['iron hammer'], item['medium potion']])

# Equip any weapons
npc['Orc:Vesh'].equip_slots['weapon'] = weapon['steel sword']
player.equip_slots['weapon'] = weapon['iron hammer']

# Add items and occupants to rooms
room['outside'].inventory.append(item['lever'])

room['arena'].occupants += [player, npc['Orc:Vesh']]

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']