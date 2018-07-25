from os import system
from room import Room
from player import Player
from item import Item

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


# Declare any items
items = {
    "mirror": {
        "name": "Mirror",
        "description": "Check out that reflection"
    }
}

mirror = Item(items["mirror"]["name"], items["mirror"]["description"])


# Link rooms together

outside.n_to = foyer

foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow

overlook.s_to = foyer

narrow.w_to = foyer
narrow.n_to = treasure

treasure.s_to = narrow


# Add items to rooms

outside.addItem(mirror)


# Make a new player object that is currently in the 'outside' room.

system("cls" or "clear")

print("Controls:")
print("   ~  Directions: n, s, e, w")
print("   ~  Actions: [get, drop] item\n")

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

def printItems():
   playerInventory = player.inventory
   availableItems  = player.currentRoom.items

   print("Items:")

   if len(availableItems) is 0:
      print("   None")
   else:
      for item in availableItems:
         print("   %s - %s" % (item.name, item.description))

   print("Inventory:")

   if len(playerInventory) is 0:
      print("   None")
   else:
      for item in playerInventory:
         print("   %s - %s" % (item.name, item.description))


while True:
   if player.currentRoom.name is "Treasure Chamber":
      print("\n\nCongratulations, %s! \n\nYou reached Treasure Chamber!\n" % (player.playerName))
      break

   print("\nCurrent room: ", player.currentRoom.name)
   print("Description: ", player.currentRoom.description)
    
   printItems()

   command = input("\nCommand> ")

   if command is "q":
      print("\nThanks for playing!")
      break

   directions = {
      "n": player.currentRoom.n_to,
      "s": player.currentRoom.s_to,
      "e": player.currentRoom.e_to,
      "w": player.currentRoom.w_to,
   }

   if len(command) is 1:
      userChoice = directions[command]
      if userChoice is None: 
         print("\nThere is no door to go to in that direction.")
      else: 
         player.setCurrentRoom(userChoice)

   else:
      commandParse = command.split(" ")
      action = commandParse[0]
      itemName = commandParse[1]

      if action not in ["get", "drop", "use"]:
         print("\nPlease use a valid action. [get, drop, use]")

      else:
         actualItem = player.currentRoom.itemAvailability(itemName)
         available = True

         if actualItem is not available:
            print("\nItem is not available in this room.\nPlease choose a valid item.")
         elif action is "get": 
            player.getItem(actualItem)
         elif action is "drop":
            player.dropItem(actualItem)