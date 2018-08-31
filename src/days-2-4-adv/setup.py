from room import Room
from item import Item, Treasure, LightSource

commandsHelp = {
"n" : "Go North",
"w" : "Go West",
"e" : "Go East",
"s" : "Go South",
"l" : "Look",
"i" : "Inventory",
"p" : "Pickup",
"u" : "Use",
"d" : "Drop",
"a" : "Attack",
"s" : "Score",
"q" : "Quit",
"h" : "help",
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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

#set light sources
room["foyer"].isLit = False
#declare all items
item = {
   "coin" : Treasure("Coin", "A shiny golden coin"),
   "scepter": Treasure("Scepter", "A short silver staff with a huge sapphire inlaid on top", 1000),
   "necklace" : Treasure("Necklace", "A heavy gold necklace set with 3 large diamonds surrounded by smaller rubies", 500),
   "torch" : LightSource("Torch", "An excellent source of light")
}
room["foyer"].inventory["coin"] = item["coin"]
room["treasure"].inventory["scepter"] = item["scepter"]
room["overlook"].inventory["necklace"] = item["necklace"]
room["outside"].inventory["torch"] = item["torch"]