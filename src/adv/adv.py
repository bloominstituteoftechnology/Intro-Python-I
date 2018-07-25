from os import system
from room import Room
from player import Player

# Declare all the rooms
rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mount beckons"
    },
    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east."
    },
    "overlook": {
        "name": "Grand Overlook",
        "description": "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."
    },
    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air."
    },
    "treasure": {
        "name": "Treasure Chamber",
        "description": "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."
    }
}

outside  = Room(rooms["outside"]["name"], rooms["outside"]["description"])
foyer    = Room(rooms["foyer"]["name"], rooms["foyer"]["description"])
overlook = Room(rooms["overlook"]["name"], rooms["overlook"]["description"])
narrow   = Room(rooms["narrow"]["name"], rooms["narrow"]["description"])
treasure = Room(rooms["treasure"]["name"], rooms["treasure"]["description"])


# Link rooms together

outside.n_to = foyer

foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow

overlook.s_to = foyer

narrow.w_to = foyer
narrow.n_to = treasure

treasure.s_to = narrow


# Make a new player object that is currently in the 'outside' room.

system("cls" or "clear")

username = input("Enter a player name: ")

player = Player(username, outside)

print("\nWelcome, %s!" % (player.playerName))

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

while True:
   if player.currentRoom.name is "Treasure Chamber":
      print("\n\nCongratulations, %s! \n\nYou reached Treasure Chamber!\n" % (player.playerName))
      break

   print("\nCurrent room: ", player.currentRoom.name)
   print("Description: ", player.description)

   direction = input("Enter a direction (n, s, e, w): ")

   if direction is "q":
      print("\nThanks for playing!")
      break

   options = {
      "n": player.currentRoom.n_to,
      "s": player.currentRoom.s_to,
      "e": player.currentRoom.e_to,
      "w": player.currentRoom.w_to
   }

   userChoice = options[direction]

   if userChoice is None: print("\nThere is no door to go to in that direction.")

   else: player.setCurrentRoom(userChoice)
