# Write a class to hold player information, e.g. what room they are in
# currently.

from time import sleep
import os


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move_to(self, direction):
        cardinal = direction + '_to'
    # if hasattr(self.location, 'cardinal'):
    #     #move towards it --->
    #     self.location = self.location.__dict__[cardinal]
    # else:
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     print('\nPick a different option, You cannot go that way...')
    #     sleep(5)
