from time import sleep
import os

class Player:
    # str, Room(class reference)
    #{name: 'Jackee', location: SOME OBJECT REFERENCE}
        def __init__(self, name, location):
            self.name = name
            self.location = location
        def move_to(self, direction):
            cardinal = direction + '_to'
            if getattr(self.location, cardinal):
                #move towards it --->
                self.location = self.location.__dict__[cardinal]
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\nPick a different option, You cannot go that way...')
                sleep(5)
