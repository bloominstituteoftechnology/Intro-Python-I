from room import Room

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "outside"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "foyer"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "overlook"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "narrow"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "treasure"),
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
    def __init__(self, player, room):
        self.player = player
        self.room = room
    
    def getRoom(self):
        print('***********************************')
        print('You are in: ' + self.room.name)
        print('This room is: ' + self.room.description)
        
        
# Make a new player object that is currently in the 'outside' room.
playerA = Main({'name': 'Thuy'}, rooms['outside'])
print('Welcome ' + playerA.player['name'] + '!')
playerA.getRoom()


move = ''

while move != 'q':
    move = input(">>>>>>Your next move? w(west), s(south), n(north), e(east) or q(quit): ")
    
    if (move != 'q'):
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
        print('See you later!')
