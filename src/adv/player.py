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
            # if hasattr(self.location, 'cardinal'):
            #     #move towards it --->
            #     self.location = self.location.__dict__[cardinal]
            # else:
            #     os.system('cls' if os.name == 'nt' else 'clear')
            #     print('\nPick a different option, You cannot go that way...')
            #     sleep(5)
            try:
                if getattr(self.location, cardinal):
                    #move towards it --->
                    self.location = self.location.__dict__[cardinal]
            except AttributeError:
                if direction == 'q':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Thank you for playing..')
                    sleep(1)
                    os._exit(0)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\nPick a different option, You cannot go that way...')
                sleep(3)
