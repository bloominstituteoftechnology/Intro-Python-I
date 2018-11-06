from room import Room
from player import Player
from item import Treasure, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

room['outside'].is_light = True
room['foyer'].is_light = True

# Add some items

t = Treasure("silver", "a piece of silver", 600)
room['overlook'].contents.append(t)

t = Treasure("pearl", "a piece of black pearl", 600)
room['treasure'].contents.append(t)


t = Treasure("medal", "a small medal with a dragon", 2000)
room['treasure'].contents.append(t)

l = LightSource("lamp", "Oil Lamp" 100)
room['foyer'].contents.append(l)

f = Food("fries", "potato")
room['treasure'].contents.append(f)


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("What's your name?\n")
plyr = Player(name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(
    f'You find yourself just {plyr.current_room.location} with no memory of how you got here  {plyr.current_room.description}. ')
while True:
    cmd = input(' How should we proceed? -> ').lower().split(' ')
    if len(cmd) == 1:
        if cmd[0] == 'q':
            print('\n Knew you didnt have the permission for this...')
            break
        elif cmd[0] in ['n', 's', 'e', 'w']:
            plyr.travel(cmd[0])
        elif cmd[0] == 'i' or cmd[0] == 'inventory':
            plyr.getInventory()
        elif cmd[0] == 'score':
            plyr.getScore()
        else:
            print('Thats not right...')
    else:
        if cmd[0] == 'get' or cmd[0] == 'take':
            itemToAdd = plyr.current_room.selectItem(cmd[1])
            if itemToAdd == None:
                print('Not inhere!')
            elif not plyr.current_room.is_light and not plyr.has_light:
                print('Good luck!')
            else:
                if hasattr(itemToAdd, 'value') and itemToAdd.value > 0:
                    plyr.score += itemToAdd.value
                    plyr.addItem(itemToAdd)
                    plyr.getScore()
                elif isinstance(itemToAdd, LightSource):
                    plyr.has_light = True
                    plyr.addItem(itemToAdd)
                else:
                    plyr.addItem(itemToAdd)

        elif cmd[0] == 'drop':
            itemToDrop = plyr.selectItem(cmd[1])
            if itemToDrop is None:
                print('You dont have anything like that')
            elif isinstance(itemToDrop, LightSource):
                plyr.has_light = False
                plyr.removeItem(itemToDrop)
                itemToDrop.on_drop()
            else:
                plyr.removeItem(itemToDrop)
                itemToDrop.on_drop()
        else:
            print('Unclear what you want...')
