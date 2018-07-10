# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.
# import textwrap

# These are the existing rooms. Add more as you see fit.

from rms import rooms

# Utility Stuff

from systext import system_text

# def print_multilines(text):
#     textwrap_list = textwrap.wrap(text)
#     for line in textwrap_list:
#         print(line)

# Write a class to hold player information, e.g. what room they are in currently
class Player:
    def __init__(self, location):
        self.location = location
        self.freedom = 0
    
    def move(self, input):
        current_loc = rooms[str(self.freedom)][self.location]
        if 'redirect' in current_loc:
            next_room = current_loc['redirect']
        elif f'{input}_to' in current_loc:
            next_room = current_loc[f'{input}_to']
        else:
            if 'error' in current_loc:
                print(current_loc['error'])
            else:
                print(system_text['key_error'])
            return 
        self.location = next_room
    
    def check_levelup(self):
        current_loc = rooms[str(self.freedom)][self.location]
        if 'level_up' in current_loc:
            self.freedom += 1
    
    def check_redirect(self):
        current_loc = rooms[str(self.freedom)][self.location]
        # print('check_redirect:',True if 'redirect' in current_loc else False)
        return True if 'redirect' in current_loc else False

    def print_location(self):
        current_loc = rooms[str(self.freedom)][self.location]
        print(f'*-------*\nLocation: {current_loc["name"]}\n')
        location_description = current_loc["description"]
        print(location_description)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p1 = Player('outside')
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

# Game Start
print(system_text['welcome'])
p1.print_location()
player_input = input(">> ")

while player_input != 'q':
    p1.move(player_input)
    p1.print_location()
    redirect = p1.check_redirect()
    p1.check_levelup()
    if redirect == False:
        player_input = input(">> ")

exit(0)
