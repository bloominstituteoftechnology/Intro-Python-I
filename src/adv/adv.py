from room import Room
from player import Player
from item import Item
# Declare all the rooms



weapons = {
    'outside':  Item([
        {
            "Sword": "Strongest steal alloy, killer blade"
        },
        {
            "Machete": "Regular blade, killer knife"
        },
        {
            "Machete": "Regular blade, killer knife"
        }
    ], [
        {
            "Sword": "Strongest steal alloy, killer blade"
        },
        {
            "Machete": "Regular blade, killer knife"
        },
        {
            "Machete": "Regular blade, killer knife"
        }
    ]),

    'foyer':    Item([
        {
            "Knife": "Strongest steal alloy, killer blade"
        },
        {
            "Gun": "Regular blade, killer knife"
        }
    ], [
        {
            "Knife": "Strongest steal alloy, killer blade"
        },
        {
            "Gun": "Regular blade, killer knife"
        }
    ]),

    'overlook': Item([
        {
            "Wand": "Strongest steal alloy, killer blade"
        },
        {
            "Machete": "Regular blade, killer knife"
        }
    ], [
        {
            "Knife": "Strongest steal alloy, killer blade"
        },
        {
            "Gun": "Regular blade, killer knife"
        }
    ]),

    'narrow':   Item([
        {
            "Sword": "Strongest steal alloy, killer blade"
        },
        {
            "Machete": "Regular blade, killer knife"
        }
    ], [
        {
            "Sword": "Strongest steal alloy, killer blade"
        },
        {
            "Machete": "Regular blade, killer knife"
        }
    ]),

    'treasure': Item([
        {
            "Sword": "Strongest steal alloy, killer blade"
        },
        {
            "Machete": "Regular blade, killer knife"
        }
    ], [
        {
            "Sword": "Strongest steal alloy, killer blade"
        },
        {
            "Machete": "Regular blade, killer knife"
        }
    ]),
}


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", weapons['outside'], weapons['outside']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", weapons['foyer'], weapons['foyer']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", weapons['overlook'], weapons['overlook']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", weapons['narrow'], weapons['narrow']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", weapons['treasure'], weapons['treasure']),
}
# Link rooms together
room['outside'].append = weapons['outside']
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('outside')
# Write a loop that:
#
# * Prints the current room name
for key, value in room.iteritems():
    # print(value, key)
    if key == new_player.room_location:
        print 'Current Room: ', value.room_name
        print 'Description: ', value.room_story
        for each in value.name_item.name_item:
            for key,value in each.iteritems():
                print "     Weapon choice:", key
                print "         Weapon description:", value
                print "\n"
            # print(each)
        # print 'Description of Item', value.description_item
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
direction_input = 'hey'
while direction_input != 'q':
    direction_input = raw_input(
    "\n\n\n Please enter directions: e east, w west, n north, s south, to quit q \n\n\n\n\n \n")
    if direction_input == "q":
        exit(1)
    direction_input = str(direction_input) + '_to'
# print(direction_input)
    clear = "\n" * 100
    new_direction = "start"
    if direction_input == "n_to":
        try:
            new_direction = room[(new_player.room_location)].n_to
        except AttributeError, message:
            new_direction = "fail"
            print "FAIL FAIL:", message
            # exit(1)
        # break
    elif direction_input == "s_to":
        try:
            new_direction = room[(new_player.room_location)].s_to
        except AttributeError, message:
            new_direction = "fail"
            print "FAIL FAIL:", message
            # exit(1)
        # break
    elif direction_input == "e_to":
        try:
            new_direction = room[(new_player.room_location)].e_to
        except AttributeError, message:
            new_direction = "fail"
            print "FAIL FAIL:", message
            # exit(1)
        # break
    else:
        try:
            new_direction = room[(new_player.room_location)].w_to
        except AttributeError, message:
            new_direction = "fail"
            print "FAIL FAIL:", message
            # exit(1)
    # print(new_direction.room_name)
    if new_direction == "fail":
        print "\n \n           Direction ", direction_input, "IS INVALID, try a different direction \n \n"
    else:
        for key, value in room.iteritems():
            if value.room_name == new_direction.room_name:
                new_player = Player(key)
            if key == new_player.room_location:
                print clear
                print "Success, Direction IS VALID \n\n\n\n\n\n \n"
                print 'Current Room: ', value.room_name
                for each in value.name_item.name_item:
                    for key,value in each.iteritems():
                        print "     Weapon choice:", key
                        print "         Weapon description:", value
                        print "\n"
                # break
    # print(new_player.room_location)
        # break

# exec("%s = %d" % (direction_input,2))
# print(type(s_to) )
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
