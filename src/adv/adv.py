from os import system
from room import Room
from player import Player
from item import Item
from data import rooms, items

outside  = Room(rooms["outside"]["name"], rooms["outside"]["description"])
foyer    = Room(rooms["foyer"]["name"], rooms["foyer"]["description"])
overlook = Room(rooms["overlook"]["name"], rooms["overlook"]["description"])
narrow   = Room(rooms["narrow"]["name"], rooms["narrow"]["description"])
treasure = Room(rooms["treasure"]["name"], rooms["treasure"]["description"])

key        = Item(items["key"]["name"], items["key"]["description"])
mirror     = Item(items["mirror"]["name"], items["mirror"]["description"])
flashlight = Item(items["flashlight"]["name"], items["flashlight"]["description"])


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
foyer.addItem(flashlight)
narrow.addItem(key)


# Make a new player object that is currently in the 'outside' room.
score = 0

def print_user_controls():
   global score
   print("\n ~ Directions: move [n, s, e, w]")
   print(" ~ Actions: [get, drop, use] item")
   print(" ~ Quit: q or quit\n")
   print("Score: %d\n" % score)


system("cls" or "clear")

print_user_controls()

username = input("Enter a player name: ")

player = Player(username, outside)

print("\nWelcome, %s!" % (player.playerName))


# PRINT ITEMS IN THE ROOM AND ITEMS IN INVENTORY

def printItems():
   playerInventory = player.inventory
   availableItems  = player.currentRoom.items

   handleRoomChange(player.currentRoom)

   print("Items in this room:")

   if len(availableItems) is 0:
      print("   None")
   else:
      for item in availableItems:
         print("   %s - %s" % (item.name, item.description))

   print("\nInventory:")

   if len(playerInventory) is 0:
      print("   None")
   else:
      for item in playerInventory:
         print("   %s - %s" % (item.name, item.description))    



def handleRoomChange(newRoom):
   if newRoom is None: 
      print("\nThere is no door to go to in that direction.")
   else: 
      player.setCurrentRoom(newRoom)
      print("\nYou enter the %s\n" % (player.currentRoom.name))
      print("%s\n" % player.currentRoom.description)



# PARSE USER INPUT
def parser(command):
   directions = {
      "n": player.currentRoom.n_to,
      "s": player.currentRoom.s_to,
      "e": player.currentRoom.e_to,
      "w": player.currentRoom.w_to
   }

   commands = {
      "get": player.getItem,
      "drop": player.dropItem,
      "use": unlock_treasure
   }

   commandParse = command.split(" ")
   action = commandParse[0]
   itemName = direction = commandParse[1]

   if action not in commands:
      if action is not "help": print("\nPlease use a valid command.")
      print_user_controls()

   if direction in directions:
      handleRoomChange(directions[direction])
   
   else:
      availableItem = player.currentRoom.itemAvailability(itemName) or player.locateInventory(itemName)

      if availableItem is None:
         print("\nItem is not available in this room.\nPlease choose a valid item.")

      else:
         commands[action](availableItem)

         

# TREASURE REACTION

def unlock_treasure(item):
   global game_over

   if item.name is not "Key":
      print("You cannot use this item here.")

   else:
      system("cls" or "clear")
      print("\n\n\n\nYou insert the key and unlock the chest.")
      print("\n\nIt's filled with gold and jewels!")
      print("\n\nCongratulations, %s! You won!" % (player.playerName))
      print("\n\nFinal score: 100\n")
      game_over = True



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

game_over = False

while game_over is not True:
   system("cls" or "clear")

   print_user_controls()
   printItems()

   command = input("\nCommand> ")

   if command in ["q", "quit"]:
      print("\nThanks for playing!")
      break

   else:
      parser(command)
