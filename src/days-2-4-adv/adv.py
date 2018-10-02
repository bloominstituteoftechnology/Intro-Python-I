from room import Room
from player import Player

class AdventureDone(Exception): pass

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",'outside'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",'foyer'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",'overlook'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",'narrow'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",'treasure'),
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

#
# Main
#
playerName = input("Please input a name:")

# Make a new player object that is currently in the 'outside' room.
currentPlayer = Player(playerName)

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
print(room[currentPlayer.room].n_to.name)
def TextEval(text):
    if text == "q":
        raise AdventureDone
    elif text =="n":
        room[currentPlayer.room].n_to

print(f"Welcome {currentPlayer.name}, pick a direction or use q to quite")
try:
    while True:
      print(f"{currentPlayer.name} is located in {room[currentPlayer.room].name}")
      print(room[currentPlayer.room].description)
      playerInput = input("Please select a direction:")
      TextEval(playerInput.lower())
      break

except AdventureDone:
    print('See you next adventure')