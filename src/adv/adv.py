from os import system
from room import Room
from player import Player
from item import Item, Treasure, LightSource
from data import rooms, items

score = 0

# INITIALIZE DATA

outside  = Room(rooms["outside"]["name"], rooms["outside"]["description"])
foyer    = Room(rooms["foyer"]["name"], rooms["foyer"]["description"])
overlook = Room(rooms["overlook"]["name"], rooms["overlook"]["description"])
narrow   = Room(rooms["narrow"]["name"], rooms["narrow"]["description"], False) # no light
treasure = Room(rooms["treasure"]["name"], rooms["treasure"]["description"])

treasureX = Treasure(items["treasure0"]["name"], items["treasure0"]["description"], items["treasure0"]["value"])
treasureY = Treasure(items["treasure1"]["name"], items["treasure1"]["description"], items["treasure1"]["value"])
treasureZ = Treasure(items["treasure2"]["name"], items["treasure2"]["description"], items["treasure1"]["value"])

key        = Item(items["key"]["name"], items["key"]["description"])
mirror     = Item(items["mirror"]["name"], items["mirror"]["description"])

flashlight = LightSource(items["flashlight"]["name"], items["flashlight"]["description"])


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

narrow.addItem(treasureX)
narrow.addItem(key)

outside.addItem(treasureY)
outside.addItem(mirror)

foyer.addItem(flashlight)

overlook.addItem(treasureZ)


# Basic user commands
def print_user_controls():
   global score
   print("\n ~ Directions: move [n, s, e, w]")
   print(" ~ Actions: [get, drop, use] item")
   print(" ~ Quit: q or quit\n")
   print("Score: %d\n" % score)


# Make a new player object that is currently in the 'outside' room.

system("cls" or "clear")

print_user_controls()

username = input("Enter a player name: ")

player = Player(username, outside)

print("\nWelcome, %s!" % (player.playerName))



# CHANGE CURRENT ROOM
def handleRoomChange(newRoom):
   if newRoom is None: 
      print("\nThere is no door to go to in that direction.")
   else: 
      player.setCurrentRoom(newRoom)
      print("\nYou enter the %s\n" % (player.currentRoom.name))
      print("%s\n" % player.currentRoom.description)
      player.currentRoom.on_enter()



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
      "take": player.getItem,
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

      elif isinstance(availableItem, Treasure):
         global score
         score += availableItem.value
         player.currentRoom.removeItem(availableItem)

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
   # CLEAR THE TERMINAL
   system("cls" or "clear")

   # PRINT BASIC COMMANDS, ITEMS IN THE ROOM, AND ITEMS IN INVENTORY
   print_user_controls()
   handleRoomChange(player.currentRoom)
   player.print_inventory()

   # AWAIT COMMAND
   command = input("\nCommand> ")

   # END GAME CONDITIONAL
   if command in ["q", "quit"]:
      print("\nThanks for playing!")
      break

   # PARSE COMMAND
   parser(command)
