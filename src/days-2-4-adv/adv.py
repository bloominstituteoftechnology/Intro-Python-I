from room import Room
from player import Player
import random 
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
    'prison' : Room('Prison', """You will have to fight your way out of the prison if you wish to go north.
     If you wish not to fight run left or right"""),
    'coward': Room("Cowards Forest", """You coward! You ran from the fight. Now the goblins have been alerted.  """),
    'kitchen' : Room ('Kitchen', """Welcome to the kitchen """)

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
room['treasure'].n_to = room['kitchen']
room['kitchen'].e_to = room['prison']
room['prison'].n_to = room['coward']
# Main

rooms = ["outside", "foyer", "overlook", "narrow", "treasure", "kitchen", "prison"]

def change_rooms(Player, direction):
    direction = direction.lower()
    try:
        if direction == "n":
            return Player.room_change(room[Player.roomKey].n_to.name)
        elif direction == "s":
            return Player.room_change(room[Player.roomKey].s_to.name)

        elif direction == "e":
            return Player.room_change(room[Player.roomKey].e_to.name)
        elif direction == "w":
            return Player.room_change(room[Player.roomKey].w_to.name)
    except:
        return "You can not go in that direction!"
# end of change_rooms function


# Make a new player object that is currently in the 'outside' room.
jonathan = Player("Jonathan", 'Outside Cave Entrance', "outside")
# Write a loop that:
directions = ["n", "s", "e", "w"]
while True:
    print(f"Current room {jonathan.currentRoom}")
    print(f"Room description {room[jonathan.roomKey].description}")
    option = input(
        "Enter q to quit, n to go North s to go South e to go East w to go West")
    option = option.lower()
    if option == "q":
        print("Exiting the game!")
        break
    elif directions.count(option) > 0:
        print(change_rooms(jonathan, option))
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
