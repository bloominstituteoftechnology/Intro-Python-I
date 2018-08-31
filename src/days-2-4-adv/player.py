# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Treasure
from item import LightSource

class Player:

    # Intialization
    def __init__(self, start_room):
        self.room = start_room  # instance variable
        self.items = []
        self.score = 0
        self.has_light = False

    # Get it to print nicely
    def __repr__(self):
        return "Current Location: {}".format(self.room)

    def __str__(self):
        return "Current Location: {}".format(self.room)

    def setRoom(self, new_room):
        self.room = new_room

    def setScore(self, score):
        self.score = score

    def addItem(self, item):

        # Check if it's a treasure
        if isinstance(item, Treasure):

            # Check if the treasure has not already been taken
            if not item.is_taken:
                self.score += item.value
                print(f'You just scored {item.value} points!')
                item.is_taken = True
            else:
                print(f'You already had this item before... no points')
        
        #Else check if it's a LightSource
        elif isinstance(item, LightSource):
            self.has_light = True

        self.items.append(item)

    def removeItem(self, item):

        if len(self.items) > 0:
            
            #Go through the item list and remove the right one
            for i in self.items:
                if i.name == item:
                    self.items.remove(i)
            
            #Check to see if any player items are LightSources
            if [i for i in item if isinstance(i, LightSource)]:
                self.has_light = True
            else:
                self.has_light = False
                
        else:
            print('Item not available to remove!')

    def getItemsList(self):
        if (self.items):
            return [i.name for i in self.items]
        else:
            return []

    def displayItems(self):
        if (self.items):
            for i in self.items:
                print('\x1b[1;35;40m' + i.name + '\x1b[0m')
        else:
            print('\x1b[1;35;40m' + "You don't have any items!" + '\x1b[0m')
