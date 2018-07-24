# Write a class to hold player information, e.g. what room they are in
# currently.
from time import sleep
import os
class Player:
    #                  str , Room(class reference)
    #           { name: 'Moises', location: SOME OBJECT REFERENCE }
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def move_to(self, direction):
        cardinal = direction + '_to'
        try:
            if getattr(self.location, cardinal):
                self.location = self.location.__dict__[cardinal]
        except AttributeError:
            # Handling Quit upon submitting 'q' as a direction
            if direction == 'q':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thank you for playing...')
                sleep(2)
                os._exit(0)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nThere is no available path in that direction\npick another direction to move towards...')
            sleep(2)
