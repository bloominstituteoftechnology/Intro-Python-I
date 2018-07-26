from time import sleep
import os

class Player:
    # { name: 'Moises', location: SOME OBJECT REFERENCE }
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []
        self.race = 'Human',
        self.score = 0
        self.visibility = 0
    
    def check_visibility(self):
        # Check if room is lit
        if self.location.is_lit == True:
            self.visibility = 1
            return
        # Check if player has light
        else:
            for item in self.inventory:
                try:
                    if getattr(item, 'lit'):
                        if item.lit == True:
                            self.visibility = 1
                            return
                except AttributeError:
                    pass
            self.visibility = 0

    def show_score(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'*50)
        print('-'*50+'\n\nYour Score is:\t'+ str(self.score)+'\n\n'+'-'*50)
        input('Press Enter/Return to go back to game')
    
    def loot(self, item_name):
        if self.visibility == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n'*50)
            print('Good luck finding that in the dark!')
            sleep(4)
            return
        # loop through room items
        # if item_name == 'all':
        #     self.inventory = self.inventory + self.location.inventory
        #     self.location.inventory = []
        #     return
        for item in self.location.inventory:
            # if an item matches the item name
            if item.name == item_name:
                # Handle inventory transactions and score
                # put it in player's inventory
                self.inventory.append(item)
                if item.on_take(self) == 1:                    
                    # remove it from room                    
                    self.location.inventory.remove(item)
                    return
                else:
                    return

        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'*50)
        print('There is no ' + item_name + ' at this location')
        sleep(4)
    
    def drop(self, item_name):
        # if item_name exists inside self.inventory
            # add it to self.location.inventory
            # remove it from self.inventory
        # if item_name == 'all':
        #     self.location.inventory = self.location.inventory + self.inventory
        #     self.inventory = []
        #     return
        for item in self.inventory:
            if item.name == item_name:
                # Handle inventory transactions and score
                if item.on_drop(self) == 1:
                    # add it to the room
                    self.location.inventory.append(item)
                    # remove it from player inventory
                    self.inventory.remove(item)
                    return
                else:
                    return

        os.system('cls' if os.name == 'nt' else 'clear')
        print('Unable to perform that action')
        sleep(2)


    def display_inventory(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'*50)
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
            print('\n'*50)
            print('\nThere is no available path in that direction\npick another direction to move towards...')
            sleep(2)
