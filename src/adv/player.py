from time import sleep
import os

class Player:
    # { name: 'Moises', location: SOME OBJECT REFERENCE }
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []
        self.race = 'Human'
    
    def loot(self, item_name):
        # loop through room items
        for item in self.location.inventory:
            # if an item matches the item name
            if item.name == item_name:
                # put it in player's inventory
                self.inventory.append(item)
                # remove it from room
                self.location.inventory.remove(item)
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('There is no ' + item_name + ' at this location')
                sleep(2)
    
    def drop(self, item_name):
        # if item_name exists inside self.inventory
            # add it to self.location.inventory
            # remove it from self.inventory
        for item in self.inventory:
            if item.name == item_name:
                # add it to the room
                self.location.inventory.append(item)
                # remove it from player inventory
                self.inventory.remove(item)
                return
            else:
                # os.system('cls' if os.name == 'nt' else 'clear')
                # print('Unable to perform that action')
                # sleep(2)
                pass

    def display_inventory(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print Items in current location
        items_info = []
        for item in self.inventory:
            items_info.append(item.info())
        print('\nThe following items are available:')
        print('-'*50)
        print('\n'.join(items_info))
        input('Press Enter/Return to go back to game')

    def move_to(self, direction):
        cardinal = direction + '_to'
        try:
            if getattr(self.location, cardinal):
                self.location = self.location.__dict__[cardinal]
        except AttributeError:
            # Handling Quit upon submitting 'q' as a direction...
            if direction == 'q':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thank you for playing...')
                sleep(2)
                os._exit(0)
            # Handling Moving in the wrong direction...
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nThere is no available path in that direction\npick another direction to move towards...')
            sleep(2)
