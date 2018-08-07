from room import Room
from player import Player

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "outside", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "foyer", ["torch"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "overlook", ["match"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "narrow",[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "treasure", []),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

class Main:
    def start(self):
        # Make a new player object that is currently in the 'outside' room.
        playerA = Player('Thuy', rooms['outside'])
        print('Welcome ' + playerA.name + '!')
        playerA.getRoom()
        
        
        move = ''
        
        while move != 'q':
            move = input(">>>>>>Your next move? w(west), s(south), n(north), e(east), l(look for items) or q(quit): ")
            
            if move != 'q':
                if move == 'l':
                    playerA.room.view_items()
                else:
                    try:
                        int(move)
                    except ValueError:
                        moveKey = move + '_to'
                        
                        try:
                            print(getattr(playerA.room,moveKey).shortname)
                            rooms[getattr(playerA.room,moveKey).shortname]
                        except AttributeError:
                            print('>>>>>>>There is no way on that direction! Try again!\n')
                            playerA.getRoom()
                        except KeyError:
                            print('>>>>>>>There is no way on that direction! Try again!\n')
                            playerA.getRoom()
                        else:
                            playerA.room = rooms[getattr(playerA.room,moveKey).shortname]
                            playerA.getRoom()
                            
                    else:
                        if int(move) <= (len(playerA.room.items)-1):
                            playerA.add_item(playerA.room.items[int(move)])
                            playerA.room.remove_item(int(move))
                            playerA.view_bag()
                            
            else:
                print('See you later!')

new_game = Main()
new_game.start()
