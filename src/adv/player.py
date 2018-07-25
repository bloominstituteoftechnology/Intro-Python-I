# Write a class to hold player information, e.g. what room they are in
# currently.
from time import sleep
import os

class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def pick_up(self, item,):
        """Pick an object, put in inventory, set its owner."""
        self.inventory.append(item)
        item.owner = self
        self.location.inventory.remove(item)

    def move_to(self, direction):
        cardinal = direction + '_to'
        if getattr(self.location, cardinal):
            #move towards it -->
            self.location = self.location.__dict__[cardinal]
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nPick a different option, you cannot go that way..')
            sleep(5)

    
