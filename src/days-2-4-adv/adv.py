from room import Room

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

#  while True:
#      print(room['name'])
#      print(room['description'])

def eval_nesw(player_cmd, current_location):
    if player_cmd == "n":
        if current_location == "outside":
            return current_location == room['foyer']
            print("You are now in the Foyer")
        elif current_location == "foyer":
            return current_location == room['overlook']
            print("You are now in the Grand Overlook")
        elif current_location == "overlook":
            print("You ran into a wall, try a different direction")
        elif current_location == "narrow":
            return current_location == room['treasure']
            print("You are now in the Treasure Chamber")
        elif current_location == "treasure":
            print("You ran into a wall, try a different direction")
    elif player_cmd == "e":
        if current_location == "outside":
            print("You ran into a wall, try a different direction")
        elif current_location == "foyer":
            return current_location == room['narrow']
            print("You are now in the Narrow Passage")
        elif current_location == "overlook":
            print("You ran into a wall, try a different direction")
        elif current_location == "narrow":
            print("You ran into a wall, try a different direction")
        elif current_location == "treasure":
            print("You ran into a wall, try a different direction")
    elif player_cmd == "s":
        if current_location == "outside":
            print("You ran into a wall, try a different direction")
        elif current_location == "foyer":
            return current_location == room['outside']
            print("You are now in the Outside Cave Entrance")
        elif current_location == "overlook":
            return current_location == room['foyer']
            print("You are now in the Foyer")
        elif current_location == "narrow":
            print("You ran into a wall, try a different direction")
        elif current_location == "treasure":
            return current_location == room['narrow']
            print("You are now in the Narrow Passage")
    elif player_cmd == "w":
        if current_location == "outside":
            print("You ran into a wall, try a different direction") 
        elif current_location == "foyer":
            print("You ran into a wall, try a different direction") 
        elif current_location == "overlook":
            print("You ran into a wall, try a different direction") 
        elif current_location == "narrow":
            return currrent_location == room['foyer']
            print("You are now in the Foyer")
        elif current_location == "treasure":
            print("You ran into a wall, try a different direction") 

choice_dictionary = {"n": "north", "e": "east", "s": "south", "w": "west"}
p = Player(input("What is your name? "))

while True:
    player_choice = get_random_rps()
    print(p)
    cmd = input("-> ")
    if cmd == "q":
        break
    elif cmd == "n" or cmd == "e" or cmd == "s" or cmd == "w":
      result = eval_nesw(cmd, player_choice)
      print(f"You chose {choice_dictionary[cmd]}")
      p.addResult(result)
      if result == 1:
          print("You win!")
      elif result == 0:
          print("Tie")
      else:
          print("You lose")
    else:
        print("I did not understand that command.")
